#!/usr/bin/env python3
"""
Qwen Video/Image Bridge — send media to Qwen Omni API and get analysis back.

Part of the qwen-video-bridge plugin for Claude Code / Cowork.

Usage:
    python qwen_bridge.py video.mp4 "Describe what happens"
    python qwen_bridge.py screenshot.png "What's in this image?"
    python qwen_bridge.py video.mp4 "Analyze" --fps 1 --json
    python qwen_bridge.py video.mp4 "Follow up" --context ctx.json

Requires:
    pip install dashscope
    export DASHSCOPE_API_KEY=sk-...
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff"}

DEFAULT_MODEL = "qwen-omni-plus-latest"
DEFAULT_FPS = 2.0

# --- Region config ---
# International (Singapore) endpoint. Chinese mainland users: change to
# https://dashscope.aliyuncs.com/api/v1
INTL_BASE_URL = "https://dashscope-intl.aliyuncs.com/api/v1"
CN_BASE_URL = "https://dashscope.aliyuncs.com/api/v1"


def get_api_key() -> str:
    """Get API key from environment."""
    key = os.environ.get("DASHSCOPE_API_KEY", "").strip()
    if not key:
        print(
            "Error: DASHSCOPE_API_KEY not set.\n"
            "Get your key at https://modelstudio.console.alibabacloud.com/\n"
            "Then: export DASHSCOPE_API_KEY=sk-...",
            file=sys.stderr,
        )
        sys.exit(1)
    return key


def detect_media_type(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    if ext in VIDEO_EXTS:
        return "video"
    if ext in IMAGE_EXTS:
        return "image"
    raise ValueError(f"Unsupported file type: {ext}. Supported: {VIDEO_EXTS | IMAGE_EXTS}")


def build_file_uri(filepath: str) -> str:
    p = Path(filepath).resolve()
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    if sys.platform == "win32":
        return f"file:///{str(p).replace(os.sep, '/')}"
    return f"file://{p}"


def analyze(
    filepath: str,
    prompt: str,
    model: str = DEFAULT_MODEL,
    fps: float = DEFAULT_FPS,
    context: Optional[list] = None,
    system_prompt: Optional[str] = None,
    region: str = "intl",
) -> dict:
    """Send media to Qwen API and return analysis."""
    try:
        import dashscope
        from dashscope import MultiModalConversation
    except ImportError:
        print(
            "Error: dashscope package not installed.\n"
            "Run: pip install dashscope",
            file=sys.stderr,
        )
        sys.exit(1)

    # Set endpoint based on region
    dashscope.base_http_api_url = CN_BASE_URL if region == "cn" else INTL_BASE_URL

    api_key = get_api_key()
    media_type = detect_media_type(filepath)
    file_uri = build_file_uri(filepath)

    # Build content block
    content = []
    if media_type == "video":
        content.append({"video": file_uri, "fps": fps})
    else:
        content.append({"image": file_uri})
    content.append({"text": prompt})

    # Build messages
    if context:
        messages = context.copy()
        messages.append({"role": "user", "content": content})
    else:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": [{"text": system_prompt}]})
        messages.append({"role": "user", "content": content})

    # Call API
    response = MultiModalConversation.call(
        api_key=api_key,
        model=model,
        messages=messages,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Qwen API error {response.status_code}: {response.code} — {response.message}"
        )

    # Extract response text
    assistant_msg = response.output.choices[0].message
    if isinstance(assistant_msg.content, list):
        result_text = "".join(item.get("text", "") for item in assistant_msg.content)
    elif isinstance(assistant_msg.content, str):
        result_text = assistant_msg.content
    else:
        result_text = str(assistant_msg.content)

    # Update messages for multi-turn
    messages.append({"role": "assistant", "content": [{"text": result_text}]})

    # Usage info
    usage = {}
    if hasattr(response, "usage") and response.usage:
        usage = {
            "input_tokens": getattr(response.usage, "input_tokens", 0),
            "output_tokens": getattr(response.usage, "output_tokens", 0),
        }

    return {"response": result_text, "messages": messages, "usage": usage}


def main():
    parser = argparse.ArgumentParser(
        description="Qwen Video/Image Bridge — analyze media via Qwen Omni API"
    )
    parser.add_argument("file", help="Path to video or image file")
    parser.add_argument("prompt", nargs="?", default=None, help="Analysis prompt")
    parser.add_argument("--prompt-file", help="Read prompt from file")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fps", type=float, default=DEFAULT_FPS, help=f"Video FPS (default: {DEFAULT_FPS})")
    parser.add_argument("--context", help="Path to JSON context file (multi-turn)")
    parser.add_argument("--save-context", help="Save context to file for follow-up")
    parser.add_argument("--system-prompt", help="System prompt for Qwen")
    parser.add_argument("--region", choices=["intl", "cn"], default="intl", help="API region (default: intl)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Determine prompt
    prompt = args.prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    if not prompt:
        prompt = "Describe what happens in this video/image in detail."

    # Load context
    context = None
    if args.context:
        with open(args.context, "r", encoding="utf-8") as f:
            context = json.load(f)

    # Call API
    result = analyze(
        filepath=args.file,
        prompt=prompt,
        model=args.model,
        fps=args.fps,
        context=context,
        system_prompt=args.system_prompt,
        region=args.region,
    )

    # Save context
    if args.save_context:
        with open(args.save_context, "w", encoding="utf-8") as f:
            json.dump(result["messages"], f, ensure_ascii=False, indent=2)

    # Output
    if args.json:
        output = {"response": result["response"], "usage": result["usage"]}
        if args.save_context:
            output["context_saved"] = args.save_context
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(result["response"])
        if result["usage"]:
            u = result["usage"]
            print(f"\n--- tokens: {u.get('input_tokens', '?')} in / {u.get('output_tokens', '?')} out ---")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)
