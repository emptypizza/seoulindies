---
layout: home
title: 서울인디게임즈
description: 서울 강남역에서 모이는 인디게임 바이브코딩 스터디. 목표 한 줄에서 시작해 에이전트와 만들고, 플레이되는 빌드로 확인합니다.
---

<section class="home-hero" aria-labelledby="hero-title">
  <picture class="home-hero__art" aria-hidden="true">
    <img src="{{ site.baseurl }}/images/seoul-indies-hero.jpg" alt="" width="1280" height="720" fetchpriority="high">
  </picture>
  <div class="home-hero__wash"></div>
  <div class="pixel-corner pixel-corner--top" aria-hidden="true"></div>
  <div class="pixel-corner pixel-corner--bottom" aria-hidden="true"></div>

  <div class="home-container home-hero__inner">
    <div class="hero-copy">
      <p class="eyebrow eyebrow--glow"><span></span> GANGNAM · AGENTIC INDIE STUDY</p>
      <h1 id="hero-title">인디게임을,<br><em>에이전트와 같이.</em></h1>
      <p class="hero-lead">서울 강남역에서 모이는 인디게임 바이브코딩 스터디입니다. 목표 한 줄에서 시작해 에이전트와 만들고, 플레이되는 빌드로 확인합니다.</p>

      <div class="hero-actions">
        <a class="button button--primary" href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">
          Discord 참여하기 <span aria-hidden="true">↗</span>
        </a>
        <a class="button button--kakao" href="{{ site.kakao_url }}" target="_blank" rel="noopener noreferrer">카카오톡 오픈채팅 <span aria-hidden="true">↗</span></a>
        <a class="button button--ghost" href="#ai-lab">스터디 방식 보기 <span aria-hidden="true">↓</span></a>
      </div>

      <dl class="hero-facts" aria-label="스터디 정보">
        <div>
          <dt>FORMAT</dt>
          <dd>바이브코딩 · <strong>에이전틱 코딩</strong></dd>
        </div>
        <div>
          <dt>WHERE</dt>
          <dd>{{ site.meeting_place }}</dd>
        </div>
        <div>
          <dt>BRING</dt>
          <dd>노트북 · 에이전트 IDE · 만들고 싶은 게임</dd>
        </div>
      </dl>
    </div>
  </div>
</section>

<div class="signal-strip" aria-label="서울인디게임즈 핵심 활동">
  <div>
    <span>VIBE CODING</span><i>✦</i>
    <span>AGENTIC</span><i>✦</i>
    <span>INDIE GAMES</span><i>✦</i>
    <span>GANGNAM</span><i>✦</i>
    <span>PLAY THE BUILD</span>
  </div>
</div>

<section class="section section--spirit" id="spirit" aria-labelledby="spirit-title">
  <div class="home-container">
    <div class="section-heading section-heading--split">
      <div>
        <p class="eyebrow">01 · STUDY SPIRIT</p>
        <h2 id="spirit-title">흐름으로 시작하고,<br><em>빌드로 끝냅니다.</em></h2>
      </div>
      <p>서울인디게임즈는 강연을 듣고 명함을 돌리는 자리가 아닙니다. 목표 한 줄을 적고, 에이전트와 구현하고, 플레이되는 화면으로 확인하는 인디게임 스터디입니다.</p>
    </div>

    <div class="spirit-grid">
      <article class="spirit-card spirit-card--cyan">
        <span class="card-index">01</span>
        <div class="pixel-icon" aria-hidden="true">▦</div>
        <h3>한 줄로 시작</h3>
        <p>거대한 기획서보다 오늘의 실험이 먼저입니다. 이번 자리에 끝낼 가장 작은 목표 한 줄이면 충분합니다.</p>
      </article>
      <article class="spirit-card spirit-card--violet">
        <span class="card-index">02</span>
        <div class="pixel-icon" aria-hidden="true">◆</div>
        <h3>에이전트가 같이</h3>
        <p>에이전트 IDE를 켜고, 시킨 일과 나온 결과를 같이 봅니다. 흐름을 타는 것과 결과를 검증하는 것을 둘 다 연습합니다.</p>
      </article>
      <article class="spirit-card spirit-card--pink">
        <span class="card-index">03</span>
        <div class="pixel-icon" aria-hidden="true">◫</div>
        <h3>빌드로 확인</h3>
        <p>설명으로 끝내지 않습니다. 움직여 보는 빌드가 나와야 공부가 끝납니다. 보여 주고 싶은 범위만 열어 같이 플레이합니다.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--lab" id="ai-lab" aria-labelledby="lab-title">
  <div class="home-container">
    <div class="section-heading">
      <p class="eyebrow">02 · VIBE CODING STUDY</p>
      <h2 id="lab-title">목표 한 줄에서<br><em>플레이되는 빌드까지.</em></h2>
      <p>정해진 요일과 시각은 없습니다. 강남역에 모이면 오늘 만들 것을 정하고, 에이전트와 구현한 뒤 움직여 보는 빌드로 확인합니다.</p>
    </div>

    <div class="lab-terminal" aria-hidden="true">
      <span class="lab-terminal__prompt">study</span>
      <code>goal "플레이되는 한 판" → agent → build</code>
    </div>

    <div class="lab-layout">
      <ol class="study-board">
        <li>
          <span class="study-label">GOAL</span>
          <div>
            <h3>오늘 만들 한 줄</h3>
            <p>이번 자리에 끝낼 가장 작은 목표를 적습니다. 게임 한 장면, 조작 하나, 깨진 빌드의 다음 수정도 목표가 됩니다.</p>
          </div>
        </li>
        <li>
          <span class="study-label">AGENT</span>
          <div>
            <h3>에이전트와 구현</h3>
            <p>에이전트 IDE에 일을 맡기고, 나온 코드와 씬을 그대로 믿지 않고 같이 읽습니다. 바이브로 시작해도 결과는 사람이 확인합니다.</p>
          </div>
        </li>
        <li>
          <span class="study-label">PLAY</span>
          <div>
            <h3>움직여 보는 빌드</h3>
            <p>설명 슬라이드 대신 실행되는 화면을 엽니다. 보여 주고 싶은 범위만 플레이하고, 다음 수정에 쓸 말을 남깁니다.</p>
          </div>
        </li>
        <li>
          <span class="study-label">TRACE</span>
          <div>
            <h3>남길 실험</h3>
            <p>어떤 프롬프트가 통했는지, 어디서 막혔는지, 다음에 시도할 한 가지를 적습니다. 완성이 아니라 다음 실험이 기록입니다.</p>
          </div>
        </li>
      </ol>

      <div class="lab-topics" aria-label="스터디에서 다루는 것">
        <article class="lab-topic">
          <span>VIBE</span>
          <h3>흐름으로 시작</h3>
          <p>목표를 먼저 두고 만들면서 길을 찾습니다. 스펙을 전부 쓴 뒤에야 움직이는 자리를 지향하지 않습니다.</p>
        </article>
        <article class="lab-topic">
          <span>AGENTIC</span>
          <h3>시킨 일과 결과</h3>
          <p>에이전트에게 맡긴 범위와 실제로 나온 결과를 나란히 봅니다. 빠른 생성보다 검증이 공부입니다.</p>
        </article>
        <article class="lab-topic">
          <span>INDIE</span>
          <h3>플레이가 과제</h3>
          <p>웹 페이지나 메모로 끝내지 않습니다. 인디게임의 조작, 장면, 루프가 움직여야 합니다.</p>
        </article>
        <article class="lab-topic">
          <span>GANGNAM</span>
          <h3>화면을 같이</h3>
          <p>각자 프로젝트를 가져옵니다. 강남역에 모이면 옆 사람의 빌드를 직접 눌러 보고, 막힌 워크플로를 나눕니다.</p>
        </article>
      </div>
    </div>

    <div class="meetup-note">
      <p><strong>처음이라면?</strong> 진행 중인 게임이 없어도 괜찮습니다. 작은 실험과 에이전트 IDE만 가져오세요. 회차 일정은 아래에서 확인합니다.</p>
      <div class="meetup-note__links">
        <a href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">Discord ↗</a>
        <a class="kakao-link" href="{{ site.kakao_url }}" target="_blank" rel="noopener noreferrer">카카오톡 오픈채팅 ↗</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--projects" id="projects" aria-labelledby="projects-title">
  <div class="home-container">
    <div class="section-heading section-heading--split">
      <div>
        <p class="eyebrow">03 · MAKERS IN PROGRESS</p>
        <h2 id="projects-title">지금 이 테이블에서<br><em>만들고 있는 게임들</em></h2>
      </div>
      <p>아이디어가 화면이 되고, 화면이 플레이가 되는 중간 과정을 공개합니다. 링크와 실제 빌드는 준비되는 순서대로 연결합니다.</p>
    </div>

    <article class="project-feature">
      <div class="project-feature__visual project-feature__visual--magrous">
        <picture class="magrous-art">
          <source srcset="{{ site.baseurl }}/images/magrous-story.webp" type="image/webp">
          <img src="{{ site.baseurl }}/images/magrous-story.jpg" alt="복셀 숲길에서 성배마차가 빛나는 포털을 향하는 메그러스 스토리 외전 ~TT원정대~ 키아트" width="768" height="1376" loading="lazy">
        </picture>
        <span class="project-state">PLAYABLE BUILD · 10 STAGES IN DEVELOPMENT</span>
        <p>GRAIL WAGON ESCORT<br>PORTRAIT ACTION</p>
      </div>

      <div class="project-feature__copy">
        <p class="project-kicker">FEATURED MAKER PROJECT</p>
        <h3>메그러스 스토리 외전 ~TT원정대~</h3>
        <p class="project-tagline">자동 전진하는 성배마차를 용병들이 호위하는 <strong>모바일 세로형 액션</strong> 게임입니다.</p>
        <p>플레이어는 4방향 격자 위를 누비며 직접 전투하고 적을 요격합니다. 아이템과 석궁 탄약을 모으고, 이동 트레일로 닫힌 고리를 만들어 영역을 점령하며 마차가 스테이지 끝에 도달하도록 지켜야 합니다.</p>
        <ul class="project-tags" aria-label="메그러스 스토리 외전 ~TT원정대~ 핵심 시스템">
          <li>4방향 격자 이동</li>
          <li>성배마차 호위</li>
          <li>직접 전투·적 요격</li>
          <li>아이템·석궁</li>
          <li>트레일 포위 점령</li>
          <li>10개 스테이지</li>
        </ul>
        <p class="project-strength">자동 전진하는 호위 목표의 압박과 플레이어가 마차 주변을 직접 누비는 조작을 결합합니다. 마차 곁을 지킬지, 아이템을 찾아 위험을 감수할지 매 순간 판단하는 것이 핵심입니다.</p>

        <div class="build-focus">
          <div>
            <span>CURRENT BUILD · UNITY MOBILE</span>
            <strong>STAGE 1–10 · DATA-DRIVEN</strong>
          </div>
          <ul>
            <li><span>01</span> 전사·궁수·힐러 편성</li>
            <li><span>02</span> 고블린·슬라임·보스 역할 확장</li>
            <li><span>03</span> Game Designer 레벨 제작 도구</li>
          </ul>
        </div>
      </div>
    </article>

    <article class="project-concept">
      <div>
        <p class="project-kicker">EARLY CONCEPT · PUZZLE ACTION</p>
        <h3>공항 터미널 궤적 퍼즐 <span>가제</span></h3>
      </div>
      <p>한 소녀가 재미있는 궤적을 활용해 공항 터미널의 문제를 풀고, 다양한 사람과 가면을 만나며 살아남는 퍼즐 액션 게임입니다. 터미널의 아이템을 모으고 NPC와 상호작용해 장애물을 넘으며 탈출 방법을 찾아갑니다.</p>
      <ul class="concept-signals" aria-label="핵심 콘셉트">
        <li>FUN TRAJECTORIES</li>
        <li>NPC &amp; MASKS</li>
        <li>TERMINAL SURVIVAL</li>
        <li>ESCAPE PUZZLES</li>
      </ul>
    </article>
  </div>
</section>

<section class="section section--people" aria-labelledby="people-title">
  <div class="home-container people-layout">
    <div class="section-heading">
      <p class="eyebrow">04 · WHO'S IN THE STUDY?</p>
      <h2 id="people-title">엔진도, 경력도 달라도<br><em>에이전트와 만든다면.</em></h2>
      <p>인디게임을 에이전트와 같이 실험하는 개발자, 워크플로를 바꾸는 제작자, 작은 프로토타입부터 시작하는 사람을 환영합니다.</p>
      <a class="text-link" href="mailto:{{ site.email }}">참여 전 궁금한 점 묻기 →</a>
    </div>

    <div class="people-list">
      <article><span>01</span><div><h3>에이전트로 실험하는 개발자</h3><p>시킨 일과 나온 빌드를 같이 읽고 다음 실험까지.</p></div></article>
      <article><span>02</span><div><h3>워크플로를 바꾸는 제작자</h3><p>이미 만들던 게임에 에이전틱 코딩을 붙여 검증합니다.</p></div></article>
      <article><span>03</span><div><h3>기획 · 아트도 같이</h3><p>코드만의 자리가 아닙니다. 장면과 연출도 에이전트와 시도합니다.</p></div></article>
      <article><span>04</span><div><h3>작은 프로토타입부터</h3><p>진행 중인 게임이 없어도, 한 줄 목표와 IDE면 시작할 수 있습니다.</p></div></article>
    </div>
  </div>
</section>

<section class="section section--news" id="news" aria-labelledby="news-title">
  <div class="home-container">
    <div class="section-heading section-heading--row">
      <div>
        <p class="eyebrow">05 · DEVLOG &amp; ARCHIVE</p>
        <h2 id="news-title">지난 기록</h2>
      </div>
      <p>실험과 실패도 다음 빌드의 재료로 남깁니다.</p>
    </div>

    <div class="post-grid">
      {% for post in site.posts limit: 3 %}
      <article class="post-card">
        <a href="{{ post.url | prepend: site.baseurl }}" aria-label="{{ post.title }}">
          <div class="post-card__cover post-card__cover--{{ forloop.index }}">
            <span>{% if post.event_status == "ended" %}PAST EVENT{% elsif post.event_status == "upcoming" %}NEXT EVENT{% else %}DEVLOG {{ forloop.index | prepend: '0' }}{% endif %}</span>
            <i aria-hidden="true"></i>
          </div>
          <div class="post-card__body">
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
            <h3>{{ post.title }}</h3>
            <span class="post-card__arrow" aria-hidden="true">↗</span>
          </div>
        </a>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section--principles" aria-labelledby="principles-title">
  <div class="home-container principles-layout">
    <div>
      <p class="eyebrow">COMMUNITY PRINCIPLES</p>
      <h2 id="principles-title">서로의 게임과 사람을<br>같이 존중합니다.</h2>
    </div>
    <ul>
      <li><span>01</span> 작업물과 IP는 각 창작자에게 있습니다.</li>
      <li><span>02</span> 피드백은 요청한 범위에서 구체적으로 나눕니다.</li>
      <li><span>03</span> 촬영·공개·빌드 공유는 먼저 동의를 구합니다.</li>
      <li><span>04</span> 차별, 괴롭힘, 무단 영업은 함께할 수 없습니다.</li>
      <li><span>05</span> 에이전트가 만든 코드와 에셋도 만든 사람의 작업입니다. 공개와 공유는 동의가 먼저입니다.</li>
    </ul>
  </div>
</section>

<section class="final-cta" aria-labelledby="cta-title">
  <div class="final-cta__grid" aria-hidden="true"></div>
  <div class="home-container">
    <p class="eyebrow eyebrow--glow">NEXT SESSION · DISCORD</p>
    <h2 id="cta-title">다음 스터디는<br><em>공지로 만납니다.</em></h2>
    <p>정해진 요일과 시각은 없습니다.<br>강남역 회차는 Discord와 카카오톡에서 안내합니다.</p>
    <div class="final-cta__actions">
      <a class="button button--primary button--large" href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">
        Discord 참여하기 <span aria-hidden="true">↗</span>
      </a>
      <a class="button button--kakao button--large" href="{{ site.kakao_url }}" target="_blank" rel="noopener noreferrer">
        카카오톡 오픈채팅 <span aria-hidden="true">↗</span>
      </a>
    </div>
  </div>
</section>
