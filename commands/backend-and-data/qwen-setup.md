---
name: qwen-setup
description: "Set up the Qwen Video Bridge (API key + dependencies)"
allowed-tools: "Bash Read Write"
category: backend-and-data
source_repo: davepoon/buildwithclaude
source_path: "plugins/give-claude-eyes/commands/qwen-setup.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/give-claude-eyes/commands/qwen-setup.md
---


Walk the user through setting up the Qwen Video Bridge plugin.

## Step 1: Check Python

```bash
python3 --version
```

Require Python 3.9+. If not available, tell the user to install Python first.

## Step 2: Install dashscope

```bash
pip install dashscope --break-system-packages 2>&1 | tail -3
```

If pip is not available, try `pip3`. If neither works, suggest `python3 -m pip install dashscope`.

## Step 3: Check API key

```bash
echo "${DASHSCOPE_API_KEY:-NOT_SET}" | head -c 10
```

If `NOT_SET`, guide the user:

1. Go to https://modelstudio.console.alibabacloud.com/ (international) or https://dashscope.console.aliyun.com/ (China)
2. Sign up / log in
3. Go to API Keys section
4. Create a new key
5. Set it as an environment variable:
   - **macOS/Linux:** Add `export DASHSCOPE_API_KEY=sk-your-key-here` to `~/.bashrc` or `~/.zshrc`
   - **Windows:** Add it to System Environment Variables, or in PowerShell: `$env:DASHSCOPE_API_KEY = "sk-your-key-here"`

## Step 4: Verify

Run a quick test with a simple prompt (no video needed — test the connection):

```bash
python3 -c "
import dashscope
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
import os
from dashscope import MultiModalConversation
r = MultiModalConversation.call(
    api_key=os.environ['DASHSCOPE_API_KEY'],
    model='qwen-omni-plus-latest',
    messages=[{'role':'user','content':[{'text':'Say OK if you can hear me.'}]}]
)
if r.status_code == 200:
    print('SUCCESS: Qwen API is working!')
else:
    print(f'ERROR: {r.status_code} — {r.message}')
"
```

If successful, tell the user they're all set and can use `/analyze-video` or just describe a video in conversation.

If it fails, help troubleshoot:
- 401 → invalid API key
- 429 → rate limit, wait and retry
- Connection error → check network, might need to switch to CN endpoint

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/give-claude-eyes/commands/qwen-setup.md`
