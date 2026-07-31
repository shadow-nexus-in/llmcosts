# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-31
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. Its architecture is designed to handle a wide range of tasks, including text and vision processing, function calling, and JSON mode. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require in-depth analysis and generation of content. The model's knowledge cutoff is 2024-11, ensuring that it has been trained on a vast amount of data up to that point.

### Strengths and Use-Cases
Mistral Medium 3 excels in tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The model's pricing is competitive, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0.

### Pricing and Competitors
In terms of pricing, Mistral Medium 3 is positioned between other models such as Claude 3.5 Haiku and GPT-4o Mini. While Claude 3.5 Haiku is more expensive, with input costs of $0.8/1M and output costs of $4.0/1M, GPT

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's beneficial to use them whenever possible. This can significantly reduce costs for repeated or similar inputs.
- **Batch API Savings**: With batch input being free, batching API calls can lead to substantial savings, especially for large volumes of similar or identical inputs.

#### Cost at Scale
Given the average cost per call, we can calculate the costs at different scales:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

To understand the cost structure better, let's calculate the cost per 1M tokens based on the average call size (500 tokens):
- **1,000 calls**: Assuming an average of 500 tokens per call, 1,000 calls would be approximately 500,000 tokens. The cost for this would be calculated based on input and output tokens. However, without the exact split of input vs. output tokens, we can only estimate based on the provided costs per 1M tokens.

#### Competitor Comparison
Comparing Mistral Medium 3 with its top competitors:
- **Claude 3.5 Ha

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
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
- Input: $0.4 per 1M tokens
- Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance.
- **HumanEval**: 77.5
  - This score evaluates the model's ability to generate human-like code. A higher score indicates better coding capabilities.
- **LMSYS Arena ELO**: 1200
  - This score represents the model's competitive ranking in the LMSYS Arena, with higher scores indicating better performance in a variety of tasks.

#### Real-World Implications
These benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
* Strong language understanding (MMLU: 80.0)
* Human-like code generation (HumanEval: 77.5)
* Competitive performance in a variety of tasks (LMSYS Arena ELO: 1200)

#### Use Cases
Based on its capabilities and benchmark performance, Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization


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

Mistral Medium 3 offers a balanced pricing model, with input costs 50% of Claude 3.5 Haiku and 267% of GPT-4o Mini. The output costs of Mistral Medium 3 are 50% of Claude 3.5 Haiku and 333% of GPT-4o Mini.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

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

However

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. Given its capabilities and limitations, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code, combined with its function calling capability, makes it an excellent choice for tasks such as code review, code completion, and debugging.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example code completion task
input_text = "def greet(name):"
output = model.generate(input_text, max_length=100)
print(output)
```

#### 2. **Summarization**
With its strong text understanding capabilities, Mistral Medium 3 is well-suited for summarization tasks. It can effectively condense long pieces of text into concise summaries, highlighting key points and main ideas.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example summarization task
input_text = "This is a long piece of text that needs to be summarized."
output = model.summarize(input_text, max_length=200)
print(output)
```

#### 3. **Content Generation**
Mistral Medium 3's ability to generate high-quality text makes it an excellent choice for content generation tasks, such as writing articles, creating product descriptions, or even composing emails.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example content generation task
input_text = "Write a

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
