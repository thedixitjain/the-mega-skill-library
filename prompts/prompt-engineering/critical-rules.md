---
name: critical-rules
description: "1. NEVER write Excel formulas to cells that will be graded on their displayed value. openpyxl does NOT compute formulas -- the evaluator will see None. Instead, compute results in Python and write literal values (numbers/strings). 2. After saving the workbook, ALWAYS reopen and verify the written values: wb2 = openpyxl.loadworkbook(OUTPUTPATH); print(wb2[sheet][cell].value) 3. Use the writefile tool to create solution.py -- it avoids shell escaping issues."
category: prompt-engineering
source_repo: microsoft/SkillOpt
source_path: "skillopt/envs/spreadsheetbench/prompts/critical_rules.md"
source_url: https://github.com/microsoft/SkillOpt/blob/HEAD/skillopt/envs/spreadsheetbench/prompts/critical_rules.md
---
## Critical Rules (MUST follow)
1. NEVER write Excel formulas to cells that will be graded on their displayed value.
   openpyxl does NOT compute formulas -- the evaluator will see None.
   Instead, compute results in Python and write literal values (numbers/strings).
2. After saving the workbook, ALWAYS reopen and verify the written values:
   `wb2 = openpyxl.load_workbook(OUTPUT_PATH); print(wb2[sheet][cell].value)`
3. Use the `write_file` tool to create solution.py -- it avoids shell escaping issues.
   Do NOT use `echo "..." > solution.py` for multi-line scripts.

---

**Source:** [`microsoft/SkillOpt`](https://github.com/microsoft/SkillOpt) → `skillopt/envs/spreadsheetbench/prompts/critical_rules.md`
