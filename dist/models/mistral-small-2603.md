# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing structure includes $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would be $37.5. The model's benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. However, its limitations include a knowledge cutoff of 2023-12, meaning it may not be aware of events or information after this date.

### Deployment Considerations
When considering the deployment of Mistral Small 4, developers should be aware of its capabilities and limitations. The model excels in tasks that require large context windows and structured outputs but may not be suitable for tasks that require knowledge after 2023-12. With no direct competitors listed, Mistral Small 4 stands out as a unique offering in the market. Its pricing model, based on input and output tokens, allows for flexible and cost-effective deployment in various

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Small 4
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This can significantly reduce costs for repeated or similar input queries.
* **Batch API Calls**: Leverage batch input to process multiple queries simultaneously, taking advantage of the free batch input pricing.

#### Cost at Scale
The cost examples provided demonstrate the pricing for Mistral Small 4 at different scales:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

To estimate costs for larger or smaller scales, we can use the input and output pricing. Assuming an average of 500 tokens per call:
* Input cost per call: $0.15 / 1,000,000 tokens \* 500 tokens = $0.000075 per call
* Output cost per call: $0.6 / 1,000,000 tokens \* 500 tokens = $0.0003 per call
* Total cost per call: $0.000075 + $0.0003 = $0.000375 per call

Using this calculation, we can estimate costs for different scales:


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on January 1, 2024. It is not open-source and has a specific pricing structure based on input and output tokens.

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

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores representing better performance. The LMSYS Arena ELO score of 1200 is a measure of the model's overall strength, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
The benchmark performance of Mistral Small 4 has the following implications for real-world use:
* The MMLU score of 80.0 suggests that the

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare prices, we would need the pricing information of the top competitors. However, since this information is not available, we can provide a general guideline for comparison:
* Look for models with similar pricing structures (input/output-based pricing) to compare costs directly.
* Consider the cost of cached input and batch input if these features are available in the competitor models.

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

When comparing performance with top competitors, consider the following factors:
* Context window size: A larger context window can handle longer input sequences, but may increase computational costs.
* Max output size: A larger max output size can generate longer responses, but may affect performance.
* Knowledge cutoff: A more recent knowledge cutoff can provide more up-to-date information, but may not be available in all models.
* Benchmarks: Compare the performance of the Mistral Small 4 model with competitors using the same benchmarks (e.g., MMLU, LMSYS Arena ELO).

#### Choosing the Right Model
The Mistral Small 4 model is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

When choosing between the Mistral Small 4 model and its competitors, consider the following factors:
* **Use case**: Select a model that is optimized for your specific use case.
* **Performance requirements**: Choose a model that meets your performance requirements (e.g., context window size, max output size

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a reliable choice for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its ability to perform function calling and generate structured outputs makes it a great choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling makes it a good choice for RAG (Retrieve, Augment, Generate) pipelines, which involve retrieving information from a knowledge base, augmenting it, and generating text based on it.
5. **Streaming**: With its support for streaming, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or live content generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Generate text based on a prompt
prompt = "Write a short story about a character who discovers a hidden world."
response = model.generate_text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
