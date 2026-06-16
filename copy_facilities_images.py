import os
import shutil

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

src_dest_pairs = [
    ("WhatsApp Image 2026-06-05 at 2.27.29 PM.jpeg", "facility_production_house.jpg"),
    ("WhatsApp Image 2026-06-05 at 2.26.47 PM.jpeg", "facility_floor_cleaner.jpg"),
    ("WhatsApp Image 2026-06-05 at 2.26.46 PM.jpeg", "facility_warehouse.jpg")
]

for src_name, dest_name in src_dest_pairs:
    src_path = os.path.join(assets_dir, src_name)
    dest_path = os.path.join(assets_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied: {src_name} -> {dest_name}")
    else:
        print(f"Source file not found: {src_path}")
