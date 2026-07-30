---
name: pattern-learn
description: "Learn patterns from successful operations."
category: data-science-and-ml
source_repo: ruvnet/ruflo
source_path: ".claude/commands/training/pattern-learn.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/training/pattern-learn.md
---
# pattern-learn

Learn patterns from successful operations.

## Usage
```bash
npx claude-flow training pattern-learn [options]
```

## Options
- `--source <type>` - Pattern source
- `--threshold <score>` - Success threshold
- `--save <name>` - Save pattern set

## Examples
```bash
# Learn from all ops
npx claude-flow training pattern-learn

# High success only
npx claude-flow training pattern-learn --threshold 0.9

# Save patterns
npx claude-flow training pattern-learn --save optimal-patterns
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/training/pattern-learn.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/training/pattern-learn.md`
