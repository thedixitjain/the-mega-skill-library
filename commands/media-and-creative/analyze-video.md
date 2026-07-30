---
name: analyze-video
description: "Analyze a video or image file using Qwen Omni"
allowed-tools: "Read Bash Write Glob"
category: media-and-creative
source_repo: davepoon/buildwithclaude
source_path: "plugins/give-claude-eyes/commands/analyze-video.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/give-claude-eyes/commands/analyze-video.md
---


Analyze a video or image file using the Qwen Vision Bridge.

## Input

- `$1` — path to the video or image file
- Remaining arguments (`$ARGUMENTS` minus `$1`) — optional analysis prompt. If not provided, use a general analysis prompt appropriate to the file type.

## Steps

1. Verify the file exists at the given path. If not, search the current directory and workspace for a matching filename.

2. Check that `DASHSCOPE_API_KEY` is set:
   ```bash
   echo $DASHSCOPE_API_KEY | head -c 5
   ```
   If empty, tell the user to run `/qwen-setup` first.

3. Ensure `dashscope` is installed:
   ```bash
   python3 -c "import dashscope" 2>&1
   ```
   If missing, install it: `pip install dashscope --break-system-packages`

4. Run the bridge:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/qwen-vision/scripts/qwen_bridge.py" "$1" "prompt here" --fps 2
   ```

5. Present the analysis to the user in a clean, readable format. If the user's prompt implies structured output (classification, comparison, scoring), format accordingly.

6. Ask if the user wants to:
   - Follow up with more questions about the same video (use `--save-context`)
   - Analyze another file
   - Save the analysis to a file

## For batch analysis

If the user provides a directory path or glob pattern instead of a single file, write a batch script following the pattern in `${CLAUDE_PLUGIN_ROOT}/skills/qwen-vision/references/batch-pattern.md` and run it.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/give-claude-eyes/commands/analyze-video.md`
