import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

new_uploads = [
    "media__1780652513623.jpg",
    "media__1780652513629.jpg",
    "media__1780652513639.jpg",
    "media__1780652513654.jpg",
    "media__1780652513672.jpg"
]

for idx, filename in enumerate(new_uploads):
    src = os.path.join(brain_dir, filename)
    dst = os.path.join(assets_dir, f"new_upload_{idx+1}.jpg")
    if os.path.exists(src):
        shutil.copy(src, dst)
        with Image.open(dst) as img:
            print(f"Copied {filename} to new_upload_{idx+1}.jpg, size={img.size}, format={img.format}")
    else:
        print(f"File {src} does not exist!")
