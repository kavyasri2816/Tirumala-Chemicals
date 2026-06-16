import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_6.png")

if not os.path.exists(src):
    print("new_upload_6.png not found")
else:
    with Image.open(src) as img:
        print(f"new_upload_6.png size: {img.size}")
        # Sample points:
        # Top-left (wall): (10, 10)
        # Top-right (wall): (img.width - 10, 10)
        # Bottom-left (floor): (10, img.height - 10)
        # Bottom-right (floor): (img.width - 10, img.height - 10)
        # Center top (wall): (img.width // 2, 10)
        points = [
            ("Top-Left Wall", (10, 10)),
            ("Top-Right Wall", (img.width - 10, 10)),
            ("Bottom-Left Floor", (10, img.height - 10)),
            ("Bottom-Right Floor", (img.width - 10, img.height - 10)),
            ("Center Top Wall", (img.width // 2, 10))
        ]
        for name, pt in points:
            print(f"{name} at {pt}: {img.getpixel(pt)}")
