---
name: slopmopsm-scour
description: "Run slop-mop's comprehensive pre-PR sweep for this repository"
allowed-tools: "Bash(sm:*)"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/slopmop/commands/sm-scour.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/slopmop/commands/sm-scour.md
---


# /slopmop:sm-scour

Run slop-mop's comprehensive pre-PR sweep for this repository.

1. Run `sm scour`.
2. Summarize every issue found — these are the things that would compound if left unchecked.
3. Propose concrete fixes for each.

Only open or update a PR when `sm scour` reports a clean run.

**Prerequisite:** `sm` must be installed. If `command not found`, suggest:
```bash
pipx install slopmop[all]
```

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/slopmop/commands/sm-scour.md`
