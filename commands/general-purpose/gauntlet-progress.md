---
name: gauntlet-progress
description: "Show challenge accuracy stats, weak areas, and streak"
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/gauntlet/commands/gauntlet-progress.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/gauntlet/commands/gauntlet-progress.md
---


# Gauntlet Progress

Show developer challenge statistics.

## Steps

1. Get developer ID from `git config user.email`
2. Load progress from `.gauntlet/progress/<developer>.json`
3. Display: overall accuracy, current streak, accuracy by category,
   total challenges, last session date

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/gauntlet/commands/gauntlet-progress.md`
