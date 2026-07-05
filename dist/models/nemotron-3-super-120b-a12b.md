# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a powerful language model developed by Nvidia. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. It boasts an impressive architecture designed to handle a wide range of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. The Nemotron 3 Super is particularly suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super has a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023. The pricing model for this service includes charges for input and output, with rates set at $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. There are no charges listed for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities in various linguistic and cognitive tasks.

### Use Cases and Cost Considerations
Given its strengths and capabilities, the Nemotron 3 Super is best utilized for complex tasks that require deep understanding and generation of text, such as advanced chatbots, content creation, and code analysis. Developers can estimate costs based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $0.3, while 100,000 calls would amount to $30.0. With no direct competitors listed, the Nemotron 3 Super presents a unique offering in

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### NVIDIA Nemotron 3 Super Pricing Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
Given the cost structure, it's essential to understand when to use cached tokens and batch API calls to optimize costs.

* **Cached Input**: Since cached input is free, it's recommended to use cached tokens whenever possible, especially for repeated input sequences.
* **Batch Input**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost of output tokens still applies.

#### Batch API Savings
To illustrate the cost savings of using batch API calls, let's consider an example:
* Assume an average output of 500 tokens per API call.
* For 1,000 calls, the total output tokens would be 500,000 tokens.
* Using the batch API, the input cost would be $0, but the output cost would be **$0.5 per 1M tokens**. Therefore, the total output cost would be **$0.25** (500,000 tokens / 1,000,000 tokens \* $0.5).

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.3**
* **10,000 calls**: **$3.0

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis focuses on its benchmark performance and what the scores imply for real-world applications.

#### Pricing
The pricing model for the Nemotron 3 Super is as follows:
- **Input**: $0.1 per 1M tokens
- **Output**: $0.5 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Benchmarks
The model's performance is measured across several benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - The MMLU score indicates the model's ability to understand and perform a wide range of tasks. A higher score suggests better performance in multitask learning scenarios.
- **HumanEval**: None
  - HumanEval is a benchmark that evaluates a model's ability to generate correct code based on human-written tests. The absence of a score here indicates that the model's coding capabilities have not been evaluated through this specific benchmark.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score measures the model's competitive performance against other models in a variety of tasks. An ELO score of 1200 suggests a moderate level of competence, with higher scores indicating better performance.
- **GSM8K**: None
  - GSM8K is a benchmark focused on math problem-solving. The lack of a score means the model's math reasoning capabilities have not been assessed through this benchmark

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. With no direct competitors listed, this comparison will focus on the model's features, pricing, and performance trade-offs to help users determine when to choose this model.

#### Pricing
The NVIDIA Nemotron 3 Super pricing is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance Trade-offs
The model has the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**
The context window is **262,144 tokens**, and the max output is **4,096 tokens**. The knowledge cutoff is **2023-12**.

#### Capabilities and Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the NVIDIA Nemotron 3 Super are:
* 1,000 calls (avg 500 tokens): **$0.3**
* 10,000 calls: **$3.0**
* 100,000 calls: **$30.0**

#### Choosing the NVIDIA Nemotron 3 Super
Given the lack of direct competitors, the NVIDIA Nemotron 3 Super is a strong choice for users who require a standard-tier model with a large context window and support for various capabilities. However, users should consider the following:
* The model's knowledge cutoff is 2023-12, which may not be suitable for applications requiring more recent information.
* The pricing structure, with a higher cost for output tokens, may be a factor for users with high output requirements.

In conclusion, the NVIDIA Nemotron 3 Super is a capable model with a unique set of features and pricing. Users should carefully evaluate their requirements and consider the trade-offs before choosing this model.

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its standard tier and closed-source architecture, it offers a range of capabilities including text generation, function calling, and structured outputs. This guide will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it an ideal choice for applications such as virtual assistants, chatbots, and content generation platforms. With its context window of 262,144 tokens and max output of 4,096 tokens, it can handle complex conversations and generate high-quality text.

#### 2. **Coding and Function Calling**
The model's ability to perform function calling and generate code makes it suitable for applications such as code completion, code review, and automated coding tasks. For example, you can use the NVIDIA Nemotron 3 Super with OpenRouter to generate code snippets in various programming languages:
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Generate code snippet
input_text = "Write a Python function to calculate the area of a rectangle"
output = model.generate(input_text)

print(output)
```

#### 3. **Analysis and Summarization**
The NVIDIA Nemotron 3 Super can be used for text analysis and summarization tasks, such as summarizing long documents, extracting key points, and performing sentiment analysis. Its ability to handle large context windows and generate structured outputs makes it an ideal choice for these tasks.

#### 4. **RAG Pipelines**
The model's support for

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
