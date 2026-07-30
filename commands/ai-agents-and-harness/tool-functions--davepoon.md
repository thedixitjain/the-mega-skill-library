---
name: tool-functions
description: "Scaffold a new AG2 ConversableAgent with tool functions, system prompt, and LLM config"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/new-agent.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/new-agent.md
---


You are scaffolding a new AG2 (AutoGen) agent. Follow the AG2 framework patterns exactly.

## Instructions

1. Ask the user for:
   - Agent name and purpose
   - What tools/capabilities it needs
   - Which LLM model to use (default: gpt-4o-mini)
   - Whether it needs external API access

2. Create the agent following this exact structure:

### File Structure
```
agents/<agent-name>/
  <agent_name>.py    # Agent definition + tools
  README.md          # Capabilities documentation
```

### Agent Code Pattern

```python
import json
from autogen import ConversableAgent
from autogen.tools import tool

# --- Tool Functions ---
# Each tool returns a JSON string with {"success": bool, "data": ..., "error": ...}

@tool()
def tool_name(param1: str, param2: int = 10) -> str:
    """Clear description of what this tool does.

    Args:
        param1: Description of param1
        param2: Description of param2 (default: 10)
    """
    try:
        # Implementation
        result = {"key": "value"}
        return json.dumps({"success": True, "data": result})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


# --- Agent Definition ---
agent = ConversableAgent(
    name="AgentName",
    description="One-line description for orchestrator routing",
    system_message="""You are a [role description].

Your capabilities:
- Capability 1
- Capability 2

Guidelines:
- Always use the appropriate tool for the task
- Return structured responses
- Handle errors gracefully and explain what went wrong
""",
    llm_config={"model": "gpt-4o-mini"},
    functions=[tool_name],
)
```

### Key Rules

- Tool functions MUST return JSON strings, not dicts or raw values
- Tool functions MUST have docstrings (used for LLM function calling schema)
- System messages should be specific about the agent's role and boundaries
- Agent `description` is used by orchestrators to route tasks -- keep it concise
- Use `@tool()` decorator from `autogen.tools`
- Group related tools in the same file
- Never use bare `except:` -- always catch specific exceptions or `Exception`

3. After scaffolding, verify the code is syntactically valid and all imports exist.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/new-agent.md`
