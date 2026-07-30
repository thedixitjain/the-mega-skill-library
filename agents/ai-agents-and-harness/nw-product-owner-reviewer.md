---
name: nw-product-owner-reviewer
description: "Use as hard gate before DESIGN wave - validates journey coherence, emotional arc quality, shared artifact tracking, Definition of Ready checklist, LeanUX antipatterns, and story sizing. Blocks handoff if any critical issue or DoR item fails. Runs on Haiku for cost efficiency."
category: ai-agents-and-harness
source_repo: nWave-ai/nWave
source_path: "docs/reference/agents/nw-product-owner-reviewer.md"
source_url: https://github.com/nWave-ai/nWave/blob/HEAD/docs/reference/agents/nw-product-owner-reviewer.md
---
# nw-product-owner-reviewer

Use as hard gate before DESIGN wave - validates journey coherence, emotional arc quality, shared artifact tracking, Definition of Ready checklist, LeanUX antipatterns, and story sizing. Blocks handoff if any critical issue or DoR item fails. Runs on Haiku for cost efficiency.

**Wave:** DESIGN
**Model:** haiku
**Max turns:** 0
**Tools:** Read, Glob, Grep

## Commands

- [`/nw-distill`](../commands/index.md)

## Skills

- [nw-dor-validation](../skills/nw-dor-validation.md) — Definition of Ready checklist criteria, antipattern detection patterns, UAT quality rules, and domain language enforcement for product owner review
- [nw-po-review-dimensions](../skills/nw-po-review-dimensions.md) — Requirements quality critique dimensions for peer review - confirmation bias detection, completeness validation, clarity checks, testability assessment, and priority validation
- [nw-por-review-criteria](../skills/nw-por-review-criteria.md) — Review dimensions and bug patterns for journey artifact reviews

---

**Source:** [`nWave-ai/nWave`](https://github.com/nWave-ai/nWave) → `docs/reference/agents/nw-product-owner-reviewer.md`
