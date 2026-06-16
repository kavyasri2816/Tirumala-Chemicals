import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_5.jpg")

if not os.path.exists(src):
    print("new_upload_5.jpg not found")
else:
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    datas = img.getdata()
    new_data = []
    
    for item in datas:
        r, g, b, a = item
        # Detect red box color:
        # Red is dominant, green and blue are low.
        is_red = (r > 110 and g < 90 and b < 90 and r > g + 30 and r > b + 30)
        
        if is_red:
            new_data.append((r, g, b, a))
        else:
            new_data.append((255, 255, 255, 0)) # transparent
            
    img.putdata(new_data)
    
    # We crop to the bounding box of the red pixels
    bbox = img.getbbox()
    if bbox:
        # Let's crop from the original image using this bbox
        orig_img = Image.open(src).convert("RGBA")
        # Let's add a small padding (e.g. 10 pixels) to avoid cutting the edges of the box
        x1, y1, x2, y2 = bbox
        x1 = max(0, x1 - 5)
        y1 = max(0, y1 - 5)
        x2 = min(w, x2 + 5)
        y2 = min(h, y2 + 5)
        
        cropped = orig_img.crop((x1, y1, x2, y2))
        
        # Center in a clean 800x800 white background canvas
        canvas_size = 800
        canvas = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 255))
        
        cw, ch = cropped.size
        ratio = min(650.0 / cw, 650.0 / ch)
        new_w = int(cw * ratio)
        new_h = int(ch * ratio)
        
        resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
        offset_x = (canvas_size - new_w) // 2
        offset_y = (canvas_size - new_h) // 2
        
        canvas.paste(resized, (offset_x, offset_y), resized)
        
        final_img = canvas.convert("RGB")
        dest_path = os.path.join(assets_dir, "cheetah_ant_killer.png")
        final_img.save(dest_path, "PNG")
        print(f"Saved Cheetah Ant Killer image to {dest_path} with size {final_img.size}")
    else:
        print("No red bounding box found!")
        # Fallback crop center region
        cropped = Image.open(src).crop((100, 200, 668, 824))
        cropped.save(os.path.join(assets_dir, "cheetah_ant_killer.png"))
        print("Saved fallback crop to assets/cheetah_ant_killer.png")
