import os
from PIL import Image, ImageFilter

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

def flood_fill_bg(img, tolerance=45):
    w, h = img.size
    # Convert to RGBA
    img = img.convert("RGBA")
    pixels = img.load()
    
    # Visited grid
    visited = [[False for _ in range(h)] for _ in range(w)]
    
    # We collect seed pixels from the borders (top, bottom, left, right)
    seeds = []
    # Top and bottom borders
    for x in range(w):
        seeds.append((x, 0))
        seeds.append((x, h-1))
    # Left and right borders
    for y in range(1, h-1):
        seeds.append((0, y))
        seeds.append((w-1, y))
        
    # Queue for BFS
    queue = []
    for x, y in seeds:
        queue.append((x, y))
        visited[x][y] = True
        
    # Standard color references for backgrounds to check if we can fill:
    # Teal wall and beige floor are the main ones
    # We get the initial colors at the corners as reference
    ref_colors = [
        pixels[0, 0][:3],
        pixels[w-1, 0][:3],
        pixels[0, h-1][:3],
        pixels[w-1, h-1][:3]
    ]
    
    while queue:
        cx, cy = queue.pop(0)
        curr_color = pixels[cx, cy][:3]
        
        # Check 4-neighborhood
        for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[nx][ny]:
                    n_color = pixels[nx, ny][:3]
                    
                    # We check if the neighbor color is close to the current color,
                    # or close to any of our starting corner reference colors.
                    is_similar = False
                    
                    # 1. Close to current background pixel
                    if distance(n_color, curr_color) < 18:
                        is_similar = True
                    # 2. Close to starting corner colors
                    elif min(distance(n_color, ref) for ref in ref_colors) < tolerance:
                        is_similar = True
                    # 3. Teal wall specifically
                    elif n_color[2] > n_color[0] + 30 and n_color[1] > n_color[0] + 20 and n_color[0] < 110:
                        is_similar = True
                    # 4. Stand shadows (dark grey/brown steps)
                    elif n_color[0] < 95 and n_color[1] < 80 and n_color[2] < 70:
                        # only fill if it's not a dark bottle
                        is_similar = True
                        
                    if is_similar:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        
    # Set visited pixels (background) to transparent
    for x in range(w):
        for y in range(h):
            if visited[x][y]:
                pixels[x, y] = (255, 255, 255, 0)
                
    return img

def extract_and_clean_bottle_premium(src_filename, name_prefix, bbox, tolerance=50):
    src_path = os.path.join(assets_dir, src_filename)
    if not os.path.exists(src_path):
        print(f"Source {src_filename} not found")
        return False
        
    img = Image.open(src_path)
    cropped = img.crop(bbox)
    
    # Run flood fill background removal
    cleaned = flood_fill_bg(cropped, tolerance=tolerance)
    
    # Smooth the alpha mask slightly to remove jagged edges (feathering)
    alpha = cleaned.split()[3]
    alpha_blur = alpha.filter(ImageFilter.GaussianBlur(1.0))
    # Threshold the blurred alpha back to solid/transparent but with smoother edges
    alpha_smooth = alpha_blur.point(lambda p: 255 if p > 100 else 0)
    cleaned.putalpha(alpha_smooth)
    
    # Crop to exact non-transparent bounding box
    bbox_inner = cleaned.getbbox()
    if bbox_inner:
        final_cropped = cleaned.crop(bbox_inner)
    else:
        final_cropped = cleaned
        
    # Center in a clean 800x800 white background canvas
    canvas_size = 800
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
    
    # Resize cropped image to fit in 650x650
    fcw, fch = final_cropped.size
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
    print(f"Extracted Premium: {name_prefix}.png (Size: {final_img.size})")
    return True

# Corrected bounding boxes (slightly wider and taller to avoid cutting off parts)
bottle_manifest = [
    # 1. new_upload_6.png (7 bottles)
    ("new_upload_6.png", "tirumala_herbal_white", (30, 140, 185, 530), 65),
    ("new_upload_6.png", "tirumala_herbal_green", (190, 140, 340, 530), 65),
    ("new_upload_6.png", "tirumala_acid_orange", (335, 140, 485, 530), 65),
    ("new_upload_6.png", "tirumala_acid_blue", (495, 140, 645, 530), 65),
    ("new_upload_6.png", "tirumala_acid_red", (640, 140, 790, 530), 65),
    ("new_upload_6.png", "tirumala_ant_killer_large", (770, 190, 890, 530), 65),
    ("new_upload_6.png", "tirumala_ant_killer_small", (875, 270, 914, 530), 65),

    # 2. new_upload_1.jpg (Acid & Black Phenyl)
    ("new_upload_1.jpg", "tirumala_acid_green_bottle", (340, 200, 430, 505), 55),
    ("new_upload_1.jpg", "tirumala_black_phenyl_brown_bottle", (415, 240, 495, 505), 50),

    # 3. new_upload_3.jpg (Tirumala Floor Cleaner - all flavors)
    ("new_upload_3.jpg", "tirumala_floor_yellow", (330, 150, 425, 470), 55),
    ("new_upload_3.jpg", "tirumala_floor_pink", (410, 150, 495, 470), 55),
    ("new_upload_3.jpg", "tirumala_floor_orange", (480, 150, 565, 470), 55),
    ("new_upload_3.jpg", "tirumala_floor_white", (550, 150, 635, 470), 55),
    ("new_upload_3.jpg", "tirumala_floor_green", (160, 470, 260, 682), 55),
    ("new_upload_3.jpg", "tirumala_floor_lavender", (565, 470, 660, 682), 55),

    # 4. new_upload_2.jpg (Liger Floor Cleaner)
    ("new_upload_2.jpg", "liger_floor_yellow", (455, 200, 540, 495), 55),
    ("new_upload_2.jpg", "liger_floor_pink", (270, 490, 365, 682), 55),
    ("new_upload_2.jpg", "liger_floor_green", (340, 490, 435, 682), 55),
    ("new_upload_2.jpg", "liger_floor_orange", (525, 175, 605, 495), 55),
    ("new_upload_2.jpg", "liger_floor_white", (195, 490, 290, 682), 55),

    # 5. new_upload_4.jpg (Home Doctor Floor Cleaner)
    ("new_upload_4.jpg", "home_doctor_floor_orange", (370, 165, 455, 495), 55),
    ("new_upload_4.jpg", "home_doctor_floor_pink", (495, 210, 570, 495), 55),
    ("new_upload_4.jpg", "home_doctor_floor_yellow", (505, 490, 590, 682), 55),
    ("new_upload_4.jpg", "home_doctor_floor_white", (650, 490, 745, 682), 55),
    ("new_upload_4.jpg", "home_doctor_floor_green", (340, 490, 435, 682), 55)
]

print("=== STARTING FLOOD FILL PREMIUM EXTRACTOR ===")
for filename, name, bbox, tol in bottle_manifest:
    extract_and_clean_bottle_premium(filename, name, bbox, tol)
print("=== COMPLETED FLOOD FILL PREMIUM EXTRACTOR ===")
