# 8. ERD

## Entity Relationship Diagram

```mermaid
erDiagram
    FESTIVAL ||--o{ PROGRAM : "has programs"
    FESTIVAL ||--o{ SCHEDULE : "has schedules"
    FESTIVAL ||--|| VENUE : "held at"
    VENUE ||--o{ ACCESS_ROUTE : "accessible via"
    FESTIVAL ||--o{ GALLERY_IMAGE : "has gallery"
    FESTIVAL ||--o{ HISTORY : "has history"

    FESTIVAL {
        int festival_id PK
        varchar festival_name
        varchar festival_name_jp
        varchar festival_name_en
        varchar city
        varchar organizer
        varchar target_audience
        varchar admission_fee
        int annual_visitors
        text description
        varchar badge_color
        datetime created_at
        datetime updated_at
    }

    PROGRAM {
        int program_id PK
        int festival_id FK
        varchar program_name
        varchar icon_class
        text description
        int display_order
    }

    SCHEDULE {
        int schedule_id PK
        int festival_id FK
        varchar event_name
        date start_date
        date end_date
        time start_time
        time end_time
        char year
        text note
    }

    VENUE {
        int venue_id PK
        varchar venue_name
        varchar venue_name_jp
        varchar address
        varchar address_jp
        varchar phone
        varchar website
        decimal latitude
        decimal longitude
        varchar operating_hours
    }

    ACCESS_ROUTE {
        int route_id PK
        int venue_id FK
        varchar transport_type
        varchar line_name
        varchar station_name
        varchar walking_time
        text description
    }

    GALLERY_IMAGE {
        int image_id PK
        int festival_id FK
        varchar image_path
        varchar caption
        varchar icon_class
        boolean is_large
        int display_order
    }

    HISTORY {
        int history_id PK
        int festival_id FK
        varchar year
        varchar title
        text description
        int display_order
    }
```

## 관계 정의

| 부모 테이블 | 자식 테이블 | 관계 유형 | FK 컬럼 | 설명 |
|------------|------------|----------|---------|------|
| FESTIVAL | PROGRAM | 1:N | festival_id | 제전 → 프로그램 |
| FESTIVAL | SCHEDULE | 1:N | festival_id | 제전 → 일정 |
| FESTIVAL | VENUE | 1:1 | - | 제전 → 장소 |
| VENUE | ACCESS_ROUTE | 1:N | venue_id | 장소 → 교통편 |
| FESTIVAL | GALLERY_IMAGE | 1:N | festival_id | 제전 → 갤러리 |
| FESTIVAL | HISTORY | 1:N | festival_id | 제전 → 연혁 |

## 인덱스 정의

| 테이블 | 인덱스명 | 컬럼 | 유형 |
|--------|----------|------|------|
| FESTIVAL | PK_festival | festival_id | PRIMARY |
| PROGRAM | PK_program | program_id | PRIMARY |
| PROGRAM | FK_program_festival | festival_id | FOREIGN KEY |
| SCHEDULE | PK_schedule | schedule_id | PRIMARY |
| SCHEDULE | FK_schedule_festival | festival_id | FOREIGN KEY |
| SCHEDULE | IDX_schedule_year | year | INDEX |
| VENUE | PK_venue | venue_id | PRIMARY |
| ACCESS_ROUTE | PK_route | route_id | PRIMARY |
| ACCESS_ROUTE | FK_route_venue | venue_id | FOREIGN KEY |
| GALLERY_IMAGE | PK_gallery | image_id | PRIMARY |
| GALLERY_IMAGE | FK_gallery_festival | festival_id | FOREIGN KEY |
| HISTORY | PK_history | history_id | PRIMARY |
| HISTORY | FK_history_festival | festival_id | FOREIGN KEY |
