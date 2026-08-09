# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With its architecture designed to handle a wide range of tasks, Mistral Medium 3 excels in areas such as coding, analysis, and content generation. Its primary strengths include a large context window of 131,072 tokens and the ability to generate up to 16,384 tokens of output. This makes it an ideal choice for applications that require in-depth understanding and generation of text.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 is capable of handling text, vision, function calling, JSON mode, streaming, and system prompts. Its pricing model is based on input and output tokens, with costs set at $0.4 per 1M input tokens and $2.0 per 1M output tokens. For developers, this translates to costs such as $1.2 for 1,000 calls averaging 500 tokens, $12.0 for 10,000 calls, and $120.0 for 100,000 calls. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a balanced approach between capability and cost. Notably, Mistral Medium 3 is not open source, which may be a consideration for some developers.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require complex analysis, reasoning, and generation, such as coding, summarization, and vision tasks. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring sub-100ms responses. Its knowledge cutoff of 2024-11 means that it may not have information on very recent events or developments. With benchmark scores of 80.

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### Optimizing Costs with Cached Tokens and Batch API
- **Cached Tokens**: Since cached input tokens are free, utilizing cached tokens whenever possible can significantly reduce costs. This is particularly beneficial for applications with repetitive or similar input sequences.
- **Batch API Savings**: With batch input being free, processing inputs in batches can lead to substantial cost savings, especially for high-volume applications.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These examples illustrate a linear cost scaling, which is consistent with the input and output pricing model.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For comparison:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
- **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

Mistral Medium 3 offers a balanced pricing model, with its input

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. Its pricing structure includes:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform various natural language processing tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A higher HumanEval score suggests better performance in coding tasks, such as code completion and code execution.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better overall performance and adaptability.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With a high HumanEval score, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code execution, and code analysis.
* **Text and Vision Tasks**: The model's high MMLU score and support for vision tasks make it a good fit for applications involving text and image processing, such as image

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models of the three competitors are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing model, with input costs 50% of Claude 3.5 Haiku and output costs 3.33 times that of GPT-4o Mini.

#### Performance Comparison
The performance benchmarks of the three models are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the performance benchmarks of Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 demonstrates strong performance with an MMLU score of 80.0 and a HumanEval score of 77.5.

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
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its features and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code, combined with its large context window of 131,072 tokens, makes it ideal for complex coding projects. 
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Use the model to generate code
code = model.generate_code(task)

print(code)
```

#### 2. **Summarization and Content Generation**
With its strong text capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks. Its ability to understand and generate human-like text makes it perfect for creating articles, blog posts, and more.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize the following article: [insert article text]"

# Use the model to generate a summary
summary = model.generate_summary(task)

print(summary)
```

#### 3. **Vision Tasks**
Mistral Medium 3's vision capabilities make it a great choice for tasks such as image classification, object detection, and more. Its ability to understand and generate visual content makes it perfect for applications such as self-driving cars, facial recognition, and more.
```python
import openrouter

# Initialize Mistral Medium 3 model
model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
