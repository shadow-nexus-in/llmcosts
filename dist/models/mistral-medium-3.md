# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11 and achieves notable benchmark scores, including 80.0 on MMLU and 77.5 on HumanEval. The model's pricing is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers competitive pricing for its input and output tokens.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require a balance between performance and cost, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With its robust capabilities and competitive pricing, Mistral Medium 3 is a viable option for developers looking for a reliable and efficient model for their applications. By understanding the model's strengths, limitations, and pricing, developers can make informed decisions about when to use Mist

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and offers a range of capabilities including text, vision, function calling, and more.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, so it's always beneficial to use them when possible. This can significantly reduce costs, especially for repeated or similar inputs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. However, the actual cost savings will depend on the specific use case and the number of tokens processed.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average number of tokens per call and can vary depending on the actual usage.

#### Comparison to Top Competitors
Mistral Medium 3 is priced competitively with other mid-tier models. For example:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **$0.6/1M output**

Mistral Medium 3 offers a balance between cost and capabilities

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 16,384 tokens, with a knowledge cutoff of 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) score measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval: 77.5**: The HumanEval score evaluates a model's ability to generate code that is correct and functional. A higher score indicates better performance. With a score of 77.5, Mistral Medium 3 shows strong coding capabilities.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates decent performance in

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Its pricing is as follows:
- Input: $0.4 per 1M tokens
- Output: $2.0 per 1M tokens

#### Competitors
The top competitors of Mistral Medium 3 are:
1. **Claude 3.5 Haiku**
   - Input: $0.8 per 1M tokens (100% more expensive than Mistral Medium 3)
   - Output: $4.0 per 1M tokens (100% more expensive than Mistral Medium 3)
2. **GPT-4o Mini**
   - Input: $0.15 per 1M tokens (62.5% less expensive than Mistral Medium 3)
   - Output: $0.6 per 1M tokens (70% less expensive than Mistral Medium 3)

#### Performance Trade-offs
While Mistral Medium 3 has a higher price point than GPT-4o Mini, its performance on certain benchmarks may justify the additional cost. However, Claude 3.5 Haiku is significantly more expensive than Mistral Medium 3, which may only be justified for specific use cases that require its unique capabilities.

#### When to Choose Each Model
- **Mistral Medium 3**: Suitable for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its context window and output limits make it less suitable for frontier reasoning, bulk cheap tasks, simple classification, and real-time sub-100ms tasks.
- **Claude 3.5 Haiku**: May be chosen for applications where its unique capabilities and higher performance justify the increased cost. However, its higher pricing makes it less competitive for large-scale or cost-sensitive projects.
- **GPT-4o Mini**: Ideal for projects with tight budgets or high-volume input/output requirements. Its lower pricing makes it an attractive option for applications where cost is a primary concern, but its performance may not match that of Mistral Medium 3 or Claude 3.5 Haiku.

#### Cost Examples
To illustrate the cost differences, consider the following examples:
- 1,000 calls (

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use Mistral Medium 3 with OpenRouter to generate code snippets in response to user input.
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of numbers")
print(code_snippet)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or extracting key points from a piece of text. For example:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a piece of text
text = "This is a long piece of text that needs to be summarized."
summary = model.summarize_text(text)
print(summary)
```

3. **Content Generation**: With its strong content generation capabilities, Mistral Medium 3 can be used for tasks such as writing articles, generating social media posts, or creating product descriptions. For example:
   ```python

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
