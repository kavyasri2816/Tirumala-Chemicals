import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def get_projection_profile(image_path, bg_func):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    col_counts = [0] * w
    
    for y in range(h):
        for x in range(w):
            r, g, b = img.getpixel((x, y))
            if not bg_func(r, g, b, x, y, w, h):
                col_counts[x] += 1
    return col_counts, w, h

def detect_regions(col_counts, threshold=10, min_width=20):
    regions = []
    in_obj = False
    start_x = 0
    for x, val in enumerate(col_counts):
        active = val > threshold
        if active and not in_obj:
            in_obj = True
            start_x = x
        elif not active and in_obj:
            in_obj = False
            end_x = x
            if end_x - start_x >= min_width:
                regions.append((start_x, end_x))
    if in_obj:
        if len(col_counts) - start_x >= min_width:
            regions.append((start_x, len(col_counts)))
    return regions

# Define background filters for each image type
# 1. Tirumala Acid/Black Phenyl (purple Venkateswara background)
def bg_purple(r, g, b, x, y, w, h):
    # purple banner, brown steps
    is_purple = (r > 100 and b > 120 and g < 100) or (r > 80 and b > 100 and g < 70)
    is_brown_step = (r > 60 and g > 30 and b < 50 and r > b + 25)
    is_top_purple_banner = (y < h * 0.45) # top section is background
    return is_purple or is_brown_step or is_top_purple_banner

# 2. Liger Floor (rainbow/pastel background + lion)
def bg_liger(r, g, b, x, y, w, h):
    # top 40% is lion background
    is_top = (y < h * 0.38)
    # brown steps
    is_brown_step = (r > 50 and g > 30 and b < 40 and r > b + 20)
    # background color
    is_light = (r > 180 and g > 180 and b > 180)
    return is_top or is_brown_step or is_light

# 3. Tirumala Floor (green Venkateswara background)
def bg_green_venk(r, g, b, x, y, w, h):
    is_green_bg = (g > r + 10 and g > b + 15) or (g > 80 and r < 80 and b < 80)
    is_brown_step = (r > 60 and g > 30 and b < 50 and r > b + 20)
    is_top = (y < h * 0.40)
    return is_green_bg or is_brown_step or is_top

# 4. Home Doctor (house background)
def bg_home_doctor(r, g, b, x, y, w, h):
    is_top = (y < h * 0.38)
    is_brown_step = (r > 55 and g > 35 and b < 45 and r > b + 15)
    return is_top or is_brown_step

# 5. new_upload_6.png (teal wall + beige floor)
def bg_upload_6(r, g, b, x, y, w, h):
    is_wall = (r < 110 and g > 100 and b > 120 and b > r + 30 and g > r + 20)
    is_floor = (r > 175 and g > 175 and b > 155) or \
               (r > 150 and g > 150 and b > 140 and abs(r - g) < 20 and abs(g - b) < 20)
    return is_wall or is_floor

images_to_test = [
    ("new_upload_1.jpg", bg_purple, 20, 25),
    ("new_upload_2.jpg", bg_liger, 20, 25),
    ("new_upload_3.jpg", bg_green_venk, 20, 25),
    ("new_upload_4.jpg", bg_home_doctor, 20, 25),
    ("new_upload_6.png", bg_upload_6, 10, 20)
]

for filename, bg_func, thresh, min_w in images_to_test:
    filepath = os.path.join(assets_dir, filename)
    if os.path.exists(filepath):
        profile, w, h = get_projection_profile(filepath, bg_func)
        regions = detect_regions(profile, threshold=thresh, min_width=min_w)
        print(f"\n--- {filename} ({w}x{h}) ---")
        print(f"Detected {len(regions)} regions:")
        for idx, (x1, x2) in enumerate(regions):
            print(f"  Bottle {idx+1}: x range ({x1}, {x2})")
    else:
        print(f"{filename} not found")
