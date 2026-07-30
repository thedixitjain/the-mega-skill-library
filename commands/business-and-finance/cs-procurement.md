---
name: cs-procurement
description: "Spend categorization + supplier rationalization + purchasing-cycle analysis. NOT vendor performance scoring (sibling vendor-management). NOT. Slash command for Claude Code, Codex CLI, Gemini CLI."
category: business-and-finance
source_repo: alirezarezvani/claude-skills
source_path: "docs/commands/cs-procurement.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/docs/commands/cs-procurement.md
---


# /cs-procurement

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/2-claude-skills/tree/main/business-operations/commands/cs-procurement.md">Source</a></span>
</div>


Run the `procurement-optimizer` skill on this input:

**$ARGUMENTS**

## Three-tool workflow

1. **`spend_categorizer.py`** — UNSPSC-aligned category mapping + Pareto analysis (which 20% of categories drive 80% of spend). Industry tuning `--profile {tech-startup,scaleup,enterprise,services,manufacturing}`.

2. **`purchasing_cycle_analyzer.py`** — Time-to-PO, time-to-payment, approval-hop count by category. Flags categories with cycle time > 2× median.

3. **`supplier_consolidation.py`** — Identifies duplicate-function suppliers (e.g., 3 monitoring tools, 2 expense platforms) + risk-balanced consolidation plan (don't consolidate to single-source for tier-1 risk).

## Distinct from

- `business-operations/skills/vendor-management` (sibling) — performance scoring of vendors you keep paying. Procurement-optimizer is **spend** rationalization + supplier consolidation.
- `finance/financial-analysis` — financial close + reporting. Procurement-optimizer is decision support, not reporting.

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `docs/commands/cs-procurement.md`
