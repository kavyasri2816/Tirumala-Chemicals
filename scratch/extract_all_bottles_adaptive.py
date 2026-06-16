import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

def extract_and_clean_bottle(src_filename, name_prefix, bbox, tolerance_top=55, tolerance_bottom=55):
    src_path = os.path.join(assets_dir, src_filename)
    if not os.path.exists(src_path):
        print(f"Source {src_filename} not found")
        return False
        
    img = Image.open(src_path)
    cropped = img.crop(bbox).convert("RGBA")
    cw, ch = cropped.size
    
    # Adaptive background colors from corners
    bg_top_left = cropped.getpixel((2, 2))[:3]
    bg_top_right = cropped.getpixel((cw - 3, 2))[:3]
    bg_bottom_left = cropped.getpixel((2, ch - 3))[:3]
    bg_bottom_right = cropped.getpixel((cw - 3, ch - 3))[:3]
    
    # We will also check if the background is a wood stand (often very dark, e.g., < 80)
    # We will make sure not to remove bright colors
    datas = cropped.getdata()
    new_data = []
    
    for y in range(ch):
        for x in range(cw):
            r, g, b, a = cropped.getpixel((x, y))
            color = (r, g, b)
            
            # Check distance to top background (wall)
            d_top = min(distance(color, bg_top_left), distance(color, bg_top_right))
            # Check distance to bottom background (floor/shelf)
            d_bottom = min(distance(color, bg_bottom_left), distance(color, bg_bottom_right))
            
            # Is it close to background?
            # We want to be careful not to remove the bottle.
            # If the bottle is white, and the background is white/light, we use smaller tolerance.
            is_bg = False
            
            # top background removal (wall/wood steps)
            if y < ch * 0.7:
                if d_top < tolerance_top:
                    is_bg = True
            else:
                if d_top < tolerance_top or d_bottom < tolerance_bottom:
                    is_bg = True
                    
            # Additional floor/wood step shadow heuristics
            # dark stand/shadow
            if r < 100 and g < 85 and b < 75:
                # unless the bottle itself is dark (Tirumala Black Phenyl)
                if "tirumala_black_phenyl" not in name_prefix:
                    is_bg = True
                    
            if is_bg:
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
        
    # Center in a clean 800x800 white background canvas
    canvas_size = 800
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
    
    # Resize cropped image to fit in 650x650
    fcw, fch = final_cropped.size
    ratio = min(650.0 / fcw, 650.0 / fch)
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
    print(f"Extracted and saved: {name_prefix}.png")
    return True

# Define coordinates for all bottles in a clean list
bottle_manifest = [
    # 1. new_upload_6.png (7 bottles)
    ("new_upload_6.png", "tirumala_herbal_white", (30, 150, 175, 520), 60, 60),
    ("new_upload_6.png", "tirumala_herbal_green", (190, 150, 335, 520), 60, 60),
    ("new_upload_6.png", "tirumala_acid_orange", (340, 150, 480, 520), 60, 60),
    ("new_upload_6.png", "tirumala_acid_blue", (500, 150, 640, 520), 60, 60),
    ("new_upload_6.png", "tirumala_acid_red", (645, 150, 785, 520), 60, 60),
    ("new_upload_6.png", "tirumala_ant_killer_large", (775, 200, 885, 520), 60, 60),
    ("new_upload_6.png", "tirumala_ant_killer_small", (880, 280, 914, 520), 60, 60),

    # 2. new_upload_1.jpg (Acid & Black Phenyl)
    ("new_upload_1.jpg", "tirumala_acid_green_bottle", (350, 210, 420, 500), 50, 50),
    ("new_upload_1.jpg", "tirumala_black_phenyl_brown_bottle", (420, 250, 485, 500), 45, 45),

    # 3. new_upload_3.jpg (Tirumala Floor Cleaner - all flavors)
    ("new_upload_3.jpg", "tirumala_floor_yellow", (340, 160, 415, 460), 50, 50),
    ("new_upload_3.jpg", "tirumala_floor_pink", (415, 160, 485, 460), 50, 50),
    ("new_upload_3.jpg", "tirumala_floor_orange", (485, 160, 555, 460), 50, 50),
    ("new_upload_3.jpg", "tirumala_floor_white", (555, 160, 625, 460), 50, 50),
    ("new_upload_3.jpg", "tirumala_floor_green", (170, 480, 250, 680), 50, 50),
    ("new_upload_3.jpg", "tirumala_floor_lavender", (575, 480, 650, 680), 50, 50),

    # 4. new_upload_2.jpg (Liger Floor Cleaner)
    ("new_upload_2.jpg", "liger_floor_yellow", (465, 210, 530, 490), 50, 50),
    ("new_upload_2.jpg", "liger_floor_pink", (280, 500, 360, 682), 50, 50),
    ("new_upload_2.jpg", "liger_floor_green", (350, 500, 430, 682), 50, 50),
    ("new_upload_2.jpg", "liger_floor_orange", (530, 180, 600, 490), 50, 50),
    ("new_upload_2.jpg", "liger_floor_white", (205, 500, 285, 682), 50, 50),

    # 5. new_upload_4.jpg (Home Doctor Floor Cleaner)
    ("new_upload_4.jpg", "home_doctor_floor_orange", (380, 175, 445, 490), 50, 50),
    ("new_upload_4.jpg", "home_doctor_floor_pink", (505, 220, 560, 490), 50, 50),
    ("new_upload_4.jpg", "home_doctor_floor_yellow", (515, 500, 580, 682), 50, 50),
    ("new_upload_4.jpg", "home_doctor_floor_white", (660, 500, 735, 682), 50, 50),
    ("new_upload_4.jpg", "home_doctor_floor_green", (350, 500, 430, 682), 50, 50)
]

print("=== STARTING ADAPTIVE EXTRACTOR ===")
for filename, name, bbox, tol_t, tol_b in bottle_manifest:
    extract_and_clean_bottle(filename, name, bbox, tol_t, tol_b)
print("=== COMPLETED ADAPTIVE EXTRACTOR ===")
