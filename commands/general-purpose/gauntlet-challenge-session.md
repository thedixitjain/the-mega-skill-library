---
name: gauntlet-challenge-session
description: "Run an ad-hoc gauntlet challenge session (5 questions, random scope)"
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/gauntlet/commands/gauntlet.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/gauntlet/commands/gauntlet.md
---


# Gauntlet Challenge Session

Invoke `Skill(gauntlet:challenge)` to run a 5-question session.

Arguments:

- No args: random scope, 5 questions
- `--count N`: run N questions
- `--scope <file-or-dir>`: limit to specific files
- `--type <type>`: force a specific challenge type

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/gauntlet/commands/gauntlet.md`
