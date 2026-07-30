---
name: obey-working-effectively-with-legacy-code-by-michael-feathers
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/working-effectively-with-legacy-code/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/working-effectively-with-legacy-code/traceability.md
---
# OBEY Working Effectively with Legacy Code by Michael Feathers

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run against the current canonical source on 2026-05-02 for alphabetical book 13 in `_rule-workbench`: `working-effectively-with-legacy-code`.
- `full.md` is a symlink to `../../working-effectively-with-legacy-code/working-effectively-with-legacy-code.md`; the canonical source text is not edited here.
- No rule is labeled `default`. Characterization, small steps, seam choice, hidden dependency reduction, test discipline, constructor/global isolation, and cleanup obligations are common agent failure modes even when they sound obvious.
- `mini.md` keeps the book thesis and the repeated local discipline: treat untrusted tests as legacy risk, characterize before redesign, create the smallest useful seam, break only the dependency that blocks feedback, keep behavioral and structural edits separate, and leave the touched area more testable.
- `nano.md` keeps the smallest always-on reminders that block the highest-risk shortcuts: rewrite-first work, edit-and-pray changes, uncharacterized behavior changes, broad dependency breaking, mixed-intent patches, and abandoned test-only seams.
- Detailed technique lists are merged into technique-family rules unless a technique changes a common implementation decision. Language/build-specific seams are retained as fallback triggers rather than promoted as general design moves.

## Mini mapping

Decision rules:

- `M1` Treat any area without trustworthy tests as legacy code; avoid rewrite-first and module-wide cleanup. Source: `Purpose` (3-16), `Primary Directive` (20-35), `Non-Negotiable Rules` (39-58), `Default Workflow for Legacy Changes` (61-74), `Forbidden Patterns` (286-305), `Final Instruction` (362-371).
- `M2` State the behavior delta and characterize uncertain, suspicious, or ugly current behavior before modification. Source: `Primary Directive` (20-35), `Non-Negotiable Rules` (39-58), `Testing Strategy Rules` (78-99), `Forbidden Patterns` (286-305), `Review Checklist` (345-358).
- `M3` Follow the legacy loop from change point through seam, dependency break, test, change, and local refactor. Source: `Primary Directive` (20-35), `Default Workflow for Legacy Changes` (61-74), `Code Generation Rules` (308-332), `Final Instruction` (362-371).
- `M4` Prefer fast focused tests; use broader interception or integration tests only as the safest first observation point. Source: `Testing Strategy Rules` (78-99), `Test Selection and Understanding Rules` (164-174), `Testing Rules` (335-342).
- `M5` Choose test points by tracing effects from the change point through values, calls, fields, outputs, collaborators, interception points, and pinch points. Source: `Test Selection and Understanding Rules` (164-174).
- `M6` Use the smallest seam for substitution, observation, or interception, with sensing vs separation explicit. Source: `Seam Rules` (102-125), `Review Checklist` (345-358).
- `M7` Break dependencies deliberately only where hidden inputs, hard outputs, hard construction, globals, statics, ambient context, or framework callbacks block testing or safe change. Source: `Non-Negotiable Rules` (39-58), `Dependency Breaking Rules` (128-161), `Handling Risky Areas` (240-267), `Forbidden Patterns` (286-305).
- `M8` Keep behavior changes, refactorings, and cleanup separate; verify small steps and discard unsupported exploratory restructuring. Source: `Test Selection and Understanding Rules` (164-174), `Legacy Refactoring Heuristics` (228-237), `Review Rules` (271-283), `Review Checklist` (345-358).
- `M9` Use sprout, wrap, and extract-and-override style moves for risky additions, then fold temporary structures into better design under tests. Source: `Preferred Legacy Techniques` (178-205), `Code Generation Rules` (308-332).
- `M10` For hard-to-test methods, split construction from use, extract side effects, carve pure computation first, and isolate policy from runtime, persistence, UI, or framework mechanisms. Source: `Dependency Breaking Rules` (128-161), `Legacy Refactoring Heuristics` (228-237), `Handling Risky Areas` (240-267), `Code Generation Rules` (308-332).
- `M11` Match dependency-breaking techniques to the actual barrier and use link/preprocessing seams only when ordinary object seams are impractical. Source: `Seam Rules` (102-125), `Dependency-Breaking Technique Index` (208-224), `Code Generation Rules` (308-332).
- `M12` In large code, sketch effects and group responsibilities before moving behavior; let setup pain, impossible observation, and repeated changes point to smaller responsibilities. Source: `Test Selection and Understanding Rules` (164-174), `Legacy Refactoring Heuristics` (228-237), `Handling Risky Areas` (240-267).
- `M13` Review legacy changes for missing tests, mixed edit intent, broad edits, hard-coded collaborators, global/static reach-through, constructor side effects, and framework-trapped business logic. Source: `Review Rules` (271-283), `Review Checklist` (345-358).
- `M14` Reject hidden dependency expansion, mocking around untestable structure without improving it, cosmetic cleanup, and large architecture before basic seams exist. Source: `Forbidden Patterns` (286-305), `Code Generation Rules` (308-332).
- `M15` Leave the touched area easier to understand, test, or change without mistaking temporary seams or build tricks for design improvement. Source: `Primary Directive` (20-35), `Non-Negotiable Rules` (39-58), `Seam Rules` (102-125), `Review Checklist` (345-358), `Final Instruction` (362-371).

Trigger rules:

- `M16` Uncertain behavior, consumer reliance on ugly behavior, or hard-to-prove paths trigger characterization or another explicit observation path. Source: `Testing Strategy Rules` (78-99), `Forbidden Patterns` (286-305).
- `M17` Excessive test setup or instantiation failure triggers breaking the first real barrier: constructor work, hidden allocation, factory call, global/static state, framework object, or hard parameter. Source: `Dependency Breaking Rules` (128-161), `Dependency-Breaking Technique Index` (208-224), `Handling Risky Areas` (240-267).
- `M18` Time, randomness, environment, thread-local state, user/request context, files, networks, process exits, database writes, messages, or control-flow logging that block repeatable tests trigger wrapping or injection. Source: `Dependency Breaking Rules` (128-161), `Handling Risky Areas` (240-267).
- `M19` Large methods or classes that defeat local reasoning trigger effect sketches, interception or pinch points, pure-computation extraction, and branch-count restraint. Source: `Test Selection and Understanding Rules` (164-174), `Handling Risky Areas` (240-267).
- `M20` Database-heavy, UI, framework, or API-boundary code triggers separating policy from boundary mechanisms while keeping real-boundary integration tests where they matter. Source: `Handling Risky Areas` (240-267), `Testing Rules` (335-342).
- `M21` Magical, temporary, public-for-test, subclass-only, link/preprocessor, or probe/sensing seams trigger cleanup obligations. Source: `Testing Strategy Rules` (78-99), `Seam Rules` (102-125), `Preferred Legacy Techniques` (178-205), `Dependency-Breaking Technique Index` (208-224).
- `M22` Repeated edits across places trigger incremental duplication removal under tests rather than broad redesign. Source: `Legacy Refactoring Heuristics` (228-237), `Final Instruction` (362-371).
- `M23` Rewrite or heroic-cleanup pressure triggers the smallest sprout, wrap, seam, characterization, or refactoring step that makes today's change safer. Source: `Primary Directive` (20-35), `Default Workflow for Legacy Changes` (61-74), `Forbidden Patterns` (286-305), `Final Instruction` (362-371).

Final checklist:

- The checklist restates `M1`-`M8`, `M15`, `M18`, and `M21` as a final scan rather than introducing new rules.

## Nano mapping

Decision rules:

- `N1` Treat code without trustworthy tests as legacy code and state what changes and what must remain. Source: `Purpose` (3-16), `Primary Directive` (20-35), `Default Workflow for Legacy Changes` (61-74).
- `N2` Characterize uncertain current behavior before changing it, including ugly behavior consumers may rely on. Source: `Non-Negotiable Rules` (39-58), `Testing Strategy Rules` (78-99), `Forbidden Patterns` (286-305).
- `N3` Use the legacy loop: change point, observation point, seam, dependency break, test, change, local refactor. Source: `Primary Directive` (20-35), `Default Workflow for Legacy Changes` (61-74), `Code Generation Rules` (308-332).
- `N4` Prefer fast focused tests, with broader harnesses only as temporary first coverage. Source: `Testing Strategy Rules` (78-99), `Test Selection and Understanding Rules` (164-174), `Testing Rules` (335-342).
- `N5` Create the narrowest useful seam for sensing or separation and break only dependencies that block feedback. Source: `Seam Rules` (102-125), `Dependency Breaking Rules` (128-161), `Legacy Refactoring Heuristics` (228-237).
- `N6` Use sprout, wrap, parameterize, inject, extract, or override moves when direct edits would be unsafe. Source: `Preferred Legacy Techniques` (178-205), `Dependency-Breaking Technique Index` (208-224), `Code Generation Rules` (308-332).
- `N7` Keep behavior changes, structural refactorings, and cleanup separate and small. Source: `Review Rules` (271-283), `Review Checklist` (345-358).
- `N8` Do not leave test-only seams, hidden dependencies, wrappers, globals, subclass tricks, or link/preprocessor tricks without cleanup plans. Source: `Seam Rules` (102-125), `Dependency-Breaking Technique Index` (208-224), `Forbidden Patterns` (286-305).

Trigger rules:

- `N9` Unclear behavior triggers characterization. Source: `Testing Strategy Rules` (78-99).
- `N10` Constructors, globals, statics, frameworks, I/O, clocks, randomness, environment, or deep object graphs trigger one narrow dependency break. Source: `Dependency Breaking Rules` (128-161), `Handling Risky Areas` (240-267).
- `N11` Large methods or classes that defeat local reasoning trigger effect sketches and a seam before semantic edits. Source: `Test Selection and Understanding Rules` (164-174), `Handling Risky Areas` (240-267).
- `N12` Rewrite or broad-cleanup temptation triggers the next smaller verified move. Source: `Primary Directive` (20-35), `Forbidden Patterns` (286-305), `Final Instruction` (362-371).

Final checklist:

- The checklist restates `N2`, `N4`, `N5`, `N7`, and `N8` as a final scan rather than introducing new rules.

## Section coverage review

- `Purpose` (3-16): covered by `M1`, `N1`; book framing is preserved in the primary bias, while repository-policy wording is intentionally lost.
- `Primary Directive` (20-35): covered by `M1`, `M2`, `M3`, `M15`, `M23`, `N1`, `N3`, and `N12`.
- `Non-Negotiable Rules` (39-58): covered by `M1`, `M2`, `M7`, `M15`, and `N2`; the five-item list is merged into thesis, characterization, seam, dependency, and improvement rules.
- `Default Workflow for Legacy Changes` (61-74): covered by `M1`, `M3`, `M23`, `N1`, `N3`; the short form is preserved, while wording duplication is merged.
- `Testing Strategy Rules` (78-99): covered by `M2`, `M4`, `M16`, `M21`, `N2`, `N4`, and `N9`; detailed separation of old/new tests is merged into behavior-delta and characterization rules.
- `Seam Rules` (102-125): covered by `M6`, `M11`, `M15`, `M21`, `N5`, and `N8`; the seam examples list is covered by `M11` or intentionally lost where it is only illustrative.
- `Dependency Breaking Rules` (128-161): covered by `M7`, `M10`, `M17`, `M18`, `N5`, and `N10`; hidden-input and hard-output lists are collapsed into dependency trigger examples.
- `Test Selection and Understanding Rules` (164-174): covered by `M4`, `M5`, `M8`, `M12`, `M19`, `N4`, and `N11`; scratch-refactoring check-in warning is covered by `M8`.
- `Preferred Legacy Techniques` (178-205): covered by `M9`, `M21`, and `N6`; individual mechanics for sprout and wrap are merged into technique-family guidance.
- `Dependency-Breaking Technique Index` (208-224): covered by `M11`, `M17`, `M21`, `N6`, `N8`, and `N10`; individual recipes are merged into barrier-based selection, with language/build-specific mechanics intentionally lost from compressed release files except as fallback seam cautions.
- `Legacy Refactoring Heuristics` (228-237): covered by `M8`, `M10`, `M12`, `M22`, `N5`; heuristic details are merged into local-refactoring and responsibility-extraction rules.
- `Handling Risky Areas` (240-267): covered by `M7`, `M10`, `M17`, `M18`, `M19`, `M20`, `N10`, and `N11`; risky-area subsections are collapsed into triggers.
- `Review Rules` (271-283): covered by `M8`, `M13`, `N7`; review list details are preserved as review-risk scan items in `mini.md` and intentionally lost from `nano.md` except for the mixed-edit rule.
- `Forbidden Patterns` (286-305): covered by `M1`, `M2`, `M7`, `M14`, `M23`, `N2`, `N8`, and `N12`.
- `Code Generation Rules` (308-332): covered by `M3`, `M9`, `M10`, `M11`, `M14`, `N3`, and `N6`; preferred first moves and avoidances are merged into decision and trigger rules.
- `Testing Rules` (335-342): covered by `M4`, `M20`, `N4`; integration-boundary detail is preserved only as a risky-area trigger.
- `Review Checklist` (345-358): covered by the final checklists plus `M2`, `M6`, `M7`, `M8`, `M13`, `M15`, `N7`; the revise-before-shipping sentence is intentionally lost as process framing.
- `Final Instruction` (362-371): covered by `M1`, `M3`, `M15`, `M22`, `M23`, `N12`; the numbered list is merged into the primary bias and final checklist.

## Subsection coverage details

- `Characterization Tests` (80-87): covered by `M2`, `M16`, `M21`, `N2`, `N9`; temporary sensing variables are covered by cleanup obligations.
- `New Behavior Tests` (89-92): covered by `M2`, `M4`, `N1`, `N4`; old-vs-new test separation is merged into behavior-delta discipline.
- `Testability Improvements` (94-99): covered by `M7`, `M10`, `M17`, `M18`, `N5`, `N10`.
- `What Counts as a Useful Seam` (104-116): covered by `M6`, `M11`, `N5`; illustrative seam names are merged into technique selection.
- `Required Behavior` (118-124): covered by `M6`, `M11`, `M15`, `M21`, `N5`, `N8`.
- `Hidden Inputs` (132-139): covered by `M7`, `M18`, `N10`.
- `Hard Outputs` (141-147): covered by `M7`, `M18`, `N10`; logging-as-control-flow is retained as a hard-output trigger in `M18`.
- `Construction Problems` (149-153): covered by `M7`, `M17`, `N10`.
- `Required Moves` (155-160): covered by `M7`, `M10`, `M11`, `N5`, `N6`.
- `Sprout Method` (180-186): covered by `M9`, `M23`, `N6`, `N12`.
- `Sprout Class` (188-194): covered by `M9`, `M23`, `N6`, `N12`.
- `Wrap Method` (196-197): covered by `M9`, `M23`, `N6`, `N12`.
- `Wrap Class` (199-200): covered by `M9`, `M23`, `N6`, `N12`.
- `Extract and Override Call` (202-204): covered by `M9`, `M11`, `M21`, `N6`, `N8`; preference for composition later is preserved as cleanup obligation.
- `Large Methods` (242-246): covered by `M10`, `M12`, `M19`, `N11`.
- `Static and Global Dependencies` (248-252): covered by `M7`, `M18`, `N10`.
- `Database-Heavy Code` (254-257): covered by `M20`; intentionally lost from `nano.md` except as boundary-dependency pressure in `N10`.
- `UI or Framework Code` (259-262): covered by `M10`, `M20`, `N10`.
- `Constructors Doing Too Much` (264-267): covered by `M10`, `M17`, `N10`.
- `Rewrite as the First Move` (288-291): covered by `M1`, `M23`, `N12`.
- `No-Safety Change` (293-296): covered by `M2`, `M4`, `M16`, `N2`, `N4`, `N9`.
- `Hidden Dependency Expansion` (298-300): covered by `M7`, `M14`, `M18`, `N5`, `N8`, `N10`.
- `Cosmetic Refactoring Only` (302-304): covered by `M1`, `M14`, `M15`, `M23`, `N12`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/working-effectively-with-legacy-code/traceability.md`
