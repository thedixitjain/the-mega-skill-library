---
name: explain-code
description: "Explain code in detail - what it does, how it works, and why"
category: general-purpose
source_repo: TheDecipherist/claude-code-mastery
source_path: "commands/explain.md"
source_url: https://github.com/TheDecipherist/claude-code-mastery/blob/HEAD/commands/explain.md
---


# Explain Code

Provide a clear, thorough explanation of the specified code.

## Input

The user will provide one of:
- A file path: `/explain src/auth/jwt.ts`
- A file path with line range: `/explain src/auth/jwt.ts:45-80`
- A function/class name: `/explain parseToken`
- Just `/explain` — explain the currently open or most recently discussed file

## Explanation Structure

### 1. Overview (2-3 sentences)
What does this code do at a high level? What problem does it solve?

### 2. Key Components

Break down the major parts:

```
## Function: functionName

**Purpose:** One sentence description

**Parameters:**
- `param1` (type) — what it's for
- `param2` (type) — what it's for

**Returns:** What and when

**Side effects:** Any mutations, API calls, state changes
```

### 3. Control Flow

Explain the execution path:
1. First, it does X
2. Then checks Y
3. If Y is true, Z happens
4. Otherwise, W happens

Use a simple flowchart for complex logic:

```
Input → Validate → Transform → Output
              ↓
           Error → Log → Return null
```

### 4. Dependencies

What does this code depend on?
- External libraries
- Internal modules
- Environment variables
- Database/API connections

### 5. Gotchas & Edge Cases

Things that might surprise someone:
- Non-obvious behavior
- Edge cases handled (or not handled)
- Performance considerations
- Known limitations

### 6. Usage Example

Show how to use this code:

```typescript
// Example usage
const result = functionName(arg1, arg2);
```

## Tone

- Assume the reader is a competent developer unfamiliar with this specific code
- Avoid jargon unless defining it
- Use "this code" not "the code" for clarity
- Be concise but complete

---

**Source:** [`TheDecipherist/claude-code-mastery`](https://github.com/TheDecipherist/claude-code-mastery) → `commands/explain.md`
