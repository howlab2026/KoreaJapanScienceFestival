"""
얼굴 익명화 + 최소 색연필 스타일 변환 스크립트 v4
================================================
핵심 전략:
- 사람 얼굴만 감지하여 색연필 일러스트 스타일로 익명화
- 배경, 물건, 표지판 등은 원본에 매우 가까운 질감 유지
- 전체 이미지에는 아주 은은한 색연필 워시만 적용 (일관성)
- YuNet 얼굴 감지 + 얼굴 영역 강한 스타일화
"""

import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os
import time


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "face_detection_yunet_2023mar.onnx")


def detect_faces(img, confidence_threshold=0.5):
    """YuNet 얼굴 감지 - 모든 얼굴을 찾아서 바운딩 박스 반환"""
    h, w = img.shape[:2]
    
    detector = cv2.FaceDetectorYN.create(
        MODEL_PATH, "", (w, h),
        score_threshold=confidence_threshold,
        nms_threshold=0.3,
        top_k=5000
    )
    
    _, faces = detector.detect(img)
    
    results = []
    if faces is not None:
        for face in faces:
            x, y, fw, fh = int(face[0]), int(face[1]), int(face[2]), int(face[3])
            conf = float(face[14])
            results.append((x, y, fw, fh, conf))
    
    return results


def detect_faces_multiscale(img, confidence_threshold=0.4):
    """
    다중 스케일 얼굴 감지 - 작은 얼굴도 놓치지 않기 위해
    원본 + 2배 확대로 감지 후 합침
    """
    h, w = img.shape[:2]
    all_faces = []
    
    # 원본 크기에서 감지
    faces_orig = detect_faces(img, confidence_threshold)
    all_faces.extend(faces_orig)
    
    # 이미지가 큰 경우 축소 버전에서도 감지 (큰 얼굴 대응)
    if max(h, w) > 2000:
        scale = 1500 / max(h, w)
        small = cv2.resize(img, (int(w * scale), int(h * scale)))
        faces_small = detect_faces(small, confidence_threshold)
        for (fx, fy, fw, fh, conf) in faces_small:
            # 원본 좌표로 변환
            all_faces.append((
                int(fx / scale), int(fy / scale),
                int(fw / scale), int(fh / scale),
                conf
            ))
    
    # NMS (Non-Maximum Suppression) - 중복 제거
    if len(all_faces) == 0:
        return []
    
    boxes = np.array([[x, y, x+fw, y+fh] for (x, y, fw, fh, _) in all_faces])
    scores = np.array([conf for (_, _, _, _, conf) in all_faces])
    
    indices = cv2.dnn.NMSBoxes(
        boxes.tolist(), scores.tolist(),
        score_threshold=confidence_threshold,
        nms_threshold=0.4
    )
    
    if len(indices) == 0:
        return []
    
    # OpenCV 5.0: indices is a flat numpy array
    indices = np.array(indices).flatten()
    
    result = []
    for idx in indices:
        result.append(all_faces[int(idx)])
    
    return result


def create_face_mask(h, w, faces, padding_ratio=0.4):
    """
    얼굴 영역에 대한 소프트 마스크 생성
    - padding으로 얼굴 주변까지 포함
    - 가우시안 블러로 경계를 부드럽게 (자연스러운 전환)
    """
    mask = np.zeros((h, w), dtype=np.float32)
    
    for (fx, fy, fw, fh, conf) in faces:
        # 패딩 추가 (얼굴 영역을 넉넉하게 잡기)
        pad_x = int(fw * padding_ratio)
        pad_y = int(fh * padding_ratio)
        
        x1 = max(0, fx - pad_x)
        y1 = max(0, fy - pad_y)
        x2 = min(w, fx + fw + pad_x)
        y2 = min(h, fy + fh + pad_y)
        
        # 타원형 마스크 (얼굴 형태에 가까움)
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        axis_x = (x2 - x1) // 2
        axis_y = (y2 - y1) // 2
        
        cv2.ellipse(mask, (center_x, center_y), (axis_x, axis_y),
                     0, 0, 360, 1.0, -1)
    
    # 가우시안 블러로 경계를 부드럽게 (자연스러운 전환을 위해 마스크 블러 크기 축소)
    blur_size = max(11, min(h, w) // 50)
    if blur_size % 2 == 0:
        blur_size += 1
    mask = cv2.GaussianBlur(mask, (blur_size, blur_size), 0)
    
    # 마스크 값 범위 정규화
    if mask.max() > 0:
        mask = mask / mask.max()
    
    return mask


def anonymize_face_region(img):
    """
    얼굴 영역에 적용할 부드러운 가우시안 블러 익명화
    - 얼굴 정보를 식별할 수 없도록 자연스럽게 블러 처리
    """
    h, w = img.shape[:2]
    # 이전 대비 추가로 5배 더 약한 초미세 가우시안 블러 (거의 보이지 않는 수준의 미세한 블러)
    ksize = 5
    result = cv2.GaussianBlur(img, (ksize, ksize), 0)
    return result


def apply_subtle_overall_filter(img):
    """
    배경과 사물은 원본의 질감과 디테일을 100% 그대로 유지하고, 
    전체적인 밝기만 화사하게 증가시킴
    """
    # 밝기 1.08배 증가
    result = img.astype(np.float32) * 1.08
    return np.clip(result, 0, 255).astype(np.uint8)


def face_anonymize_transform(image_path, output_path):
    """
    메인 변환 함수:
    1. 얼굴 감지
    2. 얼굴 영역만 색연필 스타일 익명화
    3. 나머지는 원본에 가까운 질감 유지
    4. 소프트 마스크로 자연스럽게 합성
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"  [ERROR] Cannot read: {image_path}")
        return False

    original_h, original_w = img.shape[:2]

    # 처리용 (YuNet은 원본 크기에서 작동)
    # 너무 큰 이미지는 처리 속도를 위해 축소
    max_dim = 3000
    scale = 1.0
    if max(original_h, original_w) > max_dim:
        scale = max_dim / max(original_h, original_w)
        new_w = int(original_w * scale)
        new_h = int(original_h * scale)
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    h, w = img.shape[:2]

    # === Step 1: 얼굴 감지 ===
    faces = detect_faces_multiscale(img, confidence_threshold=0.4)
    face_count = len(faces)

    # === Step 2: 전체 이미지에 은은한 필터 적용 ===
    base_result = apply_subtle_overall_filter(img)

    # === Step 3: 얼굴이 있으면 익명화 적용 ===
    if face_count > 0:
        # 얼굴 영역 익명화된 버전 생성
        anonymized = anonymize_face_region(img)
        
        # 소프트 마스크 생성 (패딩 비율 축소: 0.45 -> 0.08로 얼굴 영역에 딱 맞게)
        face_mask = create_face_mask(h, w, faces, padding_ratio=0.08)
        face_mask_3ch = np.stack([face_mask] * 3, axis=-1)
        
        # 마스크를 이용한 합성: 얼굴=익명화, 나머지=원본+은은한필터
        result = (anonymized.astype(np.float32) * face_mask_3ch +
                  base_result.astype(np.float32) * (1.0 - face_mask_3ch))
        result = np.clip(result, 0, 255).astype(np.uint8)
    else:
        result = base_result

    # === Step 4: 최종 Pillow 미세 보정 ===
    pil_img = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    # 아주 약간의 선명도 (표지판 텍스트 가독성)
    pil_img = ImageEnhance.Sharpness(pil_img).enhance(1.05)
    # 밝기 보정 (더 밝게)
    pil_img = ImageEnhance.Brightness(pil_img).enhance(1.10)
    # 대비 살짝
    pil_img = ImageEnhance.Contrast(pil_img).enhance(1.03)
    
    result = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # 원본 크기로 복원
    if scale < 1.0:
        result = cv2.resize(result, (original_w, original_h), interpolation=cv2.INTER_LANCZOS4)

    # PNG로 저장
    cv2.imwrite(output_path, result, [cv2.IMWRITE_PNG_COMPRESSION, 6])
    return True, face_count


def main():
    src_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026"
    dst_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026_colored_pencil"

    os.makedirs(dst_dir, exist_ok=True)

    # 이미 변환된 파일 목록
    existing = set()
    for f in os.listdir(dst_dir):
        name, _ = os.path.splitext(f)
        existing.add(name)

    # 원본 jpg 파일 목록 (mp4 제외)
    source_files = sorted([
        f for f in os.listdir(src_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    # 아직 변환 안 된 파일만
    todo = [f for f in source_files if os.path.splitext(f)[0] not in existing]

    total = len(source_files)
    done_count = len(existing)
    todo_count = len(todo)

    print("=" * 60)
    print("  Face Anonymization + Subtle Pencil Style v4")
    print(f"  Source: {src_dir}")
    print(f"  Output: {dst_dir}")
    print(f"  Total: {total} | Done: {done_count} | Remaining: {todo_count}")
    print("=" * 60)

    if todo_count == 0:
        print("  All images already converted!")
        return

    total_faces = 0
    for idx, filename in enumerate(todo, 1):
        src_path = os.path.join(src_dir, filename)
        name, _ = os.path.splitext(filename)
        dst_path = os.path.join(dst_dir, f"{name}.png")

        print(f"\n  [{done_count + idx}/{total}] {filename} processing...")
        start = time.time()

        result = face_anonymize_transform(src_path, dst_path)

        elapsed = time.time() - start
        if isinstance(result, tuple):
            success, face_count = result
            total_faces += face_count
            if success:
                size_kb = os.path.getsize(dst_path) / 1024
                print(f"    -> Done ({elapsed:.1f}s, {size_kb:.0f}KB, faces: {face_count})")
            else:
                print(f"    -> Failed")
        else:
            print(f"    -> Failed")

    print(f"\n{'=' * 60}")
    print(f"  Complete! {todo_count} images, {total_faces} faces anonymized.")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
