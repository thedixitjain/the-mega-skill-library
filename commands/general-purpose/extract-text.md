---
name: extract-text
description: "Extract text content from images, screenshots, or diagrams for processing and analysis."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/vision-specialist/commands/extract-text.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/vision-specialist/commands/extract-text.md
---
Extract text content from images, screenshots, or diagrams for processing and analysis.

## Steps


1. Load the image using the Read tool to examine it visually.
2. Identify text regions in the image:
3. Extract text maintaining structure:
4. Handle special content:
5. Clean up the extracted text:
6. Format the output for the intended use:

## Format


```
Source: <image path>
Text Regions Found: <count>
Extracted Content:
  [Header] <text>
```


## Rules

- Preserve the original structure and hierarchy of the text.
- Flag text that is unclear or ambiguous with low confidence.
- Maintain code formatting exactly as shown in the image.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/vision-specialist/commands/extract-text.md`
