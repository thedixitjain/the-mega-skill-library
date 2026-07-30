---
name: spreadsheet-formula-helper
description: "Write and debug spreadsheet formulas (Excel/Google Sheets), pivot tables, and array formulas; translate between dialects; use when users need working formulas with examples and edge-case checks."
category: mobile-and-platform
source_repo: composio-community/awesome-codex-skills
source_path: "spreadsheet-formula-helper/SKILL.md"
source_url: https://github.com/composio-community/awesome-codex-skills/blob/HEAD/spreadsheet-formula-helper/SKILL.md
---


# Spreadsheet Formula Helper

Produce reliable spreadsheet formulas with explanations.

## Inputs to gather
- Platform (Excel/Sheets), locale (comma vs. semicolon separators), sample data layout (headers, ranges), expected outputs, and constraints (volatile functions allowed?).
- Provide small example rows and the desired result for them.

## Workflow
1) Restate the problem with explicit ranges and sheet names; propose a minimal sample to verify.
2) Draft formula(s); when dynamic arrays are available, prefer them over copy-down formulas.
3) Explain how it works and where to place it; include named ranges if helpful.
4) Edge cases: blank rows, mixed types, timezone/date quirks, duplicates; offer guardrails (e.g., `IFERROR`, `LET`, `LAMBDA`).
5) Variants: if porting between Excel and Sheets, provide both versions.

## Output
- Primary formula, short explanation, and a 2–3 row worked example showing inputs → outputs.
- Optional: quick troubleshooting checklist for common errors.

---

**Source:** [`composio-community/awesome-codex-skills`](https://github.com/composio-community/awesome-codex-skills) → `spreadsheet-formula-helper/SKILL.md`
