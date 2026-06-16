import os
from PIL import Image, ImageFilter

def clean_perfect_crop():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    src_path = os.path.join(assets_dir, "test_perfect_crop.png")
    
    if not os.path.exists(src_path):
        print(f"Source file not found: {src_path}")
        return
        
    img = Image.open(src_path).convert("RGBA")
    width, height = img.size
    
    datas = img.getdata()
    new_data = []
    
    for item in datas:
        r, g, b, a = item
        
        # Background detection:
        # Grayish-blue background in unique_5.jpg has:
        # r ~ 130-185, g ~ 140-195, b ~ 155-215
        # And b is generally greater than r and g.
        is_bg = (120 <= r <= 195 and 130 <= g <= 205 and 145 <= b <= 230) and (b > r + 5 and b > g + 2)
        
        # Soft edges / shadows near the bottom:
        # A grey shadow near the bottom might have lower brightness, e.g., r, g, b around 100-140 and close to each other.
        is_shadow = (80 <= r <= 140 and 85 <= g <= 145 and 95 <= b <= 160) and (b > r + 3 and b > g + 2)
        
        # Check if it's clearly not a bottle color
        # Bottle pink: r > 180, g < 120, b > 100
        # Bottle blue cap/label: b > 110, r < 100, g < 120
        # Bottle white label: r > 180, g > 180, b > 170
        is_bottle = (r > 175 and g < 120 and b > 95) or \
                    (b > 100 and r < 110 and g < 130) or \
                    (r > 170 and g > 170 and b > 160) or \
                    (r > 150 and g > 130 and b < 100) # yellow text/flowers
                    
        if (is_bg or is_shadow) and not is_bottle:
            new_data.append((255, 255, 255, 0)) # transparent
        else:
            new_data.append((r, g, b, a))
            
    img.putdata(new_data)
    
    # Crop the transparent image to its exact non-transparent bounding box
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        print(f"Cropped to exact bounding box: {bbox}")
    else:
        cropped = img
        print("No bounding box found, using original size.")
        
    # Center in a clean 800x800 white background canvas
    canvas_size = 800
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
    
    # Resize cropped image to fit in 650x650
    cw, ch = cropped.size
    ratio = min(650.0 / cw, 650.0 / ch)
    new_w = int(cw * ratio)
    new_h = int(ch * ratio)
    
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Paste centered
    offset_x = (canvas_size - new_w) // 2
    offset_y = (canvas_size - new_h) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)
    
    # Convert to RGB (removes alpha channel, saving as pure white background JPG/PNG)
    final_img = canvas.convert("RGB")
    dest_path = os.path.join(assets_dir, "tirumala_floor_lizol.png")
    final_img.save(dest_path, "PNG")
    print(f"Saved cleaned perfect floor cleaner image to {dest_path}")

if __name__ == '__main__':
    clean_perfect_crop()
