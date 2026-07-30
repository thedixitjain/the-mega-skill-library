---
name: caveman-help
description: "Quick reference card for caveman modes, slash commands, and triggers"
category: general-purpose
source_repo: JuliusBrussee/caveman
source_path: "src/plugins/opencode/commands/caveman-help.md"
source_url: https://github.com/JuliusBrussee/caveman/blob/HEAD/src/plugins/opencode/commands/caveman-help.md
---

Show the caveman quick-reference card.

| Command | What |
|---|---|
| `/caveman` | Activate at default level (full) |
| `/caveman lite` | Light compression — ~30% tokens dropped |
| `/caveman ultra` | Maximum compression |
| `/caveman wenyan[-lite\|-ultra]` | Classical Chinese compression |
| `/caveman off` | Deactivate |
| `/caveman-commit` | Terse commit message |
| `/caveman-review` | One-line review findings |
| `/caveman-compress <file>` | Compress a Markdown file |
| `/caveman-stats` | Lifetime token-savings |

Natural language also works: "turn on caveman", "stop caveman", "normal mode".

Code, commits, security warnings: caveman drops out automatically.

---

**Source:** [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) → `src/plugins/opencode/commands/caveman-help.md`
