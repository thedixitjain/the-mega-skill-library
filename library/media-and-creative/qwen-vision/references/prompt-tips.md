# Prompt tips for Qwen video/image analysis

## General principles

- Be specific about what you want described. "Analyze this video" gives vague results. "Describe the character's body movement, arm positions, and weight shifts frame by frame" gives useful results.
- Ask for structured output (JSON, numbered lists) when you need to parse the response programmatically.
- Mention what to ignore if the video has irrelevant elements (e.g., "ignore the background, focus on the person's gestures").

## Video analysis prompts

### Motion/animation analysis
```
Describe the character's body movement in detail:
1. Starting pose
2. Transition movement
3. Main action/loop
4. Hand and arm positions
5. Weight distribution and shifts
6. Head movement
Ignore facial expressions and eye movement.
```

### Scene composition
```
Analyze the visual composition:
- Camera angle and movement
- Lighting setup (key, fill, rim)
- Color palette and mood
- Depth of field and focus
- Subject placement in frame
```

### Technical quality
```
Evaluate the technical quality of this generated video:
- Motion smoothness and consistency
- Artifact presence (flickering, morphing, distortion)
- Temporal coherence (do objects maintain shape between frames?)
- Hand/finger quality
- Face consistency
Rate overall quality 1-10 with explanation.
```

### Comparison
When comparing multiple videos, analyze them sequentially and ask Qwen to compare:
```
I'll show you video clips of the same character performing similar actions.
For each, describe the motion quality, smoothness, and naturalness.
Then rank them from best to worst as animation references.
```

## Image analysis prompts

### UI/screenshot analysis
```
List all UI elements visible in this screenshot:
- Navigation elements
- Content areas
- Interactive controls
- Text content (transcribe accurately)
- Visual hierarchy
```

### Reference image analysis
```
Describe this character reference image in detail:
- Body proportions and pose
- Clothing and accessories
- Art style and rendering technique
- Color palette
- Distinguishing features
```

## Output format tips

For machine-readable results, always end your prompt with:
```
Respond in this exact JSON format:
{ ... your schema ... }
Return ONLY the JSON, no other text.
```

For human-readable results, ask for markdown with headers.
