# 14. 클래스경로

## JavaScript 모듈/함수 경로

| 파일 | 경로 | 역할 |
|------|------|------|
| script.js | `js/script.js` | 메인 JavaScript (단일 파일) |

### script.js 내부 모듈 경로

```
js/script.js
├── DOMContentLoaded 이벤트 리스너 (L1)
│
├── Theme Toggle Module (L4~L32)
│   ├── themeToggleBtn ← getElementById('theme-toggle')
│   ├── themeIcon ← querySelector('i')
│   ├── savedTheme ← localStorage.getItem('theme')
│   └── function updateThemeIcon(theme) (L26~L28)
│
├── Mobile Navigation Module (L34~L53)
│   ├── mobileMenuBtn ← getElementById('mobile-menu-btn')
│   ├── mobileDrawer ← getElementById('mobile-drawer')
│   └── menuIcon ← querySelector('i')
│
├── Header & Nav Scroll Module (L55~L80)
│   ├── header ← getElementById('main-header')
│   ├── sections ← querySelectorAll('section[id]')
│   └── navLinks ← querySelectorAll('.nav-link')
│
├── Scroll Reveal Module (L82~L96)
│   ├── revealElements ← querySelectorAll('.reveal-fade')
│   └── revealObserver ← new IntersectionObserver()
│
├── Stat Counter Module (L98~L130)
│   ├── statNumbers ← querySelectorAll('.stat-number')
│   ├── statObserver ← new IntersectionObserver()
│   └── function animateCounter(el) (L109~L128)
│
├── Particle System Module (L132~L158)
│   ├── particleContainer ← getElementById('hero-particles')
│   └── function createParticles() (L137~L157)
│
├── Language Toggle Module (L160~L168)
│   └── langToggle ← getElementById('lang-toggle')
│
└── Smooth Scroll Module (L170~L183)
    └── querySelectorAll('a[href^="#"]')
```

## CSS 클래스 경로

### css/style.css 섹션 구조

```
css/style.css
├── CSS Variables & Design Tokens (L1~L80)
│   ├── :root (공통)
│   ├── .dark-theme
│   └── .light-theme
│
├── Global Reset & Base (L82~L120)
│
├── Typography (L122~L190)
│   ├── .gradient-text
│   ├── .section-header / .section-title / .section-underline
│   ├── .badge
│   └── .btn / .btn-primary / .btn-secondary / .btn-lg
│
├── Header & Navigation (L192~L270)
│   ├── .header / .header.scrolled
│   ├── .nav-container / .nav-links / .nav-link
│   ├── .icon-btn / .mobile-menu-btn
│   └── .mobile-drawer / .mobile-nav-links
│
├── Hero Section (L272~L380)
│   ├── .hero-section / .hero-particles / .particle
│   ├── .hero-glow-1 / .hero-glow-2 / .hero-glow-3
│   ├── .hero-container / .hero-content
│   ├── .hero-stats / .stat-number / .stat-label
│   └── .scroll-indicator / .mouse-icon / .wheel
│
├── About Section (L382~L440)
│   ├── .about-grid
│   └── .about-card / .about-icon-wrap
│
├── Festival Sections (L442~L550)
│   ├── .festival-section / .tokyo-section
│   ├── .festival-showcase / .festival-showcase.reverse
│   ├── .festival-info-card / .festival-badge
│   ├── .festival-details-grid / .detail-item
│   └── .program-list / .program-card / .program-icon
│
├── Comparison Table (L552~L600)
│   └── .compare-table / .tokyo-col / .osaka-col
│
├── Timeline (L602~L665)
│   ├── .timeline / .timeline-item / .timeline-dot
│   ├── .tokyo-dot / .osaka-dot
│   └── .timeline-badge / .timeline-tags / .tag
│
├── Access Section (L667~L720)
│   ├── .access-grid / .access-card
│   ├── .access-card-header / .tokyo-header / .osaka-header
│   └── .access-routes
│
├── Gallery Section (L722~L770)
│   ├── .gallery-grid / .gallery-item / .gallery-item-lg
│   ├── .gallery-placeholder
│   └── .gallery-overlay
│
├── Footer (L772~L830)
│   ├── .footer / .footer-top
│   ├── .footer-brand / .footer-nav
│   └── .footer-bottom
│
├── Reveal Animation (L832~L845)
│   └── .reveal-fade / .reveal-fade.revealed
│
├── Keyframe Animations (L847~L870)
│
└── Responsive Design (L872~END)
    ├── @media (max-width: 1024px)
    ├── @media (max-width: 768px)
    └── @media (max-width: 480px)
```
