---
name: worktree
description: "Use for non-trivial or parallel work that should happen in a separate git worktree."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/ouonet/praxis/skills/worktree/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/ouonet/praxis/skills/worktree/SKILL.md
---

# Worktree

```bash
git worktree add ../<repo>-<topic> -b <type>/<topic>   # <type>: feat | fix | chore | ...
cd ../<repo>-<topic> && <setup> && <run tests>
```

Baseline must be green. If red, STOP - don't build on broken ground. Done -> `ship`.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/ouonet/praxis/skills/worktree/SKILL.md`
