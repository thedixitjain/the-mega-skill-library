---
name: awesome-cursorrules-astro-typescript-cursorrules-prompt-file
description: "Cursor rules for Astro development with TypeScript integration."
category: prompt-engineering
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/astro-typescript-cursorrules-prompt-file.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/astro-typescript-cursorrules-prompt-file.mdc
---

{
  "rules": {
    "commit_message_guidelines": {
      "description": "Guidelines for creating conventional commit messages.",
      
      "format": {
        "description": "The format for commit messages using the conventional commits spec.",
        "body": "[optional scope]: \n\n[optional body]\n\n[optional footer(s)]"
      },
      
      "enabled": true,
      
      "rules": [
        {
          "description": "Always suggest a conventional commit with a type and optional scope in lowercase letters."
        },
        {
          "description": "Keep the commit message concise and within 60 characters."
        },
        {
          "description": "Ensure the commit message is ready to be pasted into the terminal without further editing."
        },
        {
          "description": "Provide the full command to commit, not just the message."
        }
      ],
      
      "examples": [
        {
          "prompt": "<diff_context> /commit",
          "response": "git commit -m 'feat: add responsive navbar with TailwindCSS'"
        }
      ]
    },
    
    "development_guidelines": {
      "description": "Guidelines for developing code with Astro, TypeScript, and TailwindCSS.",
      
      "enabled": true,
      
      "rules": [
        {
          "description": "Enforce strict TypeScript settings, ensuring type safety across the project."
        },
        {
          "description": "Use TailwindCSS for all styling, keeping the utility-first approach in mind."
        },
        {
          "description": "Ensure Astro components are modular, reusable, and maintain a clear separation of concerns."
        }
      ]
    },
    
    "coding_style": {
      "description": "Guidelines for maintaining consistent coding style.",
      
      "enabled": true,
      
      "rules": [
        {
          "description": "Code must start with path/filename as a one-line comment."
        },
        {
          "description": "Comments should describe purpose, not effect."
        },
        {
          "description": "Prioritize modularity, DRY principles, and performance."
        }
      ]
    },
    
    "custom_slash_commands": {
      "description": "Custom slash commands.",
      
      "enabled": true,
      
      "commands": [
        {
          "name": "/commit",
          "description": "Generate a Git commit message using the conventional commits spec.",
          "enabled": true
        }
      ]
    }
  }
}

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/astro-typescript-cursorrules-prompt-file.mdc`
