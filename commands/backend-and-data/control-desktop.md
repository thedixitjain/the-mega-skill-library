---
name: control-desktop
description: "Run a computer use task on the desktop via Claude's vision and action API"
category: backend-and-data
source_repo: athola/claude-night-market
source_path: "plugins/phantom/commands/control-desktop.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/phantom/commands/control-desktop.md
---


# /control-desktop

Run a computer use task using Claude's Computer Use API.

## Usage

```
/control-desktop <task description>
```

## What it does

1. Checks that display tools are available (xdotool, scrot)
2. Verifies ANTHROPIC_API_KEY is set
3. Runs the phantom agent loop with the given task
4. Reports results including iterations and actions taken

## Example

```
/control-desktop Open the file manager and create a new folder called "reports"
```

## Prerequisites

- `ANTHROPIC_API_KEY` environment variable set
- Display tools installed: `sudo apt install xdotool scrot xclip`
- An active X11 display (native Linux, WSLg, or Xvfb)

## Implementation

```bash
cd plugins/phantom && uv run python -m phantom.cli "$ARGS"
```

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/phantom/commands/control-desktop.md`
