<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/11-stock-research-agent/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/11-stock-research-agent/README.md`

# Stock Research Agent

Fetches real-time stock data via Yahoo Finance and generates an AI-powered investment analysis.

**Framework**: LangChain  
**LLM**: GPT-4o-mini  
**Data**: Yahoo Finance (free, no API key needed)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python agent.py --ticker AAPL
python agent.py --ticker NVDA
python agent.py --ticker TSLA
```

## Output

Real-time fundamentals + AI analysis covering investment thesis, strengths, risks, valuation, and verdict.
