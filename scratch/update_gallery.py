import os

gallery_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sri Tirumala - Branded E-commerce Product Gallery</title>
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
            font-size: 20px;
            font-weight: 700;
            border-left: 4px solid #0077b6;
            padding-left: 10px;
            color: #0f172a;
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
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .final-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        }
        .final-img-container {
            height: 180px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #ffffff;
            padding: 15px;
        }
        .final-img-container img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
        .final-title {
            padding: 12px;
            font-size: 13px;
            font-weight: 700;
            background-color: #f8fafc;
            border-top: 1px solid #e2e8f0;
            color: #0f172a;
        }
        .back-link {
            display: inline-block;
            margin-top: 30px;
            color: #0077b6;
            font-weight: 600;
            text-decoration: none;
        }
        .back-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Sri Tirumala - Branded E-commerce Product Gallery</h1>
        <p>Previewing all 33 professionally generated, adaptively cropped, and background-removed product packaging images.</p>
    </div>
"""

sections = {
    "Core Lineup Products": [
        ("Tirumala Bleaching Powder", "tirumala_bleach.png"),
        ("Tirumala Toilet Cleaner (Horpic)", "tirumala_toilet.png"),
        ("Tirumala Floor Cleaner (Ligol)", "tirumala_floor_lizol.png"),
        ("Tirumala Coli Fresh Glass Cleaner", "user_glass_cleaner.png"),
        ("Tirumala Dish Wash Liquid", "tirumala_dish.png"),
        ("Tirumala White Phenyl", "tirumala_white_phenyl.png"),
        ("Tirumala Black Phenyl", "tirumala_black_phenyl.png"),
    ],
    "Tirumala Floor Cleaner Flavors": [
        ("Jasmine Floor Cleaner (Green)", "tirumala_floor_green.png"),
        ("Rose Floor Cleaner (Pink)", "tirumala_floor_pink.png"),
        ("Lavender Floor Cleaner (Purple)", "tirumala_floor_lavender.png"),
        ("Lemon Floor Cleaner (Yellow)", "tirumala_floor_yellow.png"),
        ("Citrus Floor Cleaner (Orange)", "tirumala_floor_orange.png"),
        ("Herbal Floor Cleaner (White)", "tirumala_floor_white.png"),
    ],
    "Liger Brand Floor Cleaner (All Flavors)": [
        ("Liger Lemon Floor Cleaner (Yellow)", "liger_floor_yellow.png"),
        ("Liger Rose Floor Cleaner (Pink)", "liger_floor_pink.png"),
        ("Liger Jasmine Floor Cleaner (Green)", "liger_floor_green.png"),
        ("Liger Citrus Floor Cleaner (Orange)", "liger_floor_orange.png"),
        ("Liger Pine Floor Cleaner (White)", "liger_floor_white.png"),
    ],
    "Home Doctor Floor Cleaner (All Flavors)": [
        ("Home Doctor Citrus Cleaner (Orange)", "home_doctor_floor_orange.png"),
        ("Home Doctor Rose Cleaner (Pink)", "home_doctor_floor_pink.png"),
        ("Home Doctor Lemon Cleaner (Yellow)", "home_doctor_floor_yellow.png"),
        ("Home Doctor Pine Cleaner (White)", "home_doctor_floor_white.png"),
        ("Home Doctor Jasmine Cleaner (Green)", "home_doctor_floor_green.png"),
    ],
    "Acid & Specialized Cleaners": [
        ("Tirumala Brand Cleaning Acid", "tirumala_acid_green_bottle.png"),
        ("Tirumala Brand Acid Gell (Blue)", "tirumala_acid_blue.png"),
        ("Tirumala Brand Acid Gell (Orange)", "tirumala_acid_orange.png"),
        ("Tirumala Brand Acid Gell (Red)", "tirumala_acid_red.png"),
    ],
    "White & Black Phenyl Variants": [
        ("Herbal Phenyl (White)", "tirumala_herbal_white.png"),
        ("Herbal Phenyl (Green)", "tirumala_herbal_green.png"),
        ("Black Cleaning Liquid (Brown Bottle)", "tirumala_black_phenyl_brown_bottle.png"),
    ],
    "Pest Control & Ant Killers": [
        ("Cheetah Ant Killer (Red Box)", "cheetah_ant_killer.png"),
        ("Tirumala Brand Ant Killer (Large)", "tirumala_ant_killer_large.png"),
        ("Tirumala Brand Ant Killer (Small)", "tirumala_ant_killer_small.png"),
    ]
}

for title, items in sections.items():
    gallery_content += f'\n    <div class="section-title">{title}</div>\n    <div class="final-grid">\n'
    for name, filename in items:
        gallery_content += f"""        <div class="final-card">
            <div class="final-img-container">
                <img src="assets/{filename}" alt="{filename}">
            </div>
            <div class="final-title">{name}<br><code style="font-size:10px;font-weight:400;color:#64748b;">assets/{filename}</code></div>
        </div>\n"""
    gallery_content += '    </div>\n'

gallery_content += """
    <div style="text-align: center; margin-top: 40px; padding-bottom: 40px;">
        <a href="index.html" class="back-link">&larr; Back to Sri Tirumala Homepage</a>
    </div>
</body>
</html>
"""

workspace_dir = r"c:\Users\kavya\Desktop\Tirumala2"
gallery_path = os.path.join(workspace_dir, "gallery.html")
with open(gallery_path, "w", encoding="utf-8") as f:
    f.write(gallery_content)
print("Successfully regenerated gallery.html with Horpic and Glass Cleaner")
