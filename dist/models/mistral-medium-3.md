# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed to cater to a wide range of applications. This model is not open source. From an architectural standpoint, Mistral Medium 3 boasts a context window of 131,072 tokens and can generate up to 16,384 tokens as output. Its knowledge cutoff is 2024-11, ensuring that the information it provides is current up to that point.

### Strengths and Use Cases
The primary strengths of Mistral Medium 3 lie in its versatility and performance across various tasks. It excels in coding, analysis, question-answering (RAG), summarization, vision tasks, content generation, and function calling. The model's capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts. However, it is not suited for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, developers can effectively plan and budget for their projects.

### Pricing and Competitiveness
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks (MMLU: 80.0, HumanEval: 77.5, LMSYS Arena ELO: 1200). For example, 1,000 calls averaging 500 tokens would cost $1.2, scaling to $12.0 for 10,000 calls and $120.0 for 100,000 calls. In comparison to its competitors, such as Claude 3.5 Haiku ($0.8/1M input, $4.0/1M output) and GPT-4o Mini ($0.15/1M input, $0

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per 1M tokens + Output cost per 1M tokens)

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500) \* ($0.4/1M + $2.0/1M) = $1.2

#### Comparison with Top Competitors
Mistral Medium 3 is compared to top competitors Claude 3.5 Ha

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
Mistral Medium 3 is a mid-tier model released by Mistral AI on 2025-04-17. It is not open source and has a context window of 131,072 tokens, with a maximum output of 16,384 tokens. The knowledge cutoff for this model is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmarks
Mistral Medium 3 has the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance on these tasks. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval: 77.5** - The HumanEval benchmark evaluates a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better code generation capabilities. With a score of 77.5, Mistral Medium 3 shows strong code generation abilities.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance in

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

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

Mistral Medium 3 offers a balanced pricing model, with input costs lower than Claude 3.5 Haiku but higher than GPT-4o Mini. However, the output costs of Mistral Medium 3 are significantly higher than GPT-4o Mini but lower than Claude 3.5 Haiku.

#### Performance Comparison
The performance of the three models can be evaluated based on their benchmark scores:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a strong performance profile, with high scores in MMLU, HumanEval, and LMSYS Arena ELO. However, without the benchmark scores of Claude 3.5 Haiku and GPT-4o Mini, a direct comparison is challenging.

#### Capabilities and Use Cases
The capabilities of the three models are:
* **Mistral Medium 3**:
	+ Text, vision, function_calling, json_mode, streaming, system_prompts
	+ Best for: coding, analysis, rag, summarization, vision_tasks, content

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and even generating entire codebases. For example, you can use it with OpenRouter to generate API endpoints:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a function to generate API endpoints
def generate_api_endpoints(prompt):
    response = model.generate_text(prompt)
    return response

# Generate API endpoints using OpenRouter
api_endpoints = generate_api_endpoints("Generate API endpoints for a simple CRUD application")
print(api_endpoints)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as extracting key points from a large document or generating a summary of a long piece of text. For example:
   ```python
# Define a function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate_text(prompt)
    return response

# Summarize a piece of text
text = "This is a long piece of text that needs to be summarized."
summary = summarize_text(text)
print(summary)
```

3. **Content Generation**: With its strong performance in content generation, Mistral Medium 3 can

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
