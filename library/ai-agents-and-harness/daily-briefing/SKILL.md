---
name: daily-briefing
description: "Provides a high-signal briefing on events in a specific location and timeframe, backed by primary video sources and transcripts."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/daily-briefing/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/daily-briefing/SKILL.md
---


### Skill: What Matters Today (Location & Time Briefing)

**Objective**: Provide a highly relevant, high-signal briefing on events happening in a specific location within a specific timeframe (e.g., "the past 24 hours in Hong Kong"), backed by primary video sources.

**Execution Steps**:
1.  **Time Context**: Use `get_current_date_time` and `get_date_range` (or calculate it yourself if the user asks for exactly 24 hours) to determine the exact RFC 3339 timestamp for the cutoff.
2.  **Locate**: Use `search_youtube` to find news or vlogs about the location. 
    *   **CRITICAL**: You MUST aggressively apply the advanced filters. Pass the date from step 1 into `published_after`. Pass the relevant country code to `region_code` (e.g., 'HK' for Hong Kong). If appropriate, filter by `relevance_language`.
3.  **Filter & Rank**: Use `get_video_details` and `calculate_engagement_metrics` to fetch the views and engagement stats for these breaking videos. 
    *   *Action*: Discard low-engagement spam, auto-generated news bot channels, or clickbait. Only keep highly relevant, verified, or viral news sources with strong engagement.
4.  **Ingest (Optional but Preferred)**: Use `get_video_transcript` on the top 2-3 news clips to "read" the actual news story. Do not rely solely on clickbait titles.
5.  **Deliver**: Present a structured "Daily Briefing". Summarize the 3-5 key events that happened in that location. For each event, provide a 2-sentence summary and the direct link to the source video (or a timestamped URL if the news segment is part of a longer broadcast).

**Next Actions**: Ask the user if they want to dive deeper into any specific news story by pulling its comments/sentiment, or if they want to publish the briefing as an HTML report.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/daily-briefing/SKILL.md`
