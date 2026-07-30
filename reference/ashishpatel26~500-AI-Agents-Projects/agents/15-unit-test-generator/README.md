<!-- Harvested from https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/HEAD/agents/15-unit-test-generator/README.md -->
> **Source:** [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) → `agents/15-unit-test-generator/README.md`

# Unit Test Generator Agent

Analyzes Python code and generates comprehensive pytest test suites — happy paths, edge cases, and error conditions.

**Framework**: LangChain  
**LLM**: GPT-4o  

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
# Generate tests for a Python file
python agent.py --file my_module.py

# Generate tests for inline code
python agent.py --code "def divide(a, b): return a / b"

# Specify output file
python agent.py --file utils.py --output tests/test_utils.py
```

## Example

Input: `shopping_cart.py` with add_item, remove_item, total methods  
Output: `test_shopping.py` with 20+ pytest tests using fixtures, parametrize, and mocking
