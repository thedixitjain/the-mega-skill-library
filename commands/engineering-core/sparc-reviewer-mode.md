---
name: sparc-reviewer-mode
description: "Code review using batch file analysis for comprehensive reviews."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/reviewer.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/reviewer.md
---
# SPARC Reviewer Mode

## Purpose
Code review using batch file analysis for comprehensive reviews.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "reviewer",
  task_description: "review pull request #123",
  options: {
    security_check: true,
    performance_check: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run reviewer "review pull request #123"

# For alpha features
npx claude-flow@alpha sparc run reviewer "review pull request #123"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run reviewer "review pull request #123"
```

## Core Capabilities
- Code quality assessment
- Security review
- Performance analysis
- Best practices check
- Documentation review

## Review Criteria
- Code correctness
- Design patterns
- Error handling
- Test coverage
- Maintainability

## Batch Analysis
- Parallel file review
- Pattern detection
- Dependency checking
- Consistency validation
- Automated reporting

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/reviewer.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/reviewer.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/reviewer.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/reviewer.md`
