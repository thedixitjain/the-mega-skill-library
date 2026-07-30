---
name: workflow-from-spec
description: "Design a complete multi-agent workflow from a natural language description, selecting the right orchestration pattern"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/workflow-from-spec.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/workflow-from-spec.md
---


You are designing a complete AG2 multi-agent workflow from a user's specification.

## Instructions

1. Ask the user to describe their workflow goal in plain language. Then analyze:
   - How many distinct roles/specializations are needed?
   - Do agents need to collaborate (group chat) or work in sequence (pipeline)?
   - Does any agent need external tools or API access?
   - What's the expected input and output?

2. Select the orchestration pattern:

### Pattern Selection Guide

| Scenario | Pattern | Why |
|----------|---------|-----|
| Agents need to discuss and build on each other's ideas | Group Chat (auto) | LLM picks best next speaker |
| Fixed processing pipeline (A -> B -> C) | Sequential | Predictable flow |
| Each agent works independently, results merged | Fan-out/Fan-in | Parallel processing |
| One coordinator delegates to specialists | Hub-and-spoke | Central routing |
| Iterative refinement (draft -> review -> revise) | Two-agent loop | Focused improvement |

3. Generate the full implementation:

### Two-Agent Loop (Iterative Refinement)

```python
from autogen import ConversableAgent

creator = ConversableAgent(
    name="Creator",
    system_message="You draft content based on requirements. Incorporate feedback from the Reviewer.",
    llm_config={"model": "gpt-4o-mini"},
)

reviewer = ConversableAgent(
    name="Reviewer",
    system_message="""You review drafts critically.
- If the draft meets requirements, respond with: APPROVE
- Otherwise, provide specific, actionable feedback""",
    llm_config={"model": "gpt-4o-mini"},
)

result = creator.initiate_chat(
    reviewer,
    message="Create a [specification here]",
    max_turns=4,  # Max 2 revision cycles
)
```

### Hub-and-Spoke (Coordinator + Specialists)

```python
from autogen import ConversableAgent

coordinator = ConversableAgent(
    name="Coordinator",
    system_message="""You coordinate work between specialists.
- Analyze the request and determine which specialist(s) to engage
- Synthesize responses from specialists into a final answer
- Available specialists: [list them]""",
    llm_config={"model": "gpt-4o-mini"},
)

specialist_a = ConversableAgent(
    name="SpecialistA",
    system_message="You handle [domain A]. Respond only about your expertise.",
    llm_config={"model": "gpt-4o-mini"},
)

specialist_b = ConversableAgent(
    name="SpecialistB",
    system_message="You handle [domain B]. Respond only about your expertise.",
    llm_config={"model": "gpt-4o-mini"},
)

# Use nested chats for hub-and-spoke
coordinator.register_nested_chats(
    [
        {"recipient": specialist_a, "max_turns": 1, "summary_method": "last_msg"},
        {"recipient": specialist_b, "max_turns": 1, "summary_method": "last_msg"},
    ],
    trigger=lambda sender: True,  # Always consult specialists
)
```

### Key Rules

- Start with the simplest pattern that solves the problem
- Prefer 2-3 agents over 5+ agents -- complexity grows fast
- Every agent must have a clear termination condition
- Test with a simple input before adding complexity
- Document the workflow with a diagram in comments

4. After generating, walk through the data flow to verify correctness.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/workflow-from-spec.md`
