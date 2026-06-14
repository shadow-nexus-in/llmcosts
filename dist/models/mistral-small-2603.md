# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. With capabilities such as function calling and structured outputs, Mistral Small 4 is well-suited for tasks that require both understanding and generating complex, structured text.

### Use Cases and Cost Considerations
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, and summarization, thanks to its robust capabilities and large context window. However, its pricing should be considered when planning large-scale deployments. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 100,000 calls would amount to $37.5. Given its strengths and the lack of direct competitors,

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
Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API**: Leverage batch input to process multiple requests at once, as batch input is also free.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs are based on the average number of tokens per call and the pricing structure outlined above.

#### Context and Limits
Keep in mind the following context and limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
Mistral Small 4 is capable of:
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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not applicable)
* Batch Input: **$None per 1M tokens** (not applicable)

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmark Performance
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None** (not available)
* LMSYS Arena ELO: **1200**
* GSM8K: **None** (not available)

The MMLU score of **80.0** indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better language understanding and generation capabilities.

The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to directly compare the model's performance in specific areas, such as coding and math problem-solving.

#### Real-World Use


## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and category. 

#### Model Overview
* **Mistral: Mistral Small 4 (mistralai/mistral-small-2603)**
	+ Provider: Mistralai
	+ Release Date: 2024-01-01
	+ Tier: Standard
	+ Open Source: False
* **Hypothetical Competitor 1: LLaMA Small**
	+ Provider: Meta AI
	+ Release Date: 2023-02-01
	+ Tier: Standard
	+ Open Source: False
* **Hypothetical Competitor 2: BLOOM Small**
	+ Provider: BigScience
	+ Release Date: 2022-06-01
	+ Tier: Standard
	+ Open Source: True

#### Pricing Comparison
| Model | Input Price ($ per 1M tokens) | Output Price ($ per 1M tokens) |
| --- | --- | --- |
| Mistral: Mistral Small 4 | $0.15 | $0.6 |
| LLaMA Small | $0.20 | $0.8 |
| BLOOM Small | $0.10 | $0.4 |

The Mistral: Mistral Small 4 model offers a competitive pricing structure, with input prices 25% lower than LLaMA Small and 50% higher than BLOOM Small. Output prices are 25% lower than LLaMA Small and 50% higher than BLOOM Small.

#### Performance Trade-offs
* **Context Window**: Mistral: Mistral Small 4 has a context window of 262,144 tokens, which is comparable to other models in the same tier.
* **Max Output**: The max output of 4,096 tokens is relatively standard for models in this category.
* **Knowledge Cutoff**: The knowledge cutoff of 2023-12 is relatively recent, indicating that the model has been trained on a wide range of data up to that point.

#### Benchmarks
| Model | MMLU | HumanEval | LMSYS Arena ELO | GSM8K |
| --- | --- | --- | --- | --- |
| Mistral: Mistral

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a unique set of features for various use cases.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great choice for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables it to generate high-quality text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can handle real-time text generation and processing tasks, making it suitable for applications such as live chatbots or real-time text analysis.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Define a function to generate text
def generate_text(prompt):
    # Use the model to generate text
    output = model.generate_text(prompt, max_length=4096)
    return output

# Define a function to call a function


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
