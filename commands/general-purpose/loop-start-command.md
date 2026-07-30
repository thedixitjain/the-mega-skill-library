---
name: loop-start-command
description: "Start a managed autonomous loop pattern with safety defaults and explicit stop conditions."
category: general-purpose
source_repo: affaan-m/ECC
source_path: "commands/loop-start.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/loop-start.md
---
# Loop Start Command

Start a managed autonomous loop pattern with safety defaults.

## Usage

`/loop-start [pattern] [--mode safe|fast]`

- `pattern`: `sequential`, `continuous-pr`, `rfc-dag`, `infinite`
- `--mode`:
  - `safe` (default): strict quality gates and checkpoints
  - `fast`: reduced gates for speed

## Flow

1. Confirm repository state and branch strategy.
2. Select loop pattern and model tier strategy.
3. Enable required hooks/profile for the chosen mode.
4. Create loop plan and write runbook under `.claude/plans/`.
5. Print commands to start and monitor the loop.

## Required Safety Checks

- Verify tests pass before first loop iteration.
- Ensure `ECC_HOOK_PROFILE` is not disabled globally.
- Ensure loop has explicit stop condition.

## Arguments

$ARGUMENTS:
- `<pattern>` optional (`sequential|continuous-pr|rfc-dag|infinite`)
- `--mode safe|fast` optional

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/loop-start.md`

**Also appears in:** `affaan-m/ECC/.opencode/commands/loop-start.md`
