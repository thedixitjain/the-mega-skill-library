---
name: record-terminal
description: "Create terminal recordings with VHS tape scripts"
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/scry/commands/record-terminal.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/scry/commands/record-terminal.md
---


# /record-terminal

Record terminal sessions using VHS tape files for tutorials and documentation.

## Usage

```bash
/record-terminal <tape-file>           # Record from tape file
/record-terminal --init <name>         # Create new tape template
/record-terminal --validate <tape>     # Validate tape syntax
```

## Workflow

1. **Invoke skill**: `Skill(scry:vhs-recording)`
2. Follow the skill's workflow to:
   - Validate tape file exists
   - Check VHS installation
   - Execute recording
   - Verify GIF output

## Examples

```bash
# Record from existing tape
/record-terminal assets/tapes/quickstart.tape

# Create new tape template
/record-terminal --init demo

# Validate before recording
/record-terminal --validate assets/tapes/demo.tape
```

## See Also

- `Skill(scry:vhs-recording)` - Core recording skill
- `Skill(scry:gif-generation)` - Post-processing options
- VHS documentation: https://github.com/charmbracelet/vhs

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/scry/commands/record-terminal.md`
