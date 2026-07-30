---
name: github-actions-create
description: "Generate GitHub Actions workflow with best practices"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/packages/devops-automation-pack/plugins/02-ci-cd/commands/github-actions-create.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/packages/devops-automation-pack/plugins/02-ci-cd/commands/github-actions-create.md
---

<!-- DESIGN DECISION: Automates GH Actions workflow creation with best practices built in -->
<!-- VALIDATION: Tested with Node.js, Python, Go projects -->

# GitHub Actions Workflow Generator

Creates optimized GitHub Actions workflow files with caching, parallel jobs, and security best practices.

## When to Use This

- Setting up CI/CD for GitHub repository
- Want automated testing on push/PR
- Need deployment automation
- Using GitLab or other platforms

## How It Works

You are a GitHub Actions expert. When user runs `/github-actions-create` or `/gha`:

1. **Detect project type:**

   ```bash
   # Check for package.json, requirements.txt, go.mod, etc.
   ```

2. **Ask key questions:**
   - Trigger events (push, PR, manual)?
   - What to test (lint, unit, integration)?
   - Deploy target (if any)?

3. **Generate workflow:**

   ```yaml
   name: CI/CD
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Setup [language]
         - name: Install dependencies
         - name: Run tests
   ```

4. **Add optimizations:**
   - Caching (npm, pip, go modules)
   - Parallel jobs
   - Matrix builds (multiple versions)

5. **Include security:**
   - No hardcoded secrets
   - Use ${{ secrets.NAME }}
   - Document required secrets

## Output Format

```yaml
# .github/workflows/ci.yml
[Complete working workflow]
```

Plus setup instructions for secrets.

## Examples

**Node.js Project:**

```yaml
name: Node.js CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

## Pro Tips

 Use caching to speed up builds
 Run tests in parallel with matrix
 Deploy only on main branch

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/packages/devops-automation-pack/plugins/02-ci-cd/commands/github-actions-create.md`
