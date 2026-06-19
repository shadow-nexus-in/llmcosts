# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed to cater to a wide range of applications. This model is not open-source, indicating that its internal workings and training data are proprietary to Mistral AI. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is capable of handling complex and lengthy inputs, making it suitable for tasks that require in-depth analysis and generation.

### Technical Capabilities and Pricing
Mistral Medium 3 boasts a diverse set of capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores, with an MMLU score of 80.0, HumanEval score of 77.5, and an LMSYS Arena ELO rating of 1200. The model is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $1.2, while 100,000 calls would amount to $120.0. Compared to its competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a balanced pricing structure that aligns with its performance capabilities.

### Use Cases and Competitiveness
Mistral Medium 3 is best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. However, it may not be the optimal choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring sub-100ms response times. In comparison to its top competitors, Mistral Medium

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can help reduce the overall cost per call. However, the cost savings from batching are limited to the input tokens, as output tokens are still charged at **$2.0 per 1M tokens**.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per call:
* **1,000 calls**: **$1.2 / 1,000 = $0.0012 per call**
* **10,000 calls**: **$12.0 / 10,000 = $0.0012 per call**
* **100,000 calls**: **$120.0 / 100,000 = $0.0012 per call**

The

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Model Overview
The Mistral Medium 3 model, provided by Mistral AI, was released on 2025-04-17. It is a mid-tier model, not open source, with the following pricing:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0. This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 77.5. This score evaluates the model's ability to write correct and functional code in response to programming prompts. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200. This score measures the model's performance in a competitive arena, where it is pitted against other models in various tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score (80.0) suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of language, such as **text analysis**, **summarization**, and **content generation**.
* The high HumanEval score (77.5) indicates that the model is capable of generating correct and functional code, making it a good choice for **coding** and **function calling** tasks.


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their price differences, performance trade-offs, and use cases.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% increase over Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% increase over Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% decrease from Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% decrease from Mistral Medium 3)

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3's benchmarks suggest a strong performance in coding, analysis, and other tasks.

#### Capabilities and Use Cases
Mistral Medium 3 offers a wide range of capabilities, including:
* Text, vision, function calling, JSON mode, streaming, and system prompts
* Best for: coding, analysis, RAG, summarization, vision tasks, content generation, and function calling
* Not good for: frontier reasoning, bulk cheap tasks, simple classification, and real-time sub-100ms tasks

In contrast, Claude 3.5 Haiku and GPT-4o Mini may have different strengths and weaknesses,

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a wide range of capabilities, including text, vision, function calling, and more. Given its features and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for applications that require in-depth code review or generation. For example, you can use Mistral Medium 3 with OpenRouter to analyze code snippets and provide suggestions for improvement.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a code snippet for analysis
code_snippet = """
def add(a, b):
    return a + b
"""

# Use Mistral Medium 3 to analyze the code snippet
analysis = model.analyze_code(code_snippet)

# Print the analysis results
print(analysis)
```
#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as generating articles, blog posts, or social media content. You can use OpenRouter to integrate Mistral Medium 3 into your content generation pipeline.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a topic for content generation
topic = "Artificial Intelligence"

# Use Mistral Medium 3 to generate content
content = model.generate_content(topic)

# Print the generated content
print(content)
```
#### 3. **Vision Tasks**
Mistral Medium 3 has capabilities in vision tasks, such as image classification, object detection, and image generation. You can use OpenRouter to integrate Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
