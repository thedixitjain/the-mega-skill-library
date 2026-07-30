---
name: architecture
description: "Architecture design skill with ADR records, system design checklists, scalability assessment, and architecture patterns"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/cc-best/skills/architecture/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/cc-best/skills/architecture/SKILL.md
---


# Architecture Skill

Provides architectural guidance for system design decisions, including:

- **ADR (Architecture Decision Records)**: Structured format for recording design decisions with context, options, and rationale
- **System Design Checklist**: Scalability, reliability, observability, security considerations
- **Architecture Patterns**: Microservices, event-driven, layered, hexagonal
- **API Design**: RESTful conventions, versioning, pagination, error handling

## When Loaded

This skill is automatically injected when working with:

- `/cc-best:lead` — Technical design phase
- `architect` agent — System architecture decisions
- `planner` agent — Task breakdown and complexity analysis

## Key Principles

1. **Simplicity first** — Choose the simplest architecture that meets requirements
2. **Document decisions** — Every significant choice gets an ADR
3. **Separation of concerns** — Clear boundaries between components
4. **Design for failure** — Graceful degradation and circuit breakers

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/cc-best/skills/architecture/SKILL.md`
