---
name: workflow-create
description: "Create reusable workflow templates."
category: general-purpose
source_repo: ruvnet/ruflo
source_path: ".claude/commands/workflows/workflow-create.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/workflows/workflow-create.md
---
# workflow-create

Create reusable workflow templates.

## Usage
```bash
npx claude-flow workflow create [options]
```

## Options
- `--name <name>` - Workflow name
- `--from-history` - Create from history
- `--interactive` - Interactive creation

## Examples
```bash
# Create workflow
npx claude-flow workflow create --name "deploy-api"

# From history
npx claude-flow workflow create --name "test-suite" --from-history

# Interactive mode
npx claude-flow workflow create --interactive
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/workflows/workflow-create.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/workflows/workflow-create.md`
