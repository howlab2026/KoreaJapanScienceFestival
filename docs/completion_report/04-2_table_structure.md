# 4-2. 테이블 구조

## 개요

본 프로젝트의 데이터 모델 구조를 정의합니다. (동경 과학기술관 & 오사카 교육대학 텐노지 캠퍼스 기준)

## 1. FESTIVAL (제전 정보)

| 컬럼명 | 데이터 타입 | 설명 | 입력 예시 |
|--------|------------|------|-----------|
| festival_id | INT (PK) | 제전 ID | 1 (동경), 2 (오사카) |
| festival_name | VARCHAR(100) | 한국어 명칭 | "동경청소년과학제전", "오사카청소년과학제전" |
| festival_name_jp | VARCHAR(100) | 일본어/영문 명칭 | "Science Festival 2026 in Osaka" |
| city | VARCHAR(50) | 개최 도시 | "도쿄", "오사카" |
| venue_name | VARCHAR(100) | 개최 장소 | **"도쿄 과학기술관"**, **"오사카 교육대학 텐노지 캠퍼스"** |
| address | VARCHAR(300) | 주소 | "大阪府大阪市天王寺区南河堀町 4-88" |
| operating_hours | VARCHAR(100) | 운영 시간 | "10:00 ~ 17:00" |

## 2. VENUE (장소)

| 컬럼명 | 데이터 타입 | 설명 | 입력 예시 |
|--------|------------|------|-----------|
| venue_id | INT (PK) | 장소 ID | 2 |
| venue_name | VARCHAR(200) | 장소명 | "오사카 교육대학 텐노지 캠퍼스 (Osaka Kyoiku Univ)" |
| address | VARCHAR(500) | 주소 | "大阪府大阪市天王寺区南河堀町 4-88" |
| nearest_station_1 | VARCHAR(100) | 인근역 1 | "JR 텐노지역 (Tennoji) 도보 8분" |
| nearest_station_2 | VARCHAR(100) | 인근역 2 | "JR 테라다초역 (Teradacho) 도보 5분" |
| buildings | VARCHAR(200) | 주요 전시장 | "미래교육 공창센터 & 서관(West Bldg)" |
