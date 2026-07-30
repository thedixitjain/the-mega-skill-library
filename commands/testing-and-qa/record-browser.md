---
name: record-browser
description: "Record browser sessions using Playwright"
category: testing-and-qa
source_repo: athola/claude-night-market
source_path: "plugins/scry/commands/record-browser.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/scry/commands/record-browser.md
---


# /record-browser

Record browser sessions using Playwright specs for web UI tutorials.

> **💡 Claude Code 2.0.72+**: For interactive browser control, consider using native Chrome integration. This command is optimized for **automated recording workflows and CI/CD**. Both approaches can be combined - test interactively with Chrome, record programmatically with Playwright.

## Usage

```bash
/record-browser <spec-file>            # Record from Playwright spec
/record-browser --init <name>          # Create new spec template
/record-browser --config               # Show Playwright config
```

## Workflow

1. **Invoke skill**: `Skill(scry:browser-recording)`
2. Follow the skill's workflow to:
   - Validate Playwright installation
   - Check spec file exists
   - Execute recording with video
   - Convert to GIF using gif-generation

## Examples

```bash
# Record from existing spec
/record-browser specs/dashboard-demo.spec.ts

# Create new spec template
/record-browser --init login-flow

# Check Playwright config
/record-browser --config
```

## Requirements

- Node.js and npm
- Playwright: `npm install -D @playwright/test`
- Browsers: `npx playwright install chromium`

## See Also

- `Skill(scry:browser-recording)` - Core recording skill
- `Skill(scry:gif-generation)` - Video to GIF conversion
- Playwright docs: https://playwright.dev/

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/scry/commands/record-browser.md`
