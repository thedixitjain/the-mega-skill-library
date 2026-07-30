---
name: speckitspecify
description: "Create a feature specification (preset override)"
category: general-purpose
source_repo: github/spec-kit
source_path: "presets/scaffold/commands/speckit.specify.md"
source_url: https://github.com/github/spec-kit/blob/HEAD/presets/scaffold/commands/speckit.specify.md
---
## User Input

```text
$ARGUMENTS
```

Given the feature description above:

1. **Create the feature branch** by running the script:
   - Bash: `{SCRIPT} --json --short-name "<short-name>" "<description>"`
   - The JSON output contains BRANCH_NAME and SPEC_FILE paths.

2. **Read the spec-template** to see the sections you need to fill.

3. **Write the specification** to SPEC_FILE, replacing the placeholders in each section
   (Overview, Requirements, Acceptance Criteria) with details from the user's description.

---

**Source:** [`github/spec-kit`](https://github.com/github/spec-kit) → `presets/scaffold/commands/speckit.specify.md`
