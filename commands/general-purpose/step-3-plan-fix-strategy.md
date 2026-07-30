---
name: step-3-plan-fix-strategy
description: "Purpose: Generate fix strategies for each actionable comment."
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/sanctum/commands/fix-pr-modules/steps/3-plan.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/sanctum/commands/fix-pr-modules/steps/3-plan.md
---
# Step 3: Plan (Fix Strategy)

> **Navigation**: [← Step 2: Triage](2-triage.md) | [Main Workflow](../workflow-steps.md) | [Step 4: Fix →](4-fix.md)

**Purpose**: Generate fix strategies for each actionable comment.

**Skip when**: Fixes are obvious and don't require planning.

## 3.1 Generate Fix Strategies

For each actionable comment, superpowers analyzes:
- Code context around comment location
- Best practices for the suggested change
- Impact on related code
- Test implications

## 3.2 Determine Commit Strategy

| Strategy | When to Use |
|----------|-------------|
| **Single** | Simple fixes, few comments |
| **Separate** | Complex fixes, multiple categories |
| **Manual** | User wants control over commits |

**Step 3 Output**: Fix plan with strategies per comment

---

> **Next**: [Step 4: Fix (Apply Changes) →](4-fix.md)

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/sanctum/commands/fix-pr-modules/steps/3-plan.md`
