---
name: parallel-execute
description: "Execute tasks in parallel for maximum efficiency."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/optimization/parallel-execute.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/optimization/parallel-execute.md
---
# parallel-execute

Execute tasks in parallel for maximum efficiency.

## Usage
```bash
npx claude-flow optimization parallel-execute [options]
```

## Options
- `--tasks <file>` - Task list file
- `--max-parallel <n>` - Maximum parallel tasks
- `--strategy <type>` - Execution strategy

## Examples
```bash
# Execute task list
npx claude-flow optimization parallel-execute --tasks tasks.json

# Limit parallelism
npx claude-flow optimization parallel-execute --tasks tasks.json --max-parallel 5

# Custom strategy
npx claude-flow optimization parallel-execute --strategy adaptive
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/optimization/parallel-execute.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/optimization/parallel-execute.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/optimization/parallel-execute.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/optimization/parallel-execute.md`
