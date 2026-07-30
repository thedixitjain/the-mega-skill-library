---
name: billing-automation
description: "Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation."
category: business-and-finance
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/billing-automation/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/billing-automation/SKILL.md
---


# Billing Automation

Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation.

## Use this skill when

- Implementing SaaS subscription billing
- Automating invoice generation and delivery
- Managing failed payment recovery (dunning)
- Calculating prorated charges for plan changes
- Handling sales tax, VAT, and GST
- Processing usage-based billing
- Managing billing cycles and renewals

## Do not use this skill when

- You only need a one-off invoice or manual billing
- The task is unrelated to billing or subscriptions
- You cannot change pricing, plans, or billing flows

## Instructions

- Define plans, pricing, billing intervals, and proration rules.
- Map subscription lifecycle states and renewal/cancellation behavior.
- Implement invoicing, payments, retries, and dunning workflows.
- Model taxes and compliance requirements per region.
- Validate with sandbox payments and reconcile ledger outputs.
- If detailed templates are required, open `resources/implementation-playbook.md`.

## Safety

- Do not charge real customers in testing environments.
- Verify tax handling and compliance obligations before production rollout.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, checklists, and examples.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/billing-automation/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/billing-automation/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/billing-automation/SKILL.md`
