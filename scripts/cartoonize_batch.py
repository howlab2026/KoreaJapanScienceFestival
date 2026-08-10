import cv2
import os
import sys
import time

def process_batch(src_dir, dest_dir, max_dim=1200, sigma_s=30, sigma_r=0.15):
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")
        
    # Get all image files
    valid_extensions = ('.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(valid_extensions)]
    total_files = len(files)
    
    print(f"Found {total_files} images in {src_dir} to process.")
    start_time = time.time()
    
    success_count = 0
    for idx, filename in enumerate(files):
        src_path = os.path.join(src_dir, filename)
        # Save output as JPG for optimal size
        base_name, _ = os.path.splitext(filename)
        dest_filename = f"{base_name}_cartoon.jpg"
        dest_path = os.path.join(dest_dir, dest_filename)
        
        # Check if already processed
        if os.path.exists(dest_path):
            success_count += 1
            continue
            
        try:
            # Read image
            img = cv2.imread(src_path)
            if img is None:
                print(f"[{idx+1}/{total_files}] Failed to read {filename}")
                continue
                
            # Resize image to optimize speed and file size
            h, w = img.shape[:2]
            scale = max_dim / max(h, w)
            if scale < 1.0:
                resized = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_AREA)
            else:
                resized = img
                
            # Apply stylization (watercolor-like painting effect)
            cartoon = cv2.stylization(resized, sigma_s=sigma_s, sigma_r=sigma_r)
            
            # Save image as JPEG (quality=90)
            cv2.imwrite(dest_path, cartoon, [cv2.IMWRITE_JPEG_QUALITY, 90])
            success_count += 1
            
            if (idx + 1) % 10 == 0 or (idx + 1) == total_files:
                elapsed = time.time() - start_time
                avg_time = elapsed / (idx + 1)
                est_remaining = avg_time * (total_files - (idx + 1))
                print(f"Processed [{idx+1}/{total_files}] - {success_count} succeeded. Elapsed: {elapsed:.1f}s. Est. remaining: {est_remaining:.1f}s")
                
        except Exception as e:
            print(f"[{idx+1}/{total_files}] Error processing {filename}: {str(e)}")
            
    total_time = time.time() - start_time
    print(f"\nBatch processing complete! Successfully converted {success_count}/{total_files} images in {total_time:.1f} seconds.")

if __name__ == "__main__":
    src_folder = "c:\\Work\\HowlabScienceLab\\images\\tokyo_2026"
    dest_folder = "c:\\Work\\HowlabScienceLab\\images\\tokyo_2026_cartoon_all"
    process_batch(src_folder, dest_folder)
