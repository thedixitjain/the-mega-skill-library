---
name: deep-exploration
description: "Saves time by autonomously reading transcripts, synthesizing arguments, and generating direct jump-links to key moments."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/deep-exploration/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/deep-exploration/SKILL.md
---


### Skill: Deep Exploration & Timestamp Targeting

**Objective**: Save the user from watching hours of video by autonomously reading transcripts, synthesizing the core arguments, and generating direct jump-links to the exact moments of interest.

**Execution Steps**:
1.  **Locate**: Use `search_youtube` to find 3 to 5 highly relevant videos on the specific query. Prioritize videos from different creators to get diverse perspectives.
2.  **Ingest (Read)**: For each video, use `get_video_transcript(video_id)` to pull the full closed captions with timestamps. 
    *   *Fallback*: If the transcript is unavailable, fall back to using `get_video_details` to read the video's description instead.
3.  **Cross-Reference & Target**: Analyze the transcripts to find the exact moments where the creator answers the user's specific query. 
4.  **Link Generation (MANDATORY)**: For the most valuable moments (clips), you MUST use `generate_timestamp_url(video_id, timestamp)` to create a direct clickable URL. Do NOT try to guess the `?t=` parameter yourself.
5.  **Deliver**: Present a highly curated "Knowledge Report". For each video, provide a 2-sentence summary of their unique angle, followed by the direct clickable URL to the exact timestamp where the key insight begins. 

**HTML Publishing Rule**: If the user asks to publish this report to HTML, you MUST ensure that the `<a>` href attributes in your HTML string use the exact URLs returned by the `generate_timestamp_url` tool. Never use plain `https://youtu.be/ID` when a specific moment is discussed.

**Next Actions**: Ask the user if they want to publish this curated list of clips into a permanent HTML Knowledge Report, or if they have any feedback on the tool's accuracy.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/deep-exploration/SKILL.md`
