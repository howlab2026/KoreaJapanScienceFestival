# 2-2. 상세기능 정의

## 기능 상세 동작 정의

### 1. 테마 전환 기능

```
[기능 ID] FR-007
[기능명] 다크/라이트 테마 전환
[트리거] 헤더 영역 테마 토글 버튼 클릭

[동작 흐름]
1. 사용자가 테마 토글 버튼(🌙/☀️) 클릭
2. 현재 body 클래스 확인
   - dark-theme → light-theme로 변경
   - light-theme → dark-theme로 변경
3. CSS Custom Properties 자동 전환
4. 아이콘 업데이트 (moon ↔ sun)
5. LocalStorage에 선택한 테마 저장
6. 페이지 재방문 시 저장된 테마 자동 적용

[CSS 변수 전환 항목]
- --bg-primary, --bg-secondary, --bg-tertiary
- --bg-card, --bg-card-hover
- --text-primary, --text-secondary, --text-muted
- --accent-primary, --accent-secondary
- --border-color, --border-color-hover
- --shadow-sm, --shadow-md, --shadow-lg
- --header-bg
```

### 2. 모바일 네비게이션 드로어

```
[기능 ID] FR-008
[기능명] 모바일 메뉴 드로어
[조건] 화면 너비 768px 미만

[동작 흐름]
1. 모바일 환경에서 햄버거 아이콘(☰) 표시
2. 클릭 시 상단에서 드로어 슬라이드 다운 (translateY 애니메이션)
3. 아이콘 변경: ☰ → ✕
4. 드로어 내 메뉴 링크 클릭 시:
   - 해당 섹션으로 스크롤
   - 드로어 자동 닫힘
   - 아이콘 복원: ✕ → ☰
```

### 3. 스크롤 리빌 애니메이션

```
[기능 ID] FR-009
[기능명] Intersection Observer 기반 스크롤 리빌
[대상] .reveal-fade 클래스를 가진 모든 요소

[동작 흐름]
1. DOMContentLoaded 시 모든 .reveal-fade 요소 감지
2. IntersectionObserver 등록 (threshold: 0.12)
3. 요소가 뷰포트 진입 시:
   - .revealed 클래스 추가
   - opacity: 0 → 1
   - transform: translateY(30px) → translateY(0)
   - 0.6s ease 트랜지션
4. 한 번 리빌된 요소는 unobserve (재실행 방지)
```

### 4. 통계 카운터 애니메이션

```
[기능 ID] FR-010
[기능명] 숫자 카운터 애니메이션
[대상] .stat-number 요소 (data-target 속성)

[동작 흐름]
1. IntersectionObserver로 .stat-number 요소 감지 (threshold: 0.5)
2. 뷰포트 진입 시 카운터 시작:
   - 시작값: 0
   - 목표값: data-target 속성값
   - 지속시간: 2000ms
   - 이징: easeOutExpo
3. 1,000 이상의 숫자는 toLocaleString()으로 콤마 포맷
4. 한 번 실행 후 unobserve
```

### 5. 파티클 배경 시스템

```
[기능 ID] FR-011
[기능명] 히어로 파티클 배경
[위치] #hero-particles 컨테이너

[동작 흐름]
1. DOMContentLoaded 시 파티클 생성
2. 40개의 div.particle 동적 생성
3. 각 파티클 속성:
   - 크기: 2~8px (랜덤)
   - 색상: 6가지 랜덤 선택 (#ff6b6b, #4facfe, #f093fb, #ffd93d, #00f2fe, #ff9a56)
   - 위치: left 0~100% (랜덤)
   - 애니메이션: particleFloat (10~25s, 랜덤 delay)
4. CSS keyframes로 하단→상단 이동 + 회전 + 페이드
```

### 6. 헤더 스크롤 상태

```
[기능 ID] FR-008-sub
[기능명] 스크롤 헤더 상태 변경

[동작 흐름]
1. window scroll 이벤트 리스너
2. scrollY > 50px:
   - header에 .scrolled 클래스 추가
   - 높이 72px → 64px 축소
   - 배경색 변경 (반투명 → 불투명)
   - box-shadow 추가
3. scrollY ≤ 50px:
   - .scrolled 클래스 제거
   - 원래 상태 복원
```

### 7. 활성 네비게이션 하이라이트

```
[기능 ID] FR-008-sub2
[기능명] 현재 섹션 네비 하이라이트

[동작 흐름]
1. window scroll 이벤트에서 모든 section[id] 순회
2. 현재 scrollY와 각 섹션의 offsetTop 비교
3. 현재 활성 섹션의 ID와 일치하는 nav-link에 .active 추가
4. 나머지 nav-link에서 .active 제거
5. .active 상태: 색상 변경 + 하단 언더라인 애니메이션
```
