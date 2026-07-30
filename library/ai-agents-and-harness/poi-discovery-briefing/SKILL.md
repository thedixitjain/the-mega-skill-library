---
name: poi-discovery-briefing
description: "Extracts specific local activity recommendations and sentiment from travel vlogs into a shareable HTML BD report."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/poi-discovery-briefing/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/poi-discovery-briefing/SKILL.md
---


### Skill: POI & Activity Discovery Briefing (Travel BD)

**Objective**: Equip an Online Travel Agency (OTA) Business Development (BD) team with actionable data on local activities around a specific Point of Interest (POI). Extract recommendations from travel vloggers, gauge audience sentiment, and package it into a shareable HTML report.

**Execution Steps**:
1.  **Locate Context**: Use `search_youtube` to find highly relevant travel vlogs about the requested POI (e.g., "Mount Fuji travel vlog", "Things to do in Tokyo"). 
2.  **Extract Activities (Read)**: Use `get_video_transcript` on the top 2-3 longest vlogs. Travel vloggers often list 10+ activities in a single video. Scan the transcript to identify the specific names of activities, restaurants, or sub-locations they mention.
3.  **Map Timestamps**: Crucially, use `generate_timestamp_url` to create a direct jump link to the exact second the vlogger begins talking about each specific activity.
4.  **Community Audit**: Use `get_video_comments` for the videos to see if the audience is agreeing with the vlogger's recommendations or complaining about them (e.g., "The boat ride is a tourist trap"). 
5.  **Synthesize Report**: You must automatically format this data into a professional HTML "BD Briefing" document.
    *   For each activity discovered, list: The Activity Name, The Vlogger's Verdict, The Audience Sentiment, and the `<a href="...">` direct timestamp link.
    *   Embed the high-res thumbnail of the source video at the top of the report to make it visually appealing. (You can get this from `get_video_details`).
6.  **Deliver & Publish**: Call `publish_file(content=html_string, filename="poi_briefing.html")` to upload the final HTML string to the cloud. Return the generated public URL directly to the user in the chat so they can immediately share it with their BD team.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/poi-discovery-briefing/SKILL.md`
