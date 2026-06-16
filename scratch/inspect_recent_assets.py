import os
import time

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
files = [os.path.join(assets_dir, f) for f in os.listdir(assets_dir)]
files.sort(key=os.path.getmtime, reverse=True)

print("Recent files in assets:")
for f in files[:20]:
    print(f"{os.path.basename(f)}: size={os.path.getsize(f)} bytes, modified={time.ctime(os.path.getmtime(f))}")
