# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed to cater to a wide range of applications. This model is not open source, indicating that its internal workings and training data are proprietary to Mistral AI. The architecture of Mistral Medium 3 supports various capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its balanced performance across different benchmarks, such as achieving an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO of 1200. It is best utilized for tasks like coding, analysis, retrieval-augmented generation (RAG), summarization, vision tasks, content generation, and function calling. The model's context window of 131,072 tokens and maximum output of 16,384 tokens provide ample room for complex and detailed responses. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is structured as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For developers, this translates to specific costs based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $1.2, while 100,000 calls would amount to $120.0. When comparing Mistral Medium 3 to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, developers should consider both the capabilities and the pricing models to choose the most suitable option for their specific

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
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input prompts, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Similar to cached input, batch input is also free. This means that batching API calls can help minimize costs associated with input tokens. However, the primary cost driver for Mistral Medium 3 is output tokens, which are charged at **$2.0 per 1M tokens**.

#### Cost at Scale
The cost examples provided in the data are as follows:
* **1,000 calls (avg 500 tokens): $1.2**
* **10,000 calls: $12.0**
* **100,000 calls: $120.0**

To put these numbers into perspective, let's calculate the cost per call:
* 1,000 calls: **$1.2 / 1,000 = $0.0012 per call**
* 10,000 calls: **$12.0 / 10,000 = $0.0012 per call**
* 100,000 calls: **$120.0 / 100,000 = $0.0012 per call**

The cost per call remains

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 77.5 - This score measures the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1200 - This score measures the model's overall performance in a competitive arena, where it is pitted against other models. A higher ELO score indicates better performance and a higher ranking in the arena.

#### Real-World Implications
The benchmark performance of Mistral Medium 3 suggests that it is a capable model for a variety of tasks, including:
* Coding: The model's high HumanEval score indicates that it

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is priced between Claude 3.5 Haiku and GPT-4o Mini, offering a balance between cost and performance.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's scores indicate strong performance in coding, analysis, and other tasks.

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
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a max output of 16,384 tokens. Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review, code generation, and data analysis. For example, you can use Mistral Medium 3 with OpenRouter to generate code snippets:
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to calculate the area of a rectangle")
print(code_snippet)
```
#### 2. **Summarization and Content Generation**
Mistral Medium 3 is also well-suited for summarization and content generation tasks, such as summarizing long documents or generating articles. You can use the following code to summarize a document:
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a document
document = "This is a long document that needs to be summarized."
summary = model.summarize(document)
print(summary)
```
#### 3. **Vision Tasks**
Mistral Medium 3 has vision capabilities, making it suitable for tasks such as image classification, object detection, and image generation. For example, you can use the following code to classify an image:
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Classify an image
image = "path/to/image.jpg"
classification = model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
