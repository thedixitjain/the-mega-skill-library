# CLI UX Testing Checklist

Use this checklist to ensure comprehensive testing of command-line interfaces.

## Pre-Testing Setup

- [ ] Identify the CLI tool name and version
- [ ] Locate documentation (README, man pages, --help)
- [ ] Identify target user personas (beginner, intermediate, expert)
- [ ] Set up test environment

## 1. Discovery & Discoverability

### Help System

- [ ] `command --help` works
- [ ] `command -h` works
- [ ] `command help` works
- [ ] `command` (bare, when no args required) shows help
- [ ] Help text is comprehensive
- [ ] Help text includes examples
- [ ] Help leads with examples (most valuable first)
- [ ] Subcommands have their own help (`command subcommand --help`)
- [ ] Context-aware help (suggests relevant commands based on state)

### Version Information

- [ ] `command --version` works
- [ ] `command -v` works (if applicable)
- [ ] Version format is clear (semantic versioning preferred)

### Documentation

- [ ] README exists and is clear
- [ ] Installation instructions are complete
- [ ] Usage examples are provided
- [ ] Common use cases are documented
- [ ] Troubleshooting guide exists
- [ ] Man pages exist (for system tools)

### Discovery Methods

- [ ] Tool explains itself when run without args
- [ ] Error messages suggest help commands
- [ ] Related commands are mentioned
- [ ] Next steps suggested after operations complete
- [ ] "Getting started" guidance provided for new users

## 2. Command & API Naming

### Naming Conventions

- [ ] Command names are intuitive
- [ ] Commands use verbs (create, delete, list, update)
- [ ] Topics use plural nouns (apps, users, config)
- [ ] One naming pattern chosen and used consistently (topic:command, topic command, or command topic)
- [ ] Root topic commands list items (e.g., `config` lists config, not `config:list`)
- [ ] Abbreviations are standard or explained
- [ ] Similar operations use similar names
- [ ] Names match user mental models
- [ ] Lowercase words, hyphens avoided unless necessary

### Flag Consistency

- [ ] Long flags use double dashes (`--flag`)
- [ ] Short flags use single dash (`-f`)
- [ ] Boolean flags don't require arguments
- [ ] Flag names are descriptive
- [ ] Common flags use standard names (`--verbose`, `--quiet`, `--force`, `--output`)
- [ ] `-h` reserved for help only (never used for other purposes)
- [ ] `-v` reserved for version only (use `--verbose` for verbosity)
- [ ] `--no-color` flag supported (and `NO_COLOR` env var)
- [ ] Flags preferred over positional arguments
- [ ] Secrets never passed via flags (use files or stdin)

### Subcommands

- [ ] Subcommands are clearly named
- [ ] Subcommand structure is consistent
- [ ] Subcommands are grouped logically

## 3. Error Handling & Messages

### Error Message Quality

- [ ] Errors are specific, not generic
- [ ] Errors explain what went wrong
- [ ] Errors explain why it's a problem
- [ ] Errors suggest how to fix
- [ ] Errors include who/what is responsible (tool vs user vs external)
- [ ] Errors include relevant context (file paths, line numbers)
- [ ] Errors don't expose internal implementation details
- [ ] Similar errors are grouped to reduce noise
- [ ] Typos suggest corrections ("Did you mean 'start'?")
- [ ] Input validated early (fail fast)

### Error Scenarios to Test

- [ ] Missing required arguments: `command`
- [ ] Invalid flag: `command --invalid-flag`
- [ ] File not found: `command nonexistent.txt`
- [ ] Permission denied: `command /protected/file`
- [ ] Invalid input format: `command malformed-input`
- [ ] Network errors (if applicable)
- [ ] Timeout errors (if applicable)

### Exit Codes

- [ ] Success returns 0
- [ ] General errors return 1
- [ ] Invalid arguments return 2
- [ ] Command cannot execute returns 126
- [ ] Command not found returns 127
- [ ] Terminated by Ctrl-C returns 130
- [ ] Custom error codes documented for specific failures
- [ ] Exit codes work correctly with shell operators (`&&`, `||`)
- [ ] Exit codes are documented

## 4. Help System & Documentation

### Help Text Structure

- [ ] Usage line shows syntax clearly
- [ ] Description explains purpose
- [ ] All options are documented
- [ ] Option descriptions are clear
- [ ] Examples are included
- [ ] Related commands are mentioned
- [ ] Links to more documentation provided

### Documentation Completeness

- [ ] All features are documented
- [ ] Edge cases are explained
- [ ] Configuration options are documented
- [ ] Environment variables are listed
- [ ] Limitations are mentioned

## 5. Consistency & Patterns

### Command Patterns

- [ ] Similar operations follow same pattern
- [ ] Flag order doesn't matter (where possible)
- [ ] Subcommand structure is consistent
- [ ] Input/output formats are consistent

### Default Behavior

- [ ] Defaults are sensible and safe
- [ ] Defaults are documented
- [ ] Defaults can be overridden
- [ ] Behavior without flags is predictable

### Configuration

- [ ] Config file locations are standard (XDG Base Directory)
- [ ] Config file format is clear (YAML, JSON, TOML, etc.)
- [ ] Environment variables follow naming convention (UPPERCASE_WITH_UNDERSCORES)
- [ ] Configuration precedence order is correct:
  - [ ] 1. Command-line flags (highest priority)
  - [ ] 2. Environment variables
  - [ ] 3. Project config (`.env`, `.tool-config`)
  - [ ] 4. User config (`~/.config/tool/`)
  - [ ] 5. System config (`/etc/tool/`)
- [ ] Config precedence is documented
- [ ] Config source shown in verbose/debug mode

## 6. Visual Design & Output

### Output Formatting

- [ ] Output is well-formatted
- [ ] Columns are aligned
- [ ] Tables have headers
- [ ] Tables are grep-parseable:
  - [ ] No decorative borders or box-drawing characters
  - [ ] One row per entry (no wrapped rows)
  - [ ] Consistent column alignment
  - [ ] Predictable delimiters
- [ ] Long outputs are paginated or truncated gracefully
- [ ] Machine-readable output available (`--json`, `--terse`, `--format`)
- [ ] Output respects 80-character terminal width where practical

### Color Usage

- [ ] Colors have semantic meaning
- [ ] Colors work on dark and light backgrounds
- [ ] Color can be disabled (`--no-color`)
- [ ] NO_COLOR environment variable is respected
- [ ] Critical info isn't color-only (accessible)

### Progress Indicators

- [ ] Progress indicators chosen based on duration:
  - [ ] <2 seconds: No indicator (feels instant)
  - [ ] 2-10 seconds: Spinner with description
  - [ ] >10 seconds: Progress bar with percentage and ETA
- [ ] Long operations show progress
- [ ] Spinners animate smoothly
- [ ] Progress bars update frequently
- [ ] What's happening is described ("Installing dependencies...")
- [ ] Progress count shown ("3/10 files processed")
- [ ] Estimated time is shown (if possible)
- [ ] Progress can be disabled for scripts
- [ ] Progress disabled automatically in non-TTY contexts

### Interactive Elements

- [ ] TTY detection works (only prompt when stdin is a TTY)
- [ ] Prompts are clear
- [ ] Default values are shown
- [ ] Prompts can be skipped with flags (`--no-input`, `--yes`)
- [ ] All required data accepted via flags for automation
- [ ] Confirmation prompts for destructive operations
- [ ] Ctrl+C exits gracefully
- [ ] Second Ctrl-C forces immediate exit
- [ ] Colors disabled in pipes/non-TTY contexts

## 7. Performance & Responsiveness

### Startup Performance

- [ ] `--help` is instant (<100ms)
- [ ] `--version` is instant (<100ms)
- [ ] Simple commands feel immediate (<500ms)
- [ ] Lazy loading is used for heavy dependencies

### Operation Performance

- [ ] Long operations show progress
- [ ] Streaming output for large data
- [ ] Incremental results when possible
- [ ] Timeouts are configurable
- [ ] Performance is acceptable for target use cases

### Resource Usage

- [ ] Memory usage is reasonable
- [ ] CPU usage is reasonable
- [ ] Disk I/O is efficient
- [ ] Network usage is efficient (if applicable)

## 8. Accessibility & Inclusivity

### Language & Communication

- [ ] Language is clear and simple
- [ ] Jargon is explained or avoided
- [ ] Examples use diverse contexts
- [ ] Error messages are helpful, not blaming

### Terminal Compatibility

- [ ] Works in different shells (bash, zsh, fish)
- [ ] Works with different terminal emulators
- [ ] Works in SSH/remote sessions
- [ ] Works with different terminal sizes
- [ ] Handles terminal resize gracefully

### Keyboard Accessibility

- [ ] All features are keyboard-accessible
- [ ] Tab completion works (if applicable)
- [ ] Arrow keys work in interactive modes
- [ ] Common keyboard shortcuts work (Ctrl+C, Ctrl+D)

### Different Skill Levels

- [ ] Beginners can accomplish basic tasks
- [ ] Experts have advanced options
- [ ] Progressive disclosure of complexity
- [ ] Good defaults for common use cases

## 9. Integration & Interoperability

### Shell Integration

- [ ] Tab completion available
- [ ] Works in pipes: `cat file | command | grep pattern`
- [ ] Respects stdin/stdout/stderr correctly:
  - [ ] Primary output goes to stdout
  - [ ] Errors, warnings, progress go to stderr
  - [ ] Accepts piped input from stdin
  - [ ] Enables composability with other tools
- [ ] Exit codes work with `&&` and `||`
- [ ] Output behaves correctly when redirected (`>`, `2>`, `2>&1`)

### Standard Conventions

- [ ] Follows POSIX conventions (where applicable)
- [ ] Respects standard environment variables:
  - [ ] `NO_COLOR` - Disables all colors
  - [ ] `DEBUG` - Enables debug output
  - [ ] `EDITOR` - User's preferred editor
  - [ ] `PAGER` - User's preferred pager
  - [ ] `TMPDIR` - Temporary directory
  - [ ] `HOME` - User home directory
  - [ ] `HTTP_PROXY`, `HTTPS_PROXY` - Proxy settings
- [ ] Tool-specific environment variables use UPPERCASE_WITH_UNDERSCORES
- [ ] Reads `.env` files for project-level config
- [ ] Uses standard config locations (XDG Base Directory)
- [ ] Works with standard tools (grep, awk, sed)

### Output Formats

- [ ] JSON output available
- [ ] YAML output available (if relevant)
- [ ] CSV output available (for tabular data)
- [ ] Plain text output available
- [ ] Format is selectable via flag

### Context Awareness

- [ ] Detects project type (package.json, Cargo.toml, go.mod, requirements.txt, etc.)
- [ ] Detects Git repository and current branch
- [ ] Detects environment indicators (NODE_ENV, etc.)
- [ ] Adapts defaults based on detected context
- [ ] Explains what was detected in output
- [ ] Provides override flags if detection is incorrect
- [ ] Works sensibly when no context detected

## 10. Security & Safety

### Destructive Operations

- [ ] Destructive ops require confirmation
- [ ] `--force` flag bypasses confirmation (documented)
- [ ] Dry-run mode available (`--dry-run`, `--whatif`)
- [ ] Backup options for destructive changes

### Credential Handling

- [ ] Credentials never in command history
- [ ] Credentials from env vars or config files
- [ ] Credentials not echoed to screen
- [ ] Secure defaults for permissions

### Input Validation

- [ ] Inputs are validated
- [ ] Input validated early (fail fast)
- [ ] SQL injection prevented (if applicable)
- [ ] Command injection prevented
- [ ] Path traversal prevented

## 11. User Guidance & Onboarding

### Next-Step Suggestions

- [ ] After init, suggests what to do next
- [ ] After successful operations, suggests related commands
- [ ] After errors, suggests how to fix or get help
- [ ] Suggestions are context-aware (3-5 suggestions max)
- [ ] Provides example commands users can copy
- [ ] Links to relevant documentation

### Getting Started

- [ ] First-time users can accomplish basic tasks easily
- [ ] `init` or `quickstart` command available
- [ ] Example workflows shown in help
- [ ] Common use cases are obvious
- [ ] Reduces time-to-first-value
- [ ] Doesn't require reading documentation to start

### Progressive Disclosure

- [ ] Basic features are simple
- [ ] Advanced features available but not overwhelming
- [ ] Help shows common commands first
- [ ] Detailed options shown with `--help` flag
- [ ] Expert mode available for power users

## Testing Notes

### Observations

[Space for notes during testing]

### Issues Found

[List specific issues with severity]

### Recommendations

[Specific improvements to suggest]

## Rating Summary

Rate each category 1-5:

- Discovery & Discoverability: ___/5
- Command & API Naming: ___/5
- Error Handling & Messages: ___/5
- Help System & Documentation: ___/5
- Consistency & Patterns: ___/5
- Visual Design & Output: ___/5
- Performance & Responsiveness: ___/5
- Accessibility & Inclusivity: ___/5

**Core 8-Criteria Score: ___/5** (average of above)

### Additional Criteria

- Integration & Interoperability: ___/5
- Security & Safety: ___/5
- User Guidance & Onboarding: ___/5

**Overall UX Score: ___/5** (weighted average emphasizing core 8 criteria)

## Next Steps

Based on findings:

1. [Priority 1 action item]
2. [Priority 2 action item]
3. [Priority 3 action item]
