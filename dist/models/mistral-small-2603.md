# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including but not limited to text generation, coding, and analysis. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to process large inputs and generate substantial outputs. It has a context window of 262,144 tokens and can produce up to 4,096 tokens as output. This makes it suitable for applications requiring extensive text processing, such as chat, text generation, coding, analysis, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in various linguistic and logical tasks. Its pricing model, with input costing $0.15 per 1M tokens and output costing $0.6 per 1M tokens, provides a clear cost structure for developers to plan their applications.

### Pricing and Cost Considerations
For developers considering Mistral Small 4, understanding the pricing is crucial. The model charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no charges for cached input or batch input. Example costs include $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 offers a unique set of capabilities and pricing that can be attractive for specific use cases, particularly those that require extensive text processing and

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output token count, which is charged at **$0.6 per 1M tokens**.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

To estimate the cost at scale, we can calculate the cost per call:
* Assuming an average of 500 tokens per call, the input cost per call is **$0.15 / 1,000,000 \* 500 = $0.000075**.
* The output cost per call depends on the actual output token count. Assuming an average output of 500 tokens (conservative estimate, given the max output is 4,096 tokens), the output cost per call is **$0.6 / 1,000,000 \* 500 = $0.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on 2024-01-01. It is not open source.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
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

#### Capabilities and Use Cases
Mistral: Mistral Small 4 supports the following capabilities:
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

#### Benchmark Interpretation
The benchmarks provide insight into the model's performance:
* **MMLU (80.0)**: Measures the model's ability to understand and generate human-like language. A higher score indicates better performance. In this case, 80.0 suggests that Mistral: Mistral Small

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will focus on key aspects such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of the top competitors. However, since this information is not provided, we will discuss the general factors to consider when evaluating pricing:
- **Input and Output Costs**: Compare the costs per 1M tokens for input and output. Models with lower costs may be more economical for large-scale applications.
- **Cached Input and Batch Input Costs**: Some models may offer discounted rates for cached or batch inputs. Consider whether these options are available and how they might impact your overall costs.

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12
- **Benchmarks**: MMLU score of 80.0, LMSYS Arena ELO of 1200

When comparing with competitors, consider the following:
- **Context Window and Max Output**: Models with larger context windows and higher max output limits may be more suitable for complex tasks or tasks requiring longer input/output sequences.
- **Knowledge Cutoff**: If your application requires knowledge more recent than the cutoff date, you may need to consider a different model.
- **Benchmarks**: Compare the benchmark scores (e.g., MMLU, HumanEval, LMSYS Arena ELO, GSM8K) to evaluate the model's performance in various tasks.

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
- **Text, Function Calling, JSON Mode, Streaming, Structured Outputs**
- **Best For**: Chat, text generation, coding, analysis, RAG pipelines, summarization

When choosing a model, consider the specific capabilities required for your application:
- **Capabilities**: Ensure the model supports the necessary features for your use case.
- **Best For**: Consider the recommended use cases for the model and whether

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the top 5 best use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is well-suited for chat applications, such as customer support bots or virtual assistants.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion, code review, and data analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process and generate text makes it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Text Analysis and Insight Generation**: With its context window of 262,144 tokens, Mistral Small 4 can analyze large amounts of text data and generate insights, making it suitable for applications such as sentiment analysis and text classification.
5. **Streaming and Real-time Applications**: Mistral Small 4's streaming capability allows it to process and generate text in real-time, making it a good choice for applications such as live chat, real-time text analysis, and streaming data processing.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
