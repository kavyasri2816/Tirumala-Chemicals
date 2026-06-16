import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

uploads = [
    ("media__1780654397899.png", "screenshot_1.png"),
    ("media__1780654420574.png", "screenshot_2.png"),
    ("media__1780654454086.png", "screenshot_3.png"),
    ("media__1780654473526.png", "screenshot_4.png"),
    ("media__1780654591644.png", "user_glass_cleaner.png")
]

for src_name, dst_name in uploads:
    src = os.path.join(brain_dir, src_name)
    dst = os.path.join(assets_dir, dst_name)
    if os.path.exists(src):
        shutil.copy(src, dst)
        with Image.open(dst) as img:
            print(f"Copied {src_name} to {dst_name}, size={img.size}, format={img.format}")
    else:
        print(f"File {src} not found")
