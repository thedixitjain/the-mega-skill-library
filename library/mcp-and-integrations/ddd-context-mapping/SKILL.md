---
name: ddd-context-mapping
description: "Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns."
category: mcp-and-integrations
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/ddd-context-mapping/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/ddd-context-mapping/SKILL.md
---


# DDD Context Mapping

## Use this skill when

- Defining integration patterns between bounded contexts.
- Preventing domain leakage across service boundaries.
- Planning anti-corruption layers during migration.
- Clarifying upstream and downstream ownership for contracts.

## Do not use this skill when

- You have a single-context system with no integrations.
- You only need internal class design.
- You are selecting cloud infrastructure tooling.

## Instructions

1. List all context pairs and dependency direction.
2. Choose relationship patterns per pair.
3. Define translation rules and ownership boundaries.
4. Add failure modes, fallback behavior, and versioning policy.

If detailed mapping structures are needed, open `references/context-map-patterns.md`.

## Output requirements

- Relationship map for all context pairs
- Contract ownership matrix
- Translation and anti-corruption decisions
- Known coupling risks and mitigation plan

## Examples

```text
Use @ddd-context-mapping to define how Checkout integrates with Billing,
Inventory, and Fraud contexts, including ACL and contract ownership.
```

## Limitations

- This skill does not replace API-level schema design.
- It does not guarantee organizational alignment by itself.
- It should be revisited when team ownership changes.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/ddd-context-mapping/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/ddd-context-mapping/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/ddd-context-mapping/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-bundle-ddd-evented-architecture/skills/ddd-context-mapping/SKILL.md`
