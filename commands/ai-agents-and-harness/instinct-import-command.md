---
name: instinct-import-command
description: "Import instincts from external sources"
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: ".opencode/commands/instinct-import.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.opencode/commands/instinct-import.md
---
# Instinct Import Command

Import instincts from a file or URL: $ARGUMENTS

## Your Task

Import instincts into the continuous-learning-v2 system.

## Import Sources

### File Import
```
/instinct-import path/to/instincts.json
```

### URL Import
```
/instinct-import https://example.com/instincts.json
```

### Team Share Import
```
/instinct-import @teammate/instincts
```

## Import Format

Expected JSON structure:

```json
{
  "instincts": [
    {
      "trigger": "[situation description]",
      "action": "[recommended action]",
      "confidence": 0.7,
      "category": "coding",
      "source": "imported"
    }
  ],
  "metadata": {
    "version": "1.0",
    "exported": "2025-01-15T10:00:00Z",
    "author": "username"
  }
}
```

## Import Process

1. **Validate format** - Check JSON structure
2. **Deduplicate** - Skip existing instincts
3. **Adjust confidence** - Reduce confidence for imports (×0.8)
4. **Merge** - Add to local instinct store
5. **Report** - Show import summary

## Import Report

```
Import Summary
==============
Source: [path or URL]
Total in file: X
Imported: Y
Skipped (duplicates): Z
Errors: W

Imported Instincts:
- [trigger] (confidence: 0.XX)
- [trigger] (confidence: 0.XX)
...
```

## Conflict Resolution

When importing duplicates:
- Keep higher confidence version
- Merge application counts
- Update timestamp

---

**TIP**: Review imported instincts with `/instinct-status` after import.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.opencode/commands/instinct-import.md`
