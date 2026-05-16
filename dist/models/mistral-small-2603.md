# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks, including text generation, coding, analysis, and summarization. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens. This makes it particularly suited for applications such as chat, text generation, coding, and analysis. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its capabilities in understanding and generating human-like text. With pricing set at $0.15 per 1M input tokens and $0.6 per 1M output tokens, Mistral Small 4 offers a cost-effective solution for developers looking to integrate advanced language processing capabilities into their applications.

### Pricing and Cost Examples
The pricing model for Mistral Small 4 is based on input and output tokens, with no charges for cached or batch inputs. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would be $37.5. With its unique set of capabilities and competitive pricing, Mistral Small 4 is an attractive option for developers working on projects that require advanced text processing and generation capabilities. As it has no direct competitors listed, Mistral Small 4 stands out as a distinct offering in the market, suitable for applications such

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
Mistral: Mistral Small 4 is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This structure indicates that the primary cost factors are the input and output token counts. Cached and batch inputs are not charged, suggesting that optimizing for these can significantly reduce costs.

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to use cached tokens whenever possible. This can be particularly effective in scenarios where the same input data is processed multiple times, such as in chat applications or text generation tasks where the context does not change frequently.

#### Batch API Savings
The absence of charges for batch input tokens implies that processing inputs in batches can lead to substantial cost savings. By grouping multiple inputs together and processing them as a single batch, users can avoid the per-input charges that would apply if these were processed individually.

#### Cost at Scale
To understand the cost-effectiveness of Mistral: Mistral Small 4 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear scaling of costs with the number of API calls, which is consistent with the input/output token-based pricing model. For

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

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
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally corresponds to better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, with higher scores indicating better performance. However, without a direct comparison to other models, it is difficult to interpret the significance of this score.

The lack of HumanEval and GSM8K scores makes it challenging to evaluate the model's performance on specific tasks such as coding and mathematical

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of the model's pricing, performance, and capabilities, and discuss when to choose this model.

#### Pricing
The Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs
It is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the decision to choose the Mistral Small 4 model should be based on its capabilities, performance, and pricing. If your use case aligns with the model's supported capabilities and you require a model with a context window of 262,144 tokens and a max output of 4,096 tokens, the Mistral Small 4 model may be a good choice. However, it is essential to evaluate the model's performance and pricing in the context of your specific requirements and constraints.

### Future Competitor Comparison
Once direct competitors are listed, a more detailed comparison can be made, including price differences, performance trade-offs, and when to choose each model. This will enable a more informed decision-making process for selecting the most suitable model for your specific needs.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization and RAG Pipelines**: Mistral Small 4's capabilities in text generation and structured outputs also make it a good fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Text-based Data Analysis**: With its ability to process large amounts of text data, Mistral Small 4 can be used for text-based data analysis, such as sentiment analysis and entity extraction.
5. **Streaming and Real-time Applications**: Its support for streaming and real-time processing makes it suitable for applications that require immediate responses, such as live chatbots and real-time text analysis.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text
def generate_text(prompt):
    response = model.generate_text(prompt, max_length=4096

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
