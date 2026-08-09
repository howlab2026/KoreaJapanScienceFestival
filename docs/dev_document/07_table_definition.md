# 7. 테이블 정의서

## FESTIVAL 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | festival_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 제전 ID |
| 2 | festival_name | VARCHAR | 100 | NOT NULL | | | | 제전명(한) |
| 3 | festival_name_jp | VARCHAR | 100 | NULL | | | | 제전명(일) |
| 4 | festival_name_en | VARCHAR | 100 | NULL | | | | 제전명(영) |
| 5 | city | VARCHAR | 50 | NOT NULL | | | | 도시 |
| 6 | organizer | VARCHAR | 200 | NULL | | | | 주최기관 |
| 7 | target_audience | VARCHAR | 200 | NULL | | | | 대상 |
| 8 | admission_fee | VARCHAR | 100 | NULL | | | '무료' | 참가비 |
| 9 | annual_visitors | INT | 11 | NULL | | | 0 | 방문객수 |
| 10 | description | TEXT | - | NULL | | | | 설명 |
| 11 | badge_color | VARCHAR | 50 | NULL | | | | 배지색상 |
| 12 | created_at | DATETIME | - | NOT NULL | | | CURRENT_TIMESTAMP | 생성일 |
| 13 | updated_at | DATETIME | - | NOT NULL | | | CURRENT_TIMESTAMP | 수정일 |

---

## PROGRAM 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | program_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 프로그램ID |
| 2 | festival_id | INT | 11 | NOT NULL | | ✅ | | 제전ID |
| 3 | program_name | VARCHAR | 100 | NOT NULL | | | | 프로그램명 |
| 4 | icon_class | VARCHAR | 100 | NULL | | | | 아이콘 |
| 5 | description | TEXT | - | NULL | | | | 설명 |
| 6 | display_order | INT | 3 | NOT NULL | | | 0 | 순서 |

---

## SCHEDULE 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | schedule_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 일정ID |
| 2 | festival_id | INT | 11 | NOT NULL | | ✅ | | 제전ID |
| 3 | event_name | VARCHAR | 200 | NOT NULL | | | | 행사명 |
| 4 | start_date | DATE | - | NOT NULL | | | | 시작일 |
| 5 | end_date | DATE | - | NOT NULL | | | | 종료일 |
| 6 | start_time | TIME | - | NULL | | | | 시작시간 |
| 7 | end_time | TIME | - | NULL | | | | 종료시간 |
| 8 | year | CHAR | 4 | NOT NULL | | | | 연도 |
| 9 | note | TEXT | - | NULL | | | | 비고 |

---

## VENUE 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | venue_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 장소ID |
| 2 | venue_name | VARCHAR | 200 | NOT NULL | | | | 장소명(한) |
| 3 | venue_name_jp | VARCHAR | 200 | NULL | | | | 장소명(일) |
| 4 | address | VARCHAR | 500 | NOT NULL | | | | 주소(한) |
| 5 | address_jp | VARCHAR | 500 | NULL | | | | 주소(일) |
| 6 | phone | VARCHAR | 20 | NULL | | | | 전화번호 |
| 7 | website | VARCHAR | 300 | NULL | | | | 웹사이트 |
| 8 | latitude | DECIMAL | 10,7 | NULL | | | | 위도 |
| 9 | longitude | DECIMAL | 10,7 | NULL | | | | 경도 |
| 10 | operating_hours | VARCHAR | 200 | NULL | | | | 운영시간 |

---

## ACCESS_ROUTE 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | route_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 경로ID |
| 2 | venue_id | INT | 11 | NOT NULL | | ✅ | | 장소ID |
| 3 | transport_type | VARCHAR | 50 | NOT NULL | | | | 교통수단 |
| 4 | line_name | VARCHAR | 100 | NULL | | | | 노선명 |
| 5 | station_name | VARCHAR | 100 | NULL | | | | 역명 |
| 6 | walking_time | VARCHAR | 50 | NULL | | | | 도보시간 |
| 7 | description | TEXT | - | NULL | | | | 설명 |

---

## GALLERY_IMAGE 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | image_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 이미지ID |
| 2 | festival_id | INT | 11 | NOT NULL | | ✅ | | 제전ID |
| 3 | image_path | VARCHAR | 500 | NOT NULL | | | | 경로 |
| 4 | caption | VARCHAR | 200 | NULL | | | | 캡션 |
| 5 | icon_class | VARCHAR | 100 | NULL | | | | 아이콘 |
| 6 | is_large | BOOLEAN | - | NOT NULL | | | FALSE | 큰이미지 |
| 7 | display_order | INT | 3 | NOT NULL | | | 0 | 순서 |

---

## HISTORY 테이블

| 번호 | 컬럼명 | 데이터 타입 | 크기 | NULL | PK | FK | 기본값 | 설명 |
|------|--------|------------|------|------|-----|-----|--------|------|
| 1 | history_id | INT | 11 | NOT NULL | ✅ | | AUTO_INCREMENT | 연혁ID |
| 2 | festival_id | INT | 11 | NOT NULL | | ✅ | | 제전ID |
| 3 | year | VARCHAR | 20 | NOT NULL | | | | 연도 |
| 4 | title | VARCHAR | 200 | NOT NULL | | | | 제목 |
| 5 | description | TEXT | - | NULL | | | | 설명 |
| 6 | display_order | INT | 3 | NOT NULL | | | 0 | 순서 |
