---
name: test-command
description: "Simple test command for command parsing validation"
category: testing-and-qa
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "tests/e2e/fixtures/test-plugin/commands/test-command.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/tests/e2e/fixtures/test-plugin/commands/test-command.md
---


# Test Command

Simple slash command used for E2E testing of command parsing and execution.

## Usage

```
/test [options]
```

## Purpose

This command validates:
- Command file parsing
- Frontmatter extraction
- Shortcut registration
- Command metadata loading

## Options

- `--verbose` - Verbose output
- `--help` - Show help

## Examples

### Basic Usage

```
/test
```

Runs basic test validation.

### Verbose Mode

```
/test --verbose
```

Runs test with detailed output.

## Implementation

This command performs minimal operations to validate the command system:

1. Parse command arguments
2. Validate options
3. Execute test logic
4. Return results

## Expected Output

```
Test command executed successfully
Plugin: test-plugin
Version: 1.0.0
Status: OK
```

## Error Handling

If the command fails:
- Check plugin installation
- Verify command file exists
- Validate frontmatter format
- Ensure shortcut is unique

## Testing

This command is used exclusively in E2E tests:
- Plugin installation tests
- Command parsing tests
- Metadata validation tests

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `tests/e2e/fixtures/test-plugin/commands/test-command.md`
