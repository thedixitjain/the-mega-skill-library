---
name: abcd-framework-audit
description: "Performs a strict evaluation of a video asset using Google's official 'ABCD' framework (Attract, Brand, Connect, Direct) based on transcript and metadata."
category: security-and-compliance
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/abcd-framework-audit/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/abcd-framework-audit/SKILL.md
---


### Skill: ABCD Framework Audit (YouTube Ads & Marketing)

**Objective**: Perform a strict evaluation of a video asset using Google's official "ABCD" framework for effective YouTube creatives. This is highly valuable for B2B marketers, advertisers, and gaming publishers looking to optimize trailers or sponsored influencer content.

**Execution Steps**:
1.  **Context**: The user has already identified a video. You do not need to search for one unless asked.
2.  **Disclaimer (CRITICAL)**: Before starting the analysis, you MUST output this exact message to the user:
    *"⚠️ **Note on Analysis Scope:** I am currently running in the Open Source configuration and do not have access to my full Multimodal Vision tools. I will perform this ABCD audit based strictly on the video's **transcript, title, and metadata**. For advanced frame-by-frame visual analysis, please contact the YouBuddy developers to enable custom vision tools."*
3.  **Script Ingestion (Read)**: Use `get_video_transcript(video_id)` and `get_video_details(video_id)`. You MUST analyze the transcript and metadata against the framework:
    *"Act as a senior YouTube Advertising Strategist. Analyze this video's transcript and description strictly using Google's ABCD framework. 1) Attract: How does the script hook the viewer in the first 5 seconds? 2) Brand: When and how is the core product/brand introduced in the speech? Is it natural or forced? 3) Connect: How does the script make the viewer feel? Is the storytelling effective for the target audience? 4) Direct: What is the Call to Action (CTA) at the end? Is it clear and urgent?"*
3.  **Synthesize the "ABCD Audit"**: Take your analysis of the transcript and format it into a professional, highly structured executive summary.
4.  **Deliver**: Present the "ABCD Creative Audit" containing:
    *   **A - Attract**: Evaluation of the hook (Score out of 10).
    *   **B - Brand**: Evaluation of product integration (Score out of 10).
    *   **C - Connect**: Evaluation of emotional resonance and pacing (Score out of 10).
    *   **D - Direct**: Evaluation of the CTA (Score out of 10).
    *   **Optimization Recommendations**: 2 to 3 specific changes the client should make to improve the video's ad performance.

**Next Actions**: Ask the user if they want to publish this ABCD Audit Report as a shareable HTML asset using `publish_file`.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/abcd-framework-audit/SKILL.md`
