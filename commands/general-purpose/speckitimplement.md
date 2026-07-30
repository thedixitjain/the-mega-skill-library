---
name: speckitimplement
description: "Execute the implementation plan by processing all tasks in tasks.md."
category: general-purpose
source_repo: github/spec-kit
source_path: "presets/lean/commands/speckit.implement.md"
source_url: https://github.com/github/spec-kit/blob/HEAD/presets/lean/commands/speckit.implement.md
---
## User Input

```text
$ARGUMENTS
```

## Outline

1. Read `.specify/feature.json` to get the feature directory path.

2. **Load context**: `.specify/memory/constitution.md` and `<feature_directory>/spec.md` and `<feature_directory>/plan.md` and `<feature_directory>/tasks.md`.

3. **Execute tasks** in order:
   - Complete each task before moving to the next
   - Mark completed tasks by changing `- [ ]` to `- [x]` in `<feature_directory>/tasks.md`
   - Halt on failure and report the issue

4. **Validate**: Verify all tasks are completed and the implementation matches the spec.

---

**Source:** [`github/spec-kit`](https://github.com/github/spec-kit) → `presets/lean/commands/speckit.implement.md`
