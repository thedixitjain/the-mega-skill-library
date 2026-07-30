---
name: prompt-improve
description: "Analyze and improve a plugin prompt, skill definition, or command instruction"
category: prompt-engineering
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/security/severity1-marketplace/commands/prompt-improve.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/security/severity1-marketplace/commands/prompt-improve.md
---

# Prompt Improver

Analyze the current plugin's prompts, skill definitions, or command instructions and suggest improvements for clarity, safety, effectiveness, and best-practice adherence.

## Analysis Dimensions

1. **Clarity** — Are instructions unambiguous and easy to follow?
2. **Safety** — Does the prompt avoid encouraging dangerous operations?
3. **Effectiveness** — Will the prompt reliably produce the intended result?
4. **Completeness** — Are edge cases and error scenarios addressed?
5. **Conciseness** — Is the prompt free of unnecessary verbosity?

## Process

1. **Read** the target file (SKILL.md, command .md, or agent .md)
2. **Score** each dimension on a 1-5 scale
3. **Identify** specific improvement opportunities
4. **Suggest** concrete rewrites for weak sections
5. **Validate** that improvements preserve original intent

## Output Format

```
## Prompt Analysis: [filename]

### Scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| Clarity | X/5 | ... |
| Safety | X/5 | ... |
| Effectiveness | X/5 | ... |
| Completeness | X/5 | ... |
| Conciseness | X/5 | ... |

**Overall: X/25**

### Improvements
1. [Specific improvement with before/after]
2. [Specific improvement with before/after]

### Suggested Rewrite
[Full improved prompt text]
```

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/security/severity1-marketplace/commands/prompt-improve.md`
