---
name: ner-extractor-start-chathttpsgptcallnetchathtmldata7b22contact22
description: "This prompt is all about the extraction of the Named Entities from the specified content"
category: prompt-engineering
source_repo: friuns2/BlackFriday-GPTs-Prompts
source_path: "gpts/ner-extractor.md"
source_url: https://github.com/friuns2/BlackFriday-GPTs-Prompts/blob/HEAD/gpts/ner-extractor.md
---


# NER Extractor | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%222tOUF5oANEQ_DWOXgCy_y%22%2C%22flow%22%3Atrue%7D%7D)
This prompt is all about the extraction of the Named Entities from the specified content

# Prompt

```
Extract the NER with the score in JSON format from the following content

{{ content }}
```

## Welcome Message
Here is the Named Entity Recognition (NER) entities and their scores in JSON format from the given content:



```

{

  "entities": [

    {

      "entity": "GPT models",

      "type": "ORG",

      "score": 0.89

    },

    {

      "entity": "DevOps",

      "type": "MISC",

      "score": 0.82

    },

    {

      "entity": "GPT-J",

      "type": "ORG",

      "score": 0.98

    },

    {

      "entity": "CPU",

      "type": "PRODUCT",

      "score": 0.89

    },

    {

      "entity": "GPU",

      "type": "PRODUCT",

      "score": 0.92

    },

    {

      "entity": "NVIDIA",

      "type": "ORG",

      "score": 0.95

    },

    {

      "entity": "RTX A6000",

      "type": "PRODUCT",

      "score": 0.97

    },

    {

      "entity": "A40",

      "type": "PRODUCT",

      "score": 0.94

    }

  ]

}

```

## Conversation

**ASSISTANT**: Here is the Named Entity Recognition (NER) entities and their scores in JSON format from the given content:



```

{

  "entities": [

    {

      "entity": "GPT models",

      "type": "ORG",

      "score": 0.89

    },

    {

      "entity": "DevOps",

      "type": "MISC",

      "score": 0.82

    },

    {

      "entity": "GPT-J",

      "type": "ORG",

      "score": 0.98

    },

    {

      "entity": "CPU",

      "type": "PRODUCT",

      "score": 0.89

    },

    {

      "entity": "GPU",

      "type": "PRODUCT",

      "score": 0.92

    },

    {

      "entity": "NVIDIA",

      "type": "ORG",

      "score": 0.95

    },

    {

      "entity": "RTX A6000",

      "type": "PRODUCT",

      "score": 0.97

    },

    {

      "entity": "A40",

      "type": "PRODUCT",

      "score": 0.94

    }

  ]

}

```

---

**Source:** [`friuns2/BlackFriday-GPTs-Prompts`](https://github.com/friuns2/BlackFriday-GPTs-Prompts) → `gpts/ner-extractor.md`
