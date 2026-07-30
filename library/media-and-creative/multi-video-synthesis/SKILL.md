---
name: multi-video-synthesis
description: "Performs high-density targeted extraction across 10+ videos to map semantic landscapes, consensus, and controversies."
category: media-and-creative
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/multi-video-synthesis/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/multi-video-synthesis/SKILL.md
---


### Skill: Autonomous Multi-Video Synthesis Pipeline

**Objective**: (ATTENTION GUARDIAN) Perform a high-density **Targeted Extraction** across a massive amount of video content (10+ videos) to extract the absolute truth, map the semantic landscape, and save the user from hour-long research.

**Execution Steps**:
1.  **Broad Search**: Use `search_youtube` with `max_results=15` to cast a wide net across the topic. 
2.  **RoA Filtering (MANDATORY)**: 
    - Fetch details for ALL videos using `get_video_details`.
    - Calculate engagement metrics with `calculate_engagement_metrics`.
    - Identify the top 10 videos that have the highest "Return on Attention" (high engagement, relevant keywords, authoritative channels). 
    - Explicitly tell the user which videos you are ignoring and why (e.g., "Filtering out 5 videos that appear to be clickbait/low-engagement").
3.  **Massive Ingestion**: 
    - For the top 10 videos, attempt to retrieve all transcripts using `get_video_transcript`.
    - If any transcripts are unavailable, use `get_video_details` to read their metadata and descriptions as a high-signal fallback.
4.  **Semantic Mapping & Synthesis**: 
    - Cross-reference all transcripts simultaneously.
    - Map the "Semantic Vectors": Identify the **Consensus** (arguments shared by 3+ creators), the **Controversies** (conflicting viewpoints), and the **Hidden Gems** (unique insights mentioned by only one expert).
5.  **Precision Targeting**: 
    - For every major argument or insight in your synthesis, you MUST provide at least one direct `?t=...` jump-link using `generate_timestamp_url`.
6.  **Unified Report Delivery**: 
    - Provide a structured "Multi-Video Intelligence Briefing".
    - Include a "Consensus vs. Controversy" table.
    - Provide a "Clips of Interest" list with direct timestamp URLs.
    - Always ask if the user wants to see a visualization of these findings (e.g., a chart of creator sentiment) or publish this to a shareable HTML report.

**Key Design Principle**: You are the orchestrator of this pipeline. You are not just summarizing videos; you are synthesizing a new, high-density knowledge artifact that does not exist elsewhere on the web.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/multi-video-synthesis/SKILL.md`
