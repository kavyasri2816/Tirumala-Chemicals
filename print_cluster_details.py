import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src_path = os.path.join(assets_dir, "unique_5.jpg")

img = Image.open(src_path).convert("RGB")
width, height = img.size

pink_pixels = []
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        if r > 180 and g < 100 and b > 110 and abs(r - b) < 60:
            if 420 <= x <= 503:
                pink_pixels.append((x, y))

ys = [p[1] for p in pink_pixels]
print(f"Cluster 4 y-range: min_y = {min(ys)}, max_y = {max(ys)}")
