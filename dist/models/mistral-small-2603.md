# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate outputs of up to 4,096 tokens, making it suitable for applications requiring substantial input and output handling.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its versatility and performance across multiple benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. It is best utilized for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks, thanks to its capabilities in handling text, making function calls, and producing structured outputs. The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. This makes it a cost-effective option for developers looking to integrate advanced language processing capabilities into their applications without incurring excessive costs for input processing.

### Cost Considerations and Competitors
For developers planning to use Mistral Small 4, understanding the cost structure is crucial. The model's pricing allows for flexible budgeting, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Notably, there are no direct competitors listed for Mistral Small 4, suggesting it occupies a unique position in the market with its specific set of capabilities and pricing. As of its

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
The cost structure for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it is optimal to use:
* **Cached tokens** whenever possible, as they are free. This can significantly reduce costs for repeated input sequences.
* **Batch API calls** to take advantage of the free batch input pricing. This can lead to substantial cost savings for large-scale API calls.

#### Cost at Scale
The costs for Mistral Small 4 at various scales are as follows:
* **1,000 calls** (avg 500 tokens): $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Context and Limits
It is essential to consider the context window and output limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits may impact the model's performance and cost-effectiveness for specific use cases.

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_call

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

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
The benchmark performance of Mistral Small 4 is:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score generally corresponds to better performance in natural language understanding and generation tasks.

The **LMSYS Arena ELO score** of 1200 is a measure of the model's performance in a competitive arena, where it is pitted against other models. The ELO score is a rating system that estimates the relative skill of players (or models) in a competitive environment. A higher ELO score indicates better performance.

The lack of **HumanEval** and **GSM

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, consider the pricing of other models:
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Small 4 | $0.15 | $0.6 |
| Competitor Model | *Competitor Input Price* | *Competitor Output Price* |

Replace *Competitor Input Price* and *Competitor Output Price* with the actual prices of the competitor model.

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2023-12
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with other models, consider the following trade-offs:
- **Context Window**: A larger context window allows for more extensive conversations or text analysis but may increase computational costs.
- **Max Output**: A higher max output is beneficial for applications requiring longer responses but may impact performance.
- **Knowledge Cutoff**: This determines how up-to-date the model's knowledge is. Models with more recent knowledge cutoffs may be more desirable for certain applications.
- **Benchmarks**: Compare the MMLU and LMSYS Arena ELO scores to evaluate the model's performance in different areas.

#### Choosing the Right Model
When deciding between the Mistral Small 4 and its competitors, consider the following factors:
- **Application Requirements**: If your application requires a large context window, high max output, or specific capabilities like function calling or JSON mode, choose the model that best fits these needs.
- **Budget**: Evaluate the pricing models of each competitor and calculate the costs based on your expected usage. The cost examples provided for the Mistral Small 4 can serve as a template:
  - 1,000 calls (avg 500 tokens): $0.375
  - 10,

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is based on input and output tokens. The costs are as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral Small 4 is ideal for chatbots and text generation tasks.
2. **Coding and Function Calling**: The model's capability to call functions and generate code makes it suitable for coding tasks, such as generating boilerplate code or assisting with coding interviews.
3. **Analysis and Summarization**: Mistral Small 4 can be used for analysis and summarization tasks, such as summarizing long documents or analyzing text data.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good fit for tasks that require generating text based on external knowledge.
5. **Streaming and Structured Outputs**: With its ability to handle streaming data and generate structured outputs, Mistral Small 4 can be used for tasks such as real-time text analysis or generating structured data from unstructured text.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client()

# Define the input prompt


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
