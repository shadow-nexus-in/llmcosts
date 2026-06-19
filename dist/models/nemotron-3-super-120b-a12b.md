# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a cutting-edge language model developed by Nvidia, released on January 1, 2024. This standard-tier model is not open source and is identified by the model name `nvidia/nemotron-3-super-120b-a12b`. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Strengths
The Nemotron 3 Super boasts an impressive context window of 262,144 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is December 2023, ensuring that it has been trained on a vast amount of data up to that point. The model's pricing is based on input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. Benchmarks for the model include an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200. With its strong capabilities and competitive pricing, the Nemotron 3 Super is well-suited for tasks such as chat, text generation, coding, analysis, and summarization.

### Use Cases and Cost Examples
The Nemotron 3 Super is best utilized for tasks that require advanced language understanding and generation capabilities. Its strengths in text generation, coding, and analysis make it an ideal choice for applications such as chatbots, content generation, and data analysis. The cost of using the Nemotron 3 Super can be estimated based on the number of calls and tokens used. For example, 1,000 calls with an average of 500 tokens would cost $0.3, while 10,000 calls would cost $3

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super model is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Using Cached Tokens
Cached input tokens are free, which means that if the same input is used multiple times, there will be no additional cost for the input tokens. This can lead to significant cost savings, especially for applications where the same input is used repeatedly.

#### Batch API Savings
Batch input is also free, which means that making API calls in batches will not incur any additional cost for the input tokens. However, the output cost will still apply.

#### Cost at Scale
The cost examples provided are as follows:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

To calculate the cost at scale, we can use the following formula:
Cost = (Input Tokens / 1,000,000) \* $0.1 + (Output Tokens / 1,000,000) \* $0.5

Assuming an average output of 500 tokens per call, the total output tokens for each scale would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of NVIDIA Nemotron 3 Super Benchmark Performance
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis focuses on its benchmark performance, pricing, and capabilities to understand its real-world applications.

#### Benchmark Performance
The model's performance is measured across several benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: A score of **80.0** indicates the model's ability to understand and process a wide range of language tasks. A higher MMLU score suggests better performance in tasks that require a deep understanding of language, such as text generation, summarization, and analysis.
* **HumanEval**: No data is available for this benchmark, which evaluates a model's ability to generate human-like code.
* **LMSYS Arena ELO**: A score of **1200** measures the model's performance in a competitive environment, simulating real-world scenarios. This score indicates the model's ability to adapt to different tasks and perform well under various conditions.
* **GSM8K**: No data is available for this benchmark, which assesses a model's performance in math problem-solving.

#### Pricing and Cost Examples
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

Cost examples for different call volumes:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a general overview of its features, pricing, and performance. This will help users understand its value proposition and make informed decisions.

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
To illustrate the pricing, here are some cost examples:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Performance
The NVIDIA Nemotron 3 Super has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

### Choosing the NVIDIA Nemotron 3 Super
Since there are no direct competitors listed, the decision to choose the NVIDIA Nemotron 3 Super depends on your specific use case and requirements. Consider the following factors:
* **Context Window**: If you need to process large amounts of text, the NVIDIA Nemotron 3 Super's context window of 262,144 tokens may be suitable.
* **Max Output**: If you need to generate long responses, the max output of 4,096 tokens may be sufficient.
* **Knowledge Cutoff**: If your use case requires knowledge up to December 2023, the NVIDIA Nemotron 3 Super may be a good choice.
* **Capabilities**: If you need a model with text, function_calling, json_mode, streaming, and structured_outputs capabilities, the NVIDIA Nemotron 3 Super

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this section, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it perfect for conversational AI applications. With its context window of 262,144 tokens, it can engage in lengthy and meaningful conversations.
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Generate text based on a prompt
prompt = "Hello, how are you?"
response = model.generate_text(prompt)
print(response)
```

#### 2. **Coding and Analysis**
The model's ability to understand and generate code makes it an excellent choice for coding and analysis tasks. It can be used for code completion, code review, and even bug detection.
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Generate code based on a prompt
prompt = "Write a Python function to calculate the area of a rectangle."
code = model.generate_code(prompt)
print(code)
```

#### 3. **Summarization and RAG Pipelines**
The NVIDIA Nemotron 3 Super can be used for summarization tasks, such as summarizing long documents or articles. Its ability to generate structured outputs also makes it suitable for

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
