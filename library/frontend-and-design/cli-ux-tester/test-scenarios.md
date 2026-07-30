# CLI UX Test Scenarios

Common testing scenarios for evaluating command-line interface usability.

## Scenario 1: First-Time User

**Context**: A developer encounters your CLI for the first time.

**Test Flow**:

```bash
# What happens when they just run the command?
command

# Can they find help?
command --help
command help

# Can they discover the version?
command --version
```

**Evaluate**:

- Does the tool explain itself?
- Is help easy to find?
- Are next steps clear?
- Is there a getting started guide?

**Good Example**:

```bash
$ mytool

mytool - A tool for doing awesome things

Usage: mytool <command> [options]

Commands:
  init     Initialize a new project
  build    Build the project
  deploy   Deploy to production

Get started: mytool init
For help:    mytool --help
```

**Bad Example**:

```bash
$ mytool
Error: missing required argument
```

## Scenario 2: Missing Required Arguments

**Context**: User runs command without required arguments.

**Test Flow**:

```bash
# No arguments
command

# Some but not all arguments
command arg1

# Wrong argument types
command --flag=invalid
```

**Evaluate**:

- Error message specificity
- Suggested corrections
- Example usage shown
- Exit code is non-zero

**Good Example**:

```bash
$ deploy

Error: Missing required argument: <environment>

Usage: deploy <environment> [options]

Examples:
  deploy staging
  deploy production --tag v1.2.3

For more information: deploy --help
```

## Scenario 3: Invalid Flag or Option

**Context**: User provides an unrecognized flag.

**Test Flow**:

```bash
command --invalid-flag
command -x
command --typo
```

**Evaluate**:

- Does it suggest similar valid flags?
- Does it show available flags?
- Is the error clear about what's invalid?

**Good Example**:

```bash
$ build --optimze

Error: Unknown option '--optimze'

Did you mean '--optimize'?

Available options:
  --optimize    Enable optimizations
  --verbose     Show detailed output
  --output      Specify output directory

For more information: build --help
```

## Scenario 4: File Not Found

**Context**: User references a non-existent file.

**Test Flow**:

```bash
command nonexistent.txt
command --config missing.yml
command --input /path/does/not/exist
```

**Evaluate**:

- Shows the path that was checked
- Suggests alternatives if applicable
- Explains what file is needed and why

**Good Example**:

```bash
$ process --config app.yml

Error: Configuration file not found: 'app.yml'

Searched in:
  ./app.yml
  ~/.config/myapp/app.yml
  /etc/myapp/app.yml

To create a default config: myapp init --config
For more help: myapp --help
```

## Scenario 5: Permission Denied

**Context**: User lacks permissions for an operation.

**Test Flow**:

```bash
command /protected/file
command --output /system/file
sudo command  # If applicable
```

**Evaluate**:

- Clear about permission issue
- Suggests solution (sudo, chmod, etc.)
- Explains why permission is needed

**Good Example**:

```bash
$ install --global

Error: Permission denied to write to '/usr/local/bin'

This command requires elevated privileges.
Try: sudo install --global

Or install locally: install --user
```

## Scenario 6: Interactive Prompts

**Context**: Tool uses interactive prompts for input.

**Test Flow**:

```bash
# Run interactive command
command interactive-task

# Test with yes/no prompts
# Test with text input
# Test with selection menus
```

**Evaluate**:

- Prompts are clear
- Default values shown
- Can skip with flags for automation
- Ctrl+C exits gracefully

**Good Example**:

```bash
$ init

? Project name: (my-project) █
? Use TypeScript? (Y/n) Y
? Install dependencies? (Y/n) Y

✓ Created project 'my-project'
✓ Installed dependencies

Next steps:
  cd my-project
  npm start
```

## Scenario 7: Long-Running Operations

**Context**: Command takes significant time to complete.

**Test Flow**:

```bash
# Run operation that takes >2 seconds
command long-task

# Check for progress indication
# Test cancellation (Ctrl+C)
```

**Evaluate**:

- Progress indicator present
- Estimated time shown
- Can be cancelled gracefully
- Final summary shown

**Good Example**:

```bash
$ build

Building project...
[████████████████████████░░░░] 87% (43/50 files)
Estimated time remaining: 3s

✓ Build complete in 27s
  Output: dist/
  Size: 2.3 MB
```

## Scenario 8: Error Recovery

**Context**: Operation fails partway through.

**Test Flow**:

```bash
# Trigger partial failure
command complex-task  # That fails midway

# Check state after failure
# Try to resume or rollback
```

**Evaluate**:

- Clear about what failed
- State of partial completion
- How to recover or retry
- Rollback if destructive

**Good Example**:

```bash
$ deploy production

Deploying to production...
✓ Built assets
✓ Uploaded to CDN
✗ Database migration failed: Connection timeout

Error: Deployment partially complete

Completed:
  ✓ Build (commit abc123)
  ✓ CDN upload

Failed:
  ✗ Database migration

To retry: deploy production --resume
To rollback: deploy rollback
```

## Scenario 9: Configuration Files

**Context**: Tool uses configuration files.

**Test Flow**:

```bash
# Run without config
command

# Create config
command init --config

# Run with config
command --config custom.yml

# Invalid config
echo "invalid: ][" > bad.yml
command --config bad.yml
```

**Evaluate**:

- Config file location is clear
- Config format is documented
- Validation errors are helpful
- Can generate default config

**Good Example**:

```bash
$ run --config myconfig.yml

Error: Invalid configuration file 'myconfig.yml'

  Line 5: Unexpected token ']['

  Expected format:
    server:
      port: 3000
      host: localhost

To generate a default config: run init --config
For config docs: https://docs.example.com/config
```

## Scenario 10: Output Formats

**Context**: Tool provides multiple output formats.

**Test Flow**:

```bash
# Default output
command list

# Different formats
command list --format json
command list --format yaml
command list --format table
command list --format csv
```

**Evaluate**:

- Default format is human-readable
- Machine-readable formats available
- Format flag is consistent
- Output is valid in specified format

**Good Example**:

```bash
# Human-readable default
$ list
Users:
  - Alice (admin)
  - Bob (user)
  - Carol (user)

# Machine-readable
$ list --format json
{"users":[{"name":"Alice","role":"admin"},{"name":"Bob","role":"user"}]}

# Formatted JSON
$ list --format json --pretty
{
  "users": [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"}
  ]
}
```

## Scenario 11: Piping and Redirection

**Context**: Tool used in shell pipelines.

**Test Flow**:

```bash
# As input receiver
cat file.txt | command process

# As output producer
command generate | grep pattern

# Both
cat input.txt | command transform | grep result

# Output redirection
command > output.txt
command 2> errors.txt
command > output.txt 2>&1
```

**Evaluate**:

- Respects stdin/stdout/stderr
- Buffering is appropriate
- Exit codes work correctly
- Progress indicators disabled in pipes

**Good Example**:

```bash
# Interactive when TTY
$ transform data.txt
Processing... [████████] 100%
✓ Done

# Silent in pipes
$ transform data.txt | grep success
success: 42 records processed
```

## Scenario 12: Dry Run Mode

**Context**: User wants to preview changes.

**Test Flow**:

```bash
# Dry run
command dangerous-operation --dry-run
command dangerous-operation --whatif
command dangerous-operation --preview

# Check nothing actually changed
```

**Evaluate**:

- Dry run flag exists
- Shows what would happen
- No side effects occur
- Clear about simulation

**Good Example**:

```bash
$ delete --pattern "*.tmp" --dry-run

Dry run mode: No files will be deleted

Would delete:
  cache/temp1.tmp (2.3 MB)
  cache/temp2.tmp (1.1 MB)
  logs/debug.tmp (5.2 MB)

Total: 3 files, 8.6 MB

To execute: delete --pattern "*.tmp"
```

## Scenario 13: Tab Completion

**Context**: User expects tab completion in shell.

**Test Flow**:

```bash
# Install completions
command completion install

# Test completion
command <TAB>
command subcommand --<TAB>
```

**Evaluate**:

- Completion is available
- Installation is documented
- Completes commands
- Completes flags
- Completes file paths where relevant

## Scenario 14: Verbosity Levels

**Context**: User wants more or less output detail.

**Test Flow**:

```bash
# Quiet mode
command --quiet
command -q

# Verbose mode
command --verbose
command -v

# Debug mode
command --debug
```

**Evaluate**:

- Multiple verbosity levels
- Quiet suppresses all but essential
- Verbose shows helpful details
- Debug shows technical details

**Good Example**:

```bash
# Default
$ build
✓ Build complete

# Verbose
$ build --verbose
Compiling src/main.ts
Compiling src/utils.ts
Bundling...
Minifying...
✓ Build complete in 2.3s

# Debug
$ build --debug
[DEBUG] Config loaded from: ./config.yml
[DEBUG] Node version: 18.0.0
[DEBUG] Compiling src/main.ts
[DEBUG] AST parsed: 245 nodes
[DEBUG] Output size: 125 KB
✓ Build complete in 2.3s
```

## Scenario 15: Version Compatibility

**Context**: Tool versions change over time.

**Test Flow**:

```bash
# Check version
command --version

# Check for updates
command update --check

# Migrate from old version
```

**Evaluate**:

- Version clearly displayed
- Breaking changes documented
- Migration guides available
- Backward compatibility noted

## Scenario 16: Configuration Precedence

**Context**: Configuration from multiple sources (flags, env vars, files).

**Test Flow**:

```bash
# Test precedence order
echo "value: file" > .config
export TOOL_VALUE=env
command --value=flag

# Verify flag wins over env var
command --value=flag

# Verify env var wins over config file
unset TOOL_VALUE
export TOOL_VALUE=env
command

# Verify config file is used as fallback
unset TOOL_VALUE
command
```

**Evaluate**:

- Precedence order: flags > env vars > project config > user config > system config
- Each level documented
- Easy to debug which config is active
- Config source shown in verbose mode

**Good Example**:

```bash
$ mytool deploy --verbose
Using configuration from:
  --env flag: production (from command line)
  API_KEY: *** (from environment variable)
  timeout: 30s (from ~/.mytool/config.yml)
```

## Scenario 17: Exit Codes

**Context**: Shell scripts rely on meaningful exit codes.

**Test Flow**:

```bash
# Success
command successful-operation
echo $?  # Should be 0

# General error
command error-operation
echo $?  # Should be 1

# Invalid arguments
command --invalid-flag
echo $?  # Should be 2

# Use in shell scripts
command1 && command2  # Run command2 only if command1 succeeds
command1 || command2  # Run command2 only if command1 fails
```

**Evaluate**:

- 0 = success
- 1 = general error
- 2 = misuse (invalid arguments)
- 126 = command cannot execute
- 127 = command not found
- 130 = terminated by Ctrl-C
- Custom codes documented for specific errors

**Good Example**:

```bash
$ mytool validate file.txt
Error: Invalid file format
$ echo $?
3

# From documentation:
# Exit Codes:
#   0 - Success
#   1 - General error
#   2 - Invalid arguments
#   3 - Validation failed
#   4 - Network error
```

## Scenario 18: Environment Variable Support

**Context**: Standard environment variables affect behavior.

**Test Flow**:

```bash
# Test NO_COLOR
NO_COLOR=1 command
export NO_COLOR=1
command

# Test DEBUG
DEBUG=1 command --verbose

# Test tool-specific vars
MYTOOL_API_KEY=secret command
MYTOOL_TIMEOUT=60 command
```

**Evaluate**:

- NO_COLOR disables colors
- DEBUG enables debug output
- EDITOR used for editing operations
- PAGER used for long output
- HTTP_PROXY, HTTPS_PROXY respected
- Tool-specific vars use UPPERCASE_WITH_UNDERSCORES
- Environment variables documented

**Good Example**:

```bash
$ NO_COLOR=1 mytool status
Status: running  # No colors

$ DEBUG=1 mytool deploy
[DEBUG] Loading config from ~/.mytool/config.yml
[DEBUG] API endpoint: https://api.example.com
[DEBUG] Request: POST /deploy
Deploying...
```

## Scenario 19: Context Awareness

**Context**: Tool detects and adapts to project context.

**Test Flow**:

```bash
# In empty directory
cd /tmp/empty
command init

# In Node.js project
cd node-project/
command init  # Should detect package.json

# In Git repository
cd git-repo/
command deploy  # Should detect branch, commit

# In Python project
cd python-project/
command init  # Should detect requirements.txt or pyproject.toml
```

**Evaluate**:

- Detects project type (package.json, Cargo.toml, go.mod, etc.)
- Detects Git repository and current branch
- Adapts defaults based on context
- Explains what was detected
- Provides override flags if detection is wrong

**Good Example**:

```bash
$ cd my-node-app/
$ mytool init
✓ Detected Node.js project (package.json)
✓ Detected Git repository (branch: main)

Initializing with defaults:
  Runtime: Node.js 18
  Package manager: npm
  Deploy branch: main

To customize: mytool init --interactive
```

## Scenario 20: Grep-Parseable Output

**Context**: Output used in shell pipelines and scripts.

**Test Flow**:

```bash
# Test table output is grep-friendly
command list | grep "pattern"
command list | awk '{print $2}'
command list | cut -f1

# Check for decorative borders
command list  # Should not have === or box-drawing characters

# Verify one row per entry
command list | wc -l  # Should match number of items
```

**Evaluate**:

- No decorative borders or box-drawing characters
- One row per entry (no wrapped rows)
- Consistent column alignment
- Predictable delimiters
- Header row can be identified or skipped

**Good Example**:

```bash
# Good: Clean, parseable
$ mytool list
NAME        STATUS    PORT
api-server  running   3000
db-server   stopped   5432
cache       running   6379

$ mytool list | grep running | awk '{print $1}'
api-server
cache

# Bad: Decorative borders
$ badtool list
+------------+---------+------+
| NAME       | STATUS  | PORT |
+------------+---------+------+
| api-server | running | 3000 |
+------------+---------+------+
```

## Scenario 21: TTY Detection & Non-Interactive Mode

**Context**: Tool behaves differently in interactive vs script mode.

**Test Flow**:

```bash
# Interactive (TTY)
command deploy
# Should show prompts, colors, progress

# Non-interactive (pipe)
echo "yes" | command deploy
# Should not prompt, no colors

# Explicit non-interactive
command deploy --no-input
command deploy --yes

# In script
cat script.sh
#!/bin/bash
command deploy --env production --no-input
```

**Evaluate**:

- Detects when stdin is a TTY
- Prompts only when interactive
- --no-input flag disables all prompts
- Colors disabled in pipes (or when NO_COLOR set)
- Progress indicators disabled in non-TTY
- All required data accepted via flags

**Good Example**:

```bash
# Interactive
$ mytool deploy
? Select environment: (Use arrow keys)
❯ development
  staging
  production

# Non-interactive
$ mytool deploy --env production --no-input
Deploying to production...
✓ Deployed successfully

# In pipe (auto-detected)
$ echo "config" | mytool setup
Processing stdin input...
✓ Setup complete
```

## Scenario 22: Next-Step Suggestions

**Context**: After completing operations, users need guidance.

**Test Flow**:

```bash
# After init
command init

# After deploy
command deploy

# After error
command broken-operation

# After completion
command complete-task
```

**Evaluate**:

- Suggests logical next steps
- Provides example commands
- Links to relevant documentation
- Context-aware suggestions
- Not overwhelming (3-5 suggestions max)

**Good Example**:

```bash
$ mytool init
✓ Project initialized

Next steps:
  1. Configure API key: mytool config:set API_KEY=xxx
  2. Deploy to staging: mytool deploy --env staging
  3. View logs: mytool logs --follow

Learn more: https://docs.mytool.dev/quickstart

$ mytool deploy
✓ Deployed to production

View your app: https://myapp.production.com
View logs:     mytool logs --env production
Monitor:       mytool status --watch
Rollback:      mytool rollback
```

## Scenario 23: Root Command Patterns

**Context**: Root topic commands should list items, not require subcommands.

**Test Flow**:

```bash
# Test root topic
command config         # Should list all config
command apps           # Should list all apps
command users          # Should list all users

# Anti-pattern to check for
command config:list    # Redundant - should not exist
command apps:list      # Redundant - should not exist
```

**Evaluate**:

- Root topic lists items by default
- No redundant `:list` or `list` subcommand needed
- Consistent across all topics
- Matches user expectations (like `heroku config`)

**Good Example**:

```bash
# Good pattern
$ mytool config
API_KEY:    ***hidden***
TIMEOUT:    30s
REGION:     us-east-1

$ mytool config:set KEY=value
✓ Set KEY=value

# Bad pattern (avoid)
$ badtool config
Error: Missing subcommand

Usage: badtool config [list|set|get|delete]
```

## Testing Template

Use this template for each scenario:

```markdown
## Scenario: [Name]

**Commands Executed**:
[actual commands run]

**Observed Behavior**:
[what happened]

**Expected Behavior**:
[what should happen]

**Rating**: ___/5

**Issues**:

- [specific issue 1]
- [specific issue 2]

**Recommendations**:

- [specific improvement 1]
- [specific improvement 2]
```

## Summary

After testing all relevant scenarios:

1. **Most Common Issues**: [patterns observed]
2. **Best Aspects**: [what works well]
3. **Priority Fixes**: [top 3 improvements needed]
4. **Overall Usability**: ___/5
