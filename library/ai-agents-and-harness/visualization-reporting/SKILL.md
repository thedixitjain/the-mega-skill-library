---
name: visualization-reporting
description: "Transforms raw metrics and analysis into visual charts and published, shareable HTML reports using Google Cloud Storage."
category: ai-agents-and-harness
source_repo: google/adk-samples
source_path: "python/agents/youtube-analyst/youtube_analyst/skills/visualization-reporting/SKILL.md"
source_url: https://github.com/google/adk-samples/blob/HEAD/python/agents/youtube-analyst/youtube_analyst/skills/visualization-reporting/SKILL.md
---


### Skill: Visualization & Reporting Workflow

**Objective**: Transform raw numerical data and insights into beautiful, shareable assets. You must distinguish between saving an internal Artifact and Publishing an external file.

**Execution Steps**:
1.  **Confirm Data**: Ensure you have gathered the necessary metrics (e.g., a dictionary of channels and their engagement rates) or the final synthesized text.
2.  **Visualize**: Delegate to the `visualization_agent` to create static charts. Pass the raw data to it. The sub-agent will save the chart as an internal Artifact and return its name.
3.  **Retrieve Artifact**: Use the `load_artifacts` tool to load the raw bytes of the image artifact from the session memory.
4.  **Publish Dependencies to GCS**: If your final HTML report will display the image, you MUST publish the image bytes FIRST using `publish_file(content, filename, "image/png")`. This returns a public `https://storage.googleapis.com/...` URL.
5.  **Construct HTML**: Create a clean, well-formatted HTML string containing your analysis. Embed the charts using the *public URLs* obtained in step 4 (e.g., `<img src="https://storage.../chart.png" />`). Do NOT use local paths.
6.  **Final Delivery Options**:
    - **If the user just wants the report saved**: Call `render_html(html_content, "report.html")` to save it as an internal artifact they can download later.
    - **If the user wants a shareable link**: Call `publish_file(html_content, "report.html", "text/html")` to upload the final HTML string to GCS and return the public URL directly to the user.

---

**Source:** [`google/adk-samples`](https://github.com/google/adk-samples) → `python/agents/youtube-analyst/youtube_analyst/skills/visualization-reporting/SKILL.md`
