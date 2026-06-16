import os
from PIL import Image

def clean_pink_bottle():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    src_path = os.path.join(assets_dir, "unique_5.jpg")
    
    img = Image.open(src_path).convert("RGBA")
    width, height = img.size
    
    # Bounding box coordinates for the pink bottle in unique_5.jpg
    # x: [390, 530]
    # y: [240, 580]
    crop_x1, crop_x2 = 390, 530
    crop_y1, crop_y2 = 240, 580
    
    cropped = img.crop((crop_x1, crop_y1, crop_x2, crop_y2))
    cw, ch = cropped.size
    
    # Process pixels of the crop
    datas = cropped.getdata()
    new_data = []
    
    for item in datas:
        r, g, b, a = item
        
        # 1. Background detection: gray/blue backdrop in unique_5.jpg
        # The background is bluish-gray: r ~ [130, 185], g ~ [140, 195], b ~ [155, 215]
        # And r, g, b are close to each other.
        is_bg = (120 <= r <= 190 and 130 <= g <= 200 and 145 <= b <= 220) and (b > r + 10 and b > g + 5)
        
        # 2. Green bottle detection (adjacent bottles): green is dominant
        is_green = (g > r + 10 and g > b + 10) or (g > 100 and r < 95 and b < 105)
        
        # 3. Yellow bottle detection (adjacent bottles on the far left/right if any)
        is_yellow = (r > 160 and g > 150 and b < 110)
        
        if is_bg or is_green or is_yellow:
            new_data.append((255, 255, 255, 0)) # transparent
        else:
            new_data.append((r, g, b, a))
            
    cropped.putdata(new_data)
    
    # Find bounding box of the non-transparent pixels in the cropped image
    bbox = cropped.getbbox()
    if bbox:
        cropped_exact = cropped.crop(bbox)
    else:
        cropped_exact = cropped
        
    # Center in a clean 800x800 white background canvas
    canvas_size = 800
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
    
    # Resize cropped image to fit in 650x650
    cew, ceh = cropped_exact.size
    ratio = min(650.0 / cew, 650.0 / ceh)
    new_w = int(cew * ratio)
    new_h = int(ceh * ratio)
    
    resized = cropped_exact.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Paste centered
    offset_x = (canvas_size - new_w) // 2
    offset_y = (canvas_size - new_h) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)
    
    # Save as PNG
    dest_path = os.path.join(assets_dir, "tirumala_floor_lizol.png")
    final_img = canvas.convert("RGB")
    final_img.save(dest_path, "PNG")
    print(f"Saved cleaned floor cleaner image to {dest_path}")

if __name__ == '__main__':
    clean_pink_bottle()
