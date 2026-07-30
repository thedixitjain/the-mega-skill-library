---
name: debug
description: "Use for bugs, unexpected behavior, regressions, or failing tests you did not write."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/ouonet/praxis/skills/debug/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/ouonet/praxis/skills/debug/SKILL.md
---

# Debug

1. **Reproduce.** Minimal deterministic repro. No repro -> no fix.
2. **Root-cause.** Ask "why" until one cause explains *all* symptoms. Symptoms != cause.
3. **Regression test first** (red), then fix at the root (green). Use `tdd`.

## Don't
- Guess. Read the code and the full error.
- Change two things at once.
- Stop at the first plausible cause.

3 failed hypotheses -> re-read from scratch. Done = repro + regression test + root cause named + green.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/ouonet/praxis/skills/debug/SKILL.md`
