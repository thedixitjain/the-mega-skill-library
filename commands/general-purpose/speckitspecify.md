---
name: speckitspecify
description: "Create a specification and store it in spec.md."
category: general-purpose
source_repo: github/spec-kit
source_path: "presets/lean/commands/speckit.specify.md"
source_url: https://github.com/github/spec-kit/blob/HEAD/presets/lean/commands/speckit.specify.md
---
## User Input

```text
$ARGUMENTS
```

## Outline

1. **Ask the user** for the feature directory path (e.g., `specs/my-feature`). Do not proceed until provided.

2. Create the directory and write `.specify/feature.json`:
   ```json
   { "feature_directory": "<feature_directory>" }
   ```

3. Create a specification from the user input and store it in `<feature_directory>/spec.md`.
   - Overview, functional requirements, user scenarios, success criteria
   - Every requirement must be testable
   - Make informed defaults for unspecified details

---

**Source:** [`github/spec-kit`](https://github.com/github/spec-kit) → `presets/lean/commands/speckit.specify.md`
