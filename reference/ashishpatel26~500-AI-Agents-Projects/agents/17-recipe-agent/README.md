<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/17-recipe-agent/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/17-recipe-agent/README.md`

# Recipe Recommendation Agent

Suggests 3 recipes from your available ingredients with full instructions, nutritional info, and chef tips.

**Framework**: LangChain  
**LLM**: GPT-4o-mini  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python agent.py --ingredients "chicken, garlic, lemon, rosemary"
python agent.py --ingredients "tofu, broccoli, ginger, soy sauce" --diet vegan --time 20
python agent.py --ingredients "pasta, tomatoes, basil, parmesan" --servings 4
```
