---
name: design-service
description: "Design a backend service architecture with clear boundaries, data models, and API contracts."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/backend-architect/commands/design-service.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/backend-architect/commands/design-service.md
---
Design a backend service architecture with clear boundaries, data models, and API contracts.

## Steps


1. Define the service scope:
2. Design the data model:
3. Design the API layer:
4. Plan the service internals:
5. Design inter-service communication:
6. Plan for observability:
7. Document the service contract.

## Format


```
Service: <name>
Domain: <what it owns>
Entities: <data model summary>
API Endpoints: <list>
```


## Rules

- Each service should own its data; no shared databases.
- Design for failure: every external call can fail.
- Use interface segregation; expose only what consumers need.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/backend-architect/commands/design-service.md`
