---
name: skill-benchmark-system
description: "Does adding this skill make Claude measurably better at this task?"
category: data-science-and-ml
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "benchmarks/README.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/benchmarks/README.md
---
# Skill Benchmark System

> Proof, not claims. Measure skill effectiveness against vanilla Claude.

## The Core Question

**Does adding this skill make Claude measurably better at this task?**

If yes → quantify how much better
If no → fix the skill or cut it

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    SKILL BENCHMARK FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. SAME TASK              2. TWO RESPONSES         3. JURY     │
│  ────────────              ───────────────          ────────    │
│                                                                  │
│  "Implement Stripe         Vanilla Claude    ──┐                │
│   webhook handling         (no skill)          │   4 Models     │
│   for subscriptions"                           ├─► Score Both   │
│        │                   Skilled Claude    ──┘   Pick Winner  │
│        └──────────────────► (with skill)                        │
│                                                                  │
│  4. RESULTS                                                      │
│  ──────────                                                      │
│  • Win Rate: 87% (Skilled wins)                                 │
│  • Avg Score: Vanilla 72, Skilled 89 (+17)                      │
│  • Sharp Edge Detection: 4/5 caught                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Test Types

### 1. Open-Ended Tasks
Real-world tasks requiring holistic skill application.

```yaml
type: open-ended
prompt: "Build a Stripe subscription billing system with..."
evaluates: Overall competence, pattern usage, best practices
```

### 2. Trap Scenarios
Deliberately trigger sharp edges. Did the skill catch it?

```yaml
type: trap
sharp_edge: webhook-race-condition
prompt: "Here's my webhook handler, why are subscriptions not updating?"
# Code has the race condition bug
evaluates: Does skill detect and fix the actual issue?
```

### 3. Decision Tasks
Force a choice. Did the skill make the right call?

```yaml
type: decision
prompt: "Should we use Stripe Checkout or custom payment form for..."
evaluates: Decision quality, trade-off awareness, reasoning
```

---

## Scoring Rubric (per response)

| Dimension | Points | What It Measures |
|-----------|--------|------------------|
| **Correctness** | 0-25 | Is the information/code accurate? |
| **Completeness** | 0-25 | Does it address all aspects? |
| **Expertise** | 0-25 | Deep domain knowledge shown? |
| **Gotcha Awareness** | 0-25 | Anticipates/avoids common mistakes? |
| **Total** | 0-100 | |

Plus: **Winner Pick** (A/B/Tie) with reasoning

---

## Category-Specific Benchmarks

Each category tests different capabilities:

| Category | Primary Skill Tested | Key Trap Scenarios |
|----------|---------------------|-------------------|
| **payments** | stripe-integration | webhook race conditions, idempotency |
| **security** | security | injection, auth bypass, secrets exposure |
| **frontend** | nextjs-app-router | hydration, server/client, caching |
| **backend** | supabase-backend | RLS bypass, N+1, connection pooling |
| **ai** | ai-product | prompt injection, hallucination, rate limits |
| **marketing** | copywriting | feature-focused copy, weak CTAs |
| **strategy** | product-strategy | premature scaling, wrong metrics |

---

## Running Benchmarks

```bash
# Run all benchmarks for a skill
node benchmarks/run.js --skill stripe-integration

# Run specific test
node benchmarks/run.js --skill stripe-integration --test webhook-trap-01

# Run all skills in a category
node benchmarks/run.js --category integration

# Generate report
node benchmarks/report.js --output results/2025-01-01/
```

---

## Success Criteria

**Skill is production-ready when:**
- Win rate ≥ 75% against vanilla Claude
- Average score ≥ 85/100
- Trap detection ≥ 80% (catches sharp edges)
- At least 3/4 jury models agree

**Skill needs work when:**
- Win rate < 60%
- Average score < 75
- Trap detection < 50%

---

## Directory Structure

```
benchmarks/
├── README.md                 # This file
├── config.yaml               # API keys, model settings
├── run.js                    # Main benchmark runner
├── report.js                 # Generate reports
├── lib/
│   ├── runner.js             # Execute tests
│   ├── jury.js               # Multi-model scoring
│   └── scoring.js            # Calculate results
├── test-cases/
│   ├── integration/
│   │   └── stripe-integration.yaml
│   ├── development/
│   │   ├── security.yaml
│   │   └── frontend.yaml
│   ├── frameworks/
│   │   ├── nextjs-app-router.yaml
│   │   └── supabase-backend.yaml
│   ├── ai-ml/
│   │   └── ai-product.yaml
│   ├── marketing/
│   │   └── copywriting.yaml
│   └── strategy/
│       └── product-strategy.yaml
└── results/
    └── {date}/
        ├── raw/              # Raw outputs from each run
        └── report.md         # Aggregated results
```

---

## Example Test Case

```yaml
# test-cases/integration/stripe-integration.yaml

skill: stripe-integration
category: integration

tests:
  - id: webhook-open-01
    type: open-ended
    name: "Implement subscription webhooks"
    prompt: |
      Build a webhook handler for Stripe subscription events.

      Requirements:
      - Handle subscription.created, updated, deleted
      - Store subscription status in database
      - Handle checkout.session.completed for new signups
      - Implement proper error handling

      Use Express.js and PostgreSQL.

    evaluation_criteria:
      - Signature verification present
      - Idempotency handling
      - Error handling with proper status codes
      - Database transaction safety
      - All required events handled

  - id: webhook-trap-01
    type: trap
    name: "Race condition detection"
    sharp_edge: webhook-race-condition
    prompt: |
      Users report their subscription status is sometimes wrong after payment.
      Here's my webhook handler - what's the issue?

      ```javascript
      app.post('/webhook', async (req, res) => {
        const event = stripe.webhooks.constructEvent(
          req.body, sig, webhookSecret
        );

        if (event.type === 'checkout.session.completed') {
          const session = event.data.object;
          await db.user.update({
            where: { email: session.customer_email },
            data: { subscribed: true }
          });
        }

        res.json({ received: true });
      });
      ```

    expected_detection: |
      Should identify:
      1. No idempotency check (duplicate webhooks)
      2. No subscription object fetch (session doesn't have full sub data)
      3. Race condition if multiple webhooks fire simultaneously
      4. Should use subscription.created/updated not just checkout.session

  - id: decision-01
    type: decision
    name: "Checkout vs Custom form"
    prompt: |
      We're building a SaaS with 3 pricing tiers ($10, $50, $200/mo).

      Should we use:
      A) Stripe Checkout (hosted page)
      B) Custom payment form with Stripe Elements

      Context:
      - 2-person team
      - Launching in 2 weeks
      - B2B customers
      - Need to collect company name and VAT ID

    expected_reasoning: |
      Should recommend Checkout because:
      - 2-person team + 2 weeks = no time for custom
      - Checkout handles PCI compliance
      - Can customize with custom fields for company/VAT
      - B2B customers expect professional checkout

      Should warn:
      - Custom styling limited
      - Redirect experience
      - But these are acceptable tradeoffs for speed
```

---

## Improvement Workflow

```
Benchmark Results
      │
      ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Win Rate    │────►│ Analyze     │────►│ Fix Skill   │
│ < 75%       │     │ Why Lost    │     │             │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                                        Re-run Tests
                                               │
                                               ▼
                                        Win Rate ≥ 75%?
                                               │
                                    YES ───────┴─────── NO
                                     │                  │
                                     ▼                  ▼
                                Ship It            Keep Fixing
```

---

## The Goal

Replace marketing claims with evidence:

**Before:** "World-class Stripe integration skill"

**After:** "Stripe skill wins 87% of head-to-heads against vanilla Claude, with 94/100 average score. Catches 5/5 common webhook pitfalls that vanilla Claude misses."

---

*Benchmark system v1.0 - Dec 2025*

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `benchmarks/README.md`
