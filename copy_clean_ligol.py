import os
import shutil

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
src_path = os.path.join(assets_dir, "clean_unique_25.png")
dest_path = os.path.join(assets_dir, "tirumala_floor_lizol.png")

if os.path.exists(src_path):
    shutil.copy(src_path, dest_path)
    print(f"Copied cleaned product photo: {src_path} -> {dest_path}")
else:
    print(f"Cleaned source file not found: {src_path}")
