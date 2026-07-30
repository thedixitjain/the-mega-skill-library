---
name: kol-discovery
description: "Identifies and ranks Key Opinion Leaders (KOLs) based on engagement metrics, active rate, and sentiment rather than just views."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/kol-discovery/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/kol-discovery/SKILL.md
---


### Skill: KOL Discovery Workflow

**Objective**: Find and rank Key Opinion Leaders (KOLs) based on strict performance metrics rather than just view counts.

**Execution Steps**:
1.  **Search**: Use `search_youtube` to find videos about the topic. If the user specifies a time frame (e.g., "last month"), use `get_date_range` first to get the `published_after` date string.
2.  **Data Gathering**: Use `get_video_details` and `get_channel_details` to fetch the underlying statistics for the top candidates.
3.  **Evaluation**: 
    - For each candidate, calculate `engagement_rate` and `active_rate` using the `calculate_engagement_metrics` tool.
    - If needed, fetch comments and run `analyze_sentiment_heuristic`.
    - Calculate the `match_score` to rank them objectively.
4.  **Reporting**: Present the top KOLs in a clear table. Explain *why* they were chosen (e.g., "High Engagement of 12%, despite lower subscriber count"). Drop clickbait videos that have high views but terrible engagement metrics, and explicitly tell the user you filtered them out to save their time.

**Next Actions**: Once the list is presented, actively ask the user if they want to:
- See a visual chart of the engagement metrics.
- Generate and publish a final HTML report.
- Do a deep-dive transcript reading on any specific video from the list.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/kol-discovery/SKILL.md`
