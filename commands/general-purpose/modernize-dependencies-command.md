---
name: modernize-dependencies-command
description: "Update and modernize project dependencies"
allowed-tools: "Bash(npm *), Read"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/modernize-deps.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/modernize-deps.md
---


# Modernize Dependencies Command

Update and modernize project dependencies

## Instructions

Follow this approach to modernize dependencies: **$ARGUMENTS**

1. **Dependency Audit**
   ```bash
   # Check outdated packages
   npm outdated
   pip list --outdated
   composer outdated
   
   # Security audit
   npm audit
   pip-audit
   ```

2. **Update Strategy**
   - Start with patch updates (1.2.3 → 1.2.4)
   - Then minor updates (1.2.3 → 1.3.0)
   - Finally major updates (1.2.3 → 2.0.0)
   - Test thoroughly between each step

3. **Automated Updates**
   ```bash
   # Safe updates
   npm update
   pip install -U package-name
   
   # Interactive updates
   npx npm-check-updates -i
   ```

4. **Breaking Changes Review**
   - Read changelogs and migration guides
   - Identify deprecated APIs
   - Plan code changes needed
   - Update tests and documentation

5. **Testing and Validation**
   ```bash
   npm test
   npm run build
   npm run lint
   ```

6. **Documentation Updates**
   - Update README.md
   - Revise installation instructions
   - Update API documentation
   - Note breaking changes

Remember to update dependencies incrementally, test thoroughly, and maintain backward compatibility where possible.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/modernize-deps.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-project-setup/commands/modernize-deps.md`
