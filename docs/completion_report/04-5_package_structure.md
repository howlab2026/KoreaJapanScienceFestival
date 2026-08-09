# 4-5. 패키지 구조

## 개요

본 프로젝트는 npm 패키지나 번들러를 사용하지 않는 순수 정적 웹사이트입니다.
JavaScript는 단일 파일(`script.js`)로 구성되며, 내부적으로 기능별 모듈 구조로 조직됩니다.

## JavaScript 모듈 구조

```
js/script.js
│
├── [Module] Theme Toggle
│   ├── themeToggleBtn
│   ├── updateThemeIcon()
│   └── LocalStorage 연동
│
├── [Module] Mobile Navigation
│   ├── mobileMenuBtn
│   ├── mobileDrawer
│   └── 링크 클릭 시 자동 닫기
│
├── [Module] Header Scroll & Nav Highlight
│   ├── scroll 이벤트 리스너
│   ├── header.scrolled 토글
│   └── navLink.active 업데이트
│
├── [Module] Scroll Reveal Animation
│   ├── IntersectionObserver
│   └── .reveal-fade → .revealed
│
├── [Module] Stat Counter Animation
│   ├── IntersectionObserver
│   ├── animateCounter()
│   └── easeOutExpo 이징
│
├── [Module] Particle System
│   ├── createParticles()
│   └── DOM 동적 생성 (40개 파티클)
│
├── [Module] Language Toggle (Placeholder)
│   └── isKorean 상태 토글
│
└── [Module] Smooth Scroll
    └── anchor 링크 클릭 핸들러
```

## CSS 구조

```
css/style.css
│
├── [Section] CSS Variables & Design Tokens
│   ├── :root (공통 변수)
│   ├── .dark-theme (다크 테마 변수)
│   └── .light-theme (라이트 테마 변수)
│
├── [Section] Global Reset & Base
│
├── [Section] Typography & Accents
│   ├── 제목 스타일 (h1~h6)
│   ├── .gradient-text
│   ├── .section-header / .section-title
│   └── .badge / .btn
│
├── [Section] Header & Navigation
│   ├── .header / .nav-container
│   ├── .nav-link
│   ├── .mobile-drawer
│   └── .icon-btn
│
├── [Section] Hero Section
│   ├── .hero-section
│   ├── .hero-particles / .particle
│   ├── .hero-glow
│   ├── .hero-stats
│   └── .scroll-indicator
│
├── [Section] About Section
│   ├── .about-grid
│   └── .about-card
│
├── [Section] Festival Sections (Tokyo & Osaka)
│   ├── .festival-showcase
│   ├── .festival-info-card
│   ├── .festival-badge
│   ├── .festival-details-grid
│   └── .program-card
│
├── [Section] Comparison Table
│   └── .compare-table
│
├── [Section] Timeline / Schedule
│   ├── .timeline
│   ├── .timeline-item
│   └── .timeline-badge
│
├── [Section] Access Section
│   ├── .access-grid
│   └── .access-card
│
├── [Section] Gallery Section
│   ├── .gallery-grid
│   ├── .gallery-item
│   └── .gallery-overlay
│
├── [Section] Footer
│
├── [Section] Reveal Animation
│   └── .reveal-fade / .revealed
│
├── [Section] Keyframe Animations
│
└── [Section] Responsive Design
    ├── @media (max-width: 1024px)
    ├── @media (max-width: 768px)
    └── @media (max-width: 480px)
```

## 외부 패키지/의존성

| 패키지 | 버전 | 용도 | 로딩 방식 |
|--------|------|------|-----------|
| Google Fonts (Outfit) | latest | 영문 헤딩 폰트 | CDN `<link>` |
| Google Fonts (Noto Sans KR) | latest | 한국어 본문 폰트 | CDN `<link>` |
| Font Awesome | 6.5.0 | 아이콘 | CDN `<link>` |
