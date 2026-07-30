---
name: native-module
description: "Create a React Native native module to bridge platform-specific functionality."
category: frontend-and-design
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/react-native-dev/commands/native-module.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/react-native-dev/commands/native-module.md
---


Create a React Native native module to bridge platform-specific functionality.

## Steps


1. Define the native module interface:
2. Create the TypeScript interface:
3. Implement the iOS native code (Swift/Objective-C):
4. Implement the Android native code (Kotlin/Java):
5. Handle platform differences:
6. Test the module on both platforms.
7. Document the module API and usage.

## Format


```
Module: <name>
Methods:
  - <method>(params): <return type>
Events:
```


## Rules

- Always provide TypeScript types for the module interface.
- Handle errors consistently across both platforms.
- Use promises over callbacks for async operations.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/react-native-dev/commands/native-module.md`
