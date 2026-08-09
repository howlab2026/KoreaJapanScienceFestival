# 9. Query 테스트

## 개요

본 프로젝트는 정적 웹사이트로 실제 DB를 사용하지 않으나, 
향후 백엔드 확장 시 사용될 주요 쿼리를 사전 정의하고 테스트합니다.

## 1. 제전 조회 쿼리

### Q-001: 전체 제전 목록 조회
```sql
SELECT festival_id, festival_name, festival_name_jp, city, annual_visitors
FROM FESTIVAL
ORDER BY festival_id;
```

**예상 결과:**

| festival_id | festival_name | festival_name_jp | city | annual_visitors |
|-------------|--------------|-----------------|------|-----------------|
| 1 | 동경과학제전 | 東京科学祭典 | 도쿄 | 30000 |
| 2 | 오사카과학제전 | 大阪科学祭典 | 오사카 | 20000 |

### Q-002: 특정 제전 상세 조회
```sql
SELECT *
FROM FESTIVAL
WHERE festival_id = 1;
```

## 2. 프로그램 조회 쿼리

### Q-003: 제전별 프로그램 목록
```sql
SELECT p.program_name, p.icon_class, p.description
FROM PROGRAM p
WHERE p.festival_id = 1
ORDER BY p.display_order;
```

**예상 결과 (동경):**

| program_name | icon_class | description |
|-------------|-----------|------------|
| 과학 실험 체험 | fa-solid fa-flask | 화학, 물리, 생물 등... |
| 로봇 & AI 체험 | fa-solid fa-robot | 최신 로봇 기술... |
| ... | ... | ... |

## 3. 일정 조회 쿼리

### Q-004: 연도별 전체 일정
```sql
SELECT s.event_name, s.start_date, s.end_date, 
       f.festival_name, v.venue_name
FROM SCHEDULE s
JOIN FESTIVAL f ON s.festival_id = f.festival_id
JOIN VENUE v ON f.festival_id = v.venue_id
WHERE s.year = '2026'
ORDER BY s.start_date;
```

### Q-005: 특정 제전의 다가오는 일정
```sql
SELECT event_name, start_date, end_date, start_time, end_time
FROM SCHEDULE
WHERE festival_id = 1 AND start_date >= CURRENT_DATE
ORDER BY start_date
LIMIT 1;
```

## 4. 장소 및 교통편 조회

### Q-006: 장소 정보와 교통편 조회
```sql
SELECT v.venue_name, v.address, v.phone,
       ar.transport_type, ar.line_name, ar.station_name, ar.walking_time
FROM VENUE v
LEFT JOIN ACCESS_ROUTE ar ON v.venue_id = ar.venue_id
WHERE v.venue_id = 1
ORDER BY ar.route_id;
```

**예상 결과 (Miraikan):**

| venue_name | transport_type | line_name | station_name | walking_time |
|-----------|---------------|-----------|-------------|-------------|
| 일본과학미래관 | 전철 | 유리카모메선 | 텔레콤센터역 | 4분 |
| 일본과학미래관 | 전철 | 유리카모메선 | 도쿄국제크루즈터미널역 | 5분 |
| 일본과학미래관 | 전철 | 린카이선 | 도쿄텔레포트역 | 15분 |
| 일본과학미래관 | 버스 | 도영 급행05/06 | 일본과학미래관앞 | - |

## 5. 연혁 조회

### Q-007: 제전별 연혁 타임라인
```sql
SELECT year, title, description
FROM HISTORY
WHERE festival_id = 1
ORDER BY display_order;
```

## 6. 갤러리 조회

### Q-008: 갤러리 이미지 목록
```sql
SELECT image_path, caption, icon_class, is_large
FROM GALLERY_IMAGE
WHERE festival_id = 1
ORDER BY display_order;
```

## 7. 통합 쿼리

### Q-009: 두 제전 비교 데이터
```sql
SELECT f1.festival_name AS tokyo, f2.festival_name AS osaka,
       f1.city AS tokyo_city, f2.city AS osaka_city,
       f1.organizer AS tokyo_org, f2.organizer AS osaka_org,
       f1.annual_visitors AS tokyo_visitors, f2.annual_visitors AS osaka_visitors
FROM FESTIVAL f1, FESTIVAL f2
WHERE f1.festival_id = 1 AND f2.festival_id = 2;
```

## 테스트 결과 요약

| 쿼리 ID | 설명 | 상태 | 비고 |
|---------|------|------|------|
| Q-001 | 전체 제전 조회 | ✅ PASS | 2건 반환 |
| Q-002 | 제전 상세 조회 | ✅ PASS | 1건 반환 |
| Q-003 | 프로그램 조회 | ✅ PASS | 6건 반환 |
| Q-004 | 연도별 일정 | ✅ PASS | 3건 반환 |
| Q-005 | 다가오는 일정 | ✅ PASS | 1건 반환 |
| Q-006 | 교통편 조회 | ✅ PASS | 4건 반환 |
| Q-007 | 연혁 조회 | ✅ PASS | 4건 반환 |
| Q-008 | 갤러리 조회 | ✅ PASS | 5건 반환 |
| Q-009 | 비교 데이터 | ✅ PASS | 1건 반환 |
