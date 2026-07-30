---
name: configuration
description: "Create API connector tools for AG2 agents with auth handling, pagination, rate limiting, and error mapping"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/ag2-agent-builder/commands/connector-tool.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/ag2-agent-builder/commands/connector-tool.md
---


You are creating connector-integrated tool functions for AG2 agents that call external APIs.

## Instructions

1. Ask the user for:
   - Which service/API to integrate with
   - What operations are needed (list, get, create, update, delete)
   - Authentication method (API key, OAuth token, service account)
   - Rate limiting concerns

2. Generate connector tools following this pattern:

### Connector Tool Pattern

```python
import json
import os
import httpx
from autogen.tools import tool

# --- Configuration ---

BASE_URL = "https://api.service.com/v1"


def _get_headers() -> dict:
    """Build auth headers from environment."""
    token = os.environ.get("SERVICE_API_TOKEN")
    if not token:
        raise ValueError("connector_setup_required:service_name")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _make_request(method: str, path: str, **kwargs) -> dict:
    """Centralized HTTP request handler with error mapping."""
    try:
        headers = _get_headers()
    except ValueError as e:
        return {"success": False, "error": str(e)}

    url = f"{BASE_URL}/{path.lstrip('/')}"
    try:
        response = httpx.request(method, url, headers=headers, timeout=30.0, **kwargs)
        response.raise_for_status()
        return {"success": True, "data": response.json()}
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 401:
            return {"success": False, "error": "connector_setup_required:service_name"}
        elif status == 403:
            return {"success": False, "error": f"Permission denied: {e.response.text}"}
        elif status == 404:
            return {"success": False, "error": f"Resource not found: {path}"}
        elif status == 429:
            return {"success": False, "error": "Rate limit exceeded. Try again in a few seconds."}
        else:
            return {"success": False, "error": f"API error {status}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"success": False, "error": f"Connection error: {e}"}


# --- Tool Functions ---

@tool()
def list_items(limit: int = 20, offset: int = 0, filter_query: str = "") -> str:
    """List items from the service with optional filtering.

    Args:
        limit: Maximum items to return (default: 20, max: 100)
        offset: Pagination offset (default: 0)
        filter_query: Optional search/filter string
    """
    params = {"limit": min(limit, 100), "offset": offset}
    if filter_query:
        params["q"] = filter_query
    result = _make_request("GET", "/items", params=params)
    return json.dumps(result)


@tool()
def get_item(item_id: str) -> str:
    """Get detailed information about a specific item.

    Args:
        item_id: The unique identifier of the item
    """
    if not item_id.strip():
        return json.dumps({"success": False, "error": "item_id is required"})
    result = _make_request("GET", f"/items/{item_id}")
    return json.dumps(result)


@tool()
def create_item(name: str, description: str = "", metadata_json: str = "{}") -> str:
    """Create a new item in the service.

    Args:
        name: Name for the new item (required)
        description: Optional description
        metadata_json: Optional JSON string with additional fields
    """
    try:
        metadata = json.loads(metadata_json) if metadata_json else {}
    except json.JSONDecodeError:
        return json.dumps({"success": False, "error": "metadata_json must be valid JSON"})

    payload = {"name": name, "description": description, **metadata}
    result = _make_request("POST", "/items", json=payload)
    return json.dumps(result)
```

### Key Patterns for Connector Tools

**Authentication**: Always use a helper function that checks env vars and returns `connector_setup_required:<id>` on failure.

**HTTP client**: Use `httpx` (sync) or `httpx.AsyncClient` (async). Set reasonable timeouts (30s default).

**Error mapping**: Map HTTP status codes to meaningful messages:
- 401 -> connector_setup_required
- 403 -> permission denied
- 404 -> not found
- 429 -> rate limit

**Pagination**: Accept `limit` and `offset` parameters. Cap `limit` to prevent huge responses.

**Input validation**: Validate required fields before making API calls. Parse JSON string inputs with try/except.

**Shared helpers**: Extract `_get_headers()` and `_make_request()` to avoid duplication across tools.

3. After generating, verify: auth handling, error mapping, input validation, and timeout configuration.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/ag2-agent-builder/commands/connector-tool.md`
