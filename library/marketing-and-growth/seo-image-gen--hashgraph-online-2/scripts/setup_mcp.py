#!/usr/bin/env python3
"""Configure the Banana MCP entry in the plugin-local .mcp.json."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def config_script() -> Path:
    return Path(__file__).resolve().parents[3] / "scripts" / "configure_mcp.py"


def main() -> int:
    args = sys.argv[1:]
    if "--help" in args or "-h" in args:
        print("Usage: python3 setup_mcp.py --key YOUR_KEY")
        print("       python3 setup_mcp.py --remove")
        print("       python3 setup_mcp.py --check")
        return 0

    if "--check" in args:
        mcp_file = Path(__file__).resolve().parents[3] / ".mcp.json"
        print(f"Inspect {mcp_file} for the 'nanobanana-mcp' entry.")
        return 0

    if "--remove" in args:
        return subprocess.run(
            [sys.executable, str(config_script()), "remove", "banana"],
            check=False,
        ).returncode

    if "--key" in args:
        index = args.index("--key")
        try:
            api_key = args[index + 1]
        except IndexError:
            print("Missing value after --key", file=sys.stderr)
            return 1
    else:
        api_key = input("Google AI API key: ").strip()

    if not api_key:
        print("API key cannot be empty.", file=sys.stderr)
        return 1

    return subprocess.run(
        [sys.executable, str(config_script()), "upsert", "banana", api_key],
        check=False,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
