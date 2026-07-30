---
name: skill-suggester
description: "Scan prompt history for recurring patterns and unmet needs, then propose new skills or command templates"
category: prompt-engineering
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/skill-suggester/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/skill-suggester/SKILL.md
---


## What I do

Reads your opencode prompt history, finds repeated multi-step workflows, and recommends skill-worthy candidates. Saves you from having the same conversation twice.

## When to Use

Use this skill when the user wants to mine opencode prompt history for repeated workflows, recurring unmet needs, or candidates for new reusable skills.

## How to invoke

Run `/skill skill-suggester` to scan the full history. Optionally pass `--since <date>` (e.g. `--since 2026-05-01`) to limit the window.

## Analysis method

1. Locate prompt history files at `~/.local/state/opencode/prompt-history*.jsonl`
2. Parse each entry's message content
3. Score for skill potential by looking for:
   - **Repetition**: similar phrasing or topic used 3+ times ("scan all repos", "check my inbox")
   - **Multi-step sequences**: a request that required 5+ tool calls to complete
   - **Unsupported requests**: things you asked for that don't have a dedicated skill yet
   - **Workaround patterns**: instructions you give every time instead of a one-shot command
4. For each candidate, note:
   - How many times the pattern appeared
   - How many tool calls it consumed
   - The estimated time savings if it were a skill

## Output format

```
## Skill Candidates (last N entries)

### 1. "<candidate name>" (PRIORITY)
- **Pattern**: <what you keep asking for>
- **Frequency**: X times in history
- **Avg complexity**: Y tool calls per instance
- **Estimated savings**: ~Z minutes/week
- **Evidence**:
  - "[excerpt from prompt history]"
  - "[another excerpt]"
- **Recommendation**: <create as skill | add as command template | not worth it>

### 2. ...
```

## Key rules

- Only flag patterns that happen more than twice. One-offs are not skills.
- Include direct quotes from your past prompts as evidence.
- Rate each candidate: `high` (clear ROI, use weekly), `medium` (nice to have), `low` (rare but worth noting).
- If nothing qualifies, say so and explain why.
- After presenting candidates, ask if you want to create any of them.

## Limitations

- Prompt history can contain sensitive local context; summarize patterns without exposing unnecessary private excerpts.
- Recommendations are suggestions only and still need human review before creating or publishing a new skill.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/skill-suggester/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/skill-suggester/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/skill-suggester/SKILL.md`
