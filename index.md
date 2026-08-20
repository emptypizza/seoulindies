---
layout: home
title: 서울인디게임즈
description: 매주 토요일 오후 2시, 서울에서 각자의 인디게임을 만들고 플레이테스트하는 정기 오픈 스튜디오.
---

<section class="home-hero" aria-labelledby="hero-title">
  <picture class="home-hero__art" aria-hidden="true">
    <source srcset="{{ site.baseurl }}/images/seoul-indies-hero.webp" type="image/webp">
    <img src="{{ site.baseurl }}/images/seoul-indies-hero.jpg" alt="" width="1672" height="941" fetchpriority="high">
  </picture>
  <div class="home-hero__wash"></div>
  <div class="pixel-corner pixel-corner--top" aria-hidden="true"></div>
  <div class="pixel-corner pixel-corner--bottom" aria-hidden="true"></div>

  <div class="home-container home-hero__inner">
    <div class="hero-copy">
      <p class="eyebrow eyebrow--glow"><span></span> SEOUL · SATURDAY BUILD CLUB</p>
      <h1 id="hero-title">혼자 만들던 게임,<br><em>토요일엔 함께.</em></h1>
      <p class="hero-lead">서울의 인디게임 개발자들이 각자 만들고, 서로 플레이하고, 다음 빌드까지 연결하는 정기 오픈 스튜디오입니다.</p>

      <div class="hero-actions">
        <a class="button button--primary" href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">
          이번 토요일 참여하기 <span aria-hidden="true">↗</span>
        </a>
        <a class="button button--ghost" href="#meetup">모임 방식 보기 <span aria-hidden="true">↓</span></a>
      </div>

      <dl class="hero-facts" aria-label="정기 모임 정보">
        <div>
          <dt>WHEN</dt>
          <dd>{{ site.meeting_day }} <strong>{{ site.meeting_time }}</strong></dd>
        </div>
        <div>
          <dt>WHERE</dt>
          <dd>{{ site.meeting_place }}</dd>
        </div>
        <div>
          <dt>BRING</dt>
          <dd>노트북 · 만들던 것 · 열린 마음</dd>
        </div>
      </dl>
    </div>
  </div>
</section>

<div class="signal-strip" aria-label="서울인디게임즈 핵심 활동">
  <div>
    <span>EVERY SATURDAY</span><i>✦</i>
    <span>14:00 SEOUL</span><i>✦</i>
    <span>MAKE</span><i>✦</i>
    <span>PLAYTEST</span><i>✦</i>
    <span>SHIP THE NEXT BUILD</span>
  </div>
</div>

<section class="section section--spirit" id="spirit" aria-labelledby="spirit-title">
  <div class="home-container">
    <div class="section-heading section-heading--split">
      <div>
        <p class="eyebrow">01 · OUR INDIE SPIRIT</p>
        <h2 id="spirit-title">완성보다 먼저 필요한 건<br><em>계속 만드는 리듬</em>입니다.</h2>
      </div>
      <p>서울인디게임즈는 강연을 듣고 명함을 돌리는 자리가 아닙니다. 작은 프로토타입도 테이블 위에 올리고, 직접 눌러 보고, 다음 한 걸음을 정하는 제작자들의 주간 베이스캠프입니다.</p>
    </div>

    <div class="spirit-grid">
      <article class="spirit-card spirit-card--cyan">
        <span class="card-index">01</span>
        <div class="pixel-icon" aria-hidden="true">▦</div>
        <h3>완성 전이어도</h3>
        <p>아이디어 한 줄, 망가진 빌드, 회색 박스도 괜찮습니다. 보여 줄 수 있는 가장 작은 조각부터 시작합니다.</p>
      </article>
      <article class="spirit-card spirit-card--violet">
        <span class="card-index">02</span>
        <div class="pixel-icon" aria-hidden="true">◆</div>
        <h3>혼자 와도</h3>
        <p>팀을 억지로 만들지 않습니다. 각자의 프로젝트에 집중하고, 필요할 때 서로의 눈과 손을 빌립니다.</p>
      </article>
      <article class="spirit-card spirit-card--pink">
        <span class="card-index">03</span>
        <div class="pixel-icon" aria-hidden="true">◫</div>
        <h3>직접 플레이하기</h3>
        <p>말보다 빌드를 먼저 만집니다. 요청한 범위에서 구체적으로 피드백하고, 다음 버전을 함께 기다립니다.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--loop" id="meetup" aria-labelledby="loop-title">
  <div class="home-container">
    <div class="section-heading">
      <p class="eyebrow">02 · THE SATURDAY LOOP</p>
      <h2 id="loop-title">매주 토요일 오후 2시,<br><em>만들기 → 테스트 → 다음 빌드.</em></h2>
      <p>길게 발표하기보다 오늘 할 일을 작게 선언하고, 집중해서 만들고, 실제 화면을 함께 봅니다.</p>
    </div>

    <ol class="loop-timeline">
      <li>
        <span class="loop-step">STEP 01</span>
        <time datetime="14:00">14:00</time>
        <div>
          <h3>체크인 · 오늘의 한 줄</h3>
          <p>지금 만드는 것과 오늘 끝낼 가장 작은 목표를 나눕니다.</p>
        </div>
      </li>
      <li>
        <span class="loop-step">STEP 02</span>
        <span class="loop-time">FOCUS</span>
        <div>
          <h3>집중 제작</h3>
          <p>코드, 아트, 기획, 사운드—각자의 방식으로 조용히 진전시킵니다.</p>
        </div>
      </li>
      <li>
        <span class="loop-step">STEP 03</span>
        <span class="loop-time">PLAY</span>
        <div>
          <h3>빌드 플레이 · 피드백</h3>
          <p>보여 주고 싶은 범위만 열어 서로 플레이합니다. 감상이 아니라 다음 수정에 쓸 말을 남깁니다.</p>
        </div>
      </li>
      <li>
        <span class="loop-step">STEP 04</span>
        <span class="loop-time">NEXT</span>
        <div>
          <h3>다음 빌드 약속</h3>
          <p>오늘 만든 것과 다음 주까지의 한 걸음을 기록합니다. 완성보다 연속성을 챙깁니다.</p>
        </div>
      </li>
    </ol>

    <div class="meetup-note">
      <p><strong>처음이라면?</strong> 작업 중인 프로젝트가 없어도 괜찮습니다. 작은 실험이나 배우고 싶은 도구를 가져오세요.</p>
      <a href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">회차별 장소·참가 안내 확인 ↗</a>
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
      <div class="project-feature__visual project-feature__visual--paper">
        <span class="project-state">PLAYABLE DIRECTION · IN DEVELOPMENT</span>
        <div class="paper-stage" aria-hidden="true">
          <span class="paper-sun"></span>
          <span class="paper-castle"></span>
          <span class="paper-hero">♞</span>
          <span class="paper-unit paper-unit--one">▲</span>
          <span class="paper-unit paper-unit--two">●</span>
          <span class="paper-enemy">◆</span>
          <span class="paper-ground"></span>
        </div>
        <p>DREAM ENERGY<br>SUMMON DEFENSE</p>
      </div>

      <div class="project-feature__copy">
        <p class="project-kicker">FEATURED MAKER PROJECT</p>
        <h3>PaperHeroes</h3>
        <p class="project-tagline">꿈에너지로 종이 용병을 소환하고, 플레이어가 전선 위 영웅을 직접 조작해 적의 공세를 돌파하는 <strong>영웅 주도 소환 디펜스</strong> 게임입니다.</p>
        <p>방과 후 교실과 꿈속 전장을 배경으로, 악몽의 침공에 맞서는 용사 아이들의 상상 전투를 그립니다. 영웅의 위치와 스킬 타이밍, 용병 소환 순서, 속성 상성, 전선 유지 판단이 맞물려 매 순간 선택을 요구합니다.</p>
        <ul class="project-tags" aria-label="PaperHeroes 핵심 시스템">
          <li>꿈에너지 소환</li>
          <li>영웅 스킬·오라</li>
          <li>역할 조합</li>
          <li>속성 상성</li>
          <li>웨이브·보스전</li>
        </ul>
        <p class="project-strength">귀여운 종이공작풍 비주얼과 Paladog식 소환 액션 디펜스의 재미를 결합해, 자동 전투의 전략성과 직접 조작의 손맛을 함께 만드는 것이 목표입니다.</p>

        <div class="build-focus">
          <div>
            <span>THIS WEEK · 경환</span>
            <strong>Rail Crusade Defense 기반</strong>
          </div>
          <ul>
            <li><span>01</span> 레벨 1·2·3 디자인</li>
            <li><span>02</span> 반장 개입 시스템</li>
            <li><span>03</span> 레벨 디자인 도구 개발</li>
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
      <p class="eyebrow">04 · WHO'S AT THE TABLE?</p>
      <h2 id="people-title">엔진도, 경력도 달라도<br><em>만드는 사람이라면.</em></h2>
      <p>인디게임 개발자, 사이드프로젝트 팀, 지망생, 그리고 실제 빌드를 기꺼이 플레이해 줄 동료를 환영합니다.</p>
      <a class="text-link" href="mailto:{{ site.email }}">참여 전 궁금한 점 묻기 →</a>
    </div>

    <div class="people-list">
      <article><span>01</span><div><h3>혼자 만드는 개발자</h3><p>막힌 부분을 말로 정리하고 다음 커밋까지.</p></div></article>
      <article><span>02</span><div><h3>사이드프로젝트 팀</h3><p>주간 리듬을 만들고 새 빌드를 빠르게 검증합니다.</p></div></article>
      <article><span>03</span><div><h3>학생 · 지망생</h3><p>작은 프로토타입부터 실제 만드는 습관을 시작합니다.</p></div></article>
      <article><span>04</span><div><h3>아트 · 사운드 · 기획</h3><p>코드만이 게임은 아닙니다. 각자의 전문성을 연결합니다.</p></div></article>
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
            <span>{% if post.event_status == "ended" %}PAST EVENT{% else %}DEVLOG {{ forloop.index | prepend: '0' }}{% endif %}</span>
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
    </ul>
  </div>
</section>

<section class="final-cta" aria-labelledby="cta-title">
  <div class="final-cta__grid" aria-hidden="true"></div>
  <div class="home-container">
    <p class="eyebrow eyebrow--glow">NEXT SATURDAY · 14:00</p>
    <h2 id="cta-title">만들던 게임을<br><em>그대로 들고 오세요.</em></h2>
    <p>완성품보다 다음 버전을 기대합니다.<br>서울에서, 이번 토요일에 만나요.</p>
    <a class="button button--primary button--large" href="{{ site.join_url }}" target="_blank" rel="noopener noreferrer">
      서울인디게임즈 참여하기 <span aria-hidden="true">↗</span>
    </a>
  </div>
</section>
