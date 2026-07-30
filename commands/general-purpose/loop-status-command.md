---
name: loop-status-command
description: "Inspect active loop state, progress, and failure signals."
category: general-purpose
source_repo: affaan-m/ECC
source_path: ".opencode/commands/loop-status.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.opencode/commands/loop-status.md
---
# Loop Status Command

Inspect active loop state, progress, and failure signals.

## Usage

`/loop-status [--watch]`

## What to Report

- active loop pattern
- current phase and last successful checkpoint
- failing checks (if any)
- estimated time/cost drift
- recommended intervention (continue/pause/stop)

## Watch Mode

When `--watch` is present, refresh status periodically and surface state changes.

## Arguments

$ARGUMENTS:
- `--watch` optional

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.opencode/commands/loop-status.md`
