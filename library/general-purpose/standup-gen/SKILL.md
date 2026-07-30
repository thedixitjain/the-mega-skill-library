---
name: standup-gen
description: "Generate daily standup notes from git activity"
allowed-tools: "Bash"
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/mturac/standup-gen/skills/standup-gen/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/mturac/standup-gen/skills/standup-gen/SKILL.md
---


Role: act as a standup-note author. Produce Yesterday / Today / Blockers sections grounded only in the user's git activity.

Run the helper:

```bash
python3 scripts/standup.py --format md
```

Useful flags: `--since 2026-05-15`, `--since yesterday`, `--repos /path/repoA,/path/repoB`, `--author all`, `--format json`.

The helper fills "Yesterday" from commit subjects and leaves "Today (planned)" and "Blockers" as placeholders. Read the commit list, then propose 1–3 candidate "Today" items derived from in-flight files (e.g. files with WIP or follow-up commits). Mark blockers only if the diffs or commit messages clearly evidence one. Print the final markdown.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/mturac/standup-gen/skills/standup-gen/SKILL.md`
