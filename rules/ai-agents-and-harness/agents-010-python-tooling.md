---
name: agents-010-python-tooling
description: "Python tooling and dependency conventions for plugin-eval and tools/"
category: ai-agents-and-harness
source_repo: wshobson/agents
source_path: ".cursor/rules/010-python-tooling.mdc"
source_url: https://github.com/wshobson/agents/blob/HEAD/.cursor/rules/010-python-tooling.mdc
---


# Python tooling

This project uses the Astral Rust toolchain:

- **uv** for package management. Run `uv run <cmd>` to execute inside the venv, `uv add <pkg>` to install.
- **ruff** for linting and formatting. `uv run ruff check .` / `uv run ruff format .`.
- **ty** for type checking. `uv run ty check .`.

Do not use `pip`, `mypy`, or `black`. Do not edit `requirements.txt` for Python deps — those belong in `pyproject.toml`.

Python ≥ 3.12 is required. Use modern syntax (`X | Y`, `list[T]`, structural pattern matching).

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `.cursor/rules/010-python-tooling.mdc`

**Also appears in:** `wshobson/agents/tools/adapters/cursor_rules/010-python-tooling.mdc`
