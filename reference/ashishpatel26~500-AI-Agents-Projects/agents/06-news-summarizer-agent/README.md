<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/06-news-summarizer-agent/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/06-news-summarizer-agent/README.md`

# News Summarizer Agent

Fetches news articles on any topic and produces a structured briefing with key themes and insights.

**Framework**: LangChain  
**LLM**: GPT-4o-mini  
**Data**: NewsAPI (optional — runs with mock data without a key)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python agent.py --topic "artificial intelligence"
python agent.py --topic "climate change" --count 10
```

Works without a NewsAPI key using sample data. For real news, get a free key at newsapi.org.
