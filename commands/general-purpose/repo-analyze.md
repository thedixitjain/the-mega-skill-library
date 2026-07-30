---
name: repo-analyze
description: "Deep analysis of GitHub repository with AI insights."
category: general-purpose
source_repo: ruvnet/RuView
source_path: ".claude/commands/github/repo-analyze.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/github/repo-analyze.md
---
# repo-analyze

Deep analysis of GitHub repository with AI insights.

## Usage
```bash
npx claude-flow github repo-analyze [options]
```

## Options
- `--repository <owner/repo>` - Repository to analyze
- `--deep` - Enable deep analysis
- `--include <areas>` - Include specific areas (issues, prs, code, commits)

## Examples
```bash
# Basic analysis
npx claude-flow github repo-analyze --repository myorg/myrepo

# Deep analysis
npx claude-flow github repo-analyze --repository myorg/myrepo --deep

# Specific areas
npx claude-flow github repo-analyze --repository myorg/myrepo --include issues,prs
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/github/repo-analyze.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/github/repo-analyze.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/github/repo-analyze.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/github/repo-analyze.md`
