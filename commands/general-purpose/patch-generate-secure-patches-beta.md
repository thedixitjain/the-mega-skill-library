---
name: patch-generate-secure-patches-beta
description: "Generate secure patches for vulnerabilities (beta)"
category: general-purpose
source_repo: gadievron/raptor
source_path: ".claude/commands/patch.md"
source_url: https://github.com/gadievron/raptor/blob/HEAD/.claude/commands/patch.md
---


# /patch - Generate Secure Patches (beta)

Generate secure patches to fix vulnerabilities.

**Requires:** SARIF file from previous /scan

**What it does:**
- Analyzes findings with LLM
- Generates secure patch code
- Saves to out/*/patches/
- Does NOT generate exploits (use /exploit for that)

**Run:** `python3 raptor.py agentic --repo <path> --no-exploits --max-findings <N>`

**Example:**
```bash
/scan test/                    # First, find vulnerabilities
/patch                         # Then, generate fixes for findings
```

**Note:** Review patches before applying to production code.

---

---

**Source:** [`gadievron/raptor`](https://github.com/gadievron/raptor) → `.claude/commands/patch.md`
