---
name: test-file
description: "Generate comprehensive tests for a specific file"
allowed-tools: "Bash(find:*), Bash(ls:*)"
category: testing-and-qa
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/test-file/commands/test-file.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/test-file/commands/test-file.md
---


## Your task

Generate comprehensive unit tests for the file: @$ARGUMENTS

Requirements:
- Use the existing testing framework in this project
- Include edge cases and error scenarios
- Follow the project's testing conventions
- Aim for high test coverage
- Include both positive and negative test cases

## Project context

- Existing test files: !`find . -name "*.test.*" -o -name "*.spec.*" | head -10`
- Package.json testing setup: @package.json

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/test-file/commands/test-file.md`
