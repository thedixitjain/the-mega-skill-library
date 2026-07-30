---
name: template
description: "Save and reuse successful video templates including scripts, thumbnails,..."
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/packages/creator-studio-pack/plugins/workflow-optimization/template-library/commands/template.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/packages/creator-studio-pack/plugins/workflow-optimization/template-library/commands/template.md
---

# Template Library Command

Save successful video formats as reusable templates to streamline content creation and maintain consistency.

## Usage

```bash
/template save [video-url]                   # Save video as template
/template list                               # View all templates
/template use [template-name]                # Use template for new video
/template create [template-name]             # Create custom template
/template analyze                            # Find your best-performing formats
```

## Purpose

Streamline production by:

- **Reusing successful formats** - Don't reinvent the wheel
- **Maintaining consistency** - Brand identity across videos
- **Faster production** - Templates speed up creation
- **Quality assurance** - Proven formulas that work
- **Knowledge preservation** - Document what works

## Template Types

### Video Format Templates

```
📹 VIDEO FORMAT TEMPLATE

Name: "Transformation Story"
Performance: 9.2/10 avg CTR, 68% retention
Use Cases: Before/after, results-focused content

Structure:
├─ Hook (0:00-0:15): Show shocking result
├─ Problem Setup (0:15-2:00): Why it was broken
├─ Journey (2:00-8:00): How you fixed it
├─ Results (8:00-9:30): Before/after comparison
└─ CTA (9:30-10:00): What viewers should do next

Title Formula: "I [Action] [Thing] [Number]x [Result]"
Example: "I Made My API 11x Faster"

Thumbnail Style:
├─ Layout: Before/After split screen
├─ Text: Large metric in center (11x)
├─ Face: Excited expression, 35% of frame
└─ Colors: Problem red → Success green

Script Tone: Personal, enthusiastic, specific
Length Target: 8-12 minutes
Music: Upbeat, energetic background
Editing Style: Fast-paced, jump cuts every 3-5 seconds

Ready to use for your next transformation video!
```

### Title Templates

```
📝 TITLE TEMPLATES

Template 1: Transformation
"I [Action] My [Thing] From [Bad] to [Good]"
├─ Example: "I Made My API 11x Faster"
├─ CTR: 9.2% avg
└─ Use when: You have specific before/after results

Template 2: Comparison
"[Thing A] vs [Thing B]: Which is [Better]?"
├─ Example: "Redis vs Memcached: Which is Faster?"
├─ CTR: 7.8% avg
└─ Use when: Comparing tools or approaches

Template 3: Problem/Solution
"Why [Problem] (And How to Fix It)"
├─ Example: "Why Your API is Slow (And How to Fix It)"
├─ CTR: 6.9% avg
└─ Use when: Addressing common pain points

Template 4: Time Challenge
"[Do Thing] in [Short Time]"
├─ Example: "Add Redis Caching in 15 Minutes"
├─ CTR: 5.4% avg
└─ Use when: Quick tutorials, fast implementations

Template 5: Secret Reveal
"The [Adjective] Secret to [Outcome]"
├─ Example: "The Simple Secret to Fast APIs"
├─ CTR: 7.2% avg
└─ Use when: Non-obvious solutions, unique insights
```

### Thumbnail Templates

```
🎨 THUMBNAIL TEMPLATES

Template: "Before/After Performance"
├─ Left side: "SLOW" + bad metric (red)
├─ Right side: "FAST" + good metric (green)
├─ Center: Large arrow or "10x" text
├─ Your face: Corner, excited expression
├─ Font: Impact Bold, 96pt
└─ Performance: 9.2% CTR avg

Template: "VS Comparison"
├─ Left: Tool A logo + name
├─ Right: Tool B logo + name
├─ Center: "VS" with lightning
├─ Bottom: "Speed Test" or key metric
├─ Font: Montserrat Bold
└─ Performance: 7.8% CTR avg

Template: "Problem Alert"
├─ Top: "YOUR API IS SLOW" (red, alert style)
├─ Middle: Your concerned face (large)
├─ Bottom: "HERE'S WHY" (yellow)
├─ Background: Dark, attention-grabbing
└─ Performance: 6.9% CTR avg

Template: "Simple Text"
├─ Background: Solid color or subtle gradient
├─ Text: "15 MINUTES" or key hook
├─ Subtext: Topic description
├─ Clean, minimal, professional
└─ Performance: 5.4% CTR avg
```

### Script Templates

```
📄 SCRIPT TEMPLATE: Transformation Story

[HOOK - 0:00-0:15]
"[Shocking result statement]. In this video, I'm going to show you exactly how I [accomplished thing] in just [timeframe]."

[PROBLEM SETUP - 0:15-2:00]
"So here's the situation. I had [problem description]. It was [impact on users/business]. I tried [failed attempt 1] and [failed attempt 2], but nothing worked. Then I discovered [solution]."

[JOURNEY - 2:00-8:00]
"Let me walk you through exactly what I did.

Step 1: [First action taken]
[Show screen recording, explain reasoning]

Step 2: [Second action]
[Demo, code examples, explain why]

Step 3: [Implementation]
[Live walkthrough, gotchas, tips]"

[RESULTS - 8:00-9:30]
"And here are the results. Before: [bad metric]. After: [good metric]. That's a [percentage] improvement.

Let me show you the difference. [Side-by-side comparison, graphs, data]

This took me [timeframe] to implement, and it's been running in production for [duration] with zero issues."

[CTA - 9:30-10:00]
"If you want to [accomplish same thing], I've put all the code in the description along with [resource].

Got questions? Drop them in the comments.

And if you found this helpful, hit that subscribe button for more [content type].

Thanks for watching, and I'll see you in the next one!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Estimated Length: 10 minutes
Tone: Enthusiastic, helpful, specific
Energy: High throughout
Pacing: 130-140 words per minute
```

### Editing Templates

```
✂️ EDITING TEMPLATE: High-Energy Tutorial

Video Style: Fast-paced, engaging, tutorial
Target Length: 8-12 minutes
Retention Goal: 65%+

Timeline Structure:
├─ Video Track 1: Main footage (A-roll)
├─ Video Track 2: Screen recordings (B-roll)
├─ Video Track 3: Graphics, text overlays
├─ Audio Track 1: Voice (primary)
├─ Audio Track 2: Music (background)
└─ Audio Track 3: Sound effects

Editing Decisions:
├─ Cut silence >2 seconds
├─ Remove "um, uh" filler words
├─ Jump cuts every 3-5 seconds
├─ Speed up to 1.2x for slow sections
├─ Add zoom in/out for emphasis (8-10 times per video)
├─ Transition: Quick cuts (no fancy transitions)
└─ Color grade: Cinematic LUT preset

Audio Mix:
├─ Voice: -14 LUFS (primary)
├─ Music: -24 LUFS (12dB below voice)
├─ Sidechain: Music ducks -12dB when speaking
└─ Sound effects: -10 LUFS (occasional)

Graphics:
├─ Lower third: Intro at 0:05 (name, channel)
├─ Subtitles: Burned-in, full video
├─ Call-outs: Key points highlighted on screen
├─ Chapter markers: Every 2-3 minutes
└─ End screen: Last 20 seconds

Render Settings:
├─ Format: MP4 (H.264)
├─ Resolution: 1920x1080
├─ Framerate: 30fps
├─ Bitrate: 10Mbps
└─ Audio: AAC 320kbps

Export time: ~30 minutes per 10-minute video
```

## Using Templates

When user runs `/template use transformation-story`:

```
🎬 USING TEMPLATE: Transformation Story

Loading template...

Template Applied:
✓ Video structure loaded
✓ Title formula ready
✓ Thumbnail style set
✓ Script template opened
✓ Editing preset configured

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FILL IN YOUR DETAILS:

Title:
"I [your action] My [thing] [metric]x [result]"
Example: "I Made My API 11x Faster"
Your title: ________________________________

Thumbnail Text:
Before metric: _____ → After metric: _____
Main text: ________________________________

Script Variables:
├─ Problem: _________________________________
├─ Solution: ________________________________
├─ Timeframe: _______________________________
├─ Result metric: ___________________________
└─ Key steps: (3-5 main steps)
    1. _____________________________________
    2. _____________________________________
    3. _____________________________________

Video Length Target: 8-12 minutes
Estimated Production Time: 4 hours
Expected CTR: 8-10%
Expected Retention: 65-70%

Ready to record when you are!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Template Analysis

When user runs `/template analyze`:

```
📊 TEMPLATE PERFORMANCE ANALYSIS

Analyzing your last 20 videos...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP PERFORMING TEMPLATES:

#1: Transformation Story ⭐⭐⭐⭐⭐
├─ Videos using this: 5
├─ Avg CTR: 9.2%
├─ Avg Retention: 68%
├─ Avg Views: 98,000
└─ Recommendation: Use for all before/after content

#2: Tool Comparison ⭐⭐⭐⭐
├─ Videos using this: 3
├─ Avg CTR: 7.8%
├─ Avg Retention: 62%
├─ Avg Views: 72,000
└─ Recommendation: Great for "X vs Y" topics

#3: Problem/Solution ⭐⭐⭐⭐
├─ Videos using this: 4
├─ Avg CTR: 6.9%
├─ Avg Retention: 64%
├─ Avg Views: 64,000
└─ Recommendation: Use for educational content

UNDERPERFORMING TEMPLATES:

#4: Tips/Lists ⭐⭐
├─ Videos using this: 3
├─ Avg CTR: 4.2%
├─ Avg Retention: 52%
├─ Avg Views: 28,000
└─ Recommendation: Avoid or significantly improve format

#5: Generic Tutorial ⭐⭐
├─ Videos using this: 5
├─ Avg CTR: 3.8%
├─ Avg Retention: 48%
├─ Avg Views: 22,000
└─ Recommendation: Replace with Transformation Story template

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATIONS:

✓ Use Transformation Story for next 5 videos
✓ Retire Generic Tutorial template
✓ Create more Tool Comparison videos
✓ Test new "Secret Reveal" template
✓ Update Tips/Lists format or discontinue

Potential Impact:
├─ Switch from Generic → Transformation: +142% views
├─ Use top 3 templates only: +76% avg performance
└─ Estimated new avg views: 78K per video (up from 52K)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Integration Points

Works with other Creator Studio plugins:

- **batch-recording-scheduler**: Load templates for batch sessions
- **script-writer-pro**: Generate scripts from templates
- **thumbnail-designer**: Apply thumbnail templates
- **video-editor-ai**: Load editing templates
- **analytics-insights**: Track template performance

## Best Practices

### Template Creation

1. **Start with winners** - Template your best-performing videos
2. **Document everything** - Capture all elements (title, thumbnail, structure)
3. **Test variations** - A/B test template elements
4. **Update regularly** - Refine based on performance data
5. **Keep it flexible** - Templates guide, not constrain

### Template Usage

1. **Don't copy blindly** - Adapt to specific content
2. **Maintain creativity** - Use as starting point, not straitjacket
3. **Test new formats** - Don't rely on templates forever
4. **Track performance** - Validate templates with data
5. **Share templates** - Help other creators (build community)

Your goal: Codify successful formats into reusable templates that maintain quality while speeding up production.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/packages/creator-studio-pack/plugins/workflow-optimization/template-library/commands/template.md`
