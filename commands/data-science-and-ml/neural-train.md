---
name: neural-train
description: "Train neural patterns from operations."
category: data-science-and-ml
source_repo: ruvnet/ruflo
source_path: ".claude/commands/training/neural-train.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/training/neural-train.md
---
# neural-train

Train neural patterns from operations.

## Usage
```bash
npx claude-flow training neural-train [options]
```

## Options
- `--data <source>` - Training data source
- `--model <name>` - Target model
- `--epochs <n>` - Training epochs

## Examples
```bash
# Train from recent ops
npx claude-flow training neural-train --data recent

# Specific model
npx claude-flow training neural-train --model task-predictor

# Custom epochs
npx claude-flow training neural-train --epochs 100
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/training/neural-train.md`
