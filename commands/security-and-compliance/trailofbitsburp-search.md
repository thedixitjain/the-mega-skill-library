---
name: trailofbitsburp-search
description: "Searches Burp Suite project files for security analysis"
allowed-tools: "Bash Read"
category: security-and-compliance
source_repo: trailofbits/skills
source_path: "plugins/burpsuite-project-parser/commands/burp-search.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/burpsuite-project-parser/commands/burp-search.md
---


# Search Burp Suite Project Files

**Arguments:** $ARGUMENTS

Parse arguments:
1. **Burp file** (required): Path to .burp project file
2. **Operation** (optional): `auditItems`, `proxyHistory.*`, `responseHeader='...'`, `responseBody='...'`

Invoke the `burpsuite-project-parser` skill with these arguments for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/burpsuite-project-parser/commands/burp-search.md`
