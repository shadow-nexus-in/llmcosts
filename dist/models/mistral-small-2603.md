# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications indicate a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. This makes it suitable for tasks that require understanding and generating long pieces of text. The pricing model for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. The model is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, demonstrate its capabilities in various NLP tasks.

### Cost Considerations and Competitors
For developers considering the integration of Mistral: Mistral Small 4 into their applications, the cost can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would cost $3.75, and 100,000 calls would cost $37.5. Notably, there are no direct competitors listed for Mistral: Mist

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is processed multiple times. Since cached input is **free**, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also lead to cost savings. Although the pricing does not explicitly mention batch input costs, it is listed as **$None per 1M tokens**, indicating that batch input is free. This suggests that batching API calls can help reduce costs by minimizing the number of API calls.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear relationship between the number of API calls and the total cost.

#### Conclusion
Mistral Small 4 offers a cost-effective solution for text-based applications, with a competitive pricing structure. By leveraging cached tokens and batch API calls, users can minimize costs and optimize their usage of this model. As the number of API calls increases, the total cost scales linearly, making it essential to consider the cost

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on January 1, 2024. It is not open-source.

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

The MMLU score of **80.0** indicates the model's performance on a set of mathematical and logical tasks. A higher score generally indicates better performance. The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive setting, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores makes it difficult to directly compare the model's performance on specific tasks such as coding and math problem-solving.

#### Capabilities and Use Cases
The model has the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general analysis of its features, pricing, and performance trade-offs. This will help users understand when to choose this model and what to expect from it.

#### Model Overview
The Mistral Small 4 model is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral Small 4
Since there are no direct competitors listed, users should consider the following factors when deciding whether to choose Mistral Small 4:
* **Performance requirements**: If your application requires a high context window (262,144 tokens) and moderate output size (4,096 tokens), Mistral Small 4 may be a good choice.
* **Budget constraints**: If your budget is limited, you may want to consider the cost examples provided above and estimate the total cost of using Mistral Small 4 for your specific use case.
* **Capability requirements**: If your application requires support for text, function calling, JSON mode,

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This model is particularly suited for tasks such as chat, text generation, coding, analysis, rag pipelines, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities and pricing model, here are the top 5 best use cases for Mistral: Mistral Small 4, along with examples of how to integrate them with OpenRouter:

1. **Chat Applications**: Utilize Mistral: Mistral Small 4 for generating human-like responses in chat applications. 
    ```python
    import openrouter
    from mistralai import MistralSmall4

    # Initialize MistralSmall4 model
    model = MistralSmall4()

    # Define a function to generate chat responses
    def generate_response(input_text):
        # Use OpenRouter to route the input to MistralSmall4
        output = openrouter.route(input_text, model)
        return output

    # Example usage
    user_input = "Hello, how are you?"
    response = generate_response(user_input)
    print(response)
    ```

2. **Text Generation**: Leverage the model for text generation tasks such as writing articles, creating content, or even generating entire books.
    ```python
    import openrouter
    from mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
