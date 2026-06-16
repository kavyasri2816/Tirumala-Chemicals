import os

def create_all_gallery():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    workspace_dir = r"c:\Users\kavya\Desktop\Tirumala2"
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Unique Images Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            padding: 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
            padding: 10px;
        }
        .img-container {
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #eaeaea;
        }
        .img-container img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
        .title {
            margin-top: 10px;
            font-weight: bold;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>All Unique Images</h1>
    <div class="grid">
"""
    for i in range(30):
        filename = f"unique_{i}.jpg"
        path = os.path.join(assets_dir, filename)
        if os.path.exists(path):
            html += f"""
            <div class="card">
                <div class="img-container">
                    <img src="assets/{filename}" alt="{filename}">
                </div>
                <div class="title">{filename}</div>
            </div>"""
            
    html += """
    </div>
</body>
</html>"""
    
    with open(os.path.join(workspace_dir, "all_gallery.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Created all_gallery.html")

if __name__ == '__main__':
    create_all_gallery()
