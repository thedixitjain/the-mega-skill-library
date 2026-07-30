---
name: add-endpoint
description: "Add a new API endpoint to an existing backend service with validation and tests."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/backend-architect/commands/add-endpoint.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/backend-architect/commands/add-endpoint.md
---
Add a new API endpoint to an existing backend service with validation and tests.

## Steps


1. Define the endpoint specification:
2. Identify the framework and add the route:
3. Implement the handler:
4. Add input validation:
5. Add middleware if needed:
6. Write tests:
7. Update API documentation.

## Format


```
Endpoint: <METHOD> <path>
Auth: <required|optional|none>
Request: <body schema>
Response: <success schema>
```


## Rules

- Follow REST conventions: POST for create, PUT for replace, PATCH for update.
- Return appropriate HTTP status codes (201 for create, 204 for delete).
- Validate all input before processing.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/backend-architect/commands/add-endpoint.md`
