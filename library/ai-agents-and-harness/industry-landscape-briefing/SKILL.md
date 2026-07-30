---
name: industry-landscape-briefing
description: "Equips sellers with macro industry trends by analyzing trending data and specific analyst/competitor channels."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/industry-landscape-briefing/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/industry-landscape-briefing/SKILL.md
---


### Skill: Industry Landscape Briefing (Seller's Radar)

**Objective**: Equip an internal Google Seller with high-level, macro trends in a specific industry (e.g., Mobile Gaming, Fintech) before they meet with a client. Go beyond keyword spam and find actual industry movements.

**Execution Steps**:
1.  **Time Context**: Determine the timeframe (e.g., `get_date_range("week")`).
2.  **Trending Analysis**: Use the `get_trending_videos` tool. Provide a relevant `video_category_id` (e.g., "20" for Gaming, "28" for Science/Tech) and a `region_code` relevant to the seller's market. What is naturally rising to the top?
3.  **Analyst Channel Audit**: (Optional but highly recommended). Ask the user if there is a specific industry "Analyst" or "B2B" channel they follow. If so, use `search_channel_videos` to pull exactly what that authority figure published this week.
4.  **Ingest (Read)**: Use `get_video_transcript` on the top 2-3 videos returned from Steps 2 and 3. Do not just read titles. Synthesize the actual industry shift being discussed.
5.  **Deliver**: Present an **Executive Dashboard** containing:
    *   **Macro Trend**: 1 sentence summary of the biggest industry shift this week.
    *   **Competitor Actions**: Are competitors mentioned in these videos? What are they doing?
    *   **Direct Proof**: Include 2-3 clickable timestamp links (`generate_timestamp_url`) to the exact moments the industry shifts are analyzed by creators.

**Next Actions**: Ask the user if they want to publish this Briefing as a clean HTML asset using `publish_file`.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/industry-landscape-briefing/SKILL.md`
