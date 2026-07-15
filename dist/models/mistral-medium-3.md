# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. Its architecture is designed to handle a wide range of tasks, including text, vision, function calling, and more. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require in-depth analysis and generation of content. The model's knowledge cutoff is 2024-11, ensuring that it has a solid foundation of knowledge up to that point.

### Strengths and Use Cases
Mistral Medium 3 excels in areas such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. Developers can leverage Mistral Medium 3's capabilities to build applications that require in-depth analysis, content generation, and vision tasks, among others.

### Pricing and Cost Examples
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M tokens for input, $2.0 per 1M tokens for output, with no charges for cached input or batch input. To give developers a better idea of the costs involved, some examples are provided: 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output token count, which is charged at **$2.0 per 1M tokens**.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average token count per call and do not take into account potential batch API savings or cached token usage.

#### Comparison to Competitors
Mistral Medium 3's pricing is competitive with other models in the market:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

While Mistral Medium 3's input cost is higher than

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source.

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
* MMLU: **80.0** - This score indicates the model's ability to understand and process natural language. A higher MMLU score suggests better language understanding capabilities.
* HumanEval: **77.5** - This score evaluates the model's ability to generate human-like text. A higher HumanEval score implies more coherent and natural-sounding text generation.
* LMSYS Arena ELO: **1200** - This score represents the model's performance in a competitive arena, where it is pitted against other models. A higher ELO score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for real-world applications that require:
* Strong language understanding (MMLU: 80.0)
* Coherent text generation (HumanEval: 77.5

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score than some other models in its class, but the lack of benchmark data for Claude 3.5 Haiku and GPT-4o Mini makes a direct comparison challenging.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
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

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for generating code snippets, debugging, and even entire codebases. For example, you can use it with OpenRouter to generate API endpoints:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate API endpoint code
endpoint_code = model.generate_code("Create a REST API endpoint for user authentication")
print(endpoint_code)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can analyze large volumes of text and provide concise summaries. This makes it ideal for applications such as news article summarization or document analysis:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Analyze and summarize a large document
document_text = "..."
summary = model.summarize(document_text)
print(summary)
```

3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for image classification, object detection, and more. For example, you can use it with OpenRouter to classify images:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Classify an

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
