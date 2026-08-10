# 이미지 카툰 변환 및 갤러리 확장 계획 (Image Cartoonization & Gallery Expansion)

`images/tokyo_2026` 폴더에 있는 원본 사진들을 색연필 일러스트레이션 카툰 스타일로 변환하여 새로운 폴더에 저장하고, 변환된 이미지를 기존의 갤러리 게시판(`pages/gallery.html`)에 추가 반영하는 작업을 진행합니다.

## User Review Required

변환 대상 원본 이미지는 총 **272개**로 수량이 매우 많습니다. 에이전트 내장 이미지 생성 도구(`generate_image`)는 품질이 매우 뛰어나지만 개별 이미지당 약 10~15초가 소요되며, API 호출 제한 등으로 인해 단일 세션 내에서 272개를 모두 변환하는 것은 비현실적입니다. 

따라서 다음 **Open Questions**를 확인해 주시면 그에 맞춰 최적의 방식으로 진행하겠습니다.

> [!IMPORTANT]
> - 에이전트 도구를 이용해 대표 이미지 세트(예: 15~20장)를 고품질로 변환하여 갤러리를 확장하는 방향을 추천합니다.
> - 만약 272장 전체의 일괄 변환을 원하신다면, 외부 API(Stability AI, Replicate 등) 연동용 파이썬 스크립트를 작성하여 일괄 처리해야 합니다. 단, 이 경우 해당 서비스의 API 키와 크레딧이 추가로 필요합니다.

## Open Questions

> [!IMPORTANT]
> 1. **변환 범위 선택**:
>    - **방안 A (추천)**: 에이전트 이미지 변환 도구를 사용하여 `images/tokyo_2026`에서 **대표적인 사진 15~20장을 선정**해 고품질 색연필 스타일 카툰으로 변환하고 갤러리에 추가합니다.
>    - **방안 B**: 272장 전체 변환을 수행하기 위해 외부 API(Stability AI 등)를 사용하는 Python 스크립트를 작성하여 일괄 실행합니다. (이 경우 사용할 API와 키를 제공해주셔야 합니다.)
> 
> 2. **방안 A 선택 시 우선순위**:
>    - 방안 A로 진행할 경우, 특정 번호 대역이나 특정 주제(예: 야외 부스, 실내 전시장 등)의 이미지를 우선적으로 변환할까요? 아니면 고르게 분포된 파일들을 선별하여 처리할까요?

## Proposed Changes

### 이미지 리소스 및 갤러리 컴포넌트

---

#### [NEW] `images/tokyo_2026_cartoon_new/` (또는 `images/tokyo_2026_cartoon/`에 추가)
- 원본 이미지에서 변환된 색연필 카툰 스타일 PNG 이미지 파일들을 저장할 새 폴더를 생성합니다.

#### [MODIFY] [gallery.html](file:///c:/Work/HowlabScienceLab/pages/gallery.html)
- 새로 생성된 카툰 이미지 경로들을 `galleryItems` 배열 데이터에 추가합니다.
- 추가된 이미지 수에 따라 페이징 컨트롤 및 레이아웃이 자연스럽게 작동하는지 검증합니다.

## Verification Plan

### Manual Verification
- `images/tokyo_2026_cartoon_new` 폴더에 변환된 파일들이 정상적으로 생성되었는지 확인합니다.
- 브라우저로 [gallery.html](file:///c:/Work/HowlabScienceLab/pages/gallery.html)을 열어 새로운 이미지 카드들이 잘 로드되고, 2x5 그리드 구조와 페이징, 라이트박스 확대 보기가 올바르게 동작하는지 테스트합니다.
- 테스트용으로 변환해 본 1차 결과물을 아래에 공유합니다.

![변환 테스트 결과물](file:///C:/Users/ds2jls/.gemini/antigravity-ide/brain/0d4d20f5-e2b4-439c-b146-0492ae4883f3/tokyo_2026_cartoon_test_1786324276288.png)
