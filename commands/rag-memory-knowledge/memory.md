---
name: memory
description: "{ \"name\": \"memory\", \"description\": \"Update the project memory with what was accomplished in this session\", \"prompt\": \"Update the project memory file at .claude/PROJECTMEMORY.md with a summary of everything that was done in this session. Include:\\n1. What features were added or changed\\n2. What bugs were fixed\\n3. What decisions were made\\n4. What is still TODO\\n5. Update version history if applicable\\n\\nRead the current PROJECTMEMORY.md first, then update it preserving all existing information while adding the new session's work.\""
category: rag-memory-knowledge
source_repo: 0xSteph/pentest-ai-agents
source_path: "commands/memory.md"
source_url: https://github.com/0xSteph/pentest-ai-agents/blob/HEAD/commands/memory.md
---
{
  "name": "memory",
  "description": "Update the project memory with what was accomplished in this session",
  "prompt": "Update the project memory file at .claude/PROJECT_MEMORY.md with a summary of everything that was done in this session. Include:\n1. What features were added or changed\n2. What bugs were fixed\n3. What decisions were made\n4. What is still TODO\n5. Update version history if applicable\n\nRead the current PROJECT_MEMORY.md first, then update it preserving all existing information while adding the new session's work."
}

---

**Source:** [`0xSteph/pentest-ai-agents`](https://github.com/0xSteph/pentest-ai-agents) → `commands/memory.md`
