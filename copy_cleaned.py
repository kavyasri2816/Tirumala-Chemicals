import os
import shutil

assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"

# Define mappings from clean_unique_X.png to final filenames
mappings = {
    "clean_unique_1.png": "bleach.png",                # Bleaching Powder Jars
    "clean_unique_28.png": "liquid_bleach.png",        # Liquid Bleach 5L Can
    "clean_unique_5.png": "glass_cleaner.png",         # Coli Fresh Glass Cleaner Blue Spray
    "clean_unique_6.png": "toilet_cleaner.png",        # Toilet Cleaner Blue Squeeze Bottle
    "clean_unique_7.png": "toilet_cleaner_white.png",  # Toilet Cleaner White Orange Cap
    "clean_unique_10.png": "hand_wash_rose.png",       # Rose Hand Wash Pink Pump
    "clean_unique_13.png": "hand_wash_lemon.png",      # Lemon Hand Wash Yellow Pump
    "clean_unique_17.png": "hand_wash_herbal.png",     # Herbal Hand Wash Green Pump
    "clean_unique_20.png": "dish_wash.png",            # Dish Wash Liquid Green Squeeze
    
    # Subproducts / Floor Cleaners
    "clean_unique_27.png": "white_phenyl.png",         # White Phenyl
    "clean_unique_4.png": "lemon_floor_cleaner.png",   # Lemon Floor Cleaner (Yellow)
    "clean_unique_3.png": "lavender_floor_cleaner.png",# Lavender Floor Cleaner (Purple)
    "clean_unique_2.png": "jasmine_floor_cleaner.png", # Jasmine Floor Cleaner (Green)
}

print("=== COPYING CLEANED IMAGES TO DESCRIPTIVE NAMES ===")
for src_name, dest_name in mappings.items():
    src_path = os.path.join(assets_dir, src_name)
    dest_path = os.path.join(assets_dir, dest_name)
    if os.path.exists(src_path):
        if src_path.lower() == dest_path.lower():
            continue
        try:
            shutil.copy(src_path, dest_path)
            print(f"Copied {src_name} -> {dest_name}")
        except Exception as e:
            print(f"Error copying {src_name} to {dest_name}: {e}")
    else:
        print(f"Source file not found: {src_path}")
        
# Set category cover images
covers = {
    "bleach.png": "bleach.png", # Bleach category cover
    "glass_cleaner.png": "floor_cleaner.png", # Floor & Glass category cover
    "hand_wash_rose.png": "hand_wash.png", # Hand Wash category cover
}

for src_name, dest_name in covers.items():
    src_path = os.path.join(assets_dir, src_name)
    dest_path = os.path.join(assets_dir, dest_name)
    if os.path.exists(src_path):
        if src_path.lower() == dest_path.lower():
            continue
        try:
            shutil.copy(src_path, dest_path)
            print(f"Copied cover: {src_name} -> {dest_name}")
        except Exception as e:
            print(f"Error copying cover {src_name} to {dest_name}: {e}")
