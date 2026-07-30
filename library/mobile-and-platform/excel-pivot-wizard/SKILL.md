---
name: excel-pivot-wizard
description: "'Create advanced Excel pivot tables with calculated fields and slicers. Use when building data summaries or creating interactive dashboards. Trigger with phrases like ''excel pivot'', ''create pivot table'', ''data summary''. '"
allowed-tools: "Read, Write, Edit, Grep, Glob, Bash(cmd:*)"
category: mobile-and-platform
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/excel-pivot-wizard/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/excel-pivot-wizard/SKILL.md
---

# Excel Pivot Wizard

## Overview

Creates advanced pivot tables with calculated fields, slicers, and dynamic dashboards for data analysis and reporting.

## Prerequisites

- Excel or compatible spreadsheet software
- Tabular data with headers
- Clear understanding of analysis dimensions and measures

## Instructions

1. Verify source data is in tabular format with headers
2. Create pivot table from data range
3. Configure rows, columns, values, and filters
4. Add calculated fields for custom metrics
5. Insert slicers for interactive filtering
6. Format and style for presentation

## Output

- Configured pivot table with appropriate aggregations
- Calculated fields for derived metrics
- Interactive slicers for filtering
- Dashboard-ready formatting

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Field not found | Changed source data | Refresh data connection |
| Calculated field error | Invalid formula | Check field names match exactly |
| Slicer not updating | Disconnected report | Reconnect slicer to pivot |

## Examples

**Example: Sales Dashboard**
Request: "Create a pivot summarizing sales by region and product"
Result: Pivot with region rows, product columns, revenue values, and date slicer

**Example: Financial Analysis**
Request: "Build a pivot showing monthly trends by cost center"
Result: Time-series pivot with calculated YoY growth fields

## Resources

- [Microsoft Pivot Table Guide](https://support.microsoft.com/)
- `${CLAUDE_SKILL_DIR}/references/pivot-formulas.md` for calculated field syntax

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/excel-pivot-wizard/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/business-tools/excel-analyst-pro/skills/excel-pivot-wizard/SKILL.md`
