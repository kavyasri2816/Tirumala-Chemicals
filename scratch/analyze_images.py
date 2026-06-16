import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

for i in range(1, 6):
    filename = f"new_upload_{i}.jpg"
    filepath = os.path.join(assets_dir, filename)
    if not os.path.exists(filepath):
        print(f"{filename} does not exist")
        continue
    
    with Image.open(filepath) as img:
        # Get overall average RGB
        img_small = img.resize((1, 1))
        avg_color = img_small.getpixel((0, 0))
        
        # Get colors of the corners to see background
        w, h = img.size
        corners = [
            img.getpixel((10, 10)),
            img.getpixel((w - 10, 10)),
            img.getpixel((10, h - 10)),
            img.getpixel((w - 10, h - 10))
        ]
        avg_corner = tuple(sum(c[j] for c in corners) // 4 for j in range(3))
        
        print(f"{filename}: size={img.size}, avg_color={avg_color}, avg_corner={avg_corner}")
