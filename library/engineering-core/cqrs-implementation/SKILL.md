---
name: cqrs-implementation
description: "Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems."
category: engineering-core
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/cqrs-implementation/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/cqrs-implementation/SKILL.md
---


# CQRS Implementation

Comprehensive guide to implementing CQRS (Command Query Responsibility Segregation) patterns.

## Use this skill when

- Separating read and write concerns
- Scaling reads independently from writes
- Building event-sourced systems
- Optimizing complex query scenarios
- Different read/write data models are needed
- High-performance reporting is required

## Do not use this skill when

- The domain is simple and CRUD is sufficient
- You cannot operate separate read/write models
- Strong immediate consistency is required everywhere

## Instructions

- Identify read/write workloads and consistency needs.
- Define command and query models with clear boundaries.
- Implement read model projections and synchronization.
- Validate performance, recovery, and failure modes.
- If detailed patterns are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed CQRS patterns and templates.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/cqrs-implementation/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/cqrs-implementation/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/cqrs-implementation/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-bundle-ddd-evented-architecture/skills/cqrs-implementation/SKILL.md`
