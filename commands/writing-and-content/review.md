---
name: review
description: "Audit content against brand, style, and compliance; return a redline."
category: writing-and-content
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/content-multiplier/commands/review.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/content-multiplier/commands/review.md
---


# Review

QA any content — a draft, a competitor-inspired piece, or something a teammate wrote — against your brand rules before it ships.

Arguments: `$ARGUMENTS`

## Workflow

1. **Parse args.** Identify the content to review and any `--brand` / `--locale`.
2. **Load** the applicable brand profile (with locale overrides if given).
3. **Delegate** to the `brand-guardian` subagent to produce the **scorecard** (Voice / Style / Compliance = pass|fix per asset).
4. **Produce a redline.** For every `fix`, show the original text, the problem (which rule it breaks), and the corrected version inline.
5. **Summarize.** Give an overall pass/needs-work verdict and the top 3 things to fix first.

Read-only with respect to the user's content — propose changes, don't silently rewrite files. Never access the network.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/content-multiplier/commands/review.md`
