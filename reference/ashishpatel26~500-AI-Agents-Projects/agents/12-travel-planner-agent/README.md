<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/12-travel-planner-agent/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/12-travel-planner-agent/README.md`

# Travel Planner Agent

Three-agent CrewAI system that creates personalized travel itineraries with destination research, day-by-day plans, and budget breakdown.

**Framework**: CrewAI  
**LLM**: GPT-4o-mini  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python agent.py --destination "Tokyo, Japan" --days 7 --budget 3000
python agent.py --destination "Paris, France" --days 5 --budget 5000 --interests "art, wine, architecture"
```
