---
name: sentiment-analysis
description: "Extracts the true audience mood and key feedback by analyzing comment sentiment and keyword frequency."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/sentiment-analysis/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/sentiment-analysis/SKILL.md
---


### Skill: Sentiment Analysis Workflow

**Objective**: Understand the true audience reaction to a video, product, or creator by analyzing comment sentiment.

**Execution Steps**:
1.  **Fetch Comments**: Use `get_video_comments` to pull the top 20-50 comments for the target video.
2.  **Analyze**: 
    - Use your own semantic understanding combined with `analyze_sentiment_heuristic` to gauge the overall mood (Positive/Neutral/Negative).
    - Extract the most frequently mentioned keywords, complaints, or praises.
3.  **Synthesize**: Do not just list the comments. Write a cohesive executive summary of *what the audience actually cares about*. 

**Next Actions**: Ask the user if they would like to visualize this sentiment data or publish it as a report.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/sentiment-analysis/SKILL.md`
