# 4-4. 디렉토리 구조

## 프로젝트 전체 디렉토리 구조

```
HowlabScienceLab/
├── index.html                          # 메인 페이지 (랜딩)
│
├── css/
│   └── style.css                       # 메인 스타일시트
│
├── js/
│   └── script.js                       # 메인 JavaScript
│
├── pages/
│   ├── tokyo.html                      # 동경과학제전 상세 페이지
│   ├── osaka.html                      # 오사카과학제전 상세 페이지
│   ├── schedule.html                   # 일정 안내 페이지
│   └── access.html                     # 교통 안내 페이지
│
├── images/                             # 이미지 리소스
│   ├── hero/                           # 히어로 이미지
│   ├── tokyo/                          # 동경 관련 이미지
│   ├── osaka/                          # 오사카 관련 이미지
│   └── gallery/                        # 갤러리 이미지
│
├── docs/                               # 프로젝트 문서
│   ├── completion_report/              # 완료보고서 (17개)
│   │   ├── 01_project_info.md
│   │   ├── 01-1_system_flow.md
│   │   ├── 02_requirements.md
│   │   ├── 02-1_functional_requirements.md
│   │   ├── 02-2_detailed_functions.md
│   │   ├── 03_task_assignment.md
│   │   ├── 04_design_spec.md
│   │   ├── 04-1_erd_physical.md
│   │   ├── 04-2_table_structure.md
│   │   ├── 04-3_naming_convention.md
│   │   ├── 04-4_directory_structure.md
│   │   ├── 04-5_package_structure.md
│   │   ├── 05_dev_environment.md
│   │   ├── 06_application.md
│   │   ├── 06-1_app_procedure.md
│   │   ├── 06-2_server_config.md
│   │   └── 06-3_feature_summary.md
│   │
│   └── dev_document/                   # 개발문서 (17개)
│       ├── 01_project_overview.md
│       ├── 02_system_architecture.md
│       ├── 03_function_definition.md
│       ├── 04_data_dictionary.md
│       ├── 05_data_input_spec.md
│       ├── 06_db_object_list.md
│       ├── 07_table_definition.md
│       ├── 08_erd.md
│       ├── 09_query_test.md
│       ├── 10_naming_convention.md
│       ├── 11_screen_program_list.md
│       ├── 12_screen_design.md
│       ├── 13_screen_path.md
│       ├── 14_class_path.md
│       ├── 15_uri_mapping.md
│       ├── 16_sitemap.md
│       └── 17_project_schedule.md
│
└── README.md                           # 프로젝트 설명서
```

## 디렉토리 역할

| 디렉토리 | 역할 | 파일 수 |
|----------|------|---------|
| `/` (루트) | 메인 진입점, 설정 파일 | 1 (index.html) |
| `/css` | 스타일시트 | 1 |
| `/js` | JavaScript | 1 |
| `/pages` | 서브 페이지 | 4 |
| `/images` | 이미지 리소스 | 가변 |
| `/docs/completion_report` | 완료보고서 | 17 |
| `/docs/dev_document` | 개발문서 | 17 |
