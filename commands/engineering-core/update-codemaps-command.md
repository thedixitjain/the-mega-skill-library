---
name: update-codemaps-command
description: "Update codemaps for codebase navigation"
category: engineering-core
source_repo: affaan-m/ECC
source_path: ".opencode/commands/update-codemaps.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.opencode/commands/update-codemaps.md
---
# Update Codemaps Command

Update codemaps to reflect current codebase structure: $ARGUMENTS

## Your Task

Generate or update codemaps in `docs/CODEMAPS/` directory:

1. **Analyze codebase structure**
2. **Generate component maps**
3. **Document relationships**
4. **Update navigation guides**

## Codemap Types

### Architecture Map
```
docs/CODEMAPS/ARCHITECTURE.md
```
- High-level system overview
- Component relationships
- Data flow diagrams

### Module Map
```
docs/CODEMAPS/MODULES.md
```
- Module descriptions
- Public APIs
- Dependencies

### File Map
```
docs/CODEMAPS/FILES.md
```
- Directory structure
- File purposes
- Key files

## Codemap Format

### [Module Name]

**Purpose**: [Brief description]

**Location**: `src/[path]/`

**Key Files**:
- `file1.ts` - [purpose]
- `file2.ts` - [purpose]

**Dependencies**:
- [Module A]
- [Module B]

**Exports**:
- `functionName()` - [description]
- `ClassName` - [description]

**Usage Example**:
```typescript
import { functionName } from '@/module'
```

## Generation Process

1. Scan directory structure
2. Parse imports/exports
3. Build dependency graph
4. Generate markdown maps
5. Validate links

---

**TIP**: Keep codemaps updated when adding new modules or significant refactoring.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.opencode/commands/update-codemaps.md`
