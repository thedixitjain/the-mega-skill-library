---
name: define-specialist-agents
description: "Create a multi-agent group chat with AG2 using configurable speaker selection patterns"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/group-chat.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/group-chat.md
---


You are creating an AG2 multi-agent group chat workflow. Follow these patterns exactly.

## Instructions

1. Ask the user for:
   - What task the group needs to solve
   - How many agents and their specializations
   - Speaker selection pattern: auto (LLM picks), round_robin, or manual handoff
   - Maximum conversation rounds (default: 10)
   - Termination condition

2. Create the group chat following this pattern:

### Group Chat Pattern

```python
from autogen import ConversableAgent, GroupChat, GroupChatManager

# --- Define Specialist Agents ---

researcher = ConversableAgent(
    name="Researcher",
    description="Finds and synthesizes information",
    system_message="""You are a research specialist.
- Search for relevant information
- Summarize findings clearly
- Cite sources when possible
When your research is complete, say TERMINATE.""",
    llm_config={"model": "gpt-4o-mini"},
)

analyst = ConversableAgent(
    name="Analyst",
    description="Analyzes data and draws conclusions",
    system_message="""You are an analytical specialist.
- Analyze information provided by other agents
- Identify patterns and insights
- Provide evidence-based conclusions""",
    llm_config={"model": "gpt-4o-mini"},
)

writer = ConversableAgent(
    name="Writer",
    description="Drafts clear, structured output",
    system_message="""You are a writing specialist.
- Take research and analysis from other agents
- Produce clear, well-structured output
- When the final output is ready, say TERMINATE.""",
    llm_config={"model": "gpt-4o-mini"},
)

# --- Configure Group Chat ---

group_chat = GroupChat(
    agents=[researcher, analyst, writer],
    messages=[],
    max_round=10,
    speaker_selection_method="auto",  # "auto", "round_robin", "random", or callable
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"model": "gpt-4o-mini"},
)

# --- Run the Group Chat ---

result = researcher.initiate_chat(
    manager,
    message="Your task description here",
)
```

### Speaker Selection Options

- **auto**: LLM decides who speaks next based on conversation context (most flexible)
- **round_robin**: Agents take turns in order (predictable, good for pipelines)
- **random**: Random agent selection (useful for brainstorming)
- **callable**: Custom function `def select_speaker(last_speaker, groupchat) -> Agent`

### Termination Patterns

```python
# Option 1: Keyword termination (default)
# Any agent says "TERMINATE" in their response

# Option 2: Max rounds
group_chat = GroupChat(agents=agents, max_round=5)

# Option 3: Custom termination function
def is_termination(msg):
    content = msg.get("content", "")
    return "FINAL ANSWER:" in content

group_chat = GroupChat(
    agents=agents,
    is_termination_msg=is_termination,
)
```

### Key Rules

- Each agent needs a distinct `name` and `description` (used for speaker selection)
- System messages should clarify the agent's role within the group
- At least one agent should know when to say TERMINATE
- Use `speaker_selection_method="auto"` unless you have a specific reason not to
- Keep max_round reasonable (5-15) to avoid runaway conversations
- The manager agent handles routing -- don't add routing logic to individual agents

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/group-chat.md`
