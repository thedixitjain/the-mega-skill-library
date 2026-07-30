---
name: workflow-export
description: "Export workflows for sharing."
category: general-purpose
source_repo: ruvnet/ruflo
source_path: ".claude/commands/workflows/workflow-export.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/workflows/workflow-export.md
---
# workflow-export

Export workflows for sharing.

## Usage
```bash
npx claude-flow workflow export [options]
```

## Options
- `--name <name>` - Workflow to export
- `--format <type>` - Export format
- `--include-history` - Include execution history

## Examples
```bash
# Export workflow
npx claude-flow workflow export --name "deploy-api"

# As YAML
npx claude-flow workflow export --name "test-suite" --format yaml

# With history
npx claude-flow workflow export --name "deploy-api" --include-history
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/workflows/workflow-export.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/workflows/workflow-export.md`
