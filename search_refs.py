import os

brain_dir = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53"
search_term = "unique_"

print(f"Searching for '{search_term}' in {brain_dir}...")
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f.endswith(('.txt', '.py', '.md', '.json', '.jsonl')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    for line_no, line in enumerate(file, 1):
                        if search_term in line:
                            # print filename and line, truncate line if too long
                            print(f"{f}:{line_no} -> {line.strip()[:120]}")
            except Exception as e:
                pass
