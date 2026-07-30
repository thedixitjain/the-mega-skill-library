---
name: deep-research
description: "Deep research harness — fan-out web searches, fetch sources, adversarially verify claims, synthesize a cited report."
category: research-and-academic
source_repo: asgeirtj/system_prompts_leaks
source_path: "Anthropic/Claude Code/bundled-skills/deep-research/SKILL.md"
source_url: https://github.com/asgeirtj/system_prompts_leaks/blob/HEAD/Anthropic/Claude Code/bundled-skills/deep-research/SKILL.md
---


Run the "deep-research" workflow.

Deep research harness — fan-out web searches, fetch sources, adversarially verify claims, synthesize a cited report.

When the user wants a deep, multi-source, fact-checked research report on any topic. BEFORE invoking, check if the question is specific enough to research directly — if underspecified (e.g., "what car to buy" without budget/use-case/region), ask 2-3 clarifying questions to narrow scope. Then pass the refined question as args, weaving the answers in.

Phases:
- Scope: Decompose question (from args) into 5 search angles
- Search: 5 parallel WebSearch agents, one per angle
- Fetch: URL-dedup, fetch top 15 sources, extract falsifiable claims
- Verify: 3-vote adversarial verification per claim (need 2/3 refutes to kill)
- Synthesize: Merge semantic dupes, rank by confidence, cite sources

Invoke: Workflow({ name: "deep-research" })

## Workflow Script

[scripts/workflow-script.js](scripts/workflow-script.js)

---

**Source:** [`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks) → `Anthropic/Claude Code/bundled-skills/deep-research/SKILL.md`
