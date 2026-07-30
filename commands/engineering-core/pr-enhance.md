---
name: pr-enhance
description: "AI-powered pull request enhancements."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/github/pr-enhance.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/github/pr-enhance.md
---
# pr-enhance

AI-powered pull request enhancements.

## Usage
```bash
npx claude-flow github pr-enhance [options]
```

## Options
- `--pr-number <n>` - Pull request number
- `--add-tests` - Add missing tests
- `--improve-docs` - Improve documentation
- `--check-security` - Security review

## Examples
```bash
# Enhance PR
npx claude-flow github pr-enhance --pr-number 123

# Add tests
npx claude-flow github pr-enhance --pr-number 123 --add-tests

# Full enhancement
npx claude-flow github pr-enhance --pr-number 123 --add-tests --improve-docs
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/github/pr-enhance.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/github/pr-enhance.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/github/pr-enhance.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/github/pr-enhance.md`
