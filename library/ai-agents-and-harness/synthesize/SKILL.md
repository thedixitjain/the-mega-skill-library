---
name: synthesize
description: "Merges, dedupes, ranks, and formats research findings into a report. Use after research agents return results from multiple channels to produce a ranked report."
category: ai-agents-and-harness
source_repo: athola/claude-night-market
source_path: "plugins/tome/skills/synthesize/SKILL.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/tome/skills/synthesize/SKILL.md
---

# Finding Synthesis

## When To Use

- After research agents return results from multiple channels
- Producing a final ranked report from raw findings

## When NOT To Use

- No research session is active (run `/tome:research` first)
- Refining a single channel (use `/tome:dig` instead)

Merge findings from all channels into a ranked report.

## Workflow

1. Merge: `tome.synthesis.merger.merge_findings()`
2. Rank: `tome.synthesis.ranker.rank_findings()`
3. Group: `tome.synthesis.ranker.group_by_theme()`
4. Format: `tome.output.report.format_report()`

## Output Formats

- **report**: Full sectioned markdown
- **brief**: Condensed 1-2 pages
- **transcript**: Raw session log

## Exit Criteria

- [ ] `merge_findings()`, `rank_findings()`, and `group_by_theme()`
      all called in sequence before output is formatted
- [ ] Output formatted via `format_report()` by default, or
      `format_brief()` / `format_transcript()` when the flag is set
- [ ] Findings grouped by theme in the report, not presented as raw
      per-channel lists
- [ ] If the merged finding count is 0, this is stated explicitly
      rather than generating an empty or fabricated report
- [ ] If no active session exists, error emitted directing the user
      to run `/tome:research` first

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/tome/skills/synthesize/SKILL.md`
