---
name: observation
description: "<Observation> Execution Step: ({steps}/{maxsteps})"
category: ai-agents-and-harness
source_repo: Shubhamsaboo/awesome-llm-apps
source_path: "advanced_ai_agents/single_agent_apps/windows_use_autonomous_agent/windows_use/agent/prompt/observation.md"
source_url: https://github.com/Shubhamsaboo/awesome-llm-apps/blob/HEAD/advanced_ai_agents/single_agent_apps/windows_use_autonomous_agent/windows_use/agent/prompt/observation.md
---
```xml
<Observation>
Execution Step: ({steps}/{max_steps})

Action Response: {observation}

[Start of Desktop State]

Cursor Location: {cursor_location}

Foreground Application: {active_app}

Opened Applications:
{apps}

List of Interactive Elements:
{interactive_elements}

List of Scrollable Elements:
{scrollable_elements}

List of Informative Elements:
{informative_elements}

[End of Desktop State]

Note: Use the Done Tool if the task is completely over else continue solving.
</Observation>
```

---

**Source:** [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) → `advanced_ai_agents/single_agent_apps/windows_use_autonomous_agent/windows_use/agent/prompt/observation.md`
