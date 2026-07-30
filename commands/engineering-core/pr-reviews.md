---
name: pr-reviews
description: "Review open pull requests for code quality, project alignment, and risks."
category: engineering-core
source_repo: jayminwest/overstory
source_path: ".claude/commands/pr-reviews.md"
source_url: https://github.com/jayminwest/overstory/blob/HEAD/.claude/commands/pr-reviews.md
---
## intro

Review open pull requests for code quality, project alignment, and risks.

**Argument:** `$ARGUMENTS` — optional PR number(s) to review (e.g., `9` or `9 12 15`). If empty, review all open PRs.

## Steps

### 1. Discover PRs to review

- If `$ARGUMENTS` contains PR number(s), use those
- Otherwise, run `gh pr list --state open --json number,title,author,headRefName,additions,deletions` to get all open PRs
- If there are no open PRs, say so and stop

### 2. Spawn a review team

Use the Task tool to spawn parallel agents (one per PR). Each agent should:

#### a. Gather context
- `gh pr view <number> --json title,body,author,additions,deletions,files,commits,comments,reviews,headRefName,baseRefName`
- `gh pr diff <number>` to get the full diff
- Read any files touched by the PR to understand the surrounding code

#### b. Code quality review
- Check for correctness — does the code do what the PR claims?
- Check for bugs, edge cases, and error handling gaps
- Check adherence to project conventions (see CLAUDE.md): strict TypeScript, zero runtime deps, Biome formatting, tab indentation, 100-char line width
- Check test coverage — are new code paths tested? Do tests follow the "never mock what you can use for real" philosophy?
- Flag any security concerns (injection, unsafe input handling, etc.)

#### c. Project alignment review
- Does this change fit the project's architecture and direction?
- Does it follow existing patterns or introduce unnecessary new ones?
- Is the scope appropriate — does it do too much or too little?
- Are there breaking changes or backward-compatibility concerns?

#### d. Risk assessment
- What could go wrong if this is merged?
- Are there performance implications?
- Does it touch critical paths (config loading, agent spawning, mail system)?
- Are there dependency or compatibility risks?
- Could it conflict with other open PRs?

#### e. Produce a review summary
Each agent should return a structured review:
- **PR:** `#<number> — <title>` by `<author>`
- **Verdict:** Approve / Request Changes / Needs Discussion
- **Summary:** 2-3 sentence overview
- **Strengths:** What's good about this PR
- **Issues:** Bugs, risks, or concerns (with file:line references)
- **Suggestions:** Non-blocking improvements
- **Project alignment:** How well it fits overstory's direction

### 3. Present consolidated report

After all agents complete, present a single consolidated report with:
- A summary table of all reviewed PRs with verdicts
- The detailed review for each PR
- Any cross-PR concerns (conflicts, overlapping changes, pattern inconsistencies)
- Recommended merge order if multiple PRs are ready

---

**Source:** [`jayminwest/overstory`](https://github.com/jayminwest/overstory) → `.claude/commands/pr-reviews.md`
