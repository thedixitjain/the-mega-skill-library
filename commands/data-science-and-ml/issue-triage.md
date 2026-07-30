---
name: issue-triage
description: "Intelligent issue classification and triage."
category: data-science-and-ml
source_repo: ruvnet/RuView
source_path: ".claude/commands/github/issue-triage.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/github/issue-triage.md
---
# issue-triage

Intelligent issue classification and triage.

## Usage
```bash
npx claude-flow github issue-triage [options]
```

## Options
- `--repository <owner/repo>` - Target repository
- `--auto-label` - Automatically apply labels
- `--assign` - Auto-assign to team members

## Examples
```bash
# Triage issues
npx claude-flow github issue-triage --repository myorg/myrepo

# With auto-labeling
npx claude-flow github issue-triage --repository myorg/myrepo --auto-label

# Full automation
npx claude-flow github issue-triage --repository myorg/myrepo --auto-label --assign
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/github/issue-triage.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/github/issue-triage.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/github/issue-triage.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/github/issue-triage.md`
