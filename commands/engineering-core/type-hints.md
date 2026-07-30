---
name: type-hints
description: "Add comprehensive type hints to Python code for better IDE support and type safety."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/python-expert/commands/type-hints.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/python-expert/commands/type-hints.md
---


Add comprehensive type hints to Python code for better IDE support and type safety.

## Steps


1. Analyze the target Python file for untyped code:
2. Determine types by analyzing usage:
3. Add function signatures:
4. Add complex types:
5. Add class-level type hints:
6. Verify with mypy or pyright:
7. Update docstrings to match type annotations.

## Format


```
File: <path>
Functions Typed: <count>
Classes Typed: <count>
Type Checker: <mypy|pyright> - <pass|N errors>
```


## Rules

- Use modern syntax (str | None) for Python 3.10+ projects.
- Use typing imports for older Python versions.
- Avoid Any unless truly necessary; be specific.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/python-expert/commands/type-hints.md`
