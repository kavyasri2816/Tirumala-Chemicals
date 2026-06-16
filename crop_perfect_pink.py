import os
from PIL import Image

def test_perfect_crop():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    src_path = os.path.join(assets_dir, "unique_5.jpg")
    
    img = Image.open(src_path).convert("RGB")
    
    # Let's crop exactly the pink bottle area
    crop_x1, crop_x2 = 417, 506
    crop_y1, crop_y2 = 240, 580
    
    cropped = img.crop((crop_x1, crop_y1, crop_x2, crop_y2))
    dest_path = os.path.join(assets_dir, "test_perfect_crop.png")
    cropped.save(dest_path)
    print(f"Saved test crop to {dest_path}")

if __name__ == '__main__':
    test_perfect_crop()
