import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "test_segmented.png")

if not os.path.exists(src):
    print("test_segmented.png not found")
else:
    img = Image.open(src)
    w, h = img.size
    
    col_counts = [0] * w
    for y in range(h):
        for x in range(w):
            if img.getpixel((x, y))[3] > 0:
                col_counts[x] += 1
                
    # Print col_counts in chunks of 10 pixels for inspectability
    print("Column counts every 5 pixels:")
    for i in range(0, w, 5):
        chunk = col_counts[i:i+5]
        print(f"x={i:03d}-{i+4:03d}: {chunk}")
