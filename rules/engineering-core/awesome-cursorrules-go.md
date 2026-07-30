---
name: awesome-cursorrules-go
description: "Idiomatic Go rules. Explicit error handling, interface-based design, context-first concurrency."
category: engineering-core
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/go.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/go.mdc
---

# Go Language Rules

Expert Go developer. Simple, explicit, idiomatic.

## Error Handling
- Always handle errors — never assign to _
- fmt.Errorf("context: %w", err) for wrapping
- errors.Is() / errors.As() for checking
- Custom error types for structured errors

## Naming
- Short for short-lived vars: i, n, err, ok
- No stuttering: user.UserID → user.ID
- Acronyms: userID, httpClient (not userId, httpClient)
- Interfaces: end in -er (Reader, Writer, Handler)

## Interfaces
- Accept interfaces, return concrete types
- Define at call site, not implementation site
- Single-method interfaces preferred

## Concurrency
- context.Context first param for blocking functions
- defer cancel() after context creation
- WaitGroup for goroutine groups
- Channels for communication, Mutex for state

## Testing
- Table-driven: for _, tc := range testCases { t.Run(tc.name, ...) }
- Interface-based mocking

## Forbidden
- No _ to ignore errors
- No init() for business logic
- No global mutable state
- No interface{} where generics work
- No goroutines without termination condition

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/go.mdc`
