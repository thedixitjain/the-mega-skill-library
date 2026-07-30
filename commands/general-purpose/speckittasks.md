---
name: speckittasks
description: "Create the tasks needed for implementation and store them in tasks.md."
category: general-purpose
source_repo: github/spec-kit
source_path: "presets/lean/commands/speckit.tasks.md"
source_url: https://github.com/github/spec-kit/blob/HEAD/presets/lean/commands/speckit.tasks.md
---
## User Input

```text
$ARGUMENTS
```

## Outline

1. Read `.specify/feature.json` to get the feature directory path.

2. **Load context**: `.specify/memory/constitution.md` and `<feature_directory>/spec.md` and `<feature_directory>/plan.md`.

3. Create dependency-ordered implementation tasks and store them in `<feature_directory>/tasks.md`.
   - Every task uses checklist format: `- [ ] [TaskID] Description with file path`
   - Organized by phase: setup, foundational, user stories in priority order, polish

---

**Source:** [`github/spec-kit`](https://github.com/github/spec-kit) → `presets/lean/commands/speckit.tasks.md`
