---
name: changelog
description: "Generate changelogs from git history and validate conventional commits. Usage: /changelog <generate|lint> [options]. Slash command for Claude Code, Codex CLI, Gemini CLI."
category: engineering-core
source_repo: alirezarezvani/claude-skills
source_path: "docs/commands/changelog.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/docs/commands/changelog.md
---


# /changelog

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/changelog.md">Source</a></span>
</div>


Generate Keep a Changelog entries from git history and validate commit message format.

## Usage

```
/changelog generate [--from-tag <tag>] [--to-tag <tag>]    Generate changelog entries
/changelog lint [--from-ref <ref>] [--to-ref <ref>]       Lint commit messages
```

## Examples

```
/changelog generate --from-tag v2.0.0
/changelog lint --from-ref main --to-ref dev
/changelog generate --from-tag v2.0.0 --to-tag v2.1.0 --format markdown
```

## Scripts
- `engineering/skills/changelog-generator/scripts/generate_changelog.py` — Parse commits, render changelog (`--from-tag`, `--to-tag`, `--from-ref`, `--to-ref`, `--format markdown|json`)
- `engineering/skills/changelog-generator/scripts/commit_linter.py` — Validate conventional commit format (`--from-ref`, `--to-ref`, `--strict`, `--format text|json`)

## Skill Reference
→ `engineering/skills/changelog-generator/SKILL.md`

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `docs/commands/changelog.md`
