import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

files = [
    "test_up1_acid_green_top_left.png",
    "test_up1_black_brown_top_mid.png",
    "test_up1_acid_green_bottom_left.png",
    "test_up1_acid_green_bottom_mid.png",
    "test_up1_acid_green_bottom_right.png"
]

for filename in files:
    filepath = os.path.join(assets_dir, filename)
    if os.path.exists(filepath):
        img = Image.open(filepath).convert("RGB")
        w, h = img.size
        # average color
        avg = img.resize((1, 1)).getpixel((0,0))
        # check green ratio (g / (r + b + 1))
        # check dark ratio (r+g+b) / 3
        green_ratios = []
        brightnesses = []
        for y in range(h):
            for x in range(w):
                r, g, b = img.getpixel((x, y))
                green_ratios.append(g / (r + b + 1))
                brightnesses.append((r + g + b) / 3)
        avg_green_ratio = sum(green_ratios) / len(green_ratios)
        avg_brightness = sum(brightnesses) / len(brightnesses)
        print(f"{filename}: avg={avg}, green_ratio={avg_green_ratio:.2f}, brightness={avg_brightness:.2f}")
