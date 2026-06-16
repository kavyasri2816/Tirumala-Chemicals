import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_3.jpg")

if not os.path.exists(src):
    print("new_upload_3.jpg not found")
else:
    img = Image.open(src)
    
    # Test coordinates for top shelf (4 bottles: yellow, pink, orange, white)
    # Test coordinates for bottom left shelf (4 bottles: pink, green, orange, white)
    # Test coordinates for bottom right shelf (5 bottles: yellow, lavender, green, pink, orange)
    crops = {
        "top_yellow": (340, 160, 415, 460),
        "top_pink": (415, 160, 485, 460),
        "top_orange": (485, 160, 555, 460),
        "top_white": (555, 160, 625, 460),
        
        "bottom_green": (170, 480, 250, 680),
        "bottom_lavender": (575, 480, 650, 680),
        "bottom_pink_right": (725, 480, 800, 680)
    }
    
    for name, bbox in crops.items():
        cropped = img.crop(bbox)
        dest = os.path.join(assets_dir, f"test_up3_{name}.png")
        cropped.save(dest)
        print(f"Saved {dest} with size {cropped.size}")
