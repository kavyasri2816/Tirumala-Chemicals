import os
from PIL import Image, ImageFilter

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

def clean_bottle(src_filename, name_prefix, bbox, bg_check_func):
    src_path = os.path.join(assets_dir, src_filename)
    if not os.path.exists(src_path):
        print(f"Source {src_filename} not found")
        return False
        
    img = Image.open(src_path)
    cropped = img.crop(bbox).convert("RGBA")
    w, h = cropped.size
    
    datas = cropped.getdata()
    new_data = []
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = cropped.getpixel((x, y))
            
            # Use custom background checker
            if bg_check_func(r, g, b, x, y, w, h):
                new_data.append((255, 255, 255, 0)) # transparent
            else:
                new_data.append((r, g, b, a))
                
    cropped.putdata(new_data)
    
    # Crop to exact non-transparent bounding box
    bbox_inner = cropped.getbbox()
    if bbox_inner:
        final_cropped = cropped.crop(bbox_inner)
    else:
        final_cropped = cropped
        
    # Validation: check solidity of the cropped region
    fcw, fch = final_cropped.size
    total_pixels = fcw * fch
    non_transparent = 0
    for y in range(fch):
        for x in range(fcw):
            if final_cropped.getpixel((x, y))[3] > 0:
                non_transparent += 1
                
    density = (non_transparent / total_pixels) if total_pixels > 0 else 0
    print(f"[{name_prefix}] size={final_cropped.size}, non-transparent={non_transparent}/{total_pixels} (density={density:.2f})")
    
    # Center in a clean 800x800 white background canvas
    canvas_size = 800
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
    
    # Resize cropped image to fit in 650x650
    ratio = min(620.0 / fcw, 620.0 / fch)
    new_w = int(fcw * ratio)
    new_h = int(fch * ratio)
    
    resized = final_cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Paste centered
    offset_x = (canvas_size - new_w) // 2
    offset_y = (canvas_size - new_h) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)
    
    final_img = canvas.convert("RGB")
    dest_path = os.path.join(assets_dir, f"{name_prefix}.png")
    final_img.save(dest_path, "PNG")
    return True

# Specific background functions for each image type

# 1. new_upload_6.png (wall & floor)
def bg_upload_6(r, g, b, x, y, w, h):
    # Teal wall:
    is_teal = (r < 110 and g > 100 and b > 120 and b > r + 30 and g > r + 20)
    # Beige floor:
    is_beige = (r > 165 and g > 160 and b > 140 and abs(r-g) < 25 and abs(g-b) < 25)
    # Dark shadow/wood floor
    is_dark = (r < 90 and g < 90 and b < 85)
    return is_teal or is_beige or is_dark

# 2. new_upload_1.jpg (Acid & Black Phenyl - purple background)
def bg_upload_1(r, g, b, x, y, w, h):
    # Purple wall banner:
    is_purple = (r > 80 and b > 90 and g < 115 and r > g + 10)
    # Wood steps / shadows:
    is_dark = (r < 115 and g < 95 and b < 85)
    # Floor:
    is_beige = (r > 160 and g > 155 and b > 135 and abs(r-g) < 25)
    return is_purple or is_dark or is_beige

# 3. new_upload_3.jpg (Tirumala Floor Cleaner - green background)
def bg_upload_3(r, g, b, x, y, w, h):
    # Green wall banner:
    is_green = (g > r + 15 and g > b + 15 and g > 70) or (g > 90 and r < 90 and b < 90)
    # Wood steps / shadows:
    is_dark = (r < 115 and g < 95 and b < 85)
    # Floor:
    is_beige = (r > 160 and g > 155 and b > 135 and abs(r-g) < 25)
    return is_green or is_dark or is_beige

# 4. new_upload_2.jpg (Liger Floor Cleaner)
def bg_upload_2(r, g, b, x, y, w, h):
    # Top section is wall/lion:
    is_wall = (y < h * 0.15) or (r > 160 and g > 165 and b > 150 and abs(r-g) < 20)
    # Wood steps / shadows:
    is_dark = (r < 115 and g < 95 and b < 85)
    return is_wall or is_dark

# 5. new_upload_4.jpg (Home Doctor Floor Cleaner)
def bg_upload_4(r, g, b, x, y, w, h):
    # Top section is house wall:
    is_wall = (y < h * 0.15) or (r > 160 and g > 165 and b > 150 and abs(r-g) < 20)
    # Wood steps / shadows:
    is_dark = (r < 115 and g < 95 and b < 85)
    return is_wall or is_dark


# Coordinates manifest
bottle_manifest = [
    # 1. new_upload_6.png (7 bottles)
    ("new_upload_6.png", "tirumala_herbal_white", (30, 140, 185, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_herbal_green", (190, 140, 340, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_acid_orange", (335, 140, 485, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_acid_blue", (495, 140, 645, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_acid_red", (640, 140, 790, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_ant_killer_large", (770, 190, 890, 530), bg_upload_6),
    ("new_upload_6.png", "tirumala_ant_killer_small", (875, 270, 914, 530), bg_upload_6),

    # 2. new_upload_1.jpg (Acid & Black Phenyl)
    ("new_upload_1.jpg", "tirumala_acid_green_bottle", (340, 200, 430, 505), bg_upload_1),
    ("new_upload_1.jpg", "tirumala_black_phenyl_brown_bottle", (415, 240, 495, 505), bg_upload_1),

    # 3. new_upload_3.jpg (Tirumala Floor Cleaner - all flavors)
    ("new_upload_3.jpg", "tirumala_floor_yellow", (330, 150, 425, 470), bg_upload_3),
    ("new_upload_3.jpg", "tirumala_floor_pink", (410, 150, 495, 470), bg_upload_3),
    ("new_upload_3.jpg", "tirumala_floor_orange", (480, 150, 565, 470), bg_upload_3),
    ("new_upload_3.jpg", "tirumala_floor_white", (550, 150, 635, 470), bg_upload_3),
    ("new_upload_3.jpg", "tirumala_floor_green", (160, 470, 260, 682), bg_upload_3),
    ("new_upload_3.jpg", "tirumala_floor_lavender", (565, 470, 660, 682), bg_upload_3),

    # 4. new_upload_2.jpg (Liger Floor Cleaner)
    ("new_upload_2.jpg", "liger_floor_yellow", (455, 200, 540, 495), bg_upload_2),
    ("new_upload_2.jpg", "liger_floor_pink", (270, 490, 365, 682), bg_upload_2),
    ("new_upload_2.jpg", "liger_floor_green", (340, 490, 435, 682), bg_upload_2),
    ("new_upload_2.jpg", "liger_floor_orange", (525, 175, 605, 495), bg_upload_2),
    ("new_upload_2.jpg", "liger_floor_white", (195, 490, 290, 682), bg_upload_2),

    # 5. new_upload_4.jpg (Home Doctor Floor Cleaner)
    ("new_upload_4.jpg", "home_doctor_floor_orange", (370, 165, 455, 495), bg_upload_4),
    ("new_upload_4.jpg", "home_doctor_floor_pink", (495, 210, 570, 495), bg_upload_4),
    ("new_upload_4.jpg", "home_doctor_floor_yellow", (505, 490, 590, 682), bg_upload_4),
    ("new_upload_4.jpg", "home_doctor_floor_white", (650, 490, 745, 682), bg_upload_4),
    ("new_upload_4.jpg", "home_doctor_floor_green", (340, 490, 435, 682), bg_upload_4)
]

print("=== STARTING PERFECT CHROMA-KEY EXTRACTOR ===")
success_count = 0
for filename, name, bbox, bg_check in bottle_manifest:
    if clean_bottle(filename, name, bbox, bg_check):
        success_count += 1
print(f"=== COMPLETED PERFECT CHROMA-KEY EXTRACTOR: {success_count}/{len(bottle_manifest)} files processed ===")
