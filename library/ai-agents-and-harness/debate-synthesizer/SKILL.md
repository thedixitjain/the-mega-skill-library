---
name: debate-synthesizer
description: "Extracts the strongest arguments from heated YouTube comment threads, identifying key battlegrounds and community consensus."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/debate-synthesizer/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/debate-synthesizer/SKILL.md
---


### Skill: The Debate Synthesizer (Controversy Resolution)

**Objective**: Extract the strongest arguments from both sides of a heated debate hidden in the YouTube comment section, saving the user from reading toxic or redundant threads.

**Execution Steps**:
1.  **Locate**: Use `search_youtube` to find highly polarizing videos on the requested topic (e.g., "React vs HTMX", "OpenClaw review"). 
2.  **Fetch Top Comments**: Use `get_video_comments` for the top 1 or 2 videos, setting the `order` parameter to "relevance".
3.  **Identify the Debate**: Look through the returned list of dictionaries. Find the 2 or 3 comments that have the *highest* `reply_count` (these are the battlegrounds).
4.  **Deep Dive (Fetch Replies)**: For those highly-replied comments, use the `get_comment_replies(comment_id)` tool to extract the actual arguments happening beneath the top-level comment.
5.  **Synthesize Arguments**: Analyze the replies. Group the distinct technical/logical points into "Pro" and "Con" categories. Aggressively ignore ad-hominem attacks, spam, or low-value agreements ("+1", "this").
6.  **Deliver**: Present a structured "Debate Brief". For each side, list the top 3 strongest arguments sourced from the community. Provide the video link.

**HTML Publishing Rule**: If the user asks to publish this report, you must construct a clean HTML page showcasing the "Pro vs Con" table. You can use `get_video_details` to embed the video's thumbnail image at the top of the report. You MUST publish the thumbnail image using `publish_file` first, or link directly to the high-res URL provided by the API.

**Next Actions**: Ask the user if they want to publish the Debate Brief as a shareable HTML report.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/debate-synthesizer/SKILL.md`
