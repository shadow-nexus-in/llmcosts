# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, is part of the standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Strengths
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. The model's pricing is based on input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities. The Nemotron 3 Super is best utilized for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks, leveraging its strengths in these areas.

### Use Cases and Cost Considerations
Developers can leverage the Nemotron 3 Super for various applications, given its broad capabilities. However, it's essential to consider the cost implications of using this model. For example, 1,000 calls with an average of 500 tokens would cost $0.3, while 10,000 calls would amount to $3.0, and 100,000 calls would be $30.0. Understanding these costs and the model's limitations, such as its context window and knowledge cutoff,

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.

#### Batch API Savings
Although batch input is free, the actual cost savings will depend on the output token count. Since output tokens are charged at **$0.5 per 1M tokens**, batching can help reduce the overall cost by minimizing the number of API calls required.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.3**
* **10,000 calls**: **$3.0**
* **100,000 calls**: **$30.0**

These costs demonstrate a linear scaling of expenses with the number of API calls. To minimize costs, it is essential to optimize input token usage, leverage cached tokens, and batch API calls when possible.

#### Conclusion
The NVIDIA Nemotron 3 Super offers a robust set of capabilities, including text, function calling, JSON mode, streaming, and structured outputs. While there are no direct competitors listed, understanding the cost structure and optimizing usage patterns can help users make the most of this

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on 2024-01-01. This analysis focuses on its benchmark performance and what the scores mean for real-world use.

#### Benchmark Scores
The model has the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: None
* **LMSYS Arena ELO**: 1200
* **GSM8K**: None

These scores provide insights into the model's capabilities:
* **MMLU**: A score of 80.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher score suggests better performance in tasks that require a deep understanding of language.
* **LMSYS Arena ELO**: An ELO score of 1200 suggests the model's competitive performance in a controlled environment, where it is pitted against other models. This score is a measure of the model's overall language understanding and generation capabilities.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* **Text generation and analysis**: The model's high MMLU score suggests it is well-suited for tasks that require generating human-like text, such as chatbots, text summarization, and content generation.
* **Coding and function calling**: The model's capabilities in function calling and JSON mode suggest it can be used for tasks that require generating code or interacting with APIs.
* **RAG pipelines and summarization**: The model's high MMLU score and capabilities in structured outputs suggest it can be used

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a detailed analysis of its features, pricing, and performance. This will help users understand the value proposition of this model and make informed decisions about its adoption.

#### Model Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on January 1, 2024. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using the NVIDIA Nemotron 3 Super, consider the following examples:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

#### Performance
The NVIDIA Nemotron 3 Super has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

While there are no direct competitors to compare the NVIDIA Nemotron 3 Super with, its performance and pricing make it a compelling option for users who require a standard-tier model with advanced capabilities.

#### Choosing the NVIDIA Nemotron 3 Super
Consider the following scenarios where the NVIDIA Nemotron 3 Super may be the best choice:
* **Chat and text generation applications**: The model's high context window and max output make it well-suited for chat and text generation tasks.
* **Coding and analysis**: The model's function_calling and structured_outputs capabilities make it a good fit for coding and analysis tasks.
* **RAG pipelines and summarization**: The model's capabilities and performance make it a suitable choice for RAG pipelines and summarization tasks.

In conclusion

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this section, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. Chat and Text Generation
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it suitable for applications such as:
* Customer service chatbots
* Content generation for blogs or social media
* Automated email responses

Example code integration with OpenRouter:
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Define a chat function
def chat(input_text):
    output = model.generate_text(input_text, max_length=4096)
    return output

# Test the chat function
input_text = "Hello, how are you?"
output = chat(input_text)
print(output)
```

#### 2. Coding and Analysis
The NVIDIA Nemotron 3 Super is capable of function calling and structured outputs, making it a great choice for:
* Code completion and suggestion
* Code analysis and review
* Automated code generation

Example code integration with OpenRouter:
```python
import openrouter

# Initialize the NVIDIA Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Define a code completion function
def complete_code(input_code):
    output = model.generate_code(input_code, max_length=4096)
    return output

# Test the code completion function
input_code = "

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
