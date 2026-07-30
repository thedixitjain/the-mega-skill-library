---
name: ars-rebuttal-audit
description: "ARS academic-paper `rebuttal-audit` mode — QA an existing rebuttal draft against reviewer comments"
model: "sonnet"
category: security-and-compliance
source_repo: Imbad0202/academic-research-skills
source_path: "commands/ars-rebuttal-audit.md"
source_url: https://github.com/Imbad0202/academic-research-skills/blob/HEAD/commands/ars-rebuttal-audit.md
---


Trigger the `academic-paper` skill in `rebuttal-audit` mode. Requires BOTH the reviewer comments AND an existing rebuttal/response draft to evaluate. Produces an advisory QA report (per-comment coverage + gaps + risk flags). Does NOT generate a new response, and does NOT emit Schema 11 / Material Passport / verified status (standalone invocation runs outside the pipeline). Fidelity spectrum, low oversight.

If only reviewer comments are present (no draft yet), use `revision-coach` instead.

Mode reference: `MODE_REGISTRY.md` § academic-paper.
Skill entry: `academic-paper/SKILL.md`.

---

**Source:** [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) → `commands/ars-rebuttal-audit.md`
