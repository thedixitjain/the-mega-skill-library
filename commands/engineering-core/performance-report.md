---
name: performance-report
description: "Generate comprehensive performance reports for swarm operations."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/analysis/performance-report.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/analysis/performance-report.md
---
# performance-report

Generate comprehensive performance reports for swarm operations.

## Usage
```bash
npx claude-flow analysis performance-report [options]
```

## Options
- `--format <type>` - Report format (json, html, markdown)
- `--include-metrics` - Include detailed metrics
- `--compare <id>` - Compare with previous swarm

## Examples
```bash
# Generate HTML report
npx claude-flow analysis performance-report --format html

# Compare swarms
npx claude-flow analysis performance-report --compare swarm-123

# Full metrics report
npx claude-flow analysis performance-report --include-metrics --format markdown
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/analysis/performance-report.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/analysis/performance-report.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/analysis/performance-report.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/analysis/performance-report.md`
