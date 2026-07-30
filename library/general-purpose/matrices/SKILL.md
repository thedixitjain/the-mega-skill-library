---
name: matrices
description: "Problem-solving strategies for matrices in linear algebra"
allowed-tools: "[Bash, Read]"
category: general-purpose
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/math/linear-algebra/matrices/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/math/linear-algebra/matrices/SKILL.md
---


# Matrices

## When to Use

Use this skill when working on matrices problems in linear algebra.

## Decision Tree


1. **Identify Matrix Type**
   - Square, symmetric, orthogonal, diagonal?
   - Check properties with `sympy_compute.py matrix_type`

2. **Basic Operations**
   - Multiplication: `sympy_compute.py matmul "A" "B"`
   - Inverse: `sympy_compute.py inverse "A"`
   - Transpose: `sympy_compute.py transpose "A"`

3. **Solve Linear Systems**
   - Ax = b: `sympy_compute.py linsolve "A" "b"`
   - Check consistency with `z3_solve.py sat`

4. **Decompositions**
   - LU: `sympy_compute.py lu "A"`
   - QR: `sympy_compute.py qr "A"`
   - SVD: `sympy_compute.py svd "A"`


## Tool Commands

### Sympy_Inverse
```bash
uv run python -m runtime.harness scripts/sympy_compute.py inverse "[[1,2],[3,4]]"
```

### Sympy_Det
```bash
uv run python -m runtime.harness scripts/sympy_compute.py det "[[a,b],[c,d]]"
```

### Sympy_Linsolve
```bash
uv run python -m runtime.harness scripts/sympy_compute.py linsolve "[[1,2],[3,4]]" "[5,6]"
```

## Cognitive Tools Reference

See `.claude/skills/math-mode/SKILL.md` for full tool documentation.

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/math/linear-algebra/matrices/SKILL.md`
