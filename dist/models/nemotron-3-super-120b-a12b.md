# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA: Nemotron 3 Super
The NVIDIA: Nemotron 3 Super (nvidia/nemotron-3-super-120b-a12b) is a powerful language model developed by Nvidia, released on January 1, 2024. This model is categorized as a standard, non-open-source tier, indicating its robust capabilities and restricted accessibility. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, the Nemotron 3 Super is designed to handle complex and lengthy input sequences, making it suitable for a wide range of applications.

### Architecture and Strengths
The Nemotron 3 Super boasts an impressive architecture, with a model size of 120 billion parameters. Its primary strengths lie in its ability to process and generate high-quality text, perform function calling, and handle JSON mode, streaming, and structured outputs. The model's capabilities are further enhanced by its support for various use cases, including chat, text generation, coding, analysis, RAG pipelines, and summarization. The pricing model for this service is based on input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, demonstrating its strong language understanding and generation capabilities.

### Use Cases and Cost Considerations
The Nemotron 3 Super is best suited for applications that require advanced text processing, generation, and analysis. Its capabilities make it an ideal choice for chatbots, text generation, coding, and data analysis tasks. However, the model's pricing should be carefully considered, as the costs can add up quickly. For example, 1,000 calls with an average of 500 tokens per call would cost $0.3, while 100,000 calls would cost $30.0.

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model provided by Nvidia, released on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: No additional cost ($None per 1M tokens)
* **Batch Input**: No additional cost ($None per 1M tokens)

#### Usage Scenarios
* **Cached Tokens**: Since there is no additional cost for cached input tokens, it is recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although there is no explicit cost savings mentioned for batch input, the absence of additional cost implies that batch processing can be an efficient way to reduce the overall cost per token.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

To estimate the cost at scale, we can extrapolate from the provided examples:
* Assuming an average of 500 tokens per call, the cost per 1M tokens can be estimated as follows:
	+ 1,000 calls: 500,000 tokens (avg) / 1,000 calls = 500 tokens/call
	+ Cost per 1M tokens: $0.3 / 0.5M tokens = $0.6 per 1M tokens (approximate)
* However, the provided cost examples suggest a more complex pricing structure. To better understand the cost at scale, let's analyze the cost per call

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Model Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. It is not open-source and has a context window of 262,144 tokens, with a maximum output of 4,096 tokens. The knowledge cutoff for this model is 2023-12.

#### Pricing
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The benchmark performance of the NVIDIA Nemotron 3 Super is as follows:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, the NVIDIA Nemotron 3 Super demonstrates strong language understanding capabilities.
* **HumanEval: None**: The HumanEval benchmark evaluates a model's ability to write code that is correct and functional. Unfortunately, no HumanEval score is available for the NVIDIA Nemotron 3 Super.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. An ELO score of 1200 indicates that the NVIDIA Nemotron 3 Super is a strong competitor in this

## Competitor Comparison
### Comparison of NVIDIA Nemotron 3 Super with Top Competitors
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of the Nemotron 3 Super and make informed decisions about its adoption.

#### Model Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released on January 1, 2024. It is not open-source and has the following key features:

* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: December 2023
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the NVIDIA Nemotron 3 Super is as follows:

* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using the Nemotron 3 Super, here are some examples:

* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Performance
The Nemotron 3 Super has the following benchmark scores:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Note that the HumanEval and GSM8K benchmark scores are not available.

#### Choosing the Nemotron 3 Super
Since there are no direct competitors listed, the decision to choose the Nemotron 3 Super depends on the specific use case and requirements. Consider the following factors:

* **Context Window**: If you need to process large amounts of text, the Nemotron 3 Super's context window of 262,144 tokens may be a good fit.
* **Capabilities**: If you require advanced features like function_calling, json_mode, streaming, and structured_outputs, the Nemotron 3 Super may be a good choice.
* **Pricing**: If you are sensitive to input and output costs, the Nemotron 

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this section, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it suitable for applications like customer support chatbots and content generation platforms.
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Generate text based on a prompt
prompt = "Write a short story about a character who discovers a hidden world."
response = model.generate_text(prompt)
print(response)
```

#### 2. **Coding and Analysis**
With its capabilities in function calling and structured outputs, the NVIDIA Nemotron 3 Super can be used for coding and analysis tasks, such as code completion and data analysis.
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Analyze a piece of code and provide suggestions for improvement
code = "def add(a, b): return a + b"
response = model.analyze_code(code)
print(response)
```

#### 3. **Summarization and RAG Pipelines**
The NVIDIA Nemotron 3 Super can be used for summarization tasks, such as summarizing long documents or articles, and for RAG (Retrieve, Augment, Generate) pipelines.
```python


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
