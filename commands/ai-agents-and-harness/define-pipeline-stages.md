---
name: define-pipeline-stages
description: "Create a sequential multi-agent pipeline where each agent processes and passes results to the next"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/sequential-workflow.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/sequential-workflow.md
---


You are creating a sequential AG2 agent pipeline. Each agent processes output from the previous one.

## Instructions

1. Ask the user for:
   - The pipeline stages and what each does
   - Whether any stage needs tools
   - Input/output format expectations
   - Error handling: stop on failure or continue?

2. Create the sequential workflow:

### Sequential Pipeline Pattern

```python
from autogen import ConversableAgent

# --- Define Pipeline Stages ---

stage_1 = ConversableAgent(
    name="Extractor",
    description="Extracts structured data from raw input",
    system_message="""You extract structured data from the input.

Output format: JSON with the extracted fields.
Always output valid JSON. Do not include explanations outside the JSON block.""",
    llm_config={"model": "gpt-4o-mini"},
)

stage_2 = ConversableAgent(
    name="Transformer",
    description="Transforms and enriches extracted data",
    system_message="""You receive extracted data and transform it.

- Normalize formats
- Enrich with derived fields
- Validate completeness

Output format: JSON with transformed data.""",
    llm_config={"model": "gpt-4o-mini"},
)

stage_3 = ConversableAgent(
    name="Reporter",
    description="Generates a human-readable report from processed data",
    system_message="""You receive processed data and create a clear report.

- Summarize key findings
- Highlight anomalies
- Provide actionable recommendations""",
    llm_config={"model": "gpt-4o-mini"},
)

# --- Run Sequential Pipeline ---

# Stage 1: Extract
result_1 = stage_1.initiate_chat(
    stage_2,
    message="Raw input data here...",
    max_turns=1,  # Single exchange per stage
)

# Stage 2 -> Stage 3: Transform and Report
result_2 = stage_2.initiate_chat(
    stage_3,
    message=result_1.summary,  # Pass output forward
    max_turns=1,
)

# Final output
final_report = result_2.summary
```

### Pipeline with Validation Gate

```python
# Add a validation step between stages
validator = ConversableAgent(
    name="Validator",
    description="Validates data quality between pipeline stages",
    system_message="""You validate the data passed to you.

Check for:
- Required fields present
- Data types correct
- Values within expected ranges

If valid, respond with: VALID: <the original data>
If invalid, respond with: INVALID: <description of issues>""",
    llm_config={"model": "gpt-4o-mini"},
)

# Run with validation
result = stage_1.initiate_chat(validator, message=input_data, max_turns=1)

if "VALID:" in result.summary:
    # Continue pipeline
    stage_2.initiate_chat(stage_3, message=result.summary, max_turns=1)
else:
    # Handle validation failure
    print(f"Pipeline stopped: {result.summary}")
```

### Key Rules

- Use `max_turns=1` for clean handoffs between stages
- Each stage should have clear input/output format expectations in its system message
- Use `result.summary` to pass output between stages
- Consider adding validation gates for critical pipelines
- Keep each stage focused on one transformation

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/sequential-workflow.md`
