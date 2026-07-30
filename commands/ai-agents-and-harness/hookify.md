---
name: hookify
description: "Create hooks to prevent unwanted behaviors from conversation analysis or explicit instructions"
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "commands/hookify.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/hookify.md
---
Create hook rules to prevent unwanted Claude Code behaviors by analyzing conversation patterns or explicit user instructions.

## Usage

`/hookify [description of behavior to prevent]`

If no arguments are provided, analyze the current conversation to find behaviors worth preventing.

## Workflow

### Step 1: Gather Behavior Info

- With arguments: parse the user's description of the unwanted behavior
- Without arguments: use the `conversation-analyzer` agent to find:
  - explicit corrections
  - frustrated reactions to repeated mistakes
  - reverted changes
  - repeated similar issues

### Step 2: Present Findings

Show the user:

- behavior description
- proposed event type
- proposed pattern or matcher
- proposed action

### Step 3: Generate Rule Files

For each approved rule, create a file at `.claude/hookify.{name}.local.md`:

```yaml
---
name: rule-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern"
---
Message shown when rule triggers.
```

### Step 4: Confirm

Report created rules and how to manage them with `/hookify-list` and `/hookify-configure`.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/hookify.md`
