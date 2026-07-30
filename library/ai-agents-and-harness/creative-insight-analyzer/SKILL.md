---
name: creative-insight-analyzer
description: "Deconstructs high-performing or viral videos to extract actionable creative insights from metadata and transcript."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/creative-insight-analyzer/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/creative-insight-analyzer/SKILL.md
---


### Skill: Creative Insight & Viral Analysis (The Visual Skimmer)

**Objective**: Deconstruct high-performing or viral videos to extract actionable creative insights. Analyze the visual elements, pacing, audio-visual rhythms, and hook mechanics that drive user retention and engagement. This is critical for B2B creative strategy.

**Execution Steps**:
1.  **Locate & Validate**: Use `search_youtube` (or accept a specific video ID from the user). Use `get_video_details` to confirm the video's duration and metadata. 
    *   *Note*: If the video is excessively long (>20 mins), ask the user if they want you to analyze the whole thing or focus on a specific segment, as full video analysis takes longer.
2.  **Disclaimer (CRITICAL)**: Before starting the analysis, you MUST output this exact message to the user:
    *"⚠️ **Note on Analysis Scope:** I am currently running in the Open Source configuration and do not have access to my full Multimodal Vision tools. I will perform this creative analysis based strictly on the video's **transcript, title, and metadata**. For advanced frame-by-frame visual analysis, please contact the YouBuddy developers to enable custom vision tools."*
3.  **First Impression (Metadata Audit)**: Use `get_video_details` to evaluate the "packaging." Look at the title, tags, and description. Is the title clickbait, professional, or curiosity-inducing?
3.  **Deep Script Ingestion (Read)**: Use `get_video_transcript(video_id)`. Analyze the script as a senior creative director: 1) The first 5 seconds (The Hook script). 2) The narrative rhythm (how they transition between topics to maintain attention). 3) The core narrative structure.
4.  **Synthesize the "Viral Blueprint"**: Combine the metadata audit and the transcript analysis into a structured report. 
5.  **Deliver**: Present the "Creative Insight Report" containing:
    *   **The Hook**: What happens in the first 3-5 seconds?
    *   **Visual Elements**: Editing pace, color grading, on-screen text, face-cam usage.
    *   **Rhythm & Retention**: How the creator uses pacing and audio to prevent viewers from clicking away.
    *   **Actionable Takeaway**: 1 or 2 things the user can apply to their own content strategy.

**Next Actions**: 
1. Ask the user if they want to publish this Creative Insight Report as a shareable HTML asset using `publish_file`.
2. Proactively ask the user: *"Would you like me to run this video through Google's official **ABCD (Attract, Brand, Connect, Direct)** framework to evaluate its effectiveness as an advertisement or marketing asset?"* (If they say yes, use the `abcd_framework_audit` skill).

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/creative-insight-analyzer/SKILL.md`
