import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

files = [
    "test_up3_top_yellow.png",
    "test_up3_top_pink.png",
    "test_up3_top_orange.png",
    "test_up3_top_white.png",
    "test_up3_bottom_green.png",
    "test_up3_bottom_lavender.png",
    "test_up3_bottom_pink_right.png"
]

for filename in files:
    filepath = os.path.join(assets_dir, filename)
    if os.path.exists(filepath):
        img = Image.open(filepath).convert("RGB")
        avg = img.resize((1, 1)).getpixel((0,0))
        print(f"{filename}: avg RGB={avg}")
