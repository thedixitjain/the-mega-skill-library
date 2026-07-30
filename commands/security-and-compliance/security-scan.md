---
name: security-scan
description: "Run the security scan gate before pushing."
category: security-and-compliance
source_repo: alirezarezvani/claude-skills
source_path: ".claude/commands/security-scan.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/.claude/commands/security-scan.md
---


1. Ensure dependencies are installed:
   ```bash
   pip install safety==3.2.4
   brew install gitleaks  # or appropriate package manager
   ```
2. Scan for committed secrets:
   ```bash
   gitleaks detect --verbose --redact
   ```
   - Resolve any findings before continuing.
3. Audit Python dependencies (if requirements files exist):
   ```bash
   for f in $(find . -name "requirements*.txt" 2>/dev/null); do
       safety check --full-report --file "$f"
   done
   ```
4. Record results in the commit template's Testing section.
5. After a clean pass, proceed with commit and push workflow.

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `.claude/commands/security-scan.md`
