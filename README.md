# 서울인디게임즈

매주 토요일 오후 2시, 서울의 인디게임 개발자들이 각자 만들고,
서로 플레이하고, 다음 빌드까지 연결하는 정기 오픈 스튜디오 사이트입니다.

- 공개 사이트: <https://emptypizza.github.io/seoulindies/>
- Discord: <https://discord.gg/j4ZsncEQ5>
- 카카오톡 오픈채팅: <https://open.kakao.com/o/pIxN9iFi>
- 문의: <plusalpha.top@gmail.com>

## 로컬 빌드

Jekyll이 PATH에 있다면 다음 명령을 사용합니다.

```bash
jekyll build --future --trace
```

이 저장소를 작업한 macOS 환경에서는 설치된 Ruby gem을 직접 불러와서도 빌드할 수 있습니다.

```bash
ruby -rjekyll -e 'Jekyll::Commands::Build.process({"source" => ".", "destination" => "/private/tmp/seoulindies-build", "future" => true, "trace" => true})'
```

## 디자인

- 일정과 핵심 문구는 이미지가 아닌 HTML로 제공해 접근성과 수정 가능성을 유지합니다.
- 히어로 이미지는 제공된 네온 픽셀 포스터를 분위기 참고 자료로 삼아 이미지 생성 모델로 새로 제작했습니다.
- 원본 생성 결과는 PNG였으며, 실제 사이트에는 WebP와 JPEG 대체 이미지를 사용합니다.
- 상세 시장·레퍼런스 조사와 설계 근거는 [docs/market-and-design-research.md](docs/market-and-design-research.md)에 정리했습니다.

## 배포

`main` 브랜치가 GitHub Pages의 소스입니다. `baseurl: /seoulindies` 설정을 유지해야 하위 경로의 CSS와 이미지가 정상적으로 로드됩니다.
