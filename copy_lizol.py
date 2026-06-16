import os
import shutil

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
assets_dest = r"c:\Users\kavya\Desktop\Tirumala2\assets"

src_path = os.path.join(brain_dir, "tirumala_floor_lizol_1780648921022.png")
dest_path = os.path.join(assets_dest, "tirumala_floor_lizol.png")

if os.path.exists(src_path):
    shutil.copy(src_path, dest_path)
    print(f"Copied: {src_path} -> {dest_path}")
else:
    print(f"Source file not found: {src_path}")
