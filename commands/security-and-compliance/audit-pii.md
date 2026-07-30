---
name: audit-pii
description: "Scan the codebase and data stores for personally identifiable information (PII) exposure risks."
category: security-and-compliance
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/data-privacy/commands/audit-pii.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/data-privacy/commands/audit-pii.md
---
Scan the codebase and data stores for personally identifiable information (PII) exposure risks.

## Steps


1. Define PII categories to scan for:
2. Scan source code:
3. Scan configuration:
4. Check data flow:
5. Verify protection measures:
6. Generate a PII inventory map.
7. Recommend remediation for each exposure risk.

## Format


```
PII Audit: <project>
PII Types Found: <list>
Exposure Risks:
  [HIGH] <location>: <PII type> - <risk description>
```


## Rules

- Treat all personal data as sensitive until classified otherwise.
- Check test data and fixtures for real PII from production.
- Log access to PII for audit compliance.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/data-privacy/commands/audit-pii.md`
