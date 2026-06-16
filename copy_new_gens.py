import os
import shutil

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
assets_dest = r"c:\Users\kavya\Desktop\Tirumala2\assets"

mappings = {
    "tirumala_bleach_1780648737271.png": "tirumala_bleach.png",
    "tirumala_toilet_1780648753537.png": "tirumala_toilet.png",
    "tirumala_floor_1780648774727.png": "tirumala_floor.png",
    "tirumala_hand_1780648792888.png": "tirumala_hand.png",
    "tirumala_dish_1780648812414.png": "tirumala_dish.png",
    "tirumala_white_phenyl_1780648829485.png": "tirumala_white_phenyl.png",
    "tirumala_black_phenyl_1780648846917.png": "tirumala_black_phenyl.png"
}

print("=== COPYING NEWLY GENERATED IMAGES TO ASSETS ===")
copied_count = 0
for src_name, dest_name in mappings.items():
    src_path = os.path.join(brain_dir, src_name)
    dest_path = os.path.join(assets_dest, dest_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied: {src_name} -> {dest_name}")
        copied_count += 1
    else:
        print(f"Not found: {src_name}")

print(f"Copied {copied_count} of {len(mappings)} files.")
