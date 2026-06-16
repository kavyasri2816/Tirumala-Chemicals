import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src = os.path.join(assets_dir, "new_upload_6.png")

if not os.path.exists(src):
    print("new_upload_6.png not found")
else:
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    datas = img.getdata()
    new_data = []
    
    for item in datas:
        r, g, b, a = item
        
        # Teal wall background detection:
        # wall has R around 30-70, G around 120-190, B around 140-220
        is_wall = (r < 110 and g > 100 and b > 120 and b > r + 30 and g > r + 20)
        
        # Beige floor background detection:
        # floor has R, G, B > 180 and very close to each other
        # floor reflections: can have high values
        is_floor = (r > 175 and g > 175 and b > 155) or \
                   (r > 150 and g > 150 and b > 140 and abs(r - g) < 20 and abs(g - b) < 20)
                   
        if is_wall or is_floor:
            new_data.append((255, 255, 255, 0)) # transparent
        else:
            new_data.append((r, g, b, a))
            
    img.putdata(new_data)
    img.save(os.path.join(assets_dir, "test_segmented.png"))
    print("Saved test_segmented.png")
    
    # Analyze non-transparent pixel count per column (x-axis)
    col_counts = [0] * w
    for y in range(h):
        for x in range(w):
            if img.getpixel((x, y))[3] > 0:
                col_counts[x] += 1
                
    # Group columns into 7 regions
    in_bottle = False
    regions = []
    start_x = 0
    
    # We look for continuous columns with non-transparent pixels
    # We filter out small noise by requiring a minimum of 2 columns
    for x in range(w):
        # column has some active pixels
        active = col_counts[x] > 5 # threshold to filter noise
        if active and not in_bottle:
            in_bottle = True
            start_x = x
        elif not active and in_bottle:
            in_bottle = False
            end_x = x
            if end_x - start_x >= 5: # minimum width of a bottle
                regions.append((start_x, end_x))
                
    if in_bottle:
        regions.append((start_x, w))
        
    print(f"Detected {len(regions)} columns of bottles:")
    for idx, (x1, x2) in enumerate(regions):
        # Find y1 and y2 for this column range
        y1, y2 = h, 0
        for y in range(h):
            for x in range(x1, x2):
                if img.getpixel((x, y))[3] > 0:
                    if y < y1:
                        y1 = y
                    if y > y2:
                        y2 = y
        print(f"Bottle {idx+1}: x range ({x1}, {x2}), y range ({y1}, {y2})")
