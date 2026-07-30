---
name: generate-tests
description: "Generate tests for code - unit tests, integration tests, or edge cases"
category: testing-and-qa
source_repo: TheDecipherist/claude-code-mastery
source_path: "commands/test.md"
source_url: https://github.com/TheDecipherist/claude-code-mastery/blob/HEAD/commands/test.md
---


# Generate Tests

Generate comprehensive tests for the specified code.

## Input

The user will provide one of:
- A file path: `/test src/utils/validators.ts`
- A function name: `/test validateEmail`
- Just `/test` — generate tests for recently changed files

Optional flags via $ARGUMENTS:
- `--unit` — unit tests only (default)
- `--integration` — integration tests
- `--edge` — focus on edge cases
- `--coverage` — aim for high coverage

## Process

### 1. Detect Test Framework

Check the project for:
- `vitest.config.*` → Vitest
- `jest.config.*` → Jest
- `*.test.ts` patterns → Match existing style
- `pytest.ini` or `conftest.py` → Pytest
- `go.mod` → Go testing

If unclear, ask the user.

### 2. Analyze the Code

Identify:
- Public functions/methods to test
- Input types and valid ranges
- Expected outputs
- Error conditions
- Side effects (mocking needed?)
- Dependencies (what to mock?)

### 3. Generate Test Cases

For each function, create tests for:

**Happy Path**
- Normal input → expected output
- Common use cases

**Edge Cases**
- Empty input ([], "", null, undefined)
- Boundary values (0, -1, MAX_INT)
- Single element collections
- Very large inputs

**Error Cases**
- Invalid input types
- Out of range values
- Missing required fields
- Network/IO failures (if applicable)

### 4. Test Structure

Follow AAA pattern:

```typescript
describe('functionName', () => {
  it('should return X when given Y', () => {
    // Arrange
    const input = { ... };

    // Act
    const result = functionName(input);

    // Assert
    expect(result).toEqual(expected);
  });
});
```

### 5. Naming Convention

Test names should be readable as sentences:
- `should return empty array when input is empty`
- `should throw ValidationError when email is invalid`
- `should call API once per unique user`

NOT:
- `test1`
- `works`
- `validateEmail test`

## Output

1. Create test file at conventional location:
   - `src/foo.ts` → `src/foo.test.ts` or `__tests__/foo.test.ts`
   - `foo.py` → `test_foo.py` or `tests/test_foo.py`

2. Show summary:
   - Number of test cases generated
   - Coverage estimate
   - Any functions skipped and why

3. Run the tests to verify they pass:
   ```bash
   npm test -- --run <test-file>
   ```

## Guidelines

- Don't test implementation details, test behavior
- One assertion per test when possible
- Mock external dependencies, not internal code
- Tests should be deterministic (no random, no Date.now())
- Fast tests — avoid real network/database calls

---

**Source:** [`TheDecipherist/claude-code-mastery`](https://github.com/TheDecipherist/claude-code-mastery) → `commands/test.md`
