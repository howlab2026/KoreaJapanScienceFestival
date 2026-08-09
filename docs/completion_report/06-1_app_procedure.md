# 6-1. 어플리케이션 프로시저

## 주요 함수/프로시저 목록

| 번호 | 함수명 | 위치 | 역할 |
|------|--------|------|------|
| 1 | `updateThemeIcon(theme)` | script.js | 테마 아이콘 업데이트 |
| 2 | `animateCounter(el)` | script.js | 숫자 카운터 애니메이션 |
| 3 | `createParticles()` | script.js | 히어로 파티클 생성 |
| 4 | (anonymous) `themeToggleBtn.click` | script.js | 테마 토글 이벤트 |
| 5 | (anonymous) `mobileMenuBtn.click` | script.js | 모바일 메뉴 토글 |
| 6 | (anonymous) `window.scroll` | script.js | 헤더 상태 & 네비 하이라이트 |
| 7 | (anonymous) `revealObserver` | script.js | 스크롤 리빌 Observer |
| 8 | (anonymous) `statObserver` | script.js | 카운터 Observer |

## 프로시저 상세

### 1. updateThemeIcon(theme)

```javascript
/**
 * @description 테마에 따라 토글 버튼 아이콘을 변경
 * @param {string} theme - 'dark' 또는 'light'
 * @returns {void}
 * 
 * 동작:
 * - light → fa-sun (☀️) 아이콘
 * - dark → fa-moon (🌙) 아이콘
 */
function updateThemeIcon(theme) {
    themeIcon.className = theme === 'light' 
        ? 'fa-solid fa-sun' 
        : 'fa-solid fa-moon';
}
```

### 2. animateCounter(el)

```javascript
/**
 * @description 숫자를 0에서 목표값까지 카운트업 애니메이션
 * @param {HTMLElement} el - .stat-number 요소 (data-target 속성 필요)
 * @returns {void}
 * 
 * 알고리즘:
 * 1. data-target에서 목표값 추출
 * 2. requestAnimationFrame으로 매 프레임 업데이트
 * 3. easeOutExpo 이징 함수 적용
 * 4. 1000 이상 숫자는 toLocaleString()으로 콤마 포맷
 * 5. progress >= 1이면 종료
 * 
 * 소요 시간: 2000ms
 */
function animateCounter(el) { ... }
```

### 3. createParticles()

```javascript
/**
 * @description 히어로 섹션에 떠다니는 파티클 생성
 * @returns {void}
 * 
 * 동작:
 * 1. 6가지 색상 배열에서 랜덤 선택
 * 2. 40개의 div.particle 동적 생성
 * 3. 각 파티클에 랜덤 속성 (크기, 위치, 속도, 딜레이)
 * 4. CSS particleFloat 키프레임으로 애니메이션
 * 
 * 파티클 속성 범위:
 * - 크기: 2~8px
 * - 위치: left 0~100%
 * - 애니메이션 시간: 10~25s
 * - 딜레이: 0~15s
 */
function createParticles() { ... }
```

### 4. 테마 토글 이벤트

```javascript
/**
 * @description 다크/라이트 테마 전환 처리
 * @event click on #theme-toggle
 * 
 * 동작:
 * 1. body의 현재 클래스 확인 (dark-theme / light-theme)
 * 2. classList.replace()로 테마 클래스 교체
 * 3. LocalStorage에 테마 저장
 * 4. updateThemeIcon() 호출
 */
```

### 5. 스크롤 이벤트 핸들러

```javascript
/**
 * @description 스크롤 시 헤더 상태 변경 및 네비게이션 하이라이트
 * @event scroll on window
 * 
 * 동작 1 - 헤더:
 * - scrollY > 50px: .scrolled 클래스 추가
 * - scrollY <= 50px: .scrolled 클래스 제거
 * 
 * 동작 2 - 네비 하이라이트:
 * - 모든 section[id] 순회
 * - offsetTop - 120px 기준으로 현재 섹션 판별
 * - 해당 nav-link에 .active 클래스 추가
 */
```

## 이벤트 리스너 매핑

| 이벤트 타입 | 대상 요소 | 핸들러 | 비고 |
|------------|-----------|--------|------|
| `DOMContentLoaded` | document | 전체 초기화 | 진입점 |
| `click` | #theme-toggle | 테마 토글 | |
| `click` | #mobile-menu-btn | 모바일 메뉴 토글 | |
| `click` | .mobile-nav-link | 드로어 닫기 | forEach |
| `click` | a[href^="#"] | 스무스 스크롤 | forEach |
| `click` | #lang-toggle | 언어 토글 | placeholder |
| `scroll` | window | 헤더 상태 + 네비 | |
| `intersect` | .reveal-fade | 스크롤 리빌 | IntersectionObserver |
| `intersect` | .stat-number | 카운터 애니메이션 | IntersectionObserver |
