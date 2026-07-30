---
name: nw-test-optimizer-reviewer
description: "Use to validate test-optimizer outputs - hard-blocks if coverage dropped, production code touched, or anti-patterns went unmarked. Runs on Haiku for cost efficiency. Read-only."
category: testing-and-qa
source_repo: nWave-ai/nWave
source_path: "docs/reference/agents/nw-test-optimizer-reviewer.md"
source_url: https://github.com/nWave-ai/nWave/blob/HEAD/docs/reference/agents/nw-test-optimizer-reviewer.md
---
# nw-test-optimizer-reviewer

Use to validate test-optimizer outputs - hard-blocks if coverage dropped, production code touched, or anti-patterns went unmarked. Runs on Haiku for cost efficiency. Read-only.

**Wave:** Other
**Model:** haiku
**Max turns:** 20
**Tools:** Read, Glob, Grep

## Commands

- [`/nw-optimize-tests`](../commands/index.md)

## Skills

- [nw-tdd-methodology](../skills/nw-tdd-methodology.md) — Deep knowledge for Outside-In TDD - double-loop architecture, ATDD integration, port-to-port testing, walking skeletons, and test doubles policy
- [nw-test-optimization](../skills/nw-test-optimization.md) — Methodology for minimizing test count while maximizing behavioral coverage - behavior definition, anti-pattern catalog, consolidation patterns, stopping criterion, coverage-preserving validation

---

**Source:** [`nWave-ai/nWave`](https://github.com/nWave-ai/nWave) → `docs/reference/agents/nw-test-optimizer-reviewer.md`
