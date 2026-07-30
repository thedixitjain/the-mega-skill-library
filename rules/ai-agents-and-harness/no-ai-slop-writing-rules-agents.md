---
name: no-ai-slop-writing-rules-agents
description: "Guidelines for AI agents working in this repository."
category: ai-agents-and-harness
source_repo: realrossmanngroup/no_ai_slop_writing_rules
source_path: "AGENTS.md"
source_url: https://github.com/realrossmanngroup/no_ai_slop_writing_rules/blob/HEAD/AGENTS.md
---
# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository publishes portable writing skills for AI agents. The installable skills live under `skills/` and follow the Agent Skills directory shape:

```text
skills/
├── no-ai-slop/
│   ├── SKILL.md
│   └── references/
└── rossmann-voice/
    └── SKILL.md
```

The `.claude/skills/` directory is kept for Claude Code project-local use. Keep the skill content synchronized when changing either published skill.

## Published Skills

- `no-ai-slop`: Rules and worked examples for writing prose that does not read like AI-generated slop.
- `rossmann-voice`: Louis Rossmann's writing voice for general prose.

## Skill Format

Each skill requires a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

Optional supporting material belongs beside the skill:

```text
skills/skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

## Manual Checks

- `name` must match the parent directory name.
- `description` should state what the skill does and when to use it.
- Keep large reference material in `references/` so agents can load it on demand.
- Do not weaken the writing rules while changing the package format.

---

**Source:** [`realrossmanngroup/no_ai_slop_writing_rules`](https://github.com/realrossmanngroup/no_ai_slop_writing_rules) → `AGENTS.md`
