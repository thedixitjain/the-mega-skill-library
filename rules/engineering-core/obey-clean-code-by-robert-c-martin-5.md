---
name: obey-clean-code-by-robert-c-martin
description: "Use when you need a small always-on bias toward readable, low-surprise code."
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/clean-code/nano.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/clean-code/nano.md
---
# OBEY Clean Code by Robert C. Martin

## When to use

Use when you need a small always-on bias toward readable, low-surprise code.

## Primary bias to correct

Working code is not automatically clean code.

## Decision rules

- Preserve behavior, write for the next reader, and leave touched code cleaner within scope.
- Write for local reasoning and use precise names with one term per concept.
- Split boolean flags, mixed abstraction levels, and hidden side effects out of functions.
- Separate commands from queries and keep parameters small and meaningful.
- Keep the happy path readable; make invalid states, errors, and cleanup explicit instead of implicit.
- Use comments only for rationale or contracts, not to explain confusing code.
- When touching code, remove the smell most likely to make the next change risky or unclear.

## Trigger rules

- When a function both mutates and answers, split it.
- When a comment explains the flow, simplify the code first.
- When async, concurrency, or framework quirks spread the change, reduce shared mutable state and add the right boundary instead of more branching.

## Final checklist

- Local reasoning preserved?
- Clear names?
- Clear mutation boundaries?
- One smell removed?

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/clean-code/nano.md`
