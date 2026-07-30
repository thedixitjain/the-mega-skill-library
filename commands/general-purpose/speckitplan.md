---
name: speckitplan
description: "Create a plan and store it in plan.md."
category: general-purpose
source_repo: github/spec-kit
source_path: "presets/lean/commands/speckit.plan.md"
source_url: https://github.com/github/spec-kit/blob/HEAD/presets/lean/commands/speckit.plan.md
---
## User Input

```text
$ARGUMENTS
```

## Outline

1. Read `.specify/feature.json` to get the feature directory path.

2. **Load context**: `.specify/memory/constitution.md` and `<feature_directory>/spec.md`.

3. Create an implementation plan and store it in `<feature_directory>/plan.md`.
   - Technical context: tech stack, dependencies, project structure
   - Design decisions, architecture, file structure

---

**Source:** [`github/spec-kit`](https://github.com/github/spec-kit) → `presets/lean/commands/speckit.plan.md`
