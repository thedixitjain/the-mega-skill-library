---
name: code-review
description: "Automated code review with swarm intelligence."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/github/code-review.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/github/code-review.md
---
# code-review

Automated code review with swarm intelligence.

## Usage
```bash
npx claude-flow github code-review [options]
```

## Options
- `--pr-number <n>` - Pull request to review
- `--focus <areas>` - Review focus (security, performance, style)
- `--suggest-fixes` - Suggest code fixes

## Examples
```bash
# Review PR
npx claude-flow github code-review --pr-number 456

# Security focus
npx claude-flow github code-review --pr-number 456 --focus security

# With fix suggestions
npx claude-flow github code-review --pr-number 456 --suggest-fixes
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/github/code-review.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/github/code-review.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/github/code-review.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/github/code-review.md`
