# 4-3. 네이밍 규칙

## 1. 파일 네이밍

| 대상 | 규칙 | 예시 |
|------|------|------|
| HTML 파일 | 소문자 + kebab-case | `index.html`, `tokyo.html` |
| CSS 파일 | 소문자 + kebab-case | `style.css` |
| JS 파일 | 소문자 + kebab-case | `script.js` |
| 이미지 파일 | 소문자 + snake_case | `hero_bg.jpg`, `tokyo_venue.png` |
| 문서 파일 | 번호 + snake_case | `01_project_info.md` |

## 2. HTML 네이밍

### ID 네이밍
| 규칙 | 설명 | 예시 |
|------|------|------|
| kebab-case | 모든 ID는 하이픈 구분 | `main-header`, `hero-particles` |
| 기능 접두사 | 역할을 접두사로 표시 | `btn-tokyo`, `tab-strengths` |
| 유일성 | 페이지 내 중복 금지 | `nav-logo`, `theme-toggle` |

### Class 네이밍 (BEM 변형)
| 유형 | 규칙 | 예시 |
|------|------|------|
| Block | kebab-case | `.hero-section`, `.festival-info-card` |
| Element | Block + 하이픈 | `.hero-content`, `.festival-desc` |
| Modifier | Block + 형용사 | `.btn-primary`, `.tokyo-badge` |
| State | 상태 접두사 | `.active`, `.scrolled`, `.open`, `.revealed` |
| Utility | 기능 접두사 | `.text-center`, `.section-padding` |

## 3. CSS 네이밍

### CSS Custom Properties (변수)
| 카테고리 | 접두사 | 예시 |
|----------|--------|------|
| 배경색 | `--bg-` | `--bg-primary`, `--bg-card` |
| 텍스트색 | `--text-` | `--text-primary`, `--text-secondary` |
| 강조색 | `--accent-` | `--accent-primary`, `--accent-tokyo` |
| 그라데이션 | `--accent-gradient-` | `--accent-gradient-tokyo` |
| 테두리 | `--border-` | `--border-color`, `--border-color-hover` |
| 그림자 | `--shadow-` | `--shadow-sm`, `--shadow-md` |
| 폰트 | `--font-` | `--font-heading`, `--font-body` |
| 간격 | `--spacing-` | `--spacing-sm`, `--spacing-lg` |
| 트랜지션 | `--transition-` | `--transition-fast`, `--transition-slow` |
| 보더라디우스 | `--border-radius-` | `--border-radius-sm`, `--border-radius-lg` |

## 4. JavaScript 네이밍

| 대상 | 규칙 | 예시 |
|------|------|------|
| 변수 | camelCase | `themeToggleBtn`, `mobileDrawer` |
| 함수 | camelCase (동사+명사) | `updateThemeIcon()`, `animateCounter()` |
| 상수 | camelCase | `savedTheme`, `revealElements` |
| DOM 요소 | camelCase + 약어 | `themeIcon`, `menuIcon`, `header` |
| 이벤트 핸들러 | 동사 접두사 | `handleClick`, `handleScroll` |
| Boolean 변수 | is/has 접두사 | `isOpen`, `isKorean` |

## 5. 디렉토리/폴더 네이밍

| 대상 | 규칙 | 예시 |
|------|------|------|
| 소스 폴더 | 소문자 | `css/`, `js/`, `pages/`, `images/` |
| 문서 폴더 | snake_case | `completion_report/`, `dev_document/` |
