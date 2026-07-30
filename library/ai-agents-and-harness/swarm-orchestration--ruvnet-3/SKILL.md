---
name: swarm-orchestration
description: "> Multi-agent swarm coordination for complex tasks. Use when: 3+ files need changes, new features, refactoring. Skip when: single file edits, simple fixes, documentation."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: "v3/@claude-flow/codex/.agents/skills/swarm-orchestration/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/v3/@claude-flow/codex/.agents/skills/swarm-orchestration/SKILL.md
---


# Swarm Orchestration Skill

## Purpose
Multi-agent swarm coordination for complex tasks.

## When to Trigger
- 3+ files need changes
- new features
- refactoring

## When to Skip
- single file edits
- simple fixes
- documentation

## Commands

### Initialize Swarm
Start a new swarm with hierarchical topology

```bash
npx @claude-flow/cli swarm init --topology hierarchical --max-agents 8
```

### Route Task
Route a task to the appropriate agents

```bash
npx @claude-flow/cli hooks route --task "[task description]"
```

### Monitor Status
Check the current swarm status

```bash
npx @claude-flow/cli swarm status
```



## Best Practices
1. Check memory for existing patterns before starting
2. Use hierarchical topology for coordination
3. Store successful patterns after completion
4. Document any new learnings

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `v3/@claude-flow/codex/.agents/skills/swarm-orchestration/SKILL.md`
