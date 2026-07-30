# Batch video analysis pattern

When the user has multiple videos to classify or analyze, write a Python script like this and run it via Bash.

## Template

```python
#!/usr/bin/env python3
"""Batch analyze videos using the Qwen bridge."""

import subprocess
import json
import sys
from pathlib import Path

BRIDGE = "${CLAUDE_PLUGIN_ROOT}/skills/qwen-vision/scripts/qwen_bridge.py"
# Replace with actual values:
VIDEO_DIR = "/path/to/videos"
OUTPUT = "/path/to/results.json"

PROMPT = """Your analysis prompt here. Ask for JSON output for easy parsing.

Respond in this exact JSON format:
{
  "description": "...",
  "category": "...",
  "quality": 1-5,
  "notes": "..."
}

Return ONLY the JSON, no other text.
"""

def analyze_video(video_path: str) -> dict:
    cmd = [
        sys.executable, BRIDGE,
        video_path, PROMPT,
        "--fps", "2",
        "--json"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        output = result.stdout.strip()
        wrapper = json.loads(output)
        inner = wrapper.get("response", output)

        # Strip markdown fences if present
        text = inner.strip()
        if text.startswith("```"):
            lines = [l for l in text.split("\n") if not l.strip().startswith("```")]
            text = "\n".join(lines)

        return {"status": "ok", "data": json.loads(text)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}
    except (json.JSONDecodeError, Exception) as e:
        return {"status": "error", "message": str(e)}

def main():
    videos = sorted(Path(VIDEO_DIR).glob("*.mp4"))
    print(f"Found {len(videos)} videos")

    results = {}
    for i, video in enumerate(videos, 1):
        print(f"[{i}/{len(videos)}] {video.name} ...", end=" ", flush=True)
        r = analyze_video(str(video))
        results[video.name] = r
        status = r["data"].get("category", "?") if r["status"] == "ok" else r["status"]
        print(f"=> {status}")

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {OUTPUT}")

if __name__ == "__main__":
    main()
```

## Notes

- Adjust PROMPT to match whatever classification scheme the user needs.
- For large batches (50+ videos), consider adding a `time.sleep(1)` between calls to avoid rate limiting.
- The `--json` flag makes the bridge output `{"response": "...", "usage": {...}}` which is easier to parse.
- Always handle parse errors gracefully — VLMs sometimes return malformed JSON.
