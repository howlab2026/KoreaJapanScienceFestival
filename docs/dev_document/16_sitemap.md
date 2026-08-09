# 16. Sitemap

## 사이트맵

```mermaid
graph TD
    HOME["🏠 메인 페이지<br/>index.html"] --> SEC1["📖 소개 섹션<br/>#about"]
    HOME --> SEC2["🗼 동경과학제전 섹션<br/>#tokyo"]
    HOME --> SEC3["⛩️ 오사카과학제전 섹션<br/>#osaka"]
    HOME --> SEC4["📊 비교 섹션<br/>#compare"]
    HOME --> SEC5["📅 일정 섹션<br/>#schedule"]
    HOME --> SEC6["🗺️ 교통 섹션<br/>#access"]
    HOME --> SEC7["🖼️ 갤러리 섹션<br/>#gallery"]
    
    SEC2 --> TOKYO["🗼 동경 상세<br/>pages/tokyo.html"]
    SEC3 --> OSAKA["⛩️ 오사카 상세<br/>pages/osaka.html"]
    SEC5 --> SCHED["📅 일정 상세<br/>pages/schedule.html"]
    SEC6 --> ACCSS["🗺️ 교통 상세<br/>pages/access.html"]
    
    TOKYO --> T1["Event 01: Tokyo ふしぎ祭エンス"]
    TOKYO --> T2["Event 02: Science Agora"]
    TOKYO --> T3["연혁"]
    
    OSAKA --> O1["사이언스 페스타 2026"]
    OSAKA --> O2["관련 시설"]
    OSAKA --> O3["연혁"]
    
    SCHED --> S1["연간 일정표"]
    SCHED --> S2["상세 타임테이블"]
    SCHED --> S3["참가 안내"]
    
    ACCSS --> A1["동경 교통 + 지도"]
    ACCSS --> A2["오사카 교통 + 지도"]
    ACCSS --> A3["한국에서 가는 법"]
```

## 페이지 목록

| 레벨 | 페이지명 | URL | 비고 |
|------|----------|-----|------|
| 1 | 메인 페이지 | `/` | 8개 섹션 포함 |
| 2 | 동경과학제전 상세 | `/pages/tokyo.html` | 3개 섹션 |
| 2 | 오사카과학제전 상세 | `/pages/osaka.html` | 4개 섹션 |
| 2 | 일정 안내 | `/pages/schedule.html` | 3개 섹션 |
| 2 | 교통 안내 | `/pages/access.html` | 3개 섹션 |

## sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://japan-science-festival.kr/</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/tokyo.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/osaka.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/schedule.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/access.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
```
