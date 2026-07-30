---
name: emotion-prompting
description: "Authored by Kalyan KS. You can follow me on Twitter and LinkedIn for latest LLM, RAG and Agent updates."
category: prompt-engineering
source_repo: KalyanKS-NLP/Prompt-Engineering-Techniques-Hub
source_path: "Basic_Prompt_Engineering_Techniques/Emotion_Prompting.md"
source_url: https://github.com/KalyanKS-NLP/Prompt-Engineering-Techniques-Hub/blob/HEAD/Basic_Prompt_Engineering_Techniques/Emotion_Prompting.md
---
# **Emotion Prompting**

Authored by Kalyan KS. You can follow me on [Twitter](https://x.com/kalyan_kpl) and [LinkedIn](https://www.linkedin.com/in/kalyanksnlp/) for latest LLM, RAG and Agent updates.

## **Overview**

Emotion prompting is a prompting technique where — instead of using a dry or purely neutral instruction — you add emotionally-charged phrases  to the prompt so that a large language model (LLM) responds with better outputs. It’s like asking, *“Write a summary of this article,”* but adding something like “This is very important to my career,”. In simple words, emotion prompting means prompting with the main instruction plus an emotional appeal. 

Emotion prompting is like a teacher telling a student: *“Do this problem — and remember, doing well on this matters a lot for your future,”* instead of simply saying *“Do this problem.”*

## **Stay Updated with Generative AI, LLMs, Agents and RAG**

Join 🚀 [**AIxFunda** free newsletter](https://aixfunda.substack.com/) to get *latest updates* and *interesting tutorials* related to Generative AI, LLMs, Agents and RAG. 
- ✨ Weekly GenAI updates
- 📄 Weekly LLM, Agents and RAG research paper updates
- 📝 1 fresh blog post on an interesting topic every week

## **Implementation (News headlines classification)**

Here is the implementation of emotion prompting for news headlines classification.

```python
# !pip install langchain langchain-google-genai pydantic

import os
from google.colab import userdata
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# 1. Set your API key
os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# 2. Pydantic schema (single output field)
class EmotionPromptClassifyResponse(BaseModel):
    predicted_label: str = Field(..., description="Predicted news category")

# 3. Parser
parser = PydanticOutputParser(pydantic_object=EmotionPromptClassifyResponse)

# 4. Initialize model
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    temperature=0
)

# 5. Emotion prompting template (concise)
prompt_template = ChatPromptTemplate.from_template(
    """
Classify the following news headline into one of:
["Politics", "Sports", "Business", "Technology", "Entertainment", "Health", "World"]

This is very important to my career.

Headline: {headline}

Output JSON:
{format_instructions}
"""
)

# 6. Inject parser instructions
prompt = prompt_template.partial(format_instructions=parser.get_format_instructions())

# 7. Chain
chain = prompt | model | parser

# 8. Example headline
headline = "Government approves new policy to boost semiconductor manufacturing."

# 9. Invoke
result = chain.invoke({"headline": headline})

# 10. Display result
print("\n--- Predicted Label ---\n", result.predicted_label)
```
Here the output is
```
--- Predicted Label ---
 Politics
```

## **Implementation (Key phrases extraction)**

Here is the implementation of emotion prompting for key phrases extraction.

```python
# !pip install langchain langchain-google-genai pydantic

import os
from google.colab import userdata
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# 1. Set your API key
os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# 2. Pydantic schema for key phrase extraction
class EmotionPromptKeyphrasesResponse(BaseModel):
    key_phrases: List[str] = Field(..., description="List of extracted key phrases")

# 3. Create parser
parser = PydanticOutputParser(pydantic_object=EmotionPromptKeyphrasesResponse)

# 4. Initialize model
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    temperature=0
)

# 5. Emotion prompting template (concise)
prompt_template = ChatPromptTemplate.from_template(
    """
Extract the key phrases from the following text. Key phrases should be meaningful, concise, and capture the core concepts.
This is very important to my career.

Text: {text}

Output JSON:
{format_instructions}
"""
)

# 6. Inject parser instructions
prompt = prompt_template.partial(format_instructions=parser.get_format_instructions())

# 7. Chain
chain = prompt | model | parser

# 8. Example text
text = """The government has introduced a comprehensive plan to support renewable energy innovation.
The initiative focuses on funding solar, wind, and battery storage research programs.
Officials believe this effort will significantly accelerate the nation's clean energy transition."""

# 9. Invoke
result = chain.invoke({"text": text})

# 10. Display result
print("\n--- Extracted Key Phrases ---\n", result.key_phrases)
```

Here the output is
```
--- Extracted Key Phrases ---
 ['government plan', 'renewable energy innovation', 'funding research programs', 'solar, wind, and battery storage', 'clean energy transition']
```

---

**Source:** [`KalyanKS-NLP/Prompt-Engineering-Techniques-Hub`](https://github.com/KalyanKS-NLP/Prompt-Engineering-Techniques-Hub) → `Basic_Prompt_Engineering_Techniques/Emotion_Prompting.md`
