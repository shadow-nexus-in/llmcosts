# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard tier language model that is not open source. This model is identified by the name `xiaomi/mimo-v2-omni`. With a context window of 262,144 tokens and a maximum output of 65,536 tokens, the MiMo-V2-Omni is designed to handle a wide range of natural language processing tasks. Its knowledge cutoff is 2023-12, indicating that it was trained on data available up to December 2023.

### Architecture and Strengths
The architecture of the MiMo-V2-Omni model supports various capabilities such as text, function calling, JSON mode, streaming, and structured outputs. These features make it particularly suited for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing is based on input and output tokens, with costs of $0.4 per 1M tokens for input and $2.0 per 1M tokens for output. The model's strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. However, its limitations are noted in the absence of certain benchmark scores, such as HumanEval and GSM8K.

### Use Cases and Cost Considerations
Developers can leverage the MiMo-V2-Omni model for a variety of use cases, given its broad range of capabilities. However, it is essential to consider the cost implications of using this model. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would amount to $12.0, and 100,000 calls would cost $120.0. Understanding these costs and the model's

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Xiaomi: MiMo-V2-Omni
#### Overview
The Xiaomi: MiMo-V2-Omni model, released on 2024-01-01, is a standard, non-open-source model provided by Xiaomi. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to use cached tokens whenever possible to minimize costs.
- **Batch API Calls**: Given that batch input is free, batching API calls can significantly reduce the overall cost by minimizing the number of input tokens charged.

#### Cost at Scale
The cost examples provided indicate the following costs for different scales of API calls:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs can be broken down further based on the input and output pricing:
- For **1,000 calls** with an average of 500 tokens, assuming an average output of less than 500 tokens (to fit within the max output limit of 65,536 tokens), the cost can be estimated as follows:
  - Input cost: 500 tokens * (1M tokens / $0.4) * (1 / 1,000,000) = $0.0002 per token * 500 tokens = $0.1 for input (assuming 1 call = 1 input

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Xiaomi: MiMo-V2-Omni Benchmark Performance
#### Overview
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard tier model that is not open source. It has a context window of 262,144 tokens and a maximum output of 65,536 tokens, with a knowledge cutoff of 2023-12.

#### Pricing
The pricing for this model is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The benchmark performance of Xiaomi: MiMo-V2-Omni is as follows:
* **MMLU (Massive Multitask Language Understanding) Score**: 80.0. This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score generally suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval Score**: None. HumanEval is a benchmark that evaluates a model's ability to generate code that passes a set of unit tests. The lack of a HumanEval score makes it difficult to assess the model's coding capabilities.
* **LMSYS Arena ELO Score**: 1200. The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where models are pitted against each other to complete tasks. An ELO score of 1200 is a relatively moderate score, indicating that the model has some proficiency

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Xiaomi: MiMo-V2-Omni is a standard-tier model released by Xiaomi on 2024-01-01. It is not open-source.

#### Pricing
The pricing for the Xiaomi: MiMo-V2-Omni model is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance and Capabilities
The model has the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
It supports the following capabilities:
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
The estimated costs for using the Xiaomi: MiMo-V2-Omni model are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Xiaomi: MiMo-V2-Omni Model
Since there are no direct competitors listed, the decision to choose the Xiaomi: MiMo-V2-Omni model depends on the specific requirements of your project. Consider the following factors:
* **Context Window**: If your project requires a large context window, the Xiaomi: MiMo-V2-Omni model may be a good choice, with a context window of 262,144 tokens.
* **Output Limit**: If your project requires generating large outputs, the Xiaomi: MiMo-V2-Omni model may not be the best choice, with a maximum output limit of 65,536 tokens.
* **Knowledge Cutoff**: If your project requires knowledge up to 2023-12, the Xiaomi: MiMo-V2-Omni model may be a

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities and pricing. This guide will explore the top 5 best use cases for this model, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the model's capabilities and benchmarks, the top 5 use cases are:

1. **Chat and Text Generation**: With its high context window and ability to generate up to 65,536 tokens, Xiaomi: MiMo-V2-Omni is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's ability to perform function calling and generate structured outputs makes it a good fit for coding and analysis tasks.
3. **Summarization**: Xiaomi: MiMo-V2-Omni's high MMLU benchmark score and ability to generate concise outputs make it suitable for summarization tasks.
4. **RAG Pipelines**: The model's ability to handle JSON mode and streaming inputs makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
5. **Text Analysis**: With its high context window and ability to generate structured outputs, Xiaomi: MiMo-V2-Omni is well-suited for text analysis tasks.

### Code Integration Examples with OpenRouter
To integrate Xiaomi: MiMo-V2-Omni with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client()

# Set the model and input parameters
model = "xiaomi/mimo-v2-omni"
input_text = "This is an example input text."

# Generate output using the model
output = client.generate(
    model=model,
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
