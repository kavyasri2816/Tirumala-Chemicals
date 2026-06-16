import json
import os

log_path = r"C:\Users\kavya\.gemini\antigravity\brain\eff97faa-fa30-478c-8868-69ae1b419f53\.system_generated\logs\transcript.jsonl"

if os.path.exists(log_path):
    print("Log file exists. Searching lines 300-380...")
    with open(log_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if 300 <= idx <= 380:
                try:
                    data = json.loads(line)
                    content = data.get('content', '')
                    tool_calls_str = str(data.get('tool_calls', ''))
                    print(f"--- Line {idx} | Type: {data.get('type')} | Source: {data.get('source')} ---")
                    if content:
                        print(f"Content: {content[:500]}")
                    if 'tool_calls' in data:
                        print(f"Tool calls: {tool_calls_str[:500]}")
                except Exception as e:
                    pass
else:
    print("Log file not found.")


