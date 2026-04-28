# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, developed by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex text generation and analysis tasks.

### Technical Specifications and Use Cases
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no additional costs for cached input or batch input. The model's capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in various linguistic tasks. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing this model for specific use cases.

### Cost Considerations and Competitors
For developers planning to integrate Mistral Small 4 into their applications, cost is an important consideration. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls. While there are no direct competitors listed for Mistral Small 4, its unique combination of capabilities, such as function calling and structured outputs, along with its pricing model, makes it an attractive option for developers seeking a robust language model for

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into its cost structure, usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached inputs)
- **Batch Input**: $None per 1M tokens (suggesting no specific discount for batch inputs, but costs are calculated based on input and output tokens)

#### Usage Scenarios
- **Cached Tokens**: Since there's no additional cost for cached input tokens, it's beneficial to use cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there's no explicit discount for batch inputs, processing inputs in batches can help reduce the overall number of API calls, potentially leading to cost savings through reduced overhead and more efficient use of input tokens.

#### Cost at Scale
The cost examples provided give insight into the model's cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear cost scaling with the number of API calls, which is consistent with the input and output token pricing.

#### Calculating Costs
To understand the cost implications, consider the following:
- For a single API call with an average of 500 tokens, the cost can be broken down into input and output costs. Assuming an average output of 100 tokens (a rough estimate for many text-based applications), the costs

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of **80.0** indicates the model's performance on a set of mathematical and logical tasks. A higher score generally indicates better performance.

The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive setting, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Capabilities and Use Cases
The model has the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will serve as a baseline for comparison when evaluating other models in the market.

#### Model Overview
The Mistral: Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. It has the following key features:

* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral: Mistral Small 4 model is as follows:

* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using the Mistral: Mistral Small 4 model, consider the following examples:

* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The performance of the Mistral: Mistral Small 4 model is measured by the following benchmarks:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Note that the HumanEval and GSM8K benchmarks are not available for this model.

#### Choosing the Mistral: Mistral Small 4 Model
When to choose the Mistral: Mistral Small 4 model:

* **Use cases**: chat, text_generation, coding, analysis, rag_pipelines, summarization
* **Requirements**: standard, non-open-source model with a context window of 262,144 tokens and max output of 4,096 tokens

Since there are no direct competitors listed, it is essential to evaluate other models in the market based on their features, pricing, and performance to determine the best fit

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples mentioning OpenRouter:

1. **Chat Applications**: Mistral Small 4 can be used to power chatbots that can understand and respond to user queries. 
    * **Example**: Using OpenRouter, you can integrate Mistral Small 4 into your chat application to generate human-like responses.
    ```python
import openrouter

# Initialize OpenRouter with Mistral Small 4
router = openrouter.Router(model="mistralai/mistral-small-2603")

# Define a function to generate responses
def generate_response(user_input):
    response = router.generate_text(user_input)
    return response

# Test the function
user_input = "Hello, how are you?"
response = generate_response(user_input)
print(response)
```

2. **Text Generation**: Mistral Small 4 can be used for text generation tasks such as writing articles, stories, or even entire books.
    * **Example**: Using OpenRouter, you can integrate Mistral Small 4 into your text generation application to generate high-quality content.
    ```python
import openrouter

# Initialize OpenRouter with Mistral Small 4
router = openrouter.Router(model="mistralai/mistral-small-2603")

# Define a function to generate text
def generate_text(prompt):
    text = router.generate_text(prompt)
    return text

# Test the function


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
