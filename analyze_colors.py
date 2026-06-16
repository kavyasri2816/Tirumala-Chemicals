import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
files = [f for f in os.listdir(assets_dir) if f.startswith("unique_") and f.endswith(".jpg")]
files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

for filename in files:
    path = os.path.join(assets_dir, filename)
    try:
        img = Image.open(path).convert("RGB")
        # Resize to 1x1 to get average color
        img_small = img.resize((1, 1))
        r, g, b = img_small.getpixel((0, 0))
        print(f"{filename}: Average RGB = ({r}, {g}, {b}) | size = {img.size}")
    except Exception as e:
        print(f"Error {filename}: {e}")

