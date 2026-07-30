---
name: dispatch-agents
description: "Use when you have 2+ independent tasks with no shared state — dispatches parallel subagents for each task."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/yimwoo/hotl-plugin/skills/dispatch-agents/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/yimwoo/hotl-plugin/skills/dispatch-agents/SKILL.md
---


# Dispatching Parallel Agents

## When to Use

- Tasks are truly independent (no shared files, no sequential dependency)
- Each task is well-defined with clear success criteria
- 2-5 tasks in parallel (more than 5 becomes hard to review)

## Process

1. List all tasks and confirm independence
2. For each task, write a self-contained prompt including:
   - Full context (don't assume agent knows anything)
   - Exact files to touch
   - Success criteria
   - How to verify
3. Dispatch all agents simultaneously using the Agent tool
4. Collect results and merge
5. Run verification across all changes together
6. Invoke `requesting-code-review` to dispatch the `code-reviewer` agent on merged result, then handle findings via `receiving-code-review`

## Safety

Never dispatch agents for tasks involving shared state — race conditions and conflicts will waste more time than sequential execution saves.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/yimwoo/hotl-plugin/skills/dispatch-agents/SKILL.md`
