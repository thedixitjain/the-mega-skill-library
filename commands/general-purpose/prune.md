---
name: prune
description: "Delete pending instincts older than 30 days that were never promoted"
category: general-purpose
source_repo: affaan-m/ECC
source_path: "commands/prune.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/prune.md
---
# Prune Pending Instincts

Remove expired pending instincts that were auto-generated but never reviewed or promoted.

## Implementation

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" prune
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py prune
```

## Usage

```
/prune                    # Delete instincts older than 30 days
/prune --max-age 60      # Custom age threshold (days)
/prune --dry-run         # Preview without deleting
```

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/prune.md`
