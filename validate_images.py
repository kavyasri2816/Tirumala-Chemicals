import os

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
expected_files = [
    "bleach.png",
    "liquid_bleach.png",
    "floor_cleaner.png",
    "glass_cleaner.png",
    "white_phenyl.png",
    "lemon_floor_cleaner.png",
    "lavender_floor_cleaner.png",
    "jasmine_floor_cleaner.png",
    "toilet_cleaner.png",
    "toilet_cleaner_white.png",
    "dish_wash.png",
    "hand_wash.png",
    "hand_wash_rose.png",
    "hand_wash_lemon.png",
    "hand_wash_herbal.png"
]

print("=== VERIFYING FINAL IMAGES ===")
missing_count = 0
for filename in expected_files:
    path = os.path.join(assets_dir, filename)
    if os.path.exists(path):
        size_kb = os.path.getsize(path) / 1024
        print(f"OK: {filename} ({size_kb:.1f} KB)")
    else:
        print(f"MISSING: {filename}")
        missing_count += 1

print(f"Verification finished. Missing files: {missing_count}")
if missing_count == 0:
    print("SUCCESS: All product images successfully renamed and cleaned!")
else:
    print("WARNING: Some expected files are missing!")
