---
name: technical-change-tracker
description: "Track code changes with structured JSON records, state machine enforcement, and AI session handoff for bot continuity"
allowed-tools: "[claude, cursor, gemini, codex]"
category: ai-agents-and-harness
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/technical-change-tracker/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/technical-change-tracker/SKILL.md
---


# Technical Change Tracker

## Overview

Track every code change with structured JSON records and accessible HTML output. Ensures AI bot sessions can resume seamlessly when previous sessions expire or are abandoned.

## When to Use This Skill

- Use when you need structured change tracking across AI coding sessions
- Use when a bot session expires mid-task and the next session needs full context to resume
- Use when onboarding a project with undocumented change history

## How It Works

### State Machine

```
planned -> in_progress -> implemented -> tested -> deployed
             |
             +-> blocked
```

### Commands

`/tc init` | `/tc create` | `/tc update` | `/tc status` | `/tc resume` | `/tc close` | `/tc export` | `/tc dashboard` | `/tc retro`

### Session Handoff

Each TC stores: progress summary, next steps, blockers, key context, and files in progress — so the next bot session picks up exactly where the last left off.

### Non-Blocking

TC bookkeeping runs via background subagents. Never interrupts coding work.

## Features

- Structured JSON records with append-only revision history
- Test cases with log snippet evidence
- WCAG AA+ accessible HTML output (dark theme, rem-based fonts)
- CSS-only dashboard with status filters
- Python stdlib only — zero external dependencies
- Retroactive bulk creation from git history via `/tc retro`

## Full Repository

https://github.com/Elkidogz/technical-change-skill — MIT License

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/technical-change-tracker/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/technical-change-tracker/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/technical-change-tracker/SKILL.md`
