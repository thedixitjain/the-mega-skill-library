---
name: caveman-review
description: "Caveman-style code review — one-line findings with severity"
category: engineering-core
source_repo: JuliusBrussee/caveman
source_path: "src/plugins/opencode/commands/caveman-review.md"
source_url: https://github.com/JuliusBrussee/caveman/blob/HEAD/src/plugins/opencode/commands/caveman-review.md
---

Review the current diff (or files: $ARGUMENTS).

One line per finding. Format: `L<line>: <severity> <problem>. <fix>.`
Severity emoji: 🔴 critical · 🟡 warn · 🟢 nit. Skip non-issues.
Group by file. End with a one-line verdict.

---

**Source:** [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) → `src/plugins/opencode/commands/caveman-review.md`
