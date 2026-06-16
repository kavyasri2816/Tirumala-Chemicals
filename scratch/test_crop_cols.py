import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_6.png")

if not os.path.exists(src):
    print("new_upload_6.png not found")
else:
    img = Image.open(src)
    w, h = img.size
    
    # 7 columns
    regions = [
        ("herbal_white", (30, 150, 175, 520)),
        ("herbal_green", (190, 150, 335, 520)),
        ("acid_orange", (340, 150, 480, 520)),
        ("acid_blue", (500, 150, 640, 520)),
        ("acid_red", (645, 150, 785, 520)),
        ("ant_large", (775, 200, 885, 520)),
        ("ant_small", (880, 280, 914, 520)) # wait, let's verify if the small bottle goes up to 914
    ]
    
    for name, bbox in regions:
        cropped = img.crop(bbox)
        dest = os.path.join(assets_dir, f"test_{name}.png")
        cropped.save(dest)
        print(f"Saved {dest} with size {cropped.size}")
