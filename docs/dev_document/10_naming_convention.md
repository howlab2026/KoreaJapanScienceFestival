# 10. 네이밍 규칙

> 완료보고서의 [4-3. 네이밍 규칙](../completion_report/04-3_naming_convention.md)과 동일한 내용입니다.

## 네이밍 규칙 요약

### 파일 네이밍
- HTML/CSS/JS: **kebab-case** (소문자 + 하이픈)
- 이미지: **snake_case** (소문자 + 언더스코어)
- 문서: **번호_snake_case** (번호 접두사)

### HTML 네이밍
- ID: **kebab-case** (예: `main-header`, `theme-toggle`)
- Class: **BEM 변형** (예: `.festival-info-card`, `.btn-primary`)
- State: `.active`, `.scrolled`, `.open`, `.revealed`

### CSS 네이밍
- Custom Properties: **카테고리 접두사** (예: `--bg-primary`, `--text-secondary`)
- 카테고리: `--bg-`, `--text-`, `--accent-`, `--shadow-`, `--font-`, `--spacing-`, `--transition-`, `--border-`

### JavaScript 네이밍
- 변수/함수: **camelCase** (예: `themeToggleBtn`, `updateThemeIcon()`)
- Boolean: **is/has 접두사** (예: `isOpen`, `isKorean`)
- DOM 요소: **camelCase** (예: `menuIcon`, `header`)

### 코드 컨벤션
| 항목 | 규칙 |
|------|------|
| 들여쓰기 | 4 spaces |
| 줄 끝 | LF |
| 인코딩 | UTF-8 |
| CSS 선언 순서 | Layout → Box Model → Typography → Visual → Animation |
| JS 세미콜론 | 사용 |
| JS 따옴표 | 작은따옴표 ('), 템플릿 리터럴은 백틱 (`) |
