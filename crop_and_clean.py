import os
from PIL import Image, ImageChops, ImageFilter

def remove_background_and_crop(src_path, dest_path):
    try:
        img = Image.open(src_path).convert("RGBA")
        width, height = img.size
        
        # We will scan pixels and create a mask
        # Typically background is green sheet. Let's detect green.
        # We also have some greyish/white floor backgrounds.
        datas = img.getdata()
        
        new_data = []
        for item in datas:
            r, g, b, a = item
            
            # 1. Green screen detection
            # Green is dominant
            is_green = (g > r * 1.05 and g > b * 1.05 and g > 30) or (g - r > 15 and g - b > 15)
            
            # 2. Light grey/white floor or background detection
            is_light_bg = (max(r, g, b) - min(r, g, b) < 25) and (r > 160 and g > 160 and b > 160)
            
            # 3. Soft yellow or brown floor detection
            is_floor = (r > 130 and g > 120 and b > 80) and (r - b > 30 and g - b > 20) and (r < 220 and g < 200 and b < 150) and (g > r * 0.8)
            
            # Combine
            if is_green or is_light_bg:
                new_data.append((255, 255, 255, 0)) # transparent
            else:
                new_data.append((r, g, b, a))
                
        img.putdata(new_data)
        
        # Simple cleanup: smooth the mask slightly if possible, or just crop
        bbox = img.getbbox()
        if not bbox:
            # If everything was removed, revert to original image centered
            img = Image.open(src_path).convert("RGBA")
            bbox = (0, 0, img.size[0], img.size[1])
            
        cropped = img.crop(bbox)
        
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
        
        # Paste using resized alpha channel as mask, but on white canvas
        canvas.paste(resized, (offset_x, offset_y), resized)
        
        # Convert to RGB (removes alpha channel, saving as pure white background JPG/PNG)
        final_img = canvas.convert("RGB")
        final_img.save(dest_path, "PNG")
        return True
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return False

if __name__ == '__main__':
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    
    print("=== STARTING CROP & BACKGROUND REMOVAL ===")
    for i in range(30):
        src = os.path.join(assets_dir, f"unique_{i}.jpg")
        dest = os.path.join(assets_dir, f"clean_unique_{i}.png")
        if os.path.exists(src):
            success = remove_background_and_crop(src, dest)
            if success:
                print(f"Successfully cleaned: unique_{i}.jpg -> clean_unique_{i}.png")
            else:
                print(f"Failed to clean: unique_{i}.jpg")
        else:
            print(f"File not found: {src}")
