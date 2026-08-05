# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require in-depth analysis and generation of content. The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and content generation. With a high MMLU score of 80.0 and a HumanEval score of 77.5, this model has demonstrated its proficiency in understanding and generating human-like code. Additionally, its LMSYS Arena ELO score of 1200 indicates a high level of competence in solving problems. The primary use cases for Mistral Medium 3 include coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times.

### Pricing and Cost Examples
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. The cost of using this model can be estimated based on the number of calls and tokens used. For example, 1,000 calls with an average of 500 tokens per call would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source. The model has a context window of 131,072 tokens and a maximum output of 16,384 tokens, with a knowledge cutoff of 2024-11.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, so it is always beneficial to use cached tokens when possible. This can significantly reduce the cost of API calls, especially for repeated or similar inputs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce the overall cost. However, the cost savings from batch API calls only apply to the input tokens, and the output tokens are still charged at $2.0 per 1M tokens.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per 1M tokens + Output cost per 1M tokens) / 1,000,000

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500)

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Analysis
#### Overview
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on April 17, 2025. This model is not open-source and has a specific pricing structure for input and output tokens.

#### Pricing Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmark Performance
Mistral Medium 3 has the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval: 77.5** - The HumanEval benchmark assesses a model's ability to generate code that is both correct and readable. A higher score indicates better coding abilities.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive choice for various applications. This guide outlines the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it ideal for code review, generation, and analysis. Its `function_calling` capability allows for seamless integration with external libraries and APIs.
2. **Summarization and Content Generation**: With its strong text processing capabilities, Mistral Medium 3 is well-suited for summarization, content generation, and text analysis tasks.
3. **Vision Tasks**: Mistral Medium 3's `vision` capability enables it to process and understand visual data, making it a great choice for image classification, object detection, and other computer vision tasks.
4. **RAG (Retrieval-Augmented Generation)**: Mistral Medium 3's `rag` capability allows it to retrieve relevant information from external knowledge sources, making it ideal for tasks that require extensive knowledge retrieval.
5. **System Prompts and Streaming**: With its `system_prompts` and `streaming` capabilities, Mistral Medium 3 can handle complex system prompts and process large amounts of data in real-time.

### Code Integration Example with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Define a function to generate code using the model
def generate_code(prompt):
    input_ids = openrouter.tokenize(prompt, model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
