import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
files = [f for f in os.listdir(assets_dir) if f.startswith("unique_") and f.endswith(".jpg")]
files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

for filename in files:
    path = os.path.join(assets_dir, filename)
    try:
        img = Image.open(path).convert("RGB")
        # Resize to 200x200 for faster scanning
        img_small = img.resize((200, 200))
        pink_count = 0
        yellow_count = 0
        green_count = 0
        
        for y in range(200):
            for x in range(200):
                r, g, b = img_small.getpixel((x, y))
                # Pink detector: high red, high blue, low green
                if r > 150 and b > 100 and g < 120 and abs(r - b) < 80:
                    pink_count += 1
                # Yellow detector: high red, high green, low blue
                if r > 160 and g > 150 and b < 100:
                    yellow_count += 1
                # Green detector: high green, low red, low blue
                if g > 120 and r < 100 and b < 100:
                    green_count += 1
                    
        if pink_count > 500 or yellow_count > 500:
            print(f"{filename}: pink_pixels={pink_count}, yellow_pixels={yellow_count}, green_pixels={green_count}")
    except Exception as e:
        print(f"Error {filename}: {e}")
