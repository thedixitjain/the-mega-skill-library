---
name: setup-help
description: "Walk a user through setup or installation one step at a time with the remaining steps visible."
allowed-tools: "[claude, codex]"
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/setup-help/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/setup-help/SKILL.md
---


# setup-help

## When to Use

- Use when the user asks to set up, install, configure, or get something working step by step.
- Use when the setup has multiple steps and benefits from one-at-a-time guidance.

Guide the user through any setup, one step at a time, in plain English.

## Response format (every single response)

1. **Current step** — ONE atomic action. A single click, field, or command — not a checklist. 1–2 lines max. If it needs sub-steps, it's too big: split it and push the rest into "Still remaining". Plain English.
2. A `----` divider.
3. **Still remaining** — a numbered list of the setup steps left after this one. Max 8 items, ever.

Repeat this format for every response until setup is done.

## Rules

- Before the first step, build a complete canonical checklist from the user's outline, repo/docs, current screen, and any discovered prerequisites.
- The **Still remaining** list must never exceed 8 items — more is overwhelming. Track ALL unfinished checklist items internally; if more than 8 remain, show the nearest steps individually and merge the later ones into broader phase-level items so the list stays at 8 or fewer. Never silently drop a required step from internal tracking.
- If a new required step is discovered mid-setup, add it to **Still remaining** immediately in the correct order.
- Before every response, audit the current step plus **Still remaining** against the canonical checklist. If any unfinished step is missing, fix the list before replying.
- Only give instructions for the current step. Do not jump ahead.
- Keep it concise. Short sentences. No filler.
- After the user finishes a step, move the next "remaining" item up to "Current step".
- Update the "Still remaining" list each time as steps get done.
- When nothing remains, say setup is complete instead of showing the list.

## Limitations

- Adapted from `davidondrej/skills`; verify local paths, tools, credentials, and agent features before acting.
- For commands, remote access, scheduling, browser automation, or file-changing workflows, get explicit user approval and confirm the target environment first.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/setup-help/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/setup-help/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/setup-help/SKILL.md`
