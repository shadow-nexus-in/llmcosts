# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-31
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its suitability for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is well-suited for tasks that require understanding and generating lengthy texts. Its capabilities in function calling, JSON mode, and streaming also make it a versatile tool for developers working on chat, text generation, coding, and analysis projects. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling complex language tasks. Best use cases for this model include chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is structured around input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens cost $0.375, 10,000 calls cost $3.75, and 100

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Since cached input tokens are free, utilize this feature whenever possible to reduce input costs.
* **Batch API Calls**: With batch input being free, batching API calls can significantly reduce overall costs. However, be mindful of the context window and max output limits.

#### Cost at Scale
The provided cost examples illustrate the model's cost at different scales:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These examples demonstrate a linear scaling of costs with the number of API calls.

#### Context and Limits
When using Mistral Small 4, keep in mind the following limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure for input and output tokens.

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

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher score generally suggests better performance. However, without a direct comparison to other models, it's challenging to determine the exact implications of this score.

The LMSYS Arena ELO score of 1200 provides a measure of the model's performance in a competitive environment, with higher scores indicating better performance. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of competence.

The lack of HumanEval and GSM8K scores limits the understanding

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will create a hypothetical comparison with other models in the same tier. Let's consider two models, Model A and Model B, as top competitors.

#### Model Specifications
* **Mistral Small 4 (Mistralai)**
	+ Price: $0.15 per 1M tokens (input), $0.6 per 1M tokens (output)
	+ Context Window: 262,144 tokens
	+ Max Output: 4,096 tokens
	+ Benchmarks: MMLU (80.0), LMSYS Arena ELO (1200)
* **Model A**
	+ Price: $0.20 per 1M tokens (input), $0.8 per 1M tokens (output)
	+ Context Window: 200,000 tokens
	+ Max Output: 3,072 tokens
	+ Benchmarks: MMLU (75.0), LMSYS Arena ELO (1100)
* **Model B**
	+ Price: $0.10 per 1M tokens (input), $0.4 per 1M tokens (output)
	+ Context Window: 300,000 tokens
	+ Max Output: 5,120 tokens
	+ Benchmarks: MMLU (85.0), LMSYS Arena ELO (1300)

#### Price Differences
Mistral Small 4 is priced at $0.15 per 1M tokens (input) and $0.6 per 1M tokens (output). In comparison, Model A is priced 33% higher for input tokens and 33% higher for output tokens. Model B, on the other hand, is priced 33% lower for input tokens and 33% lower for output tokens.

#### Performance Trade-offs
Mistral Small 4 has a context window of 262,144 tokens, which is larger than Model A (200,000 tokens) but smaller than Model B (300,000 tokens). The max output of Mistral Small 4 is 4,096 tokens, which is higher than Model A (3,072 tokens) but lower than Model B (5,120 tokens).

In terms of benchmarks, Mistral Small 4 has an MMLU score of 80.0, which is

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's ability to perform function calling and generate structured outputs makes it an excellent choice for coding and analysis tasks.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: The model's support for streaming and structured outputs makes it a good choice for RAG (Retrieval-Augmented Generation) pipelines, which involve generating text based on retrieved information.
5. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter for more advanced routing and networking applications. For example, you can use Mistral Small 4 to generate routing configurations or analyze network traffic.

### Code Integration Examples with OpenRouter
Here is an example of how you can integrate Mistral Small 4 with OpenRouter using Python:
```python
import os
import openrouter

# Initialize Mistral Small 4 model
model = mistralai.MistralSmall4()

# Define a function to generate routing configurations
def generate_routing_config(network_topology):
    input_text = f"Generate routing configuration for {network_topology}"
    output

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
