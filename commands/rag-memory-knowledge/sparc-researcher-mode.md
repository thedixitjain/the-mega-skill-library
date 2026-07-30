---
name: sparc-researcher-mode
description: "Deep research with parallel WebSearch/WebFetch and Memory coordination."
category: rag-memory-knowledge
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/researcher.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/researcher.md
---
# SPARC Researcher Mode

## Purpose
Deep research with parallel WebSearch/WebFetch and Memory coordination.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "researcher",
  task_description: "research AI trends 2024",
  options: {
    depth: "comprehensive",
    sources: ["academic", "industry", "news"]
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run researcher "research AI trends 2024"

# For alpha features
npx claude-flow@alpha sparc run researcher "research AI trends 2024"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run researcher "research AI trends 2024"
```

## Core Capabilities
- Information gathering
- Source evaluation
- Trend analysis
- Competitive research
- Technology assessment

## Research Methods
- Parallel web searches
- Academic paper analysis
- Industry report synthesis
- Expert opinion gathering
- Data compilation

## Memory Integration
- Store research findings
- Build knowledge graphs
- Track information sources
- Cross-reference insights
- Maintain research history

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/researcher.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/researcher.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/researcher.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/researcher.md`
