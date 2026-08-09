# 6-2. 서버 및 기타 설정

## 1. 개발 서버 설정

### VS Code Live Server 설정

```json
// .vscode/settings.json
{
    "liveServer.settings.port": 5500,
    "liveServer.settings.root": "/",
    "liveServer.settings.CustomBrowser": "chrome",
    "liveServer.settings.donotVerifyTags": true,
    "liveServer.settings.donotShowInfoMsg": true
}
```

## 2. 배포 서버 설정

### 2.1 Nginx 설정 (참고)

```nginx
server {
    listen 80;
    server_name japan-science-festival.kr;

    root /var/www/HowlabScienceLab;
    index index.html;

    # GZIP 압축
    gzip on;
    gzip_types text/css application/javascript text/html;
    gzip_min_length 256;

    # 캐시 설정
    location ~* \.(css|js|jpg|jpeg|png|gif|ico|svg|woff2)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # SPA-like 라우팅 (정적 파일 우선)
    location / {
        try_files $uri $uri/ /index.html;
    }

    # 보안 헤더
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    add_header Referrer-Policy "strict-origin-when-cross-origin";

    # HTTPS 리다이렉트
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name japan-science-festival.kr;

    ssl_certificate /etc/ssl/certs/site.crt;
    ssl_certificate_key /etc/ssl/private/site.key;

    root /var/www/HowlabScienceLab;
    index index.html;
}
```

### 2.2 GitHub Pages 배포

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

### 2.3 Netlify 설정

```toml
# netlify.toml
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
    Cache-Control = "public, max-age=3600"

[[headers]]
  for = "/css/*"
  [headers.values]
    Cache-Control = "public, max-age=2592000, immutable"

[[headers]]
  for = "/js/*"
  [headers.values]
    Cache-Control = "public, max-age=2592000, immutable"
```

## 3. 기타 설정

### 3.1 .gitignore

```
# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Temp
*.log
tmp/
```

### 3.2 SEO 관련 파일 (권장)

#### robots.txt
```
User-agent: *
Allow: /
Sitemap: https://japan-science-festival.kr/sitemap.xml
```

#### sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://japan-science-festival.kr/</loc>
    <lastmod>2026-08-09</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/tokyo.html</loc>
    <lastmod>2026-08-09</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/osaka.html</loc>
    <lastmod>2026-08-09</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/schedule.html</loc>
    <lastmod>2026-08-09</lastmod>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://japan-science-festival.kr/pages/access.html</loc>
    <lastmod>2026-08-09</lastmod>
    <priority>0.7</priority>
  </url>
</urlset>
```
