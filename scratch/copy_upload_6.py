import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

src = os.path.join(brain_dir, "media__1780652697100.png")
dst = os.path.join(assets_dir, "new_upload_6.png")

if os.path.exists(src):
    shutil.copy(src, dst)
    with Image.open(dst) as img:
        print(f"Copied media__1780652697100.png to new_upload_6.png, size={img.size}, format={img.format}")
else:
    print(f"File {src} does not exist!")
