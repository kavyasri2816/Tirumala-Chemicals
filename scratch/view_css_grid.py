import os

css_path = r"c:\Users\kavya\Desktop\Tirumala2\style.css"

if not os.path.exists(css_path):
    print("style.css not found")
else:
    with open(css_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        if ".products-grid" in line:
            # print surrounding 15 lines
            start = max(0, idx - 2)
            end = min(len(lines), idx + 15)
            print(f"Lines {start+1}-{end}:")
            for i in range(start, end):
                print(f"{i+1}: {lines[i]}", end="")
            print("\n" + "="*40 + "\n")
