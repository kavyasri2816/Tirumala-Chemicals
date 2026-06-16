import os
import time

workspace_dir = r"c:\Users\kavya\Desktop\Tirumala2"
print("=== SCANNING FOR IMAGES ===")
for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, f)
            mtime = os.path.getmtime(path)
            size = os.path.getsize(path)
            print(f"{os.path.relpath(path, workspace_dir)}: size={size} bytes, modified={time.ctime(mtime)}")
