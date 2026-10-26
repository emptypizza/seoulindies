import json
import os
import sys
import time
import asyncio
from pathlib import Path

import discord
from discord import app_commands
from openai import OpenAI
from dotenv import load_dotenv

from oauth_xai import get_access_token, token_shape

ENV_PATH = Path(__file__).resolve().parent / ".env"
SETTINGS_PATH = Path(__file__).resolve().parent / "settings.json"
LOG_PATH = Path("/Users/choimarc/seoulindies/.cursor/debug-41f19f.log")
EFFORTS = ("none", "minimal", "low", "medium", "high", "xhigh", "max")
MODELS = (
    "grok-4.7",
    "grok-4.6",
    "grok-4.5",
    "grok-4.20-multi-agent",
    "grok-4",
)
DEFAULTS = {"model": "grok-4.7", "effort": "xhigh"}
HELP_ITEMS = (
    ("/model", "모델 목록. 뒤에 id를 붙이면 변경"),
    ("/effort", "effort 목록. 뒤에 단계를 붙이면 변경"),
    ("/help", "이 목록"),
    ("/status", "현재 모델과 effort"),
)

load_dotenv(ENV_PATH)


def _key_shape(value):
    text = value or ""
    return {
        "set": bool(text),
        "len": len(text),
        "xai_prefix": text.startswith("xai-"),
        "has_space": any(char.isspace() for char in text),
        "quoted": (text[:1] in "\"'" and text[:1] == text[-1:]),
    }


def _agent_log(hypothesis_id, message, data):
    # #region agent log
    try:
        payload = {
            "sessionId": "41f19f",
            "hypothesisId": hypothesis_id,
            "location": "bot.py",
            "message": message,
            "data": data,
            "timestamp": int(time.time() * 1000),
        }
        with LOG_PATH.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        pass
    # #endregion


def _file_api_key():
    if not ENV_PATH.exists():
        return ""
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("XAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip("\"'")
    return ""


def _chunks(text, size=2000):
    return [text[index:index + size] for index in range(0, len(text), size)] or [text]


def load_settings():
    settings = dict(DEFAULTS)
    if SETTINGS_PATH.exists():
        try:
            stored = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            stored = {}
        if isinstance(stored, dict):
            if isinstance(stored.get("model"), str) and stored["model"].strip():
                settings["model"] = stored["model"].strip()
            if stored.get("effort") in EFFORTS:
                settings["effort"] = stored["effort"]
    return settings


def save_settings(settings):
    SETTINGS_PATH.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")


def system_prompt(settings):
    return (
        f"You are Grok. The API model id is {settings['model']} and the reasoning effort is {settings['effort']}. "
        f"If asked your model, version, or effort, say {settings['model']} with reasoning effort {settings['effort']}."
    )


def _catalog(items, current):
    shown = list(items)
    if current not in shown:
        shown.insert(0, current)
    return "\n".join(
        f"▸ {item}" if item == current else f"▹ {item}"
        for item in shown
    )


def _command_view(title, body, color, note=""):
    plain = title + "\n" + body
    if note:
        plain += "\n" + note
    embed = discord.Embed(title=title, description=body, color=color)
    if note:
        embed.set_footer(text=note)
    return {"plain": plain, "embed": embed}


def apply_command(text):
    parts = text.split(maxsplit=1)
    if not parts or not parts[0].startswith("/"):
        return None
    name = parts[0][1:].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""
    if name not in {"model", "effort", "help", "status"}:
        return None
    settings = load_settings()
    if name == "help":
        body = "\n".join(f"▸ {command}  {detail}" for command, detail in HELP_ITEMS)
        return _command_view("명령", body, 0x57F287)
    if name == "status":
        body = f"▸ model   {settings['model']}\n▸ effort  {settings['effort']}"
        return _command_view("현재 설정", body, 0xFEE75C)
    if name == "model":
        note = ""
        if arg:
            settings["model"] = arg
            save_settings(settings)
            note = "모델을 바꿨습니다."
        return _command_view("모델", _catalog(MODELS, settings["model"]), 0x5865F2, note)
    note = ""
    if arg:
        if arg not in EFFORTS:
            return _command_view(
                "effort",
                _catalog(EFFORTS, settings["effort"]),
                0xED4245,
                "없는 값입니다. 목록에 있는 단계를 고르세요.",
            )
        settings["effort"] = arg
        save_settings(settings)
        note = "effort를 바꿨습니다."
    return _command_view("effort", _catalog(EFFORTS, settings["effort"]), 0xEB459E, note)


def run_cli(argv):
    command = argv[0].lstrip("/").lower()
    argument = " ".join(argv[1:]).strip()
    if command not in {"model", "effort", "help", "status"}:
        print("commands: model, effort, status, help")
        return 2
    print(apply_command(f"/{command} {argument}".strip())["plain"])
    return 0


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


@tree.command(name="model", description="현재 모델을 보거나 바꿉니다")
@app_commands.describe(model_id="바꿀 모델 id. 생략하면 현재 값")
async def slash_model(interaction: discord.Interaction, model_id: str | None = None):
    text = "/model" if not model_id else f"/model {model_id}"
    await interaction.response.send_message(embed=apply_command(text)["embed"])


@tree.command(name="effort", description="reasoning effort를 보거나 바꿉니다")
@app_commands.describe(level="none, minimal, low, medium, high, xhigh, max. 생략하면 현재 값")
@app_commands.choices(level=[app_commands.Choice(name=item, value=item) for item in EFFORTS])
async def slash_effort(
    interaction: discord.Interaction,
    level: app_commands.Choice[str] | None = None,
):
    text = "/effort" if level is None else f"/effort {level.value}"
    await interaction.response.send_message(embed=apply_command(text)["embed"])


@tree.command(name="help", description="명령 목록")
async def slash_help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=apply_command("/help")["embed"])


@tree.command(name="status", description="현재 모델과 effort")
async def slash_status(interaction: discord.Interaction):
    await interaction.response.send_message(embed=apply_command("/status")["embed"])


@bot.event
async def on_ready():
    print(f"{bot.user} 온라인!")
    await tree.sync()
    for guild in bot.guilds:
        tree.copy_global_to(guild=guild)
        await tree.sync(guild=guild)
    print(f"commands synced to {len(bot.guilds)} guilds")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    is_dm = message.guild is None
    # 서버에서는 멘션했을 때만, DM에서는 그냥 보낸 메시지에 응답
    if not is_dm and bot.user not in message.mentions:
        return

    content = message.content
    if not is_dm:
        content = (
            content.replace(f"<@{bot.user.id}>", "")
            .replace(f"<@!{bot.user.id}>", "")
        )
    content = content.strip()
    if not content:
        await message.reply("무엇을 도와드릴까요?")
        return

    async with message.channel.typing():
        command_reply = apply_command(content)
        if command_reply is not None:
            await message.reply(embed=command_reply["embed"])
            return

        settings = load_settings()
        load_dotenv(ENV_PATH, override=True)
        oauth_token = get_access_token()
        api_key = oauth_token or os.getenv("XAI_API_KEY") or ""
        file_key = _file_api_key()
        # #region agent log
        _agent_log(
            "E",
            "credential selected before request",
            {
                "source": "oauth" if oauth_token else "api_key",
                "oauth": token_shape(),
                "api_key": _key_shape(api_key if not oauth_token else ""),
                "file_api_key": _key_shape(file_key),
                "model": settings["model"],
                "effort": settings["effort"],
                "is_dm": is_dm,
            },
        )
        # #endregion
        try:
            response = await asyncio.to_thread(
                OpenAI(api_key=api_key, base_url="https://api.x.ai/v1").chat.completions.create,
                model=settings["model"],
                reasoning_effort=settings["effort"],
                messages=[
                    {"role": "system", "content": system_prompt(settings)},
                    {"role": "user", "content": content},
                ],
            )
            reply = response.choices[0].message.content or ""
            # #region agent log
            _agent_log(
                "D",
                "xai request succeeded",
                {"reply_len": len(reply), "response_model": response.model},
            )
            # #endregion
            parts = _chunks(reply)
            await message.reply(parts[0])
            for part in parts[1:]:
                await message.channel.send(part)
        except Exception as e:
            body = getattr(e, "body", None)
            code = body.get("code") if isinstance(body, dict) else None
            # #region agent log
            _agent_log(
                "D",
                "xai request failed",
                {
                    "status": getattr(e, "status_code", None),
                    "code": code,
                    "error_type": type(e).__name__,
                },
            )
            # #endregion
            await message.reply(f"오류가 발생했습니다: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raise SystemExit(run_cli(sys.argv[1:]))
    bot.run(os.getenv("DISCORD_TOKEN"))
