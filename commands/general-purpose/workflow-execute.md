---
name: workflow-execute
description: "Execute saved workflows."
category: general-purpose
source_repo: ruvnet/ruflo
source_path: ".claude/commands/workflows/workflow-execute.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/workflows/workflow-execute.md
---
# workflow-execute

Execute saved workflows.

## Usage
```bash
npx claude-flow workflow execute [options]
```

## Options
- `--name <name>` - Workflow name
- `--params <json>` - Workflow parameters
- `--dry-run` - Preview execution

## Examples
```bash
# Execute workflow
npx claude-flow workflow execute --name "deploy-api"

# With parameters
npx claude-flow workflow execute --name "test-suite" --params '{"env": "staging"}'

# Dry run
npx claude-flow workflow execute --name "deploy-api" --dry-run
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/workflows/workflow-execute.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/workflows/workflow-execute.md`
