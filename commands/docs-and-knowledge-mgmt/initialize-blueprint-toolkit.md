---
name: initialize-blueprint-toolkit
description: "Initialize СС Blueprint Toolkit - copy actual documentation templates to your project"
allowed-tools: "Bash, Read, Write"
category: docs-and-knowledge-mgmt
source_repo: croffasia/cc-blueprint-toolkit
source_path: "claude/commands/init.md"
source_url: https://github.com/croffasia/cc-blueprint-toolkit/blob/HEAD/claude/commands/init.md
---


# Initialize Blueprint Toolkit

Copy PRP templates and documentation from the Blueprint Toolkit to your current project.

## Installation Steps

Execute the following steps to set up the toolkit in your project:

### 1. Clone the toolkit repository
```bash
git clone https://github.com/croffasia/cc-blueprint-toolkit.git /tmp/cc-blueprint-toolkit-temp
```

### 2. Create documentation directories
```bash
mkdir -p docs/templates docs/prps docs/tasks
```

### 3. Copy templates to project
```bash
cp -r /tmp/cc-blueprint-toolkit-temp/docs/templates/* docs/templates/ && rm -rf /tmp/cc-blueprint-toolkit-temp
```

## Verification

After installation, verify the following files exist:
- `docs/templates/prp_document_template.md`
- `docs/templates/technical-task-template.md`
- `docs/templates/brainstorming_session_template.md`

## Success Message

Display to user:
```
✅ Blueprint Toolkit initialized successfully!

📁 Templates installed:
   → docs/templates/prp_document_template.md
   → docs/templates/technical-task-template.md
   → docs/templates/brainstorming_session_template.md

📂 Directories created:
   → docs/prps/     (for generated PRPs)
   → docs/tasks/    (for task breakdowns)

🚀 Ready to use:
   /brainstorm          - Start feature planning session
   /prp:generate        - Create implementation blueprint
   /prp:execute         - Execute PRP directly (simple features)
   /task:execute        - Execute task breakdown (complex features)

💡 Tip: Start with /brainstorm to explore your feature ideas,
   then use /prp:generate to create a detailed implementation plan.
```

---

**Source:** [`croffasia/cc-blueprint-toolkit`](https://github.com/croffasia/cc-blueprint-toolkit) → `claude/commands/init.md`
