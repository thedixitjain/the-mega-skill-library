---
name: product-launch-audit
description: "Provides an executive dashboard comparing Creator vs Audience verdicts for a recent client product launch."
category: security-and-compliance
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/product-launch-audit/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/product-launch-audit/SKILL.md
---


### Skill: Product Launch Audit (Seller's Ammunition)

**Objective**: Provide an internal Google Seller (e.g., Ads/Cloud rep) with a comprehensive audit of what Creators AND Audiences are saying about a specific client's product launch (e.g., a new game, phone, or software).

**Execution Steps**:
1.  **Locate**: Use `search_youtube` to find videos about the specific product launch. *Critically*, use `get_date_range` to filter for videos published within the launch window (e.g., `published_after` set to 7 or 14 days ago).
2.  **Creator Verdict (Ingest)**: Use `get_video_transcript` on the top 3 review videos to understand what the KOLs (Key Opinion Leaders) think. Are they praising the graphics? Complaining about the price?
3.  **Audience Verdict (Ingest)**: Use the `aggregate_comment_sentiment` tool on those same top video IDs. This tool pulls comments across all the videos at once. Synthesize what the actual consumers are saying in the comments. Does the audience agree with the creator?
4.  **Synthesize The Pitch**: Compare the Creator Verdict vs. the Audience Verdict. Identify the "Pitch Angle." (e.g., "The client needs to run an ad campaign emphasizing free-to-play mechanics because the audience incorrectly assumes it's expensive based on creator reviews").
5.  **Deliver**: Present an **Executive Dashboard** containing:
    *   **The Good**: 1-2 positive bullet points.
    *   **The Bad**: 1-2 negative bullet points.
    *   **The Pitch Angle**: How the seller can use this data in their client meeting.
    *   **Direct Proof**: Include 2-3 clickable timestamp links (`generate_timestamp_url`) backing up the summary.

**Next Actions**: Ask the user if they want to publish this Executive Dashboard as a clean HTML asset using `publish_file`.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/product-launch-audit/SKILL.md`
