# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that operates on a closed-source architecture. Its primary strengths lie in its capabilities to handle a wide range of tasks, including text and vision processing, function calling, and streaming, making it a versatile tool for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require in-depth analysis and generation of content.

### Architecture and Pricing
The model's architecture is designed to efficiently process input and output tokens, with pricing set at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This pricing structure makes it an attractive option for developers who need to process large amounts of data, but may not be the most cost-effective choice for bulk or simple tasks. The model's benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in various areas, including coding, analysis, and content generation. With a knowledge cutoff of 2024-11, developers can rely on Mistral Medium 3 to provide accurate and up-to-date information.

### Use Cases and Competitors
Mistral Medium 3 is best suited for tasks such as coding, analysis, summarization, and vision tasks, where its capabilities in function calling, JSON mode, and streaming can be fully utilized. However, it may not be the best choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. In terms of cost, Mistral Medium 3 is competitive with other models, such as Claude 3.5 Haiku and GPT-4o Mini, although its pricing structure is unique. For example, 1,000

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
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average number of tokens per call and the pricing structure outlined above.

#### Comparison to Competitors
Mistral Medium 3's pricing is competitive with other models in the market. For example:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Provider**: Mistral AI
* **Release Date**: 2025-04-17
* **Tier**: Mid
* **Open Source**: False

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU**: 80.0
* **HumanEval**: 77.5
* **LMSYS Arena ELO**: 1200
* **GSM8K**: None

The **MMLU** score measures the model's ability to understand and generate human-like text. A score of 80.0 indicates that the model is capable of producing coherent and contextually relevant text.

The **HumanEval** score evaluates the model's ability to write correct and functional code. A score of 77.5 suggests that the model is proficient in coding tasks, but may struggle with more complex or nuanced coding challenges.

The **LMSYS Arena ELO

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the price differences, performance trade-offs, and use cases for Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 offers a balanced pricing approach, with input costs higher than GPT-4o Mini but lower than Claude 3.5 Haiku. The output costs for Mistral Medium 3 are higher than both competitors.

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks, with a high MMLU score and a moderate LMSYS Arena ELO rating.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

####

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, offered by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it ideal for applications such as code review, code generation, and technical writing. When integrating with OpenRouter, you can leverage Mistral Medium 3's capabilities to analyze code snippets and provide insightful feedback.

```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a code snippet for analysis
code_snippet = """
def greet(name: str) -> None:
    print(f"Hello, {name}!")
"""

# Use OpenRouter to send the code snippet to Mistral Medium 3
response = openrouter.send_request(model, code_snippet)

# Print the analysis results
print(response)
```

#### 2. **Summarization and Content Generation**
With its strong text capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks, such as generating product descriptions, summarizing long documents, or creating engaging blog posts. When using OpenRouter, you can easily integrate Mistral Medium 3 into your content generation pipeline.

```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a long document for summarization
document = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

# Use OpenRouter to send the document to Mistral Medium 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
