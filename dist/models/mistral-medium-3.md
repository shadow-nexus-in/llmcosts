# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use-Cases
Mistral Medium 3 excels in tasks that require a combination of natural language understanding and generation. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model is best utilized for tasks such as coding, analysis, summarization, and vision tasks, where its capabilities in function calling and JSON mode can be fully leveraged. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model, with Claude 3.5 Haiku charging $0.8/1M input and $4.0/1M output, and GPT-4o Mini charging $0.15/1M input and $0.6/1M output.

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can lead to substantial cost savings. By grouping multiple input sequences into a single API call, you can avoid incurring additional costs for input tokens.

#### Cost at Scale
To illustrate the cost implications of using Mistral Medium 3 at scale, consider the following examples:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These examples demonstrate a linear cost relationship, with the cost increasing directly with the number of API calls.

#### Comparison to Top Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output
* GPT-4o Mini: $0.15/1M input, $0.6/1M output

While Mistral Medium 3's input pricing is competitive, its output

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
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate code that passes unit tests. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher score suggests better overall performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of natural language, such as text analysis, summarization, and content generation.
* The strong HumanEval score indicates that the model is capable of generating high-quality code, making it a good choice for coding tasks.
* The LMSYS Arena ELO score suggests that Mistral Medium 3 is a competitive model that can hold its own against other models in a variety of tasks.

####

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will analyze its strengths and weaknesses against top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 has a high MMLU score of 80.0 and a HumanEval score of 77.5, indicating strong performance in coding and analysis tasks.

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
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub 100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 can be estimated as follows:
* 

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use Mistral Medium 3 with OpenRouter to generate code snippets in various programming languages.
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of numbers")
print(code_snippet)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks such as sentiment analysis, entity recognition, and text summarization. For example, you can use Mistral Medium 3 to summarize a large document into a concise summary.
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a document
document = "This is a large document that needs to be summarized"
summary = model.summarize(document)
print(summary)
```

3. **Content Generation**: With its strong content generation capabilities, Mistral Medium 3 can be used for tasks such as writing articles, generating product descriptions, and creating social media posts.

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
