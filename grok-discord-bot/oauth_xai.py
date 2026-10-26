"""Browser OAuth for a Grok Heavy / SuperGrok subscription.

The Discord bot calls api.x.ai with the access token from this login.
That token spends the subscription quota, not console.x.ai API credits.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import secrets
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

CLIENT_ID = "b1a00492-073a-47ea-816f-4c329264a828"
SCOPE = "openid profile email offline_access grok-cli:access api:access"
REDIRECT_HOST = "127.0.0.1"
REDIRECT_PORT = 56121
REDIRECT_PATH = "/callback"
REDIRECT_URI = f"http://{REDIRECT_HOST}:{REDIRECT_PORT}{REDIRECT_PATH}"
DISCOVERY_URL = "https://auth.x.ai/.well-known/openid-configuration"
TOKEN_PATH = Path(__file__).resolve().parent / "oauth" / "xai_oauth_tokens.json"
REFRESH_SKEW_SECONDS = 15 * 60


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _pkce_pair() -> tuple[str, str]:
    verifier = _b64url(secrets.token_bytes(32))
    challenge = _b64url(hashlib.sha256(verifier.encode("ascii")).digest())
    return verifier, challenge


def _discover() -> dict:
    try:
        with urllib.request.urlopen(DISCOVERY_URL, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        return {
            "authorization_endpoint": data.get("authorization_endpoint"),
            "token_endpoint": data.get("token_endpoint"),
        }
    except Exception:
        return {}


def _token_endpoint() -> str:
    return _discover().get("token_endpoint") or "https://auth.x.ai/oauth2/token"


def _post_form(url: str, fields: dict) -> dict:
    body = urllib.parse.urlencode(fields).encode("utf-8")
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def _read_tokens() -> dict | None:
    if not TOKEN_PATH.exists():
        return None
    try:
        payload = json.loads(TOKEN_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    tokens = payload.get("tokens") if isinstance(payload, dict) else None
    if not isinstance(tokens, dict) or not tokens.get("access_token"):
        return None
    return tokens


def _write_tokens(tokens: dict) -> None:
    TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = TOKEN_PATH.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps({"version": 1, "tokens": tokens}, indent=2),
        encoding="utf-8",
    )
    os.replace(temporary, TOKEN_PATH)
    try:
        os.chmod(TOKEN_PATH, 0o600)
    except OSError:
        pass


def _expires_soon(tokens: dict) -> bool:
    expires_at = tokens.get("expires_at")
    if not expires_at:
        return True
    return time.time() + REFRESH_SKEW_SECONDS >= float(expires_at)


def _refresh(tokens: dict) -> dict | None:
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        return None
    try:
        issued = _post_form(
            _token_endpoint(),
            {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "client_id": CLIENT_ID,
            },
        )
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return None
    access_token = issued.get("access_token")
    if not access_token:
        return None
    return {
        "access_token": access_token,
        "refresh_token": issued.get("refresh_token") or refresh_token,
        "token_type": issued.get("token_type", "Bearer"),
        "expires_at": time.time() + int(issued.get("expires_in", 3600)),
        "scope": issued.get("scope"),
    }


def get_access_token() -> str | None:
    tokens = _read_tokens()
    if not tokens:
        return None
    if _expires_soon(tokens):
        refreshed = _refresh(tokens)
        if not refreshed:
            return None
        tokens = refreshed
        _write_tokens(tokens)
    access_token = tokens.get("access_token")
    return access_token or None


def token_shape() -> dict:
    tokens = _read_tokens() or {}
    access_token = tokens.get("access_token") or ""
    return {
        "stored": bool(access_token),
        "len": len(access_token),
        "has_refresh": bool(tokens.get("refresh_token")),
        "expires_soon": _expires_soon(tokens) if access_token else None,
    }


class _Callback(BaseHTTPRequestHandler):
    code = None
    state = None
    error = None

    def do_GET(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _Callback.code = (query.get("code") or [None])[0]
        _Callback.state = (query.get("state") or [None])[0]
        _Callback.error = (query.get("error") or [None])[0]
        body = (
            "<h1>로그인되었습니다</h1><p>이 탭을 닫아도 됩니다.</p>"
            if not _Callback.error
            else f"<h1>로그인 실패</h1><p>{_Callback.error}</p>"
        )
        payload = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):
        return


def login(timeout: float = 600.0) -> bool:
    verifier, challenge = _pkce_pair()
    state = _b64url(secrets.token_bytes(16))
    endpoints = _discover()
    authorize = endpoints.get("authorization_endpoint") or "https://auth.x.ai/oauth2/authorize"
    query = urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECT_URI,
            "scope": SCOPE,
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
            "prompt": "consent",
            "access_type": "offline",
        }
    )
    auth_url = f"{authorize}?{query}"
    print(auth_url, flush=True)
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    _Callback.code = None
    _Callback.state = None
    _Callback.error = None
    try:
        server = ThreadingHTTPServer((REDIRECT_HOST, REDIRECT_PORT), _Callback)
    except OSError as error:
        print(f"callback port {REDIRECT_PORT} is busy: {error}", flush=True)
        return False
    server.timeout = 1.0
    deadline = time.time() + timeout
    try:
        while time.time() < deadline and not (_Callback.code or _Callback.error):
            server.handle_request()
    finally:
        server.server_close()

    if _Callback.error or not _Callback.code or _Callback.state != state:
        print("login did not finish", flush=True)
        return False

    try:
        issued = _post_form(
            _token_endpoint(),
            {
                "grant_type": "authorization_code",
                "code": _Callback.code,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
                "code_verifier": verifier,
            },
        )
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:300]
        print(f"token exchange failed: {error.code} {detail}", flush=True)
        return False

    access_token = issued.get("access_token")
    if not access_token:
        print("token exchange returned no access token", flush=True)
        return False
    _write_tokens(
        {
            "access_token": access_token,
            "refresh_token": issued.get("refresh_token"),
            "token_type": issued.get("token_type", "Bearer"),
            "expires_at": time.time() + int(issued.get("expires_in", 3600)),
            "scope": issued.get("scope"),
        }
    )
    print(f"saved {TOKEN_PATH} access_len={len(access_token)}", flush=True)
    return True


if __name__ == "__main__":
    raise SystemExit(0 if login() else 1)
