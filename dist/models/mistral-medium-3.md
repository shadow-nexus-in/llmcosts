# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged from its benchmarks. It achieves a score of 80.0 on the MMLU benchmark, 77.5 on HumanEval, and 1200 on the LMSYS Arena ELO. The model's primary strengths lie in its ability to handle complex tasks such as coding, analysis, and vision tasks. It is also suitable for tasks that require summarization, content generation, and function calling. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Use Cases
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. The cost of using this model can be estimated using the provided cost examples: $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,000 calls. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model. Developers can use this model for a variety of tasks, including coding, analysis, and content generation

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
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the actual cost savings come from reducing the number of API calls. This can be beneficial for large-scale applications where a single API call can process multiple inputs.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

To put this into perspective, assuming an average of 500 tokens per call, the cost per 1M tokens can be estimated as follows:
* **1,000 calls**: 500,000 tokens / 1,000 calls = 500 tokens per call; $1.2 / 500,000 tokens = $0.0000024 per token (input) + $0.000008 per token (output) = $0.0000104 per token
* **10,000 calls**: 5,000,000 tokens / 10,000 calls = 500 tokens per call;

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Overview
Mistral Medium 3, a mid-tier model released by Mistral AI on 2025-04-17, offers a range of capabilities including text, vision, function calling, and more. This analysis will delve into the model's benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
- **HumanEval**: 77.5
- **LMSYS Arena ELO**: 1200

These scores indicate the model's performance in various tasks:
- **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks and domains. A score of 80.0 suggests strong language understanding capabilities.
- **HumanEval**: Evaluates the model's ability to write correct and functional code in response to programming tasks. A score of 77.5 indicates good coding skills, but with potential room for improvement.
- **LMSYS Arena ELO**: Assesses the model's overall performance in a competitive arena, with a score of 1200 indicating a moderate level of competence.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
- Strong language understanding (e.g., text analysis, summarization)
- Good coding skills (e.g., coding, function calling)
- Moderate overall performance (e.g., content generation, vision tasks)

However, the model may not be the best fit for tasks

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of price, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output tokens.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

Without benchmark data for Claude 3.5 Haiku and GPT-4o Mini, it is challenging to make a direct performance comparison. However, Mistral Medium 3's scores indicate strong capabilities in areas like coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks like:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

In contrast, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time tasks with sub-100ms latency

#### Cost Examples
To illustrate the cost of

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. Given its capabilities and limitations, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code makes it an ideal choice for tasks such as code review, code completion, and bug detection.
```python
import openrouter

# Initialize the model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Get the response
response = model.generate(task)

# Print the response
print(response)
```

#### 2. **Summarization**
Mistral Medium 3 is capable of summarizing long pieces of text into concise and meaningful summaries. This makes it a great choice for tasks such as text summarization, news article summarization, and document summarization.
```python
import openrouter

# Initialize the model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize the following text: [insert long text here]"

# Get the response
response = model.generate(task)

# Print the response
print(response)
```

#### 3. **Content Generation**
Mistral Medium 3 can generate high-quality content, including text, images, and videos. This makes it a great choice for tasks such as content creation, blog writing, and social media management.
```python
import openrouter

# Initialize the model
model = openrouter.MistralMedium3()

# Define a content generation task
task = "Write a blog post about the benefits of AI in marketing."

# Get the response

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
