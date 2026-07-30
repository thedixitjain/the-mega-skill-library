---
name: publish
description: "1. Check git status - if untracked files exist: - Add obvious patterns to .gitignore (.log, .DSStore, nodemodules, dist, etc.) - If unclear (source files, configs), STOP and ask user 2. Build package (npm run build) - fix any errors 3. Bump patch version in package.json 4. Commit ALL changes, tag, push: git add -A && git commit -m \"v<version>\" && git tag v<version> && git push --follow-tags 5. Publish: npm publish --access public"
category: engineering-core
source_repo: badlogic/claude-commands
source_path: "publish.md"
source_url: https://github.com/badlogic/claude-commands/blob/HEAD/publish.md
---
1. Check git status - if untracked files exist:
   - Add obvious patterns to .gitignore (*.log, .DS_Store, node_modules, dist, etc.)
   - If unclear (source files, configs), STOP and ask user
2. Build package (`npm run build`) - fix any errors
3. Bump patch version in package.json
4. Commit ALL changes, tag, push: `git add -A && git commit -m "v<version>" && git tag v<version> && git push --follow-tags`
5. Publish: `npm publish --access public`

---

**Source:** [`badlogic/claude-commands`](https://github.com/badlogic/claude-commands) → `publish.md`
