import os
import time

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"

all_files = []
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        filepath = os.path.join(root, f)
        all_files.append((filepath, os.path.getmtime(filepath)))

all_files.sort(key=lambda x: x[1], reverse=True)

print("Recently modified files in brain folder:")
for path, mtime in all_files[:25]:
    print(f"{os.path.relpath(path, brain_dir)}: size={os.path.getsize(path)} bytes, modified={time.ctime(mtime)}")
