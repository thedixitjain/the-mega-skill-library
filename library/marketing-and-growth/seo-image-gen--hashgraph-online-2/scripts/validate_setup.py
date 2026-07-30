#!/usr/bin/env python3
"""Validate that the plugin-local .mcp.json contains Banana configuration."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    mcp_path = Path(__file__).resolve().parents[3] / ".mcp.json"
    if not mcp_path.exists():
        print(f"Missing MCP config: {mcp_path}")
        return 1

    payload = json.loads(mcp_path.read_text())
    servers = payload.get("mcpServers", {})
    if "nanobanana-mcp" not in servers:
        print("nanobanana-mcp is not configured.")
        return 1

    print(f"nanobanana-mcp is configured in {mcp_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
