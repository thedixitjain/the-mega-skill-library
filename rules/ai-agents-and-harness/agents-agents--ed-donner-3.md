---
name: agents-agents
description: "The crew generates report.md containing: - Unified cleaned dataset with data quality notes - Probabilistic climate forecasts with uncertainty ranges - Risk heatmaps and critical threshold timelines - Prioritized intervention plan with cost/benefit analysis - Comprehensive final report with interactive mitigation map summary"
category: ai-agents-and-harness
source_repo: ed-donner/agents
source_path: "3_crewai/community_contributions/PrasadGaitonde/AGENTS.md"
source_url: https://github.com/ed-donner/agents/blob/HEAD/3_crewai/community_contributions/PrasadGaitonde/AGENTS.md
---
The crew generates `report.md` containing:
- Unified cleaned dataset with data quality notes
- Probabilistic climate forecasts with uncertainty ranges
- Risk heatmaps and critical threshold timelines
- Prioritized intervention plan with cost/benefit analysis
- Comprehensive final report with interactive mitigation map summary

### Running Locally

```bash
# Default (Mekong Delta)
crewai run

# Custom region - edit src/global_climate_modeling_local_mitigation/main.py
inputs = {'region': 'Your Region Here'}
```

### Configuration Files

- `config/agents.yaml` - Defines the 5 agents (team_lead, data_engineer, climate_modeler, impact_analyst, solution_architect)
- `config/tasks.yaml` - Defines 5 sequential tasks with region-specific variable interpolation
- `crew.py` - Crew orchestration class with @agent, @task, and @crew decorators
- `main.py` - Entry point with region input parameter

---

**Source:** [`ed-donner/agents`](https://github.com/ed-donner/agents) → `3_crewai/community_contributions/PrasadGaitonde/AGENTS.md`
