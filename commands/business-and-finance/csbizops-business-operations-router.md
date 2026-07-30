---
name: csbizops-business-operations-router
description: "Top-level Business Operations router. Routes the inquiry to one of six BizOps sub-skills (process, vendor, capacity, comms, knowledge, procurement) and returns a digest. Invokes the business-operations-skills orchestrator (context: fork)."
category: business-and-finance
source_repo: alirezarezvani/claude-skills
source_path: "business-operations/commands/cs-bizops.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/business-operations/commands/cs-bizops.md
---


# /cs:bizops — Business Operations router

Use the `cs-bizops-orchestrator` agent + `business-operations-skills` orchestrator skill to handle this inquiry:

**$ARGUMENTS**

## Routing protocol

1. Classify the inquiry against the six BizOps lanes:
   - **PROCESS** — bottleneck, cycle time, handoff, workflow → `process-mapper`
   - **VENDOR** — SLA, third-party risk, SaaS audit → `vendor-management`
   - **CAPACITY** — headcount, utilization, hiring sequence → `capacity-planner`
   - **COMMS** — all-hands, change announcement, internal newsletter → `internal-comms`
   - **KNOWLEDGE** — SOP, runbook, onboarding doc → `knowledge-ops`
   - **PROCUREMENT** — spend audit, supplier rationalization → `procurement-optimizer`

2. If top lane signal score ≥ 2 keyword hits → invoke that sub-skill in forked context.

3. If single-signal or tie → ask **one** clarifying question naming the top two candidate lanes.

4. After sub-skill runs, return ≤ 200-word digest to the parent context.

## Output expectations

- What was analyzed
- Top 3 findings with severity (CRITICAL/HIGH/MEDIUM)
- Top 3 next actions with named owners
- Path to artifact(s) saved to the user's working directory
- Suggested chain (which sub-skill to invoke next, if any)

## Anti-patterns

- ❌ Running multiple sub-skills to be thorough — pick one, digest, chain on request
- ❌ Auto-approving an ops change — surface findings, the human decides

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `business-operations/commands/cs-bizops.md`
