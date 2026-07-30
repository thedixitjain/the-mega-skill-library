---
name: model-route-command
description: "Recommend the best model tier for the current task based on complexity, risk, and budget."
category: business-and-finance
source_repo: affaan-m/ECC
source_path: "commands/model-route.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/model-route.md
---
# Model Route Command

Recommend the best model tier for the current task by complexity and budget.

## Usage

`/model-route [task-description] [--budget low|med|high]`

## Routing Heuristic

- `haiku`: deterministic, low-risk mechanical changes
- `sonnet`: default for implementation and refactors
- `opus`: architecture, deep review, ambiguous requirements

## Required Output

- recommended model
- confidence level
- why this model fits
- fallback model if first attempt fails

## Arguments

$ARGUMENTS:
- `[task-description]` optional free-text
- `--budget low|med|high` optional

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/model-route.md`

**Also appears in:** `affaan-m/ECC/.opencode/commands/model-route.md`
