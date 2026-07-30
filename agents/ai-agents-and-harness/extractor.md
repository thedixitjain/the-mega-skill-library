---
name: extractor
description: "| Autonomous knowledge extraction agent. Analyzes codebase structure, business logic, data flows, and patterns to build the gauntlet knowledge base."
allowed-tools: "Read Grep Glob Bash Write"
model: "sonnet"
category: ai-agents-and-harness
source_repo: athola/claude-night-market
source_path: "plugins/gauntlet/agents/extractor.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/gauntlet/agents/extractor.md
---


# Knowledge Extractor Agent

Analyze a codebase and produce `.gauntlet/knowledge.json`.

## Workflow

1. Discover source files via Glob (skip tests, configs, generated)
2. Run AST extraction:
   ```bash
   python3 plugins/gauntlet/scripts/extractor.py <target-dir> \
     --output .gauntlet/knowledge.json
   ```
3. Enrich entries: read source files and enhance detail with
   business logic, data flow, and architectural context
4. Cross-reference: link entries that share files in related_files
5. Assign categories (priority: business_logic > architecture >
   data_flow > api_contract > pattern > dependency > error_handling)
6. Validate: non-empty detail, valid difficulty (1-4), at least
   one tag
7. Save to `.gauntlet/knowledge.json`

## Error Handling

- Skip unparseable files, log warning
- Fall back to Read + Grep if script fails
- Report partial results rather than failing entirely

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/gauntlet/agents/extractor.md`
