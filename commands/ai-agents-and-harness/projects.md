---
name: projects
description: "List known projects and their instinct statistics"
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "commands/projects.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/projects.md
---
# Projects Command

List project registry entries and per-project instinct/observation counts for continuous-learning-v2.

## Implementation

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" projects
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py projects
```

## Usage

```bash
/projects
```

## What to Do

1. Read `~/.claude/homunculus/projects.json`
2. For each project, display:
   - Project name, id, root, remote
   - Personal and inherited instinct counts
   - Observation event count
   - Last seen timestamp
3. Also display global instinct totals

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/projects.md`
