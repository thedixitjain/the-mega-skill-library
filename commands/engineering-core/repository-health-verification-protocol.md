---
name: repository-health-verification-protocol
description: "Sets up and manages Husky Git hooks by configuring pre-commit hooks, establishing commit message standards, integrating with linting tools, and ensuring code quality on commits."
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/husky/commands/husky.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/husky/commands/husky.md
---


# Repository Health Verification Protocol

This command outlines a comprehensive protocol for verifying and maintaining a repository's health.

## Key Goals
- Verify repo is in a working state
- Run CI checks
- Fix any identified issues
- Prepare files for staging

## Main Steps
1. Update dependencies with `pnpm i`
2. Run linter checks
3. Verify builds and types
4. Run test coverage
5. Sort package.json
6. Lint packages
7. Double-check all previous steps
8. Stage files (avoiding git submodules)

## Error Handling Protocol
1. Explain why something broke
2. Propose and implement a fix
3. Check for similar issues elsewhere
4. Clean up debugging code

## Important Guidelines
- Never commit, only stage files
- Run tests package-by-package
- Be willing to make necessary fixes
- Use typescript and tests as safeguards

The document emphasizes a methodical approach to maintaining code quality and resolving issues systematically.

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/husky/commands/husky.md`
