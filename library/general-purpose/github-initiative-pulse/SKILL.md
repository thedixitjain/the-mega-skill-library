---
name: github-initiative-pulse
description: "Generates markdown digests and CSV exports for GitHub initiative health. Use when reporting on issue/PR progress across a milestone or project."
allowed-tools: "[]"
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/minister/skills/github-initiative-pulse/SKILL.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/minister/skills/github-initiative-pulse/SKILL.md
---

# GitHub Initiative Pulse

## When NOT To Use

- Delivery-performance metrics (use `minister:dora-metrics`)
- Approving a release (use `minister:release-health-gates`)

## Overview

Turns tracker data and GitHub board metadata into initiative-level summaries. Provides markdown helpers and CSV exports for pasting into issues, PRs, or Discussions.

## Ritual

1. Capture work via `tracker.py add` or sync from GitHub Projects.
2. Review blockers/highlights using the **Blocker Radar** table.
3. Generate GitHub comment via `tracker.py status --github-comment` or module snippets.
4. Cross-link the weekly Status Template and share with stakeholders.

## Key Metrics

| Metric | Description |
|--------|-------------|
| Completion % | Done tasks / total tasks per initiative. |
| Avg Task % | Mean completion percent for all in-flight tasks. |
| Burn Rate | Hours burned per week (auto-calculated). |
| Risk Hotlist | Tasks flagged `priority=High` or due date in past. |

## GitHub Integrations

- Links every task to an issue/PR URL.
- Supports auto-labeling by referencing `phase` in the tracker record.
- Encourages posting digests to coordination issues or PR timelines.

## Exit Criteria

- All initiatives represented with updated metrics.
- Markdown digest pasted into relevant GitHub thread.
- Risk follow-ups filed as issues with owners and due dates.
## Troubleshooting

### Common Issues

If metrics appear outdated, ensure `tracker.py` has successfully synced with GitHub. If the Markdown digest renders incorrectly in GitHub, check for unescaped characters in task titles or missing newlines between table rows.

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/minister/skills/github-initiative-pulse/SKILL.md`
