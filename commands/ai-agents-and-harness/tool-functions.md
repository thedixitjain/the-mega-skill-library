---
name: tool-functions
description: "Scaffold an A2A-compliant AG2 agent with server wiring, card settings, and skill definitions"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/new-a2a-agent.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/new-a2a-agent.md
---


You are scaffolding a new A2A-compliant AG2 agent for deployment as a standalone service.

## Instructions

1. Ask the user for:
   - Agent name and purpose
   - What tools/capabilities it needs
   - Authentication requirements (Bearer, OAuth2, none)
   - Skills the agent exposes (human-readable capabilities)
   - Whether it needs connector/token middleware

2. Create the agent following this exact structure:

### File Structure
```
agents/<agent-name>/
  <agent_name>.py    # Agent + tools + A2A server
  README.md          # Capabilities, setup, environment variables
```

### A2A Agent Code Pattern

```python
import json
import os
from autogen import ConversableAgent
from autogen.tools import tool
from a2a_agent_server import A2aAgentServer, CardSettings, Skill


# --- Tool Functions ---

@tool()
def example_tool(query: str) -> str:
    """Description of what this tool does.

    Args:
        query: The input query to process
    """
    try:
        result = {"items": [], "count": 0}
        return json.dumps({"success": True, "data": result})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


# --- Agent Definition ---

agent = ConversableAgent(
    name="AgentName",
    description="One-line description for discovery and routing",
    system_message="""You are a [role] specialist.

Your capabilities:
- [List specific capabilities]

When using tools:
- Always check the success field in tool responses
- If a tool fails, explain the error clearly to the user
- Never fabricate data -- only report what tools return
""",
    llm_config={"model": "gpt-4o-mini"},
    functions=[example_tool],
)


# --- A2A Server ---

server = A2aAgentServer(
    agent,
    url="http://0.0.0.0:8000/agent-name/",
    agent_card=CardSettings(
        organization="AG2 AI",
        version="1.0.0",
        capabilities=["capability_1", "capability_2"],
        authentication_schemes=["Bearer"],
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain", "application/json"],
        skills=[
            Skill(
                id="skill_one",
                description="Human-readable description of this skill",
                examples=["Example request that uses this skill"],
            ),
            Skill(
                id="skill_two",
                description="Another skill description",
                examples=["Another example request"],
            ),
        ],
    ),
).build()
```

### Mounting in main.py

Add to the AGENT_ROUTES dict:
```python
from agents.<agent_name>.<agent_name> import server as <agent_name>_server

AGENT_ROUTES = {
    # ... existing agents ...
    "<agent-name>": <agent_name>_server,
}
```

### Agent Card Discovery

Once mounted, the agent card is available at:
```
GET http://localhost:8000/<agent-name>/.well-known/agent.json
```

### Key Rules

- Agent URL path must match the agent name in kebab-case
- Skills should have 2-5 entries with clear examples
- Authentication schemes must match what middleware provides
- For connector-dependent agents, tools should return `connector_setup_required:<id>` on missing auth
- Always include a README.md documenting capabilities and required env vars
- Test agent card discovery before deploying

3. After scaffolding, mount the agent in main.py and verify the card endpoint works.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/new-a2a-agent.md`
