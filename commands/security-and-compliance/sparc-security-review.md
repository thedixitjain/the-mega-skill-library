---
name: sparc-security-review
description: "🛡️ Security Reviewer - You perform static and dynamic audits to ensure secure code practices. You flag secrets, poor mod..."
category: security-and-compliance
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/security-review.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/security-review.md
---


# 🛡️ Security Reviewer

## Role Definition
You perform static and dynamic audits to ensure secure code practices. You flag secrets, poor modular boundaries, and oversized files.

## Custom Instructions
Scan for exposed secrets, env leaks, and monoliths. Recommend mitigations or refactors to reduce risk. Flag files > 500 lines or direct environment coupling. Use `new_task` to assign sub-audits. Finalize findings with `attempt_completion`.

## Available Tools
- **read**: File reading and viewing
- **edit**: File modification and creation

## Usage

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "security-review",
  task_description: "audit API security",
  options: {
    namespace: "security-review",
    non_interactive: false
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run security-review "audit API security"

# For alpha features
npx claude-flow@alpha sparc run security-review "audit API security"

# With namespace
npx claude-flow sparc run security-review "your task" --namespace security-review

# Non-interactive mode
npx claude-flow sparc run security-review "your task" --non-interactive
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run security-review "audit API security"
```

## Memory Integration

### Using MCP Tools (Preferred)
```javascript
// Store mode-specific context
mcp__claude-flow__memory_usage {
  action: "store",
  key: "security-review_context",
  value: "important decisions",
  namespace: "security-review"
}

// Query previous work
mcp__claude-flow__memory_search {
  pattern: "security-review",
  namespace: "security-review",
  limit: 5
}
```

### Using NPX CLI (Fallback)
```bash
# Store mode-specific context
npx claude-flow memory store "security-review_context" "important decisions" --namespace security-review

# Query previous work
npx claude-flow memory query "security-review" --limit 5
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/security-review.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/security-review.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/security-review.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/security-review.md`
