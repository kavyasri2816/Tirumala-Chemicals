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
                tcs = data.get('tool_calls', [])
                if tcs:
                    for tc in tcs:
                        if tc.get('name') == 'generate_image':
                            args = tc.get('args', {})
                            # Check if args is a dict or a string representing a dict
                            if isinstance(args, str):
                                args = json.loads(args)
                            print(f"Step: {data.get('step_index')}")
                            print(f"  ImageName: {args.get('ImageName')}")
                            print(f"  ImagePaths: {args.get('ImagePaths')}")
                            print(f"  Prompt: {args.get('Prompt')}")
                            print("=" * 60)
            except Exception as e:
                pass
