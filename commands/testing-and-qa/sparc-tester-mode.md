---
name: sparc-tester-mode
description: "Comprehensive testing with parallel execution capabilities."
category: testing-and-qa
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/tester.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/tester.md
---
# SPARC Tester Mode

## Purpose
Comprehensive testing with parallel execution capabilities.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "tester",
  task_description: "full regression suite",
  options: {
    parallel: true,
    coverage: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run tester "full regression suite"

# For alpha features
npx claude-flow@alpha sparc run tester "full regression suite"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run tester "full regression suite"
```

## Core Capabilities
- Test planning
- Test execution
- Bug detection
- Coverage analysis
- Report generation

## Test Types
- Unit tests
- Integration tests
- E2E tests
- Performance tests
- Security tests

## Parallel Features
- Concurrent test runs
- Distributed testing
- Load testing
- Cross-browser testing
- Multi-environment validation

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/tester.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/tester.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/tester.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/tester.md`
