# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy text-based applications.

### Primary Use-Cases and Strengths
The main use-cases for Mistral: Mistral Small 4 include chat, text generation, coding, analysis, RAG pipelines, and summarization. This model is particularly adept at handling tasks that require a deep understanding of context and the ability to generate coherent and lengthy responses. With a context window of 262,144 tokens and a knowledge cutoff of 2023-12, Mistral: Mistral Small 4 is well-equipped to handle a wide range of applications, from simple text generation to more complex tasks like coding and analysis. Its performance is backed by benchmarks such as an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its capability in understanding and generating human-like text.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would cost $3.75, and 100,000

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
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Batch input is also free, making it an attractive option for large-scale API calls. This can significantly reduce costs when making multiple requests.

#### Cost at Scale
The costs for Mistral Small 4 at different scales are as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls. It is essential to consider these costs when planning large-scale deployments or applications.

#### Context and Limits
Mistral Small 4 has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits should be taken into account when designing applications to ensure they operate within the model's capabilities.

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
The Mistral Small 4 model, provided by Mistralai, has the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: Not available
* **LMSYS Arena ELO**: 1200

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate text across a wide range of tasks. A score of 80.0 suggests that Mistral Small 4 has a good understanding of language, but may not be as proficient as models with higher scores.
* **HumanEval**: Evaluates the model's ability to generate code that is correct and functional. Unfortunately, this score is not available for Mistral Small 4.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that Mistral Small 4 is a mid-tier model, capable of holding its own against other models, but may struggle against top-tier models.

### Real-World Implications
In real-world use cases, these scores mean that Mistral Small 4 is suitable for:
* **Text generation**: With a decent MMLU score, Mistral Small 4 can generate coherent and contextually relevant text.
* **Coding**: Although the HumanEval score is not available, the model's capabilities include function_calling and json_mode, suggesting it can be used for coding tasks.
* **Analysis and summarization**: Mistral Small 4's context window of 262,144 tokens and max output

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help in understanding where Mistral: Mistral Small 4 stands in the market and when to choose this model over others.

#### Model Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on 2024-01-01. It is not open source.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2023-12

#### Benchmarks
The model's performance is measured by the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

#### Capabilities and Best Use Cases
Mistral: Mistral Small 4 supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Given the lack of direct competitors, Mistral: Mistral Small 4 can be considered for its unique combination of capabilities, including text generation, coding, and analysis. Its pricing model, based on input and output tokens, makes it suitable for applications where the input and output sizes are relatively small.

When to choose Mistral: Mistral Small 4:
- **Development and testing**: For development and testing purposes, Mistral: Mistral Small 4 can be a

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it an excellent choice for coding tasks, such as code completion and code analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great choice for summarization tasks.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it an excellent choice for tasks that require generating text based on external knowledge sources.
5. **Streaming**: With its support for streaming, Mistral Small 4 can be used for real-time text generation and processing tasks.

### Code Integration Example with OpenRouter
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

# Test the function


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
