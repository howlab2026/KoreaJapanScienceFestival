# 4. 데이터사전

## 데이터 항목 사전

### 1. 제전(Festival) 데이터

| 항목명 | 영문명 | 데이터 타입 | 크기 | 필수 | 설명 | 예시 |
|--------|--------|------------|------|------|------|------|
| 제전ID | festival_id | INT | 11 | Y | 고유 식별자 | 1, 2 |
| 제전명 | festival_name | VARCHAR | 100 | Y | 한국어 제전명 | "동경과학제전" |
| 제전명(일) | festival_name_jp | VARCHAR | 100 | N | 일본어 제전명 | "東京科学祭典" |
| 제전명(영) | festival_name_en | VARCHAR | 100 | N | 영문 제전명 | "Tokyo Science Festival" |
| 도시 | city | VARCHAR | 50 | Y | 개최 도시 | "도쿄", "오사카" |
| 주최기관 | organizer | VARCHAR | 200 | N | 주최 기관명 | "JST", "도쿄도" |
| 대상 | target_audience | VARCHAR | 200 | N | 참가 대상 | "초·중·고, 일반인" |
| 참가비 | admission_fee | VARCHAR | 100 | N | 입장/참가비 | "무료" |
| 연간방문객 | annual_visitors | INT | 11 | N | 연간 방문객 수 | 30000 |
| 설명 | description | TEXT | - | N | 제전 설명 | (텍스트) |
| 배지색상 | badge_color | VARCHAR | 50 | N | CSS 그라데이션 | "tokyo"/"osaka" |

### 2. 프로그램(Program) 데이터

| 항목명 | 영문명 | 데이터 타입 | 크기 | 필수 | 설명 | 예시 |
|--------|--------|------------|------|------|------|------|
| 프로그램ID | program_id | INT | 11 | Y | 고유 식별자 | 1 |
| 소속제전ID | festival_id | INT | 11 | Y | FK → FESTIVAL | 1 |
| 프로그램명 | program_name | VARCHAR | 100 | Y | 프로그램명 | "과학 실험 체험" |
| 아이콘클래스 | icon_class | VARCHAR | 100 | N | FA 아이콘 | "fa-solid fa-flask" |
| 설명 | description | TEXT | - | N | 프로그램 설명 | (텍스트) |
| 표시순서 | display_order | INT | 3 | Y | 화면 표시 순서 | 1, 2, 3 |

### 3. 일정(Schedule) 데이터

| 항목명 | 영문명 | 데이터 타입 | 크기 | 필수 | 설명 | 예시 |
|--------|--------|------------|------|------|------|------|
| 일정ID | schedule_id | INT | 11 | Y | 고유 식별자 | 1 |
| 소속제전ID | festival_id | INT | 11 | Y | FK → FESTIVAL | 1 |
| 행사명 | event_name | VARCHAR | 200 | Y | 행사명 | "Tokyo ふしぎ祭エンス 2026" |
| 시작일 | start_date | DATE | - | Y | 시작일 | 2026-04-18 |
| 종료일 | end_date | DATE | - | Y | 종료일 | 2026-04-19 |
| 시작시간 | start_time | TIME | - | N | 시작 시간 | 10:00 |
| 종료시간 | end_time | TIME | - | N | 종료 시간 | 17:00 |
| 연도 | year | CHAR | 4 | Y | 연도 | "2026" |
| 비고 | note | TEXT | - | N | 비고 사항 | "사전예약 권장" |

### 4. 장소(Venue) 데이터

| 항목명 | 영문명 | 데이터 타입 | 크기 | 필수 | 설명 | 예시 |
|--------|--------|------------|------|------|------|------|
| 장소ID | venue_id | INT | 11 | Y | 고유 식별자 | 1 |
| 장소명 | venue_name | VARCHAR | 200 | Y | 한국어명 | "일본과학미래관" |
| 장소명(일) | venue_name_jp | VARCHAR | 200 | N | 일본어명 | "日本科学未来館" |
| 주소 | address | VARCHAR | 500 | Y | 한국어 주소 | (주소) |
| 전화번호 | phone | VARCHAR | 20 | N | 전화번호 | "03-3570-9151" |
| 위도 | latitude | DECIMAL | 10,7 | N | 위도 | 35.6195 |
| 경도 | longitude | DECIMAL | 10,7 | N | 경도 | 139.7763 |

### 5. 교통편(Access Route) 데이터

| 항목명 | 영문명 | 데이터 타입 | 크기 | 필수 | 설명 | 예시 |
|--------|--------|------------|------|------|------|------|
| 경로ID | route_id | INT | 11 | Y | 고유 식별자 | 1 |
| 장소ID | venue_id | INT | 11 | Y | FK → VENUE | 1 |
| 교통수단 | transport_type | VARCHAR | 50 | Y | 교통수단 | "전철", "버스" |
| 노선명 | line_name | VARCHAR | 100 | N | 노선명 | "유리카모메선" |
| 역명 | station_name | VARCHAR | 100 | N | 역/정류장 | "텔레콤센터역" |
| 도보시간 | walking_time | VARCHAR | 50 | N | 도보 소요시간 | "4분" |

### 6. 설정(Settings) 데이터

| 항목명 | 영문명 | 저장소 | 키 | 값 | 설명 |
|--------|--------|--------|-----|-----|------|
| 테마설정 | theme | LocalStorage | `theme` | `"dark"` / `"light"` | 사용자 테마 선택 |
