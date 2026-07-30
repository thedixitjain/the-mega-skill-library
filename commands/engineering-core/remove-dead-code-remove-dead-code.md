---
name: remove-dead-code-remove-dead-code
description: "Safely remove identified dead code from the codebase."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/dead-code-finder/commands/remove-dead-code.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/dead-code-finder/commands/remove-dead-code.md
---
# /remove-dead-code - Remove Dead Code

Safely remove identified dead code from the codebase.

## Steps

1. Load the dead code report from the most recent analysis
2. Filter to high-confidence items only (unless user requests medium/low)
3. Group removals by file to minimize file operations
4. For each file, identify the dead code segments to remove
5. Check for side effects: does the dead code initialize anything or register handlers
6. Remove unused imports that result from removing dead code
7. Remove empty files if all exports are unused
8. Clean up empty directories if all files are removed
9. Run the project's linter to verify no new errors are introduced
10. Run the test suite to confirm nothing breaks
11. Generate a summary: files modified, lines removed, items removed
12. Create a git-friendly diff for review before committing

## Rules

- Only remove items flagged as high-confidence unless explicitly told otherwise
- Verify each removal does not break the build before proceeding to the next
- Keep a backup list of all removed items for potential restoration
- Do not remove code that has TODO or FIXME comments attached
- Remove associated tests only if the user explicitly requests it
- Process removals incrementally: one file at a time with validation
- Stop immediately if any test fails and report the causing removal

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/dead-code-finder/commands/remove-dead-code.md`
