---
name: orchestrate
description: "Coordinate focused subagents on substantial work, keep their ownership non-overlapping, and integrate verified results. Use for large-scope Codex tasks; keep trivial work with the coordinator."
allowed-tools: "[codex]"
category: ai-agents-and-harness
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/orchestrate/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/orchestrate/SKILL.md
---


# Orchestrate

Coordinate substantial work across focused subagents while remaining available
to the user and retaining responsibility for the integrated result.

## When to Use

- Use when a task has multiple independent research, review, or implementation lanes.
- Use when parallel work will materially reduce elapsed time or improve coverage.
- Use when a coordinator must synthesize several bounded outputs into one verified result.

Keep trivial tasks with the coordinator.

## Workflow

1. Decompose the task into distinct, bounded assignments with explicit outputs.
2. Run narrow, read-only scouts in parallel with low reasoning effort and no
   inherited conversation when the runtime supports those controls. Give each
   scout all scoped context and evidence required to complete its assignment.
3. Use medium reasoning effort for routine implementation and high reasoning
   effort for difficult work.
4. Give each subagent distinct ownership. Prevent overlapping assignments, and
   instruct leaf workers not to delegate.
5. Integrate the outputs, resolve conflicts, and verify the combined result.
6. Keep approvals and externally consequential decisions with the user.

## Examples

- For a repository-wide feature, assign non-overlapping agents to architecture
  inspection, implementation, and test review, then integrate their findings
  and run the final verification from the coordinator.
- For a research brief, assign independent sources or questions to read-only
  scouts, reconcile disagreements, and keep the final judgment with the
  coordinator.

## Limitations

- Requires a runtime that exposes subagent or delegation tools; otherwise keep
  the work with the coordinator.
- Delegation does not authorize file mutations, public actions, purchases, or
  other consequential operations beyond the user's original scope.
- Parallel agents can add cost and coordination overhead, so use them only when
  the task is substantial enough to benefit.
- The coordinator remains responsible for checking claims, changes, tests, and
  the final answer.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/orchestrate/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/orchestrate/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/orchestrate/SKILL.md`
