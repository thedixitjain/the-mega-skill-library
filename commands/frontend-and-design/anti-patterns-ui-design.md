---
name: anti-patterns-ui-design
description: "These approaches look like reasonable design choices but consistently create confusion, frustration, and poor user experience."
category: frontend-and-design
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "design/ui-design/anti-patterns.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/design/ui-design/anti-patterns.md
---
# Anti-Patterns: UI Design

These approaches look like reasonable design choices but consistently create confusion, frustration, and poor user experience.

---

## 1. The Icon Guessing Game

**The Mistake:**
```
Using icons without labels for non-universal actions.

UNIVERSAL ICONS (okay alone):
✓ Search (magnifying glass)
✓ Menu (hamburger)
✓ Close (X)
✓ Home (house)
✓ Settings (gear) - sometimes
✓ Play/Pause (triangle/bars)

NOT UNIVERSAL (need labels):
✗ Abstract icons for features
✗ Industry-specific symbols
✗ Metaphors that don't translate
✗ Multiple possible meanings

EXAMPLES OF CONFUSION:
[🔔] - Notifications? Reminders? Alerts?
[📤] - Share? Upload? Export?
[📋] - Copy? Notes? Tasks? Clipboard?
[🏷️] - Tags? Labels? Categories?

THE FIX:
Icon + Label (best)
Tooltip (acceptable for space constraints)
Only icons for truly universal actions

IMPLEMENTATION:
<button>
  <icon name="bell" />
  <span>Notifications</span>
</button>

/* Not this */
<button aria-label="Notifications">
  <icon name="custom-bell-variant" />
</button>
```

**Why It's Wrong:**
- Users spend time guessing instead of doing
- Different cultures interpret icons differently
- Tooltips require hover (no mobile support)
- Users avoid features they don't understand

---

## 2. The Infinite Scroll Trap

**The Mistake:**
```
Using infinite scroll for content where users need to find specific items.

BAD USE CASES:
- E-commerce product listings
- Search results
- Data tables
- Anything users filter/compare

PROBLEMS:
1. Can't link to specific page
2. Can't estimate content size
3. Footer is unreachable
4. Browser back breaks position
5. "Where was that item I saw?"
6. Performance degrades with length

GOOD USE CASES:
- Social media feeds (consumption)
- Activity logs (time-based)
- Infinite exploration (discovery)

THE FIX - PAGINATION OR LOAD MORE:

Pagination:
[1] [2] [3] [...] [50]
Showing 21-40 of 500 results

Load More:
[Load more results]
Showing 40 of 500 results

Virtual Scrolling (for huge lists):
Renders only visible items
Maintains scroll position
Works with search/filter
```

**Why It's Wrong:**
- Users lose their place
- No mental model of content size
- Poor accessibility
- SEO implications
- Difficult to share or bookmark

---

## 3. The Carousel Crime

**The Mistake:**
```
Auto-advancing carousels, especially on hero sections.

THE PROBLEMS:
1. Users can't read fast enough
2. Movement causes distraction
3. CTA changes before click
4. Content users want scrolls away
5. Accessibility nightmare
6. ~1% of users click past first slide

RESEARCH SHOWS:
- Hero carousels have near-zero engagement
- Auto-advance increases bounce rate
- Users perceive them as ads (banner blindness)

BAD IMPLEMENTATION:
<Carousel autoAdvance={5000}>
  <Slide>Important Message 1</Slide>
  <Slide>Important Message 2</Slide>
  <Slide>Important Message 3</Slide>
</Carousel>

THE FIX:
Option 1: Pick your best content, feature it static
Option 2: Grid layout showing all options
Option 3: User-controlled carousel (no auto-advance)
Option 4: Vertical scroll (mobile-native)

IF YOU MUST USE CAROUSEL:
- No auto-advance
- Visible navigation dots
- Swipe support
- Pause on hover
- Respect prefers-reduced-motion
```

**Why It's Wrong:**
- Users don't control their experience
- Important content gets missed
- Accessible control is complex
- Mobile swipe conflicts with page scroll

---

## 4. The Mystery Meat Navigation

**The Mistake:**
```
Navigation where users must interact to discover where things go.

EXAMPLES:
- Icon-only sidebar (hover to reveal labels)
- Hamburger menu hiding primary navigation
- Deep dropdowns requiring precise hovering
- Labels that use internal jargon

BAD:
[🏠] [📊] [⚙️] [👤]  // What are these?

[≡] ← Everything hidden here

"Go to Workspace Hub" ← What's a Workspace Hub?

GOOD:
[Home] [Dashboard] [Settings] [Profile]

Primary navigation visible on desktop

"Your projects" ← Users know their projects
```

**Why It's Wrong:**
- Users waste time exploring instead of doing
- Hidden navigation = hidden features
- Reduces discoverability
- Increases time to task

---

## 5. The Overzealous Validation

**The Mistake:**
```
Validating too aggressively or at the wrong time.

BAD PATTERNS:
1. Immediate error on empty required field
   User tabs into field → instant red error

2. Format validation while typing
   Phone: "5" → "Invalid phone number!"

3. Password requirements shown as errors
   "Must contain uppercase" shown as error
   while user is still typing

4. Clearing the field on invalid input
   User types, gets error, field cleared

GOOD VALIDATION TIMING:
- On blur (after user leaves field)
- On submit (final check)
- Real-time ONLY for success confirmation

GOOD PATTERNS:
// Show requirements upfront, not as errors
<PasswordField>
  <Requirement met={hasUppercase}>
    One uppercase letter
  </Requirement>
  <Requirement met={hasNumber}>
    One number
  </Requirement>
</PasswordField>

// Validate on blur
<input onBlur={validate} />

// Inline success
<EmailField>
  {isValid && <CheckIcon />}
</EmailField>
```

**Why It's Wrong:**
- Creates anxiety before user has chance
- Slows down form completion
- Punishes correct behavior (typing)
- Makes users feel like failures

---

## 6. The Deceptive Pattern

**The Mistake:**
```
Dark patterns that trick users against their interests.

EXAMPLES:

Confirmshaming:
[ Opt out, I don't like saving money ]

Pre-checked options:
[✓] Sign me up for marketing emails
[✓] Share my data with partners

Hidden unsubscribe:
Unsubscribe link in 6pt font, gray on gray

Misdirection:
[Subscribe Now!]  [No thanks, continue in tiny text]

Bait and switch:
"Free Trial" → requires credit card → auto-charges

Roach motel:
Easy to sign up, impossible to delete account

Trick questions:
"Uncheck this box to not receive no emails"
```

**Why It's Wrong:**
- Destroys trust permanently
- Illegal in many jurisdictions (GDPR, CCPA)
- Creates negative brand association
- Users will leave and warn others
- Short-term gains, long-term damage

---

## 7. The Feature Factory

**The Mistake:**
```
Adding every feature request without considering the interface.

SYMPTOMS:
- Settings page with 47 options
- Toolbar with 30 icons
- Modal with 10 form sections
- Homepage with 15 CTAs
- Navigation with 20+ items

THE RESULT:
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Header with everything

[Feature 1] [Feature 2] [Feature 3] [Feature 4]
[Feature 5] [Feature 6] [Feature 7] [Feature 8]
[Feature 9] [And more...] [See all] [...]

Every element screaming for attention = none get it

THE FIX:
1. Hierarchy: 3 levels max visible at once
2. Progressive disclosure: Show more as needed
3. Smart defaults: Most users never change settings
4. Personas: Design for the 80% use case
5. Say no: Not every request deserves a button
```

**Why It's Wrong:**
- Paradox of choice paralyzes users
- Increased cognitive load
- Nothing feels important
- Power users can't find things either
- Maintenance nightmare

---

## 8. The Pixel Perfect Obsession

**The Mistake:**
```
Spending days perfecting static designs that break in reality.

WHAT DESIGNERS OBSESS OVER:
- Perfect spacing in one viewport
- Ideal content length
- Specific image dimensions
- Beautiful but fragile layouts

WHAT REALITY DELIVERS:
- Variable content lengths (names, titles)
- User-generated content (any length)
- Different viewport sizes
- Different browsers/devices
- Zoom and text scaling
- Translated content (German is 30% longer)

THE FIX:
1. Design with real content
   Use actual data, not "Lorem ipsum"

2. Test extremes
   What if the name is "X"?
   What if it's 40 characters?

3. Build in flexibility
   Min-width, max-width, truncation

4. Design in browser
   Responsive from the start

5. Accept imperfection
   Consistent systems > pixel-perfect one-offs
```

**Why It's Wrong:**
- The design breaks immediately in production
- Developers make impossible trade-offs
- Real content doesn't match mockups
- Maintenance becomes whack-a-mole

---

## 9. The Trendy Traps

**The Mistake:**
```
Following design trends without considering usability.

TREND → PROBLEM:

"Neumorphism" (soft 3D emboss)
→ Low contrast, poor accessibility

"Glassmorphism" (frosted glass)
→ Performance issues, contrast depends on background

"Ultra-thin fonts"
→ Unreadable, especially on Windows

"Low contrast aesthetic"
→ Accessibility failure

"Hidden navigation"
→ Discoverability death

"Full-bleed hero video"
→ Performance, distraction, data usage

"Brutalism"
→ Unusable for actual tasks

THE RULE:
Can you use this trend AND maintain:
- WCAG AA contrast (4.5:1)?
- Clear hierarchy?
- Obvious interactions?
- Good performance?
- Cross-device compatibility?

If no, skip the trend.
```

**Why It's Wrong:**
- Trends are optimized for awards, not users
- Usually sacrifices accessibility
- Ages poorly (looks dated quickly)
- Solves designer problems, not user problems

---

## 10. The One-Size-Fits-None

**The Mistake:**
```
Same exact UI for mobile, tablet, and desktop.

MOBILE PROBLEMS:
- Touch targets too small (hover-sized elements)
- Too much information density
- Horizontal scrolling
- Tiny text
- Unreachable navigation

DESKTOP PROBLEMS:
- Elements too large (mobile-sized)
- Single column wasting space
- Touch-sized buttons look childish
- Missing efficiency features
- Unused screen real estate

THE FIX:
Design for mobile first, then enhance for desktop.

MOBILE-SPECIFIC:
- Bottom navigation (thumb zone)
- Full-width buttons
- Stacked layouts
- Touch-sized targets (44px+)
- Simplified information

DESKTOP-SPECIFIC:
- Horizontal navigation
- Multi-column layouts
- Hover states
- Keyboard shortcuts
- Information density
```

**Why It's Wrong:**
- Each device has different affordances
- Touch vs. cursor requires different targets
- Screen real estate varies 10x
- Context of use differs

---

## 11. The Notification Nightmare

**The Mistake:**
```
Overusing notifications, badges, and alerts.

THE NOISE:
🔴 (17) Messages
🔴 (3) Notifications
🔴 (5) Updates
🔔 New feature!
💡 Tip: Did you know...
⚠️ Complete your profile
📢 Limited time offer!

User learns to ignore everything.

NOTIFICATION HIERARCHY:
CRITICAL (always interrupt):
- Security alerts
- Transaction confirmations
- Destructive action warnings

IMPORTANT (badge only):
- New messages
- Direct mentions
- Required actions

INFORMATIONAL (in-app only):
- Feature announcements
- Tips and suggestions
- Marketing

NONE (don't notify):
- Someone you don't follow posted
- Weekly newsletter available
- Similar items in stock

THE FIX:
1. Categorize all notifications
2. Aggressive default opt-outs
3. Easy granular controls
4. Respect user preferences
5. Batch non-urgent items
```

**Why It's Wrong:**
- Creates notification fatigue
- Important alerts get ignored
- Users disable all notifications
- Brand becomes annoying

---

## 12. The False Consistency

**The Mistake:**
```
Applying the same pattern everywhere, even where it hurts.

EXAMPLES:

"All buttons must be blue"
→ Destructive action in blue looks safe

"All forms have same layout"
→ Login form has unnecessary complexity

"All cards look the same"
→ Actionable cards look like info cards

"Same nav everywhere"
→ Full nav during checkout is distracting

"Consistent empty states"
→ Same illustration doesn't help context

THE REALITY:
Consistency is a means, not an end.
The goal is predictability for users.

WHEN TO BREAK CONSISTENCY:
- Destructive actions (should feel different)
- Focused flows (checkout, onboarding)
- Error states (should stand out)
- Celebrations (should feel special)
- Different user contexts

WHAT TO KEEP CONSISTENT:
- Interaction patterns (how things work)
- Language and tone
- Core visual elements (logo, primary colors)
- Spacing and layout systems
- Navigation location
```

**Why It's Wrong:**
- Hurts usability in specific contexts
- Important things don't stand out
- Forces patterns where they don't fit
- Design for process, not for users

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `design/ui-design/anti-patterns.md`
