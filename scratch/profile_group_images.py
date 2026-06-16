import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def profile_image_columns(filename, num_cols=12):
    filepath = os.path.join(assets_dir, filename)
    if not os.path.exists(filepath):
        print(f"{filename} not found")
        return
        
    img = Image.open(filepath).convert("RGB")
    w, h = img.size
    col_w = w // num_cols
    
    # We profile the middle region vertically (e.g. from 40% to 90% of height) to focus on the bottles
    y1, y2 = int(h * 0.45), int(h * 0.95)
    
    print(f"\n=== Column Color Profiling for {filename} (Width={w}, Height={h}) ===")
    for c in range(num_cols):
        x1 = c * col_w
        x2 = (c + 1) * col_w
        cropped = img.crop((x1, y1, x2, y2))
        avg = cropped.resize((1, 1)).getpixel((0,0))
        # classify color based on simple RGB rules
        r, g, b = avg
        color_name = "Grey/Brown"
        if r > 180 and g > 180 and b > 180:
            color_name = "White"
        elif r > 170 and g > 160 and b < 130:
            color_name = "Yellow/Orange"
        elif r > 150 and g < 110 and b > 110:
            color_name = "Pink/Lavender"
        elif g > r + 15 and g > b + 15:
            color_name = "Green"
        elif r > 150 and g > 110 and b < 100:
            color_name = "Yellow/Orange"
            
        print(f"Col {c:02d}: x range ({x1:03d}, {x2:03d}) -> Avg RGB={avg} -> Classification: {color_name}")

profile_image_columns("new_upload_2.jpg")
profile_image_columns("new_upload_3.jpg")
profile_image_columns("new_upload_4.jpg")
