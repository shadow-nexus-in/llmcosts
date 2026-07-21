# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require complex text understanding and generation. The model's architecture supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use-Cases
Mistral Medium 3 excels in tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The model's pricing is competitive, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0.

### Comparison and Cost Considerations
When compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of capabilities and pricing. While Claude 3.5 Haiku charges $0.8/1M input and $4.0/1M output, and GPT-4o Mini charges $0.15/1M input and $0.6/1M output, Mistral Medium 3 provides a more comprehensive set

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it is optimal to use:
* **Cached tokens** when possible, as they are free. This can significantly reduce costs for repeated input sequences.
* **Batch API calls** to take advantage of the free batch input pricing. This can lead to substantial cost savings for large-scale applications.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls** (avg 500 tokens): $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the input and output pricing, we can estimate the costs:
* 1,000 calls: (500,000 tokens / 1,000,000) \* $0.4 (input) + (500,000 tokens / 1,000,000) \* $2

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
- Input: $0.4 per 1M tokens
- Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to understand and generate human-like text across a wide range of tasks. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
- **HumanEval**: 77.5
  - HumanEval evaluates a model's ability to write correct and functional code based on human-written prompts. A higher score indicates better coding capabilities. With a score of 77.5, Mistral Medium 3 shows strong coding abilities, making it suitable for tasks like coding and function calling.
- **LMSYS Arena ELO**: 1200
  - LMSYS Arena ELO measures a model's competitive performance in a variety of tasks, with higher scores indicating better performance. An ELO score of 1200 suggests that Mistral Medium 3 has a moderate level of competitiveness in real-world applications.

#### Real-World Implications
The benchmark scores indicate that Mistral Medium 3 is well-suited for tasks that require strong language understanding, coding abilities, and moderate competitiveness. Specifically

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini, on the other hand, is significantly cheaper for input but also for output.

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Without direct comparisons of benchmarks for Claude 3.5 Haiku and GPT-4o Mini, it's challenging to assess their performance relative to Mistral Medium 3. However, Mistral Medium 3's scores indicate strong capabilities in coding and analysis tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
*

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for developers and data analysts. You can use it to generate code snippets, analyze data, and even create custom functions.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Generate code snippet
code = model.generate_code("Create a Python function to calculate the area of a rectangle")
print(code)
```

#### 2. **Summarization and Content Generation**
With its strong text capabilities, Mistral Medium 3 is perfect for summarization and content generation tasks. You can use it to summarize long documents, generate articles, or even create social media posts.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Summarize a document
summary = model.summarize("This is a long document that needs to be summarized")
print(summary)
```

#### 3. **Vision Tasks**
Mistral Medium 3 also has vision capabilities, making it suitable for tasks such as image classification, object detection, and image generation.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Classify an image
image = "path/to/image.jpg"
classification = model.classify_image(image)
print(classification)
```

#### 4. **RAG (Retrieval-Augmented Generation)**
Mistral Medium

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
