# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. The architecture of Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is well-suited for a variety of applications.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 include its ability to perform tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its pricing model is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities and pricing, Mistral Small 4 is best utilized in scenarios where these specific strengths can be leveraged, such as in chatbots, content generation platforms, and coding assistance tools.

### Technical Specifications and Cost Considerations
From a technical standpoint, Mistral: Mistral Small 4 has a knowledge cutoff of 2023-12, indicating that its training data does not include information beyond this date. The model's pricing can be estimated based on the number of calls and tokens used. For example, 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls. Understanding these specifications and cost examples is crucial for developers looking to integrate Mistral Small 4 into their applications, allowing them to plan and budget effectively for their projects. With no

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. This analysis will delve into the cost structure, optimal usage scenarios, and cost at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

This structure indicates that the primary cost drivers are the input and output token counts. Cached and batch inputs do not incur additional costs, suggesting that utilizing these features can help optimize expenses.

#### When to Use Cached Tokens
Given that cached input tokens do not incur any additional cost, it is beneficial to use cached tokens whenever possible. This can significantly reduce the overall cost, especially in scenarios where the same input data is processed multiple times.

#### Batch API Savings
Although the pricing does not specify a direct cost savings for batch inputs, the fact that batch inputs are listed as $None per 1M tokens implies that batching can be an efficient way to process large volumes of data without incurring additional costs per token. However, the actual cost savings would depend on the reduction in the number of API calls needed when batching, as each call still incurs costs based on input and output tokens.

#### Cost at Scale
The provided cost examples give insight into the cost at scale:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear scaling of costs

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. 

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher score generally indicates better performance. 
The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting, with higher scores indicating better performance.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general analysis of its pricing, performance, and capabilities to help determine when to choose this model.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
These benchmarks indicate that the model has a moderate level of performance. The context window of 262,144 tokens and max output of 4,096 tokens suggest that it is suitable for a wide range of applications.

#### Capabilities and Use Cases
Mistral: Mistral Small 4 has the following capabilities:
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
The cost of using Mistral: Mistral Small 4 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Based on the provided data, Mistral: Mistral Small 4 appears to be a moderately priced model with a moderate level of performance. It is suitable for a wide range of applications, including chat, text generation, coding, and analysis. However, without direct competitors to compare it to, it is difficult to determine the exact scenarios in which it would be the best choice.

In general, Mistral: Mistral Small 4 may be a good choice when:
* A moderate level of performance is required
* A wide range of capabilities is needed (e.g. text, function_calling, json_mode, streaming, structured_outputs)
* The application requires a context window of up to 262,144 tokens and a max output of up

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. It offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs, making it suitable for various applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities and pricing model, here are the top 5 best use cases for Mistral Small 4, including specific code integration examples with OpenRouter:

1. **Chat Applications**: Mistral Small 4 can be used to power chat applications due to its text generation capabilities. 
    ```python
    import openrouter
    from mistralai import MistralSmall4

    # Initialize Mistral Small 4 model
    model = MistralSmall4()

    # Define a chat function
    def chat(input_text):
        # Generate response using Mistral Small 4
        response = model.generate_text(input_text)
        return response

    # Use OpenRouter to route chat requests
    openrouter.add_route('/chat', chat)
    ```
2. **Text Summarization**: With its ability to process and generate text, Mistral Small 4 can be used for text summarization tasks.
    ```python
    import openrouter
    from mistralai import MistralSmall4

    # Initialize Mistral Small 4 model
    model = MistralSmall4()

    # Define a summarization

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
