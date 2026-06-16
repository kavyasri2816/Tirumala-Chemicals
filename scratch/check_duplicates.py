import os
import hashlib

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

def get_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

# Get hashes of all unique_*.jpg
unique_hashes = {}
for filename in os.listdir(assets_dir):
    if filename.startswith("unique_") and filename.endswith(".jpg"):
        filepath = os.path.join(assets_dir, filename)
        unique_hashes[get_md5(filepath)] = filename

print("Comparing new uploads with existing assets:")
for i in range(1, 6):
    filepath = os.path.join(assets_dir, f"new_upload_{i}.jpg")
    if os.path.exists(filepath):
        h = get_md5(filepath)
        if h in unique_hashes:
            print(f"new_upload_{i}.jpg is IDENTICAL to {unique_hashes[h]}")
        else:
            print(f"new_upload_{i}.jpg is a NEW image (MD5: {h})")
