import os
import hashlib

def get_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
files = [f for f in os.listdir(assets_dir) if f.startswith("WhatsApp Image")]
files.sort()

unique_hashes = {}
for filename in files:
    filepath = os.path.join(assets_dir, filename)
    h = get_md5(filepath)
    if h not in unique_hashes:
        unique_hashes[h] = []
    unique_hashes[h].append(filename)

print(f"Found {len(unique_hashes)} unique images.")
for idx, (h, filenames) in enumerate(unique_hashes.items()):
    print(f"unique_{idx}.jpg: {filenames[0]} (Count: {len(filenames)})")
