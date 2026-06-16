import os
from PIL import Image

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
for i in range(30):
    filename = f"unique_{i}.jpg"
    path = os.path.join(assets_dir, filename)
    if os.path.exists(path):
        try:
            img = Image.open(path)
            # Let's get average color or check if it's pink or what it shows
            # We can also just print the image size
            print(f"{filename}: size={img.size}")
        except Exception as e:
            print(f"Error {filename}: {e}")
