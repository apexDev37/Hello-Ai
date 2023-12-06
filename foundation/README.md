# I. Foundations

> This directory includes foundation demos that leverage Langchain core components.

#### Core Components covered

- Models
- Prompts
- Parsers

## Demos

> Navigate through the demo scripts for various implementations using the OpenAI Models.

| Name             | Script       | Description                                                                         |
| ---------------- | ------------ | ----------------------------------------------------------------------------------- |
| Greeting-Checker | `demo-01.py` | Determines whether a "greeting" is formal, recognized, and offers meta data for it. |

- Prompt

```python
"""
Analyze the text enclosed in backticks to identify whether it constitutes a typical and formal greeting.
If the text is indeed a greeting, provide information on the language it is in, three synonyms for the greeting, and specify five countries where it is commonly used.

If the text is not a greeting, kindly suggest three universally recognized and formal greetings from around the world at random.
Text: `{customer_greeting}`
"""
```

- Response

```python
"""
The provided text "`hello`" is a common and formal greeting in English.

Language: English

Synonyms:
1. Hi
2. Greetings
3. Good day

Countries where it is commonly used:
1. United States
2. United Kingdom
3. Canada
4. Australia
5. New Zealand
"""
```

| Name        | Script       | Description                                                                                                                          |
| ----------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Holy-Prompt | `demo-02.py` | Analyzes a user's prompt input, transforms it, and prompts the LLM using the AI's optimally engineered version of the user's prompt. |

- Example

```python

# User prompt input
[prompt] >>> Give the difference between flake8 and pylint.

# LLM optimized prompt
{'ai_prompt': 'Explain the distinctions between flake8 and pylint, including their purposes, features, and use cases.'}

------------------------------------------------------

# User prompt input
[prompt] >>> Write a poem about a sunset.

# LLM optimized prompt
{'ai_prompt': 'Craft a captivating poem that evokes the beauty and tranquility of a sunset. Use vivid imagery and descriptive language to paint a picture of the sun\'s descent, the fading hues of the sky, and the serene ambiance of the twilight hour. Consider incorporating metaphors, similes, and personification to enhance the emotional impact of the poem. Remember, the goal is to create a poem that resonates with readers and leaves a lasting impression.'}
```
