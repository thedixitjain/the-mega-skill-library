---
name: runway-reference-architecture
description: "\"Runway reference architecture \\u2014 AI video generation and creative\\ \\ AI platform.\\nUse when working with Runway for video generation, image editing,\\ \\ or creative AI.\\nTrigger with phrases like \\\"runway reference architecture\\\",\\ \\ \\\"runway-reference-architecture\\\", \\\"AI video generation\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(pip:*), Bash(npm:*), Bash(curl:*), Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/runway-reference-architecture/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/runway-reference-architecture/SKILL.md
---

# Runway Reference Architecture

## Overview

Implementation patterns for Runway reference architecture — AI video generation platform.

## Prerequisites

- Completed `runway-install-auth` setup

## Instructions

### Step 1: SDK Pattern

```python
from runwayml import RunwayML

client = RunwayML()

task = client.image_to_video.create(
    model='gen3a_turbo',
    prompt_text='A serene lake at dawn, mist rising, birds flying',
    duration=5,
)
result = task.wait_for_task_output()
if result.status == 'SUCCEEDED':
    print(f"Video: {result.output[0]}")
```

## Output

- Runway integration for reference architecture

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Check RUNWAYML_API_SECRET |
| 402 Insufficient credits | No credits | Add credits at dev.runwayml.com |
| Task FAILED | Content policy | Adjust prompt |

## Resources

- [Runway API Documentation](https://docs.dev.runwayml.com/)
- [Python SDK](https://github.com/runwayml/sdk-python)

## Next Steps

See related Runway skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/runway-reference-architecture/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/runway-pack/skills/runway-reference-architecture/SKILL.md`
