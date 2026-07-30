---
name: code-review
description: "Review code changes for bugs, security issues, and improvements"
category: engineering-core
source_repo: TheDecipherist/claude-code-mastery
source_path: "commands/review.md"
source_url: https://github.com/TheDecipherist/claude-code-mastery/blob/HEAD/commands/review.md
---


# Code Review

Review the current changes systematically.

## 1. Get the Changes

```bash
git diff --staged
```

If nothing is staged, check unstaged changes:

```bash
git diff
```

## 2. Review Checklist

For each changed file, evaluate:

### Correctness
- [ ] Logic is correct and handles edge cases
- [ ] No off-by-one errors
- [ ] Null/undefined handled properly
- [ ] Async operations awaited correctly
- [ ] Error paths don't leave state inconsistent

### Security
- [ ] No hardcoded secrets or credentials
- [ ] User input is validated/sanitized
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Sensitive data not logged

### Performance
- [ ] No N+1 query patterns
- [ ] No unnecessary re-renders (React)
- [ ] Large lists are paginated or virtualized
- [ ] Expensive operations are memoized where appropriate

### Maintainability
- [ ] Code is readable without excessive comments
- [ ] No magic numbers (use constants)
- [ ] Functions do one thing
- [ ] No dead code

## 3. Output Format

For each issue found:

```
**[SEVERITY]** filename:line_number
Issue: <description>
Suggestion: <how to fix>
```

Severity levels:
- **CRITICAL** — Must fix before merge (security, data loss, crashes)
- **HIGH** — Should fix (bugs, performance issues)
- **MEDIUM** — Consider fixing (code smell, maintainability)
- **LOW** — Optional (style, minor improvements)

## 4. Summary

End with:
- Total issues by severity
- Overall assessment (approve / request changes)
- Any praise for well-written code

---

**Source:** [`TheDecipherist/claude-code-mastery`](https://github.com/TheDecipherist/claude-code-mastery) → `commands/review.md`
