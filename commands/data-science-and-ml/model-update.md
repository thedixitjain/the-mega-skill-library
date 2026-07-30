---
name: model-update
description: "Update neural models with new data."
category: data-science-and-ml
source_repo: ruvnet/ruflo
source_path: ".claude/commands/training/model-update.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/training/model-update.md
---
# model-update

Update neural models with new data.

## Usage
```bash
npx claude-flow training model-update [options]
```

## Options
- `--model <name>` - Model to update
- `--incremental` - Incremental update
- `--validate` - Validate after update

## Examples
```bash
# Update all models
npx claude-flow training model-update

# Specific model
npx claude-flow training model-update --model agent-selector

# Incremental with validation
npx claude-flow training model-update --incremental --validate
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/training/model-update.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/training/model-update.md`
