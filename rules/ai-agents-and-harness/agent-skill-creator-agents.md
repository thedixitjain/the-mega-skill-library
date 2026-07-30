---
name: agent-skill-creator-agents
description: "Turn any workflow into a reusable, cross-platform agent skill. The user describes what they do — in plain English, or by handing over a PDF, a link, a script, a transcript — and this skill builds a complete, validated, security-scanned agent skill with functional code, its own eval suite, and a cross-platform installer."
category: ai-agents-and-harness
source_repo: FrancyJGLisboa/agent-skill-creator
source_path: "AGENTS.md"
source_url: https://github.com/FrancyJGLisboa/agent-skill-creator/blob/HEAD/AGENTS.md
---
# agent-skill-creator

Turn any workflow into a reusable, cross-platform agent skill. The user
describes what they do — in plain English, or by handing over a PDF, a link, a
script, a transcript — and this skill builds a complete, validated,
security-scanned agent skill with functional code, its own eval suite, and a
cross-platform installer.

## Activation

Invoke with `/agent-skill-creator <description or material>`, or naturally:

- "Create a skill for analyzing CSV files"
- "Every day I process invoices manually, automate this"
- "Validate this skill" / "Export this skill for Cursor"

## How to use this file

This is the cross-tool companion file (AAIF format). The full factory
instructions — the five-phase pipeline, quality gates, eval emission, and
cross-platform export — live in [SKILL.md](SKILL.md) at this repo root. Read
SKILL.md and follow it; treat this file as the pointer, not the instructions.

## What generated skills carry

Every skill this factory produces ships with: spec-compliant SKILL.md +
AGENTS.md, functional scripts, an eval spec with golden cases and a regression
gate (scripts/run_evals.py), a self-maintenance loop (scripts/evolve.py),
plugin manifests for native in-tool installs, and a 17-platform installer.

---

**Source:** [`FrancyJGLisboa/agent-skill-creator`](https://github.com/FrancyJGLisboa/agent-skill-creator) → `AGENTS.md`
