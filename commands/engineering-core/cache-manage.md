---
name: cache-manage
description: "Manage operation cache for performance."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/optimization/cache-manage.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/optimization/cache-manage.md
---
# cache-manage

Manage operation cache for performance.

## Usage
```bash
npx claude-flow optimization cache-manage [options]
```

## Options
- `--action <type>` - Action (view, clear, optimize)
- `--max-size <mb>` - Maximum cache size
- `--ttl <seconds>` - Time to live

## Examples
```bash
# View cache stats
npx claude-flow optimization cache-manage --action view

# Clear cache
npx claude-flow optimization cache-manage --action clear

# Set limits
npx claude-flow optimization cache-manage --max-size 100 --ttl 3600
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/optimization/cache-manage.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/optimization/cache-manage.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/optimization/cache-manage.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/optimization/cache-manage.md`
