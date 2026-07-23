# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy tasks.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. This positions the model as a robust tool for applications requiring in-depth understanding and generation of text, such as chat, text generation, coding, and analysis. The model's capabilities in function calling, JSON mode, and streaming further enhance its versatility. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating strong performance in specific areas. However, its suitability for certain tasks may be limited by the absence of direct competitors and specific benchmark scores like HumanEval and GSM8K.

### Pricing and Cost Efficiency
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. This pricing structure suggests that the model is cost-efficient for applications with moderate to high output requirements. For example, 1,000 calls averaging 500 tokens would cost $0.375, scaling to $3.75 for 10

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is free, the actual cost savings come from reducing the number of API calls. By batching inputs, users can significantly lower their overall costs by minimizing the number of calls.

#### Cost at Scale
The costs for Mistral Small 4 at different scales are as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Context and Limits
It's essential to consider the context window and max output limits when optimizing for cost:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens

Staying within these limits can help avoid unnecessary costs associated with excessive input or output tokens.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, especially when utilizing cached tokens and batching API calls. By understanding the cost structure and optimizing usage, users can effectively manage

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

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
The model's benchmark performance is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better language understanding and generation capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance in specific areas, such as coding and math problem-solving.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general analysis of its pricing, performance, and capabilities to help users decide when to choose this model.

#### Pricing
The Mistral: Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the Mistral: Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral: Mistral Small 4 Model
Since there are no direct competitors listed, the decision to choose the Mistral: Mistral Small 4 model depends on the specific requirements of your project. Consider the following factors:
* **Pricing**: If your project requires a moderate number of input and output tokens, the Mistral: Mistral Small 4 model may be a cost-effective option.
* **Performance**: If your project requires a large context window and moderate output length, the Mistral: Mistral Small 4 model may be a good choice.
* **Capabilities**: If your project requires a model that supports text, function calling, JSON mode, streaming, and structured outputs, the Mistral: Mistral Small 4 model may be a good fit.
* **Use Cases**: If your

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the top 5 best use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Text-Based Applications**: Its support for text, JSON mode, and streaming capabilities make it suitable for a wide range of text-based applications, such as text classification, sentiment analysis, and language translation.
5. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter for advanced routing and networking applications, such as network configuration and optimization.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter
from mistralai import MistralSmall4

# Initialize OpenRouter and Mistral Small 4
openrouter.init()
model = MistralSmall4()

# Define a function to generate text using Mistral Small 4
def generate_text(prompt):
    input_ids = open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
