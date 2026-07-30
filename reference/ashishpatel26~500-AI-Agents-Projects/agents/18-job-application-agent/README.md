<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/18-job-application-agent/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/18-job-application-agent/README.md`

# Job Application Agent

CrewAI agent that generates a complete job application package: cover letter, tailored resume bullets, interview questions, and salary range.

**Framework**: CrewAI  
**LLM**: GPT-4o-mini  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
# Uses built-in sample
python agent.py

# Your own job + profile
python agent.py \
  --job-desc "$(cat job_posting.txt)" \
  --candidate "$(cat my_profile.txt)"
```

## Output includes

- Tailored cover letter (250-300 words)
- Top 5 resume bullets to highlight
- 10 interview questions with answer frameworks
- Salary negotiation range
