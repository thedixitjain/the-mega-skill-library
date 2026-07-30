---
name: caveman-init
description: "Drop the always-on caveman activation rule into the current repo for every IDE agent"
category: ai-agents-and-harness
source_repo: JuliusBrussee/caveman
source_path: "commands/caveman-init.md"
source_url: https://github.com/JuliusBrussee/caveman/blob/HEAD/commands/caveman-init.md
---


Write the per-repo caveman rule files (Cursor, Windsurf, Cline, Copilot, AGENTS.md) into the current repo, then report the result.

How to run the init script — pick the first that applies:

1. If `src/tools/caveman-init.js` exists in the current repo (you are inside a caveman checkout), run: `node src/tools/caveman-init.js $ARGUMENTS`
2. Otherwise download and run the standalone script (it is self-contained and supports stdin execution): `curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/src/tools/caveman-init.js | node - $ARGUMENTS`

Use `--dry-run` first if the user did not pass `--force`, so we never silently overwrite an existing rule file.

---

**Source:** [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) → `commands/caveman-init.md`
