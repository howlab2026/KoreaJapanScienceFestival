import cv2
import os
import sys
import time

def process_remaining(src_dir, dest_dir, max_dim=1200, sigma_s=30, sigma_r=0.15):
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")
        
    # Get all image files in source directory
    valid_extensions = ('.jpg', '.jpeg', '.png')
    src_files = [f for f in os.listdir(src_dir) if f.lower().endswith(valid_extensions)]
    total_src = len(src_files)
    
    # Get already processed files in destination directory
    dest_files = set(os.listdir(dest_dir))
    
    # Determine files to process
    to_process = []
    for f in src_files:
        base_name, _ = os.path.splitext(f)
        dest_filename = f"{base_name}_cartoon.png"
        if dest_filename in dest_files:
            continue
        to_process.append((f, dest_filename))
        
    total_to_process = len(to_process)
    print(f"Total source files: {total_src}")
    print(f"Already processed: {total_src - total_to_process}")
    print(f"Remaining to process: {total_to_process}")
    
    if total_to_process == 0:
        print("No new files to process.")
        return
        
    start_time = time.time()
    success_count = 0
    
    for idx, (src_name, dest_name) in enumerate(to_process):
        src_path = os.path.join(src_dir, src_name)
        dest_path = os.path.join(dest_dir, dest_name)
        
        try:
            # Read image
            img = cv2.imread(src_path)
            if img is None:
                print(f"[{idx+1}/{total_to_process}] Failed to read {src_name}")
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
            
            # Save image as PNG with compression level 9 (max compression)
            cv2.imwrite(dest_path, cartoon, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            success_count += 1
            
            if (idx + 1) % 10 == 0 or (idx + 1) == total_to_process:
                elapsed = time.time() - start_time
                avg_time = elapsed / (idx + 1)
                est_remaining = avg_time * (total_to_process - (idx + 1))
                print(f"Processed [{idx+1}/{total_to_process}] - {success_count} succeeded. Elapsed: {elapsed:.1f}s. Est. remaining: {est_remaining:.1f}s")
                
        except Exception as e:
            print(f"[{idx+1}/{total_to_process}] Error processing {src_name}: {str(e)}")
            
    total_time = time.time() - start_time
    print(f"\nIncremental batch processing complete! Successfully converted {success_count}/{total_to_process} new images in {total_time:.1f} seconds.")

if __name__ == "__main__":
    src_folder = "c:\\Work\\HowlabScienceLab\\images\\tokyo_2026"
    dest_folder = "c:\\Work\\HowlabScienceLab\\images\\tokyo_2026_cartoon"
    process_remaining(src_folder, dest_folder)
