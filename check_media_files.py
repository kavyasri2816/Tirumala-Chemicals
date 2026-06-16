import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
for f in os.listdir(assets_dir):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Check if file is recently modified or contains 'media' or 'warehouse' or 'production'
        if 'media' in f.lower() or 'warehouse' in f.lower() or 'production' in f.lower():
            path = os.path.join(assets_dir, f)
            img = Image.open(path)
            print(f"{f}: size={img.size}")
