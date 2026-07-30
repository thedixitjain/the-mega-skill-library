# Harness Pattern Language

Use these patterns as reusable harness building blocks.

## 1. Request Assembler

Purpose:

- combine stable instructions, runtime context, user context, tools, and history into a final model request

Questions:

- what sources feed the system prompt
- what sources are per-turn only
- where tool affordances are injected
- whether history needs normalization or repair

## 2. Turn Loop

Purpose:

- define the repeated control flow of the harness

Typical stages:

- gather
- think or plan
- act
- verify
- continue or stop

## 3. Capability Plane

Purpose:

- expose tools as bounded capabilities rather than raw shell access

Questions:

- what each tool is for
- what permission mode it requires
- what output proves success
- how failures or partial results are handled

## 4. Context Governor

Purpose:

- keep the active context window coherent over time

Includes:

- retrieval and grounding
- memory selection
- summarization and compaction
- context-budget decisions

## 5. Permission Gate

Purpose:

- align risk with authority

Examples:

- read-only mode
- approval-required write mode
- bounded auto mode
- stronger confirmation for destructive actions

## 6. Transcript Spine

Purpose:

- keep a durable semantic record of what the agent saw, did, and decided

This is different from raw logs. It should preserve enough structure for:

- debugging
- audits
- resume flows
- post-hoc reasoning

## 7. Recovery Plane

Purpose:

- let the harness survive interruption, partial completion, or context collapse

Common needs:

- resumable task state
- compact boundaries
- rehydration of durable instructions
- partial artifact preservation

## 8. Extension Plane

Purpose:

- let the harness grow without destabilizing the core loop

Examples:

- plugins
- MCP integrations
- subagents
- external skills

Extension should come after the core loop, not before it.

## 9. Human Control Surface

Purpose:

- give users visibility and steering power

Includes:

- current plan
- pending approvals
- recent actions
- interruption points
- summaries of what changed

## 10. Evaluation Plane

Purpose:

- measure whether the harness is actually good

Evaluate:

- usefulness
- correctness
- controllability
- recovery quality
- latency
- cost
- operator burden

