---
name: anonymize
description: "Implement data anonymization and pseudonymization for PII protection."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/data-privacy/commands/anonymize.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/data-privacy/commands/anonymize.md
---
Implement data anonymization and pseudonymization for PII protection.

## Steps


1. Identify data that needs anonymization:
2. Choose the anonymization technique:
3. Implement anonymization:
4. Build the anonymization pipeline:
5. Verify anonymization:
6. Automate the pipeline for recurring use.

## Format


```
Anonymization: <dataset or table>
Technique: <masking|pseudonymization|generalization>
Fields Processed:
  - <field>: <technique applied> (<example>)
```


## Rules

- Never use production data in development without anonymization.
- Pseudonymized data must not be reversible without the key.
- Maintain referential integrity across related tables.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/data-privacy/commands/anonymize.md`
