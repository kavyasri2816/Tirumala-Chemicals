import json
import os

log_path = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53\.system_generated\logs\transcript.jsonl"

if not os.path.exists(log_path):
    print("Logs not found at", log_path)
else:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('step_index') == 139:
                    print("Step 139 content:")
                    print(data.get('content'))
                    print("=" * 60)
            except Exception as e:
                pass
