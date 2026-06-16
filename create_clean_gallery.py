import os

def create_clean_gallery():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    workspace_dir = r"c:\Users\kavya\Desktop\Tirumala2"
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sri Tirumala - Product Images Audit Gallery</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
            padding: 40px 20px;
            margin: 0;
        }
        .header {
            max-width: 1200px;
            margin: 0 auto 40px auto;
            text-align: center;
        }
        .header h1 {
            color: #0f172a;
            font-size: 32px;
            margin-bottom: 10px;
        }
        .header p {
            color: #64748b;
            font-size: 16px;
        }
        .section-title {
            max-width: 1200px;
            margin: 40px auto 20px auto;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
            color: #1e293b;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto 40px auto;
        }
        .card {
            background-color: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            border: 1px solid #e2e8f0;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .img-comparison {
            display: flex;
            background-color: #f8fafc;
            border-bottom: 1px solid #f1f5f9;
        }
        .img-half {
            width: 50%;
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px;
            position: relative;
        }
        .img-half img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
        .img-half span {
            position: absolute;
            bottom: 5px;
            left: 5px;
            background-color: rgba(15, 23, 42, 0.7);
            color: #fff;
            font-size: 9px;
            padding: 2px 6px;
            border-radius: 3px;
            text-transform: uppercase;
        }
        .details {
            padding: 15px;
            text-align: center;
            background: #fff;
        }
        .filename {
            font-size: 13px;
            font-weight: 600;
            color: #334155;
            word-break: break-all;
            margin-bottom: 8px;
        }
        .final-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .final-card {
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            text-align: center;
        }
        .final-img-container {
            height: 180px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #ffffff;
            padding: 10px;
        }
        .final-img-container img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
        .final-title {
            padding: 10px;
            font-size: 12px;
            font-weight: 700;
            background-color: #f8fafc;
            border-top: 1px solid #e2e8f0;
            color: #0f172a;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Sri Tirumala - Product Images Audit Gallery</h1>
        <p>Comparison of original user photos (left) vs cropped and background-removed e-commerce shots (right)</p>
    </div>
    
    <h2 class="section-title">Final Website Product Mapping</h2>
    <div class="final-grid">
"""
    
    # Final descriptive files
    descriptives = [
        ("bleach.png", "Bleaching Powder Jars"),
        ("liquid_bleach.png", "Liquid Bleach Can"),
        ("floor_cleaner.png", "Floor Cleaner Category Cover"),
        ("glass_cleaner.png", "Coli Fresh Glass Cleaner"),
        ("white_phenyl.png", "White Phenyl Bottle"),
        ("lemon_floor_cleaner.png", "Lemon Floor Cleaner"),
        ("lavender_floor_cleaner.png", "Lavender Floor Cleaner"),
        ("jasmine_floor_cleaner.png", "Jasmine Floor Cleaner"),
        ("toilet_cleaner.png", "Toilet Cleaner (Blue)"),
        ("toilet_cleaner_white.png", "Toilet Cleaner (White/Bathroom)"),
        ("dish_wash.png", "Dish Wash Liquid"),
        ("hand_wash.png", "Hand Wash Category Cover"),
        ("hand_wash_rose.png", "Rose Hand Wash (Pink)"),
        ("hand_wash_lemon.png", "Lemon Hand Wash (Yellow)"),
        ("hand_wash_herbal.png", "Herbal Hand Wash (Green)")
    ]
    
    for f, label in descriptives:
        html += f"""
        <div class="final-card">
            <div class="final-img-container">
                <img src="assets/{f}" alt="{f}">
            </div>
            <div class="final-title">{label}<br><code style="font-size:10px;font-weight:400;">assets/{f}</code></div>
        </div>"""
        
    html += """
    </div>
    
    <h2 class="section-title">Original vs Cleaned Comparisons</h2>
    <div class="grid">
"""

    # We map original unique indices to the final descriptive filename
    mappings = {
        1: "bleach.png",
        28: "liquid_bleach.png",
        5: "glass_cleaner.png",
        6: "toilet_cleaner.png",
        7: "toilet_cleaner_white.png",
        10: "hand_wash_rose.png",
        13: "hand_wash_lemon.png",
        17: "hand_wash_herbal.png",
        20: "dish_wash.png",
        27: "white_phenyl.png",
        4: "lemon_floor_cleaner.png",
        3: "lavender_floor_cleaner.png",
        2: "jasmine_floor_cleaner.png"
    }
    
    for idx, dest_name in mappings.items():
        html += f"""
        <div class="card">
            <div class="img-comparison">
                <div class="img-half">
                    <img src="assets/unique_{idx}.jpg" alt="Original unique_{idx}.jpg">
                    <span>Original</span>
                </div>
                <div class="img-half">
                    <img src="assets/{dest_name}" alt="Cleaned {dest_name}">
                    <span>Cleaned</span>
                </div>
            </div>
            <div class="details">
                <div class="filename">unique_{idx}.jpg &rarr; {dest_name}</div>
            </div>
        </div>"""

    html += """
    </div>
</body>
</html>"""

    dest_path = os.path.join(workspace_dir, "gallery.html")
    with open(dest_path, "w", encoding="utf-8") as out:
        out.write(html)
    print(f"Cleaned Gallery HTML written successfully to {dest_path}")

if __name__ == '__main__':
    create_clean_gallery()
