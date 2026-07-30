---
name: context-prime
description: "Load project context by reading README.md and exploring relevant project files"
allowed-tools: "Read, Bash(git *)"
category: docs-and-knowledge-mgmt
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/context-prime.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/context-prime.md
---


Read README.md, THEN run `git ls-files | grep -v -f (sed 's|^|^|; s|$|/|' .cursorignore | psub)` to understand the context of the project

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/context-prime.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-context-loading-priming/commands/context-prime.md`
