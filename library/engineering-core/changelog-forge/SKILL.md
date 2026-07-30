---
name: changelog-forge
description: "Group conventional commits since last tag into a CHANGELOG entry"
allowed-tools: "Bash"
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/mturac/changelog-forge/skills/changelog-forge/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/mturac/changelog-forge/skills/changelog-forge/SKILL.md
---


Role: act as a release scribe. Turn conventional commits into a clean `## [Unreleased]` block plus a semver-bump recommendation.

Run the helper:

```bash
python3 scripts/forge.py --format md
```

Useful flags: `--from v1.2.0`, `--to HEAD`, `--write` (prepend to `CHANGELOG.md`, idempotent), `--format json`.

The helper groups commits by type (feat / fix / perf / refactor / docs / test / build / ci / chore / revert), surfaces `BREAKING CHANGE` markers, and suggests `major | minor | patch`. Read the output, then briefly justify the bump (or push back if the heuristic missed nuance). Only run `--write` when the user explicitly asks for it.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/mturac/changelog-forge/skills/changelog-forge/SKILL.md`
