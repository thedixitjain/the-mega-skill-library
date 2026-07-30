---
name: ddd-strategic-design
description: "Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains."
category: frontend-and-design
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/ddd-strategic-design/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/ddd-strategic-design/SKILL.md
---


# DDD Strategic Design

## Use this skill when

- Defining core, supporting, and generic subdomains.
- Splitting a monolith or service landscape by domain boundaries.
- Aligning teams and ownership with bounded contexts.
- Building a shared ubiquitous language with domain experts.

## Do not use this skill when

- The domain model is stable and already well bounded.
- You need tactical code patterns only.
- The task is purely infrastructure or UI oriented.

## Instructions

1. Extract domain capabilities and classify subdomains.
2. Define bounded contexts around consistency and ownership.
3. Establish a ubiquitous language glossary and anti-terms.
4. Capture context boundaries in ADRs before implementation.

If detailed templates are needed, open `references/strategic-design-template.md`.

## Required artifacts

- Subdomain classification table
- Bounded context catalog
- Glossary with canonical terms
- Boundary decisions with rationale

## Examples

```text
Use @ddd-strategic-design to map our commerce domain into bounded contexts,
classify subdomains, and propose team ownership.
```

## Limitations

- This skill does not produce executable code.
- It cannot infer business truth without stakeholder input.
- It should be followed by tactical design before implementation.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/ddd-strategic-design/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/ddd-strategic-design/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/ddd-strategic-design/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-bundle-ddd-evented-architecture/skills/ddd-strategic-design/SKILL.md`
