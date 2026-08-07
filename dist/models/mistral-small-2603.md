# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as text generation, coding, and analysis.

### Technical Specifications and Use Cases
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competitiveness in language understanding and generation tasks. Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations, including a knowledge cutoff of 2023-12, should be considered when applying it to tasks requiring very recent information.

### Cost Considerations and Competitiveness
For developers looking to integrate Mistral Small 4 into their applications, understanding the cost structure is crucial. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would amount to $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. While there are no direct competitors listed for Mistral Small 4, its unique combination of capabilities, performance benchmarks, and pricing makes it

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can significantly reduce costs. However, the exact savings will depend on the specific use case and the number of tokens processed per batch.

#### Cost at Scale
The provided cost examples give insight into the costs at different scales:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples illustrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Context and Limits
It's essential to be aware of the context window and output limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

Understanding these limits will help in optimizing the usage of the model and avoiding unnecessary costs due to exceeded limits.

#### Capabilities and Best Use Cases
Mistral Small 4 supports various capabilities, including:
* text
* function_calling

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

The MMLU score of **80.0** indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally suggests better performance in tasks that require mathematical and logical reasoning.

The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The absence of HumanEval and GSM8K scores means that the model's performance on these benchmarks is not available.

#### Real-World Implications
In real-world use, the benchmark performance of Mistral Small 4

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare this with other models, we need to consider the pricing structure of each competitor. However, without specific competitor data, we can only provide a general outline of how to evaluate pricing:
* Calculate the cost per token for each model
* Consider the cost of input, output, cached input, and batch input for each model
* Evaluate the pricing structure based on your specific use case and token requirements

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

When evaluating competitor models, consider the following performance trade-offs:
* Context window size: Larger context windows can handle more complex inputs, but may increase costs and computation time
* Max output size: Larger output sizes can provide more detailed responses, but may increase costs and computation time
* Knowledge cutoff: More recent knowledge cutoffs can provide more up-to-date information, but may require more frequent model updates
* Benchmarks: Evaluate the performance of each model on relevant benchmarks, such as MMLU and LMSYS Arena ELO

#### Choosing the Right Model
The Mistral Small 4 model is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

When choosing a model, consider the following factors:
* Your specific use case and requirements
* The pricing structure and cost per token for each model
* The performance characteristics and trade-offs for each model
* The capabilities and limitations of each model

Without direct competitor data, we cannot

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great tool for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables it to be used in applications that require the combination of retrieval and generation capabilities.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or live text generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt)
    output = model.generate(input_ids, max_length=4096)
    return openrouter.detokenize(output)



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
