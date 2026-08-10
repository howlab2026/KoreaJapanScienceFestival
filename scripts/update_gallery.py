import os
from PIL import Image

html_path = r"c:\Work\HowlabScienceLab\pages\gallery.html"
cartoon_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026_cartoon"
thumb_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026_cartoon_thumb"

# Ensure directories exist
os.makedirs(thumb_dir, exist_ok=True)

# List all png files in the cartoon directory
files = sorted([f for f in os.listdir(cartoon_dir) if f.lower().endswith(".png")])

print(f"Total source images: {len(files)}")

# 1. Sync Thumbnails (Create missing, delete orphaned)
existing_thumbs = set(os.listdir(thumb_dir))
source_set = set(files)

# Delete orphaned thumbnails
orphans = existing_thumbs - source_set
for orphan in orphans:
    orphan_path = os.path.join(thumb_dir, orphan)
    try:
        os.remove(orphan_path)
        print(f"Removed orphaned thumbnail: {orphan}")
    except Exception as e:
        print(f"Error removing {orphan}: {e}")

# Create missing thumbnails
created_count = 0
for f in files:
    src_path = os.path.join(cartoon_dir, f)
    dst_path = os.path.join(thumb_dir, f)

    if f not in existing_thumbs:
        try:
            with Image.open(src_path) as img:
                # Resize keeping aspect ratio (max bounding box 320x240)
                img.thumbnail((320, 240), Image.Resampling.LANCZOS)
                # Save optimized thumbnail
                img.save(dst_path, "PNG", optimize=True)
                created_count += 1
                if created_count % 30 == 0 or created_count == 1:
                    print(f"Created {created_count} thumbnails...")
        except Exception as e:
            print(f"Error creating thumbnail for {f}: {e}")

print(f"Thumbnail sync complete. Created: {created_count}, Total: {len(files)}")

# 2. Format JS array for gallery.html
js_items = []
for f in files:
    js_items.append(
        f'                {{ img: "../images/tokyo_2026_cartoon/{f}", thumb: "../images/tokyo_2026_cartoon_thumb/{f}" }},'
    )

js_block = "            const galleryItems = [\n" + "\n".join(js_items) + "\n            ];"

# 3. Write back to html
with open(html_path, "r", encoding="utf-8") as file:
    content = file.read()

start_marker = "            const galleryItems = ["
end_marker = "            ];"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("Start marker not found in HTML!")
    exit(1)

end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print("End marker not found in HTML!")
    exit(1)

end_idx += len(end_marker)

new_content = content[:start_idx] + js_block + content[end_idx:]

with open(html_path, "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Successfully updated gallery.html with {len(files)} items!")
