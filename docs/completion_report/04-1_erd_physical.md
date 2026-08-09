# 4-1. ERD 물리모드

## 개요

본 프로젝트는 순수 프론트엔드 정적 웹사이트로 RDBMS를 사용하지 않습니다.
그러나 콘텐츠의 논리적 데이터 구조를 ERD로 표현하여 향후 CMS 연동 또는 백엔드 확장 시 참고합니다.

## ERD (물리 모델)

```mermaid
erDiagram
    FESTIVAL ||--o{ PROGRAM : "has"
    FESTIVAL ||--o{ SCHEDULE : "has"
    FESTIVAL ||--|| VENUE : "held_at"
    VENUE ||--o{ ACCESS_ROUTE : "has"
    FESTIVAL ||--o{ GALLERY_IMAGE : "has"
    FESTIVAL ||--o{ HISTORY : "has"

    FESTIVAL {
        int festival_id PK "제전 ID"
        varchar festival_name "제전명"
        varchar festival_name_jp "제전명 (일본어)"
        varchar festival_name_en "제전명 (영문)"
        varchar city "도시"
        varchar organizer "주최기관"
        varchar target_audience "대상"
        varchar admission_fee "참가비"
        int annual_visitors "연간 방문객"
        text description "설명"
        varchar badge_color "배지 색상 코드"
    }

    PROGRAM {
        int program_id PK "프로그램 ID"
        int festival_id FK "제전 ID"
        varchar program_name "프로그램명"
        varchar icon_class "아이콘 클래스"
        text description "설명"
        int display_order "표시 순서"
    }

    SCHEDULE {
        int schedule_id PK "일정 ID"
        int festival_id FK "제전 ID"
        varchar event_name "행사명"
        date start_date "시작일"
        date end_date "종료일"
        time start_time "시작시간"
        time end_time "종료시간"
        varchar year "연도"
        text note "비고"
    }

    VENUE {
        int venue_id PK "장소 ID"
        varchar venue_name "장소명"
        varchar venue_name_jp "장소명 (일본어)"
        varchar address "주소"
        varchar address_jp "주소 (일본어)"
        varchar phone "전화번호"
        varchar website "웹사이트"
        decimal latitude "위도"
        decimal longitude "경도"
        varchar operating_hours "운영시간"
    }

    ACCESS_ROUTE {
        int route_id PK "경로 ID"
        int venue_id FK "장소 ID"
        varchar transport_type "교통수단"
        varchar line_name "노선명"
        varchar station_name "역/정류장명"
        varchar walking_time "도보시간"
        text description "설명"
    }

    GALLERY_IMAGE {
        int image_id PK "이미지 ID"
        int festival_id FK "제전 ID"
        varchar image_path "이미지 경로"
        varchar caption "캡션"
        varchar icon_class "아이콘 클래스"
        boolean is_large "큰 이미지 여부"
        int display_order "표시 순서"
    }

    HISTORY {
        int history_id PK "연혁 ID"
        int festival_id FK "제전 ID"
        varchar year "연도"
        varchar title "제목"
        text description "설명"
        int display_order "표시 순서"
    }
```

## 테이블 관계 설명

| 관계 | 설명 | 카디널리티 |
|------|------|-----------|
| FESTIVAL → PROGRAM | 제전별 프로그램 | 1:N |
| FESTIVAL → SCHEDULE | 제전별 일정 | 1:N |
| FESTIVAL → VENUE | 제전별 개최 장소 | 1:1 |
| VENUE → ACCESS_ROUTE | 장소별 교통편 | 1:N |
| FESTIVAL → GALLERY_IMAGE | 제전별 갤러리 이미지 | 1:N |
| FESTIVAL → HISTORY | 제전별 연혁 | 1:N |
