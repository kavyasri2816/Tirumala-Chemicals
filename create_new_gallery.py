import os

def create_new_gallery():
    workspace_dir = r"c:\Users\kavya\Desktop\Tirumala2"
    
    html = """<!DOCTYPE html>
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
        .final-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .final-card {
            background-color: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
            text-align: center;
            transition: transform 0.2s;
        }
        .final-card:hover {
            transform: translateY(-5px);
        }
        .final-img-container {
            height: 240px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #ffffff;
            padding: 20px;
        }
        .final-img-container img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
        .final-title {
            padding: 15px;
            font-size: 14px;
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
        <p>Previewing the 7 professionally generated product packaging images with consistent branding and clean white background</p>
    </div>
    
    <div class="final-grid">
"""
    
    descriptives = [
        ("tirumala_bleach.png", "Tirumala Bleaching Powder"),
        ("tirumala_toilet.png", "Tirumala Horipic Toilet Cleaner"),
        ("tirumala_floor_lizol.png", "Tirumala Ligol Floor Cleaner"),
        ("tirumala_hand.png", "Tirumala Hand Wash"),
        ("tirumala_dish.png", "Tirumala Dish Wash Liquid"),
        ("tirumala_white_phenyl.png", "Tirumala White Phenyl"),
        ("tirumala_black_phenyl.png", "Tirumala Black Phenyl")
    ]
    
    for f, label in descriptives:
        html += f"""
        <div class="final-card">
            <div class="final-img-container">
                <img src="assets/{f}" alt="{f}">
            </div>
            <div class="final-title">{label}<br><code style="font-size:11px;font-weight:400;color:#64748b;">assets/{f}</code></div>
        </div>"""
        
    html += """
    </div>
    <div style="text-align: center; margin-top: 40px;">
        <a href="index.html" class="back-link">&larr; Back to Sri Tirumala Homepage</a>
    </div>
</body>
</html>"""

    dest_path = os.path.join(workspace_dir, "gallery.html")
    with open(dest_path, "w", encoding="utf-8") as out:
        out.write(html)
    print(f"Branded Gallery HTML written successfully to {dest_path}")

if __name__ == '__main__':
    create_new_gallery()
