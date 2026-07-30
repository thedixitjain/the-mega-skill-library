---
name: install-watchdog
description: ">- Install the egregore watchdog daemon for automatic session relaunching"
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/egregore/commands/install-watchdog.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/egregore/commands/install-watchdog.md
---


# install-watchdog

Install a system-level daemon that monitors the egregore
and relaunches it after crashes, rate limits, or context
overflows.

## What It Does

On macOS, installs a launchd agent
(`com.egregore.watchdog`) that runs the watchdog script
at a fixed interval. On Linux, installs a systemd user
timer (`egregore-watchdog.timer`) instead.

The watchdog checks:

1. Whether active work items remain in the manifest.
2. Whether a cooldown period is still active.
3. Whether a session is already running (via pidfile).

If work remains and no session is running, the watchdog
relaunches the egregore.

## Prerequisites

- `jq` must be installed (used to parse manifest and
  budget files).
- The `claude` CLI must be on your PATH.

## Options

| Option       | Default | Description                   |
|--------------|---------|-------------------------------|
| `--window`   | `5h`    | Time window for the session   |
| `--interval` | `300`   | Check interval in seconds     |

## See Also

- `/egregore:uninstall-watchdog` to remove the daemon.
- `/egregore:summon` to start processing.

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/egregore/commands/install-watchdog.md`
