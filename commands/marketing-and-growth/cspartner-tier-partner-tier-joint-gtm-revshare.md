---
name: cspartner-tier-partner-tier-joint-gtm-revshare
description: "Partner tier classification (Referral / Reseller / OEM / SI / Strategic) + joint GTM plan + revshare model. NOT technical sale and NOT channel economics math. Direct invocation of the partnerships-architect skill."
category: marketing-and-growth
source_repo: alirezarezvani/claude-skills
source_path: "commercial/commands/cs-partner-tier.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/commercial/commands/cs-partner-tier.md
---


# /cs:partner-tier — Partner tier + joint GTM + revshare

Run the `partnerships-architect` skill on this input:

**$ARGUMENTS**

## Three-tool workflow

1. **`partner_tier_classifier.py`** — 5-tier deterministic classification: REFERRAL (informal) / RESELLER (transactional + margin) / OEM (white-label + integration) / SI/CONSULTING (services attach) / STRATEGIC (multi-year + co-investment). Hard floors per tier (STRATEGIC requires ≥5 named accounts sourced + multi-year commit + dedicated resources). Tier verdict + **kill criteria** for when partnership should unwind.

2. **`joint_gtm_planner.py`** — 90-day joint GTM plan with pre-launch milestones, launch motion, mid-quarter checkpoint, 90-day success criteria. Validates: cannot plan "channel-led" for REFERRAL tier.

3. **`revshare_modeler.py`** — Recommended revshare % band based on contribution depth (REFERRAL 5-10%, RESELLER 20-35%, OEM 40-55%) + break-even partner-program ROI + long-term economics crossover.

## Hard rule

**Insist on independent-demand evidence before classifying STRATEGIC.** Forrester: channel-led deals from your own pipeline cost more than direct.

## Distinct from

- `business-growth/sales-engineer` — technical sale (demos, POCs)
- Sibling `channel-economics` — cost-to-serve + ROI math, not partnership structure
- `c-level-advisor/cro-advisor` — strategic CRO
- `c-level-advisor/ma-playbook` — acquisition, not partnership

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `commercial/commands/cs-partner-tier.md`
