---
name: claude-instructions-for-local-skill-loading
description: "When a user first needs skills and ~/.spawner/skills doesn't exist:"
category: general-purpose
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "CLAUDE_INSTRUCTIONS.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/CLAUDE_INSTRUCTIONS.md
---
# Claude Instructions for Local Skill Loading

> This file tells Claude how to load skills locally. Include this in system context.

## First-Time Setup

When a user first needs skills and `~/.spawner/skills` doesn't exist:

```
1. Check: Does ~/.spawner/skills exist?
   - Windows: %USERPROFILE%\.spawner\skills
   - macOS/Linux: ~/.spawner/skills

2. If NO, clone the repo:
   git clone https://github.com/vibeforge1111/vibeship-spawner-skills ~/.spawner/skills

3. Confirm: "Skills ready! I have 105 skills loaded locally."
```

## Loading a Skill

To load a skill, read the YAML files from local disk:

```
# Example: Load backend skill
Read: ~/.spawner/skills/development/backend/skill.yaml
Read: ~/.spawner/skills/development/backend/sharp-edges.yaml
Read: ~/.spawner/skills/development/backend/validations.yaml
Read: ~/.spawner/skills/development/backend/collaboration.yaml
```

## Finding Skills by Category

| Need | Category Path |
|------|--------------|
| Backend/API work | `development/backend`, `development/api-designer` |
| Frontend/UI | `development/frontend`, `design/ui-design` |
| Database | `data/postgres-wizard`, `data/redis-specialist` |
| AI/LLM | `ai/llm-architect`, `ai/ml-memory` |
| Auth | `development/auth-specialist` |
| Testing | `development/test-architect`, `development/qa-engineering` |
| DevOps | `development/devops`, `development/infra-architect` |
| Security | `development/security`, `development/cybersecurity` |

## Skill File Purposes

| File | Contains |
|------|----------|
| `skill.yaml` | Identity, patterns, anti-patterns, handoffs |
| `sharp-edges.yaml` | Gotchas and warnings with severity |
| `validations.yaml` | Code checks to run |
| `collaboration.yaml` | Prerequisites, cross-domain insights |

## Updating Skills

When user asks to update skills:

```bash
cd ~/.spawner/skills && git pull
```

## Pack Loading (Optional)

To load an entire pack, read `registry.yaml` and load listed skills:

```yaml
# registry.yaml defines packs
packs:
  essentials:
    skills:
      - development/backend
      - development/frontend
      # ... load each skill in list
```

## Natural Language Triggers

| User Says | Action |
|-----------|--------|
| "Help me build an app" | Check skills exist, load essentials if needed |
| "I need database help" | Load `data/postgres-wizard` |
| "Set up authentication" | Load `development/auth-specialist` |
| "Review my code" | Load `development/code-reviewer` |
| "Deploy this" | Load `development/devops` |
| "Make it look good" | Load `design/ui-design` |

## Error Handling

If skills directory is corrupted or incomplete:

```bash
rm -rf ~/.spawner/skills
git clone https://github.com/vibeforge1111/vibeship-spawner-skills ~/.spawner/skills
```

## Key Principles

1. **Local first** - Always read from local files, never API
2. **Auto-setup** - Clone repo on first use, no user action needed
3. **Silent** - Don't announce every skill load, just use the knowledge
4. **Offline works** - Once cloned, no internet needed

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `CLAUDE_INSTRUCTIONS.md`
