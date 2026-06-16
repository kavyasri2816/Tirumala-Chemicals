import os
import hashlib

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def get_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

all_files = [f for f in os.listdir(assets_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
hashes = {}
for filename in all_files:
    filepath = os.path.join(assets_dir, filename)
    hashes[filename] = get_md5(filepath)

for i in range(1, 6):
    upload_name = f"new_upload_{i}.jpg"
    upload_path = os.path.join(assets_dir, upload_name)
    if not os.path.exists(upload_path):
        continue
    upload_hash = hashes[upload_name]
    matches = []
    for f, h in hashes.items():
        if f != upload_name and h == upload_hash:
            matches.append(f)
    print(f"{upload_name} matches: {matches}")
