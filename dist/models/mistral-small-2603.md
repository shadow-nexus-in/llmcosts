# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy interactions.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. This makes it particularly adept at handling tasks that require understanding and generating lengthy, coherent texts. Its capabilities in function calling, JSON mode, and streaming further enhance its utility in applications such as chat, text generation, coding, analysis, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in various linguistic and logical tasks. However, its pricing structure, which includes $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, should be considered when planning its integration into applications.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 includes charges of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, with no charges specified for cached input or batch input. This pricing structure translates to costs such as $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost per 1M tokens
- **Batch Input**: No additional cost per 1M tokens

#### Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is beneficial to use cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no explicit discount mentioned for batch inputs, the absence of additional costs implies that batching can help in reducing the overall cost per token by minimizing the number of API calls.

#### Cost at Scale
The cost examples provided give insight into the cost at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Calculating Costs
Given the input and output pricing, the total cost for a single API call can be estimated based on the number of input and output tokens. For instance, if an average call involves 500 input tokens and assuming an output of significantly fewer tokens (given the max output is 4,096 tokens), the cost can be approximated as follows:
- Input cost for 500 tokens: $(500 / 1

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, with higher scores indicating better performance. However, without a direct comparison to other models, it is difficult to determine the significance of this score.

The lack of HumanEval and GSM8K scores makes it difficult to evaluate the model's performance on coding and mathematical tasks.

#### Real-World Use
In real-world use, the Mistral Small 4

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general analysis of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Pricing
The Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* MMLU: 80.0
* LMSYS Arena ELO: 1200

The Mistral Small 4 model is capable of:
* Text generation
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
When to choose the Mistral Small 4 model:
* When you need a model with a large context window (262,144 tokens) and moderate output size (4,096 tokens).
* When your application requires text generation, function calling, or JSON mode capabilities.
* When you prioritize a balance between performance and cost, as the model's pricing is competitive with other standard-tier models.

Keep in mind that the Mistral Small 4 model has a knowledge cutoff of 2023-12, which may limit its ability to provide up-to-date information on very recent events or developments. However, for many applications, this should not be a significant concern.

In the absence of direct competitors, the Mistral Small 4 model appears to be a solid choice for a wide range of natural language processing tasks. Its capabilities, performance, and pricing make it an attractive option for developers and businesses looking for a reliable and cost

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral: Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4's ability to generate concise and accurate summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good fit for tasks that require generating text based on external knowledge sources.
5. **Streaming**: With its support for streaming, Mistral: Mistral Small 4 can be used for real-time text generation and processing tasks.

### Code Integration Example with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
