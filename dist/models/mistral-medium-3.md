# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model that offers a balance between performance and cost. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a wide range of tasks, including but not limited to coding, analysis, and content generation. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 include its large context window of 131,072 tokens and its ability to generate up to 16,384 tokens as output. This makes it suitable for tasks that require processing and understanding large amounts of data, such as complex coding tasks, in-depth analysis, and detailed content generation. The model's benchmark scores, such as an MMLU score of 80.0 and a HumanEval score of 77.5, indicate its strong performance in various evaluation metrics. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is structured as follows: $0.4 per 1M tokens for input, $2.0 per 1M tokens for output, with no charges for cached input or batch input. To put this into perspective, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would amount to $12.0, and 100,000 calls would cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of capabilities and pricing, making it an

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
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs. This can be particularly beneficial for applications with repetitive or similar input patterns.

#### Batch API Savings
Since batch input is also free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output token count, as output tokens are charged at **$2.0 per 1M tokens**.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per call:
* **1,000 calls**: **$1.2 / 1,000 = $0.0012 per call**
* **10,000 calls**: **$12.0 / 10,000 = $0.0012 per call**
* **100,000 calls**: **$120.0 / 100,000 = $0.0012 per call**

As shown, the cost per call

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
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost. Released on 2025-04-17, it is not open-source.

#### Pricing
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

#### Benchmarks
The benchmark performance of Mistral Medium 3 is:
* MMLU: **80.0** - This score indicates the model's ability to understand and process natural language. A higher MMLU score suggests better performance in tasks that require language understanding.
* HumanEval: **77.5** - This score evaluates the model's ability to generate human-like text. A higher HumanEval score indicates better performance in tasks that require text generation.
* LMSYS Arena ELO: **1200** - This score measures the model's overall performance in a competitive environment. A higher ELO score suggests better performance compared to other models.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

On the other hand, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0


## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for various tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and even generating entire codebases. For example, you can use Mistral Medium 3 with OpenRouter to generate API documentation:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate API documentation
api_docs = model.generate_api_docs("https://api.example.com")
print(api_docs)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and sentiment analysis. Its large context window of 131,072 tokens allows it to process long documents and generate concise summaries:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a long document
summary = model.summarize("This is a very long document...")
print(summary)
```

3. **Content Generation**: With its strong language generation capabilities, Mistral Medium 3 can be used for content generation, such as writing articles, blog posts, and social media content:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate a blog post
blog_post = model.generate_content

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
