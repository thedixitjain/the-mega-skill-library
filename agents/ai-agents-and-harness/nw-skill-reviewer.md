---
name: nw-skill-reviewer
description: "Use to review SKILL.md quality during DISTILL/DELIVER verification when deliverabletype is plugin or skill. Validates skill structure, scope discipline, frontmatter, and domain-knowledge quality. Thin reviewer — reuses nw-agent-builder skill assets. Runs on Haiku for cost efficiency."
category: ai-agents-and-harness
source_repo: nWave-ai/nWave
source_path: "docs/reference/agents/nw-skill-reviewer.md"
source_url: https://github.com/nWave-ai/nWave/blob/HEAD/docs/reference/agents/nw-skill-reviewer.md
---
# nw-skill-reviewer

Use to review SKILL.md quality during DISTILL/DELIVER verification when deliverable_type is `plugin` or `skill`. Validates skill structure, scope discipline, frontmatter, and domain-knowledge quality. Thin reviewer — reuses nw-agent-builder skill assets. Runs on Haiku for cost efficiency.

**Wave:** Other
**Model:** haiku
**Max turns:** 20
**Tools:** Read, Glob, Grep

## Skills

- [nw-ab-critique-dimensions](../skills/nw-ab-critique-dimensions.md) — Review dimensions for validating agent quality - template compliance, safety, testing, and priority validation
- [nw-agent-creation-workflow](../skills/nw-agent-creation-workflow.md) — Detailed 5-phase workflow for creating agents - from requirements analysis through validation and iterative refinement

---

**Source:** [`nWave-ai/nWave`](https://github.com/nWave-ai/nWave) → `docs/reference/agents/nw-skill-reviewer.md`
