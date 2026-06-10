# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance is reflected in its benchmark scores: MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). These scores indicate that the model excels in tasks that require complex reasoning and problem-solving. The model's primary strengths lie in its ability to handle large context windows and generate high-quality output, making it ideal for tasks such as summarization, vision tasks, and function calling. However, it is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Use Cases
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. This pricing model makes it competitive with other mid-tier models, such as Claude 3.5 Haiku and GPT-4o Mini. The cost examples provided indicate that the model can be used for a variety of tasks, from small-scale development to large-scale production, with costs ranging from $1.2 for 1,000 calls to $120.0 for 100,000 calls. Overall, Mistral Medium 3 is a solid choice for developers who need a reliable and versatile model for a range

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. This can significantly reduce costs for applications where input data is repetitive or can be cached.

#### Batch API Savings
Batch input is also free, which means that batching API calls can lead to substantial savings, especially for high-volume applications. However, the cost savings from batching apply only to the input side, as output costs remain the same.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens): $1.2**
* **10,000 calls: $12.0**
* **100,000 calls: $120.0**

These examples suggest a linear cost scaling, where the cost per call remains constant. For applications requiring a large number of API calls, the cost can add up quickly.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For comparison:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and language translation.
* **HumanEval**: 77.5 - This score evaluates the model's ability to write correct and functional code in response to a given prompt. A higher score indicates better coding capabilities, which is useful for tasks such as code generation, code completion, and code review.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks and challenges. A higher ELO score indicates better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* **Coding and code generation**: With a high HumanEval score, the model is well-suited for tasks such as code completion, code review, and code generation.
* **Text analysis and generation**: The model

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

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
  + MMLU: 80.0
  + HumanEval: 77.5
  + LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Given the available data, Mistral Medium 3 demonstrates strong performance across various benchmarks.

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
* RAG (Retrieval-Augmented Generation)
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
### Practical Advice on Top 5 Best Use Cases for Mistral Medium 3
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code, combined with its analysis capabilities, makes it an ideal choice for tasks such as code review, code completion, and debugging.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example code completion task
input_code = "def greet(name):"
output = model.complete_code(input_code)
print(output)
```

#### 2. **Summarization**
With its strong text understanding and generation capabilities, Mistral Medium 3 is well-suited for summarization tasks. It can effectively condense long pieces of text into concise, meaningful summaries.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example summarization task
input_text = "This is a long piece of text that needs to be summarized."
output = model.summarize(input_text)
print(output)
```

#### 3. **Content Generation**
Mistral Medium 3's ability to generate high-quality text makes it an excellent choice for content generation tasks, such as writing articles, creating product descriptions, or even composing emails.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example content generation task
input_prompt = "Write a product description for a new smartwatch."
output =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
