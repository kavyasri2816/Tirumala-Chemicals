import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_1.jpg")

if not os.path.exists(src):
    print("new_upload_1.jpg not found")
else:
    img = Image.open(src)
    
    crops = {
        "acid_green_top_left": (350, 210, 420, 500),
        "black_brown_top_mid": (420, 250, 485, 500),
        "black_brown_top_right": (485, 250, 555, 500),
        "acid_green_top_right": (555, 210, 625, 500),
        "acid_green_bottom_left": (130, 635, 210, 955) # wait, height is 682, so y can't be > 682!
    }
    
    # Bottom shelf y ranges should be around 480 to 682
    crops_valid = {
        "acid_green_top_left": (350, 210, 420, 500),
        "black_brown_top_mid": (420, 250, 485, 500),
        "acid_green_bottom_left": (130, 480, 210, 680),
        "acid_green_bottom_mid": (215, 480, 290, 680),
        "acid_green_bottom_right": (500, 480, 580, 680)
    }
    
    for name, bbox in crops_valid.items():
        cropped = img.crop(bbox)
        dest = os.path.join(assets_dir, f"test_up1_{name}.png")
        cropped.save(dest)
        print(f"Saved {dest} with size {cropped.size}")
