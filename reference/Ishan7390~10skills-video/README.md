<!-- Harvested from https://github.com/Ishan7390/10skills-video/blob/HEAD/README.md -->
> **Source:** [`Ishan7390/10skills-video`](https://github.com/Ishan7390/10skills-video) → `README.md`

# 10 Claude Code Skills

A curated collection of 8 Claude Code skills that supercharge how you write, think, code, and communicate. Install any of these skills in seconds and invoke them directly from your Claude Code session.

---

## What Are Claude Code Skills?

Skills are portable, installable behavior packages for [Claude Code](https://claude.ai/code). Each `.skill` file bundles a prompt, tools list, and metadata into a single archive. Once installed, a skill activates automatically when its trigger phrases are detected — or you can invoke it explicitly with `/skill-name`.

### How to Install a Skill

```bash
# Install from a local file
claude skill install ./caveman.skill

# Install directly from a URL
claude skill install https://raw.githubusercontent.com/Ishan7390/10skills-video/main/caveman.skill
```

### How to Use a Skill

After installing, invoke a skill by typing its slash command in any Claude Code session:

```
/caveman
/humanizer
/hook-forge
/decision-framer
```

Most skills also **auto-trigger** when they detect relevant phrases in your prompt — no slash command needed.

---

## Skills in This Collection

### 1. `caveman.skill` — Caveman Mode
**Slash command:** `/caveman`

Ultra-compressed communication that cuts token usage by ~75% while preserving full technical accuracy. Claude speaks like a caveman — terse, direct, zero filler.

**Intensity levels:**
| Level | What changes |
|-------|-------------|
| `lite` | No filler or hedging; full sentences kept |
| `full` *(default)* | Drop articles, fragments OK, short synonyms |
| `ultra` | Abbreviate everything, arrows for causality (X → Y) |
| `wenyan-full` | Classical Chinese register (文言文) |

**Trigger phrases:** "caveman mode", "talk like caveman", "less tokens", "be brief", `/caveman lite|full|ultra`

**Example:**
- Normal: *"Sure! The issue you're experiencing is likely caused by a token expiry misconfiguration..."*
- Caveman: *"Token expiry uses `<` not `<=`. Fix:"*

---

### 2. `decision-framer.skill` — Decision Framer
**Slash command:** `/decision-framer`

A strategic advisor that cuts through decision paralysis by reframing what you're actually deciding. Returns exactly five structured sections: the real decision, distinct options (including ones you missed), the three criteria that actually matter, the two unknowns that would change your mind, and your honest default if you do nothing.

**Trigger phrases:** "should I", "I'm torn between", "trying to decide", "stuck on", "X or Y", "what would you do"

**Best for:** Career moves, hiring decisions, build-vs-buy, product prioritization, big purchases.

---

### 3. `expand-and-contract.skill` — Expand and Contract
**Slash command:** `/expand-and-contract`

Scope management for half-formed ideas. First **expands** every possible thing a concept *could* include, then **contracts** each item into one of four buckets:

| Bucket | Meaning |
|--------|---------|
| **Core** | Must have — defines the thing |
| **Nice-to-have** | Adds value, cut if pressed |
| **Maybe later** | Parked for v2 |
| **Out** | Explicitly descoped |

**Trigger phrases:** "what's in scope", "help me scope this", "what should this include", "narrow this down", "expand and contract"

---

### 4. `find-skills.skill` — Find Skills
**Slash command:** `/find-skills`

Helps you discover and install skills that match what you're trying to do. Searches available skill registries and suggests the best match for your use case.

**Trigger phrases:** "find a skill for", "is there a skill that", "how do I do X", "can Claude..."

---

### 5. `hook-forge.skill` — Hook Forge
**Slash command:** `/hook-forge`

A direct-response copywriting engine that generates **10 hooks** for any piece of content — each using a different psychological trigger. Never start a post, email, or article without running this first.

**The 10 psychological triggers:**
1. **Curiosity** — makes readers feel they're missing something
2. **Loss Frame** — what they lose by not reading
3. **Contrast** — what people think vs. what's actually true
4. **Specificity** — a precise number or detail that signals credibility
5. **Controversy** — a claim that splits the room
6. **Pattern Interrupt** — starts mid-thought, breaks expected structure
7. **Identity** — speaks to who the reader sees themselves as
8. **Social Proof** — anchors the claim in what others are doing
9. **Future Pace** — puts the reader in a moment after they've acted
10. **Direct** — states the benefit plainly and immediately

**Best for:** LinkedIn posts, newsletters, YouTube titles, email subject lines, landing page headlines.

---

### 6. `humanizer.skill` — Humanizer
**Slash command:** `/humanizer`  
**Version:** 2.3.0

Removes signs of AI-generated writing from any text, making it sound natural and human. Based on Wikipedia's comprehensive "Signs of AI writing" guide.

**Patterns it fixes:**
- Inflated symbolism and promotional language
- Superficial `-ing` analyses ("*By implementing this...*")
- Vague attributions ("*studies show...*", "*experts say...*")
- Em dash overuse
- The AI "rule of three" list structure
- Overused AI vocabulary (*delve, nuanced, leverage, robust, paradigm*)
- Negative parallelisms ("*not only X, but also Y*")
- Excessive conjunctive phrases ("*It is worth noting that...*")

**Usage:** Paste your text and run `/humanizer`. Works on emails, blog posts, documentation, social copy, and more.

---

### 7. `infographic-builder.skill` — Infographic Builder
**Slash command:** `/infographic-builder`

Builds a single-file, self-contained HTML infographic from any text, data, or article. No external dependencies — the output is one `.html` file you can open in a browser, embed in Notion, or share directly.

**Supported infographic types:**
- Process / step-by-step
- Stats & numbers
- Comparison / pros & cons
- Timeline
- Hierarchy / org chart
- Cycle / loop
- Listicle
- Anatomy / breakdown

**The skill will ask you 3–4 clarifying questions** (unless obvious from context):
1. Where will this be used? (web, Notion, social, deck slide)
2. Aesthetic / vibe? (minimal, bold, dark, corporate, playful)
3. Brand colors?
4. Interactive or static?

**Trigger phrases:** "make an infographic", "visualize this", "turn this into a graphic", "one-pager", "visual summary", "social graphic"

---

### 8. `karpathy-guidelines.skill` — Karpathy Guidelines
**Slash command:** `/karpathy-guidelines`

Behavioral guidelines that reduce the most common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876). Activates when writing, reviewing, or refactoring code.

**Key principles enforced:**
- **Think before coding** — surface assumptions, don't hide confusion
- **Make surgical changes** — don't refactor what wasn't asked about
- **Define verifiable success** — what does "done" actually look like?
- **Avoid overcomplication** — three similar lines beats a premature abstraction
- **No half-finished work** — finish what's asked before expanding scope

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

**Trigger phrases:** writing, reviewing, or refactoring any code file.

---

## Quick Reference

| Skill | Slash Command | Auto-Triggers |
|-------|--------------|---------------|
| Caveman | `/caveman` | "caveman mode", "less tokens" |
| Decision Framer | `/decision-framer` | "should I", "torn between", "help me decide" |
| Expand and Contract | `/expand-and-contract` | "what's in scope", "help me scope this" |
| Find Skills | `/find-skills` | "find a skill for", "how do I..." |
| Hook Forge | `/hook-forge` | "write hooks for", "give me hooks" |
| Humanizer | `/humanizer` | "humanize this", "remove AI writing" |
| Infographic Builder | `/infographic-builder` | "make an infographic", "visualize this" |
| Karpathy Guidelines | `/karpathy-guidelines` | Auto-activates during code tasks |

---

## Install All Skills at Once

```bash
# Clone this repo and install all skills
git clone https://github.com/Ishan7390/10skills-video.git
cd 10skills-video
for f in *.skill; do claude skill install "./$f"; done
```

---

## License

Skills are provided as-is for personal and commercial use.
