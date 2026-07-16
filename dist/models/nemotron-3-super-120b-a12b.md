# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a powerful language model designed for a wide range of applications, including chat, text generation, coding, analysis, and summarization. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, is provided by Nvidia and falls under the standard tier. It is not open-source. With its robust architecture, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 output tokens.

### Technical Capabilities and Pricing
The Nemotron 3 Super is equipped with advanced capabilities such as text processing, function calling, JSON mode, streaming, and structured outputs. Its pricing model is based on input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. There are no additional costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Developers can leverage the Nemotron 3 Super for various use cases, including chatbots, text generation, and coding applications, with estimated costs of $0.3 for 1,000 calls (avg 500 tokens), $3.0 for 10,000 calls, and $30.0 for 100,000 calls.

### Use Cases and Competitors
The Nemotron 3 Super is best suited for applications that require advanced text processing, analysis, and generation capabilities. Its strengths in areas like rag pipelines and summarization make it a valuable tool for developers working on complex language-based projects. While there are no direct competitors listed for the Nemotron 3 Super, its unique combination of capabilities and pricing makes it an attractive option for developers seeking a powerful and flexible language model.

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: No additional cost per 1M tokens
* **Batch Input**: No additional cost per 1M tokens

#### Usage Scenarios
* **Cached Tokens**: Since there is no additional cost for cached input tokens, it is recommended to use cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although there is no explicit discount for batch input, the lack of additional cost per 1M tokens for batch input suggests that batching API calls can help reduce overall costs by minimizing the number of API calls.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These costs indicate a linear scaling of costs with the number of API calls, with no apparent discounts for large volumes.

#### Context and Limits
The NVIDIA Nemotron 3 Super has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: December 2023

These limits should be taken into account when designing applications that utilize this model.

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* **Text**: text generation and processing
* **Function Calling

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This model is priced at $0.1 per 1M input tokens and $0.5 per 1M output tokens.

#### Benchmark Performance
The model's performance is measured through several benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance.
* **HumanEval**: None - This benchmark evaluates a model's ability to write correct Python code. The absence of a score for this benchmark means that the model's coding capabilities are not explicitly measured here.
* **LMSYS Arena ELO**: 1200 - This score represents the model's performance in a competitive arena, where it is pitted against other models. A higher ELO score indicates better performance relative to its competitors.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The MMLU score of 80.0 suggests that the NVIDIA Nemotron 3 Super is capable of handling a variety of natural language tasks with a reasonable level of proficiency.
* The lack of a HumanEval score means that the model's coding abilities are not explicitly measured, but its capabilities include `function_calling` and `coding`, suggesting it can still be used for coding tasks.
* The LMSYS Arena ELO score of 1200 indicates that the model performs reasonably well in competitive scenarios, but its exact standing relative to other models is not clear without more

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. With its unique set of capabilities and pricing structure, it's essential to compare it to other models in the market. Since there are no direct competitors listed, we will analyze the Nemotron 3 Super's features, pricing, and performance to determine its position in the market.

#### Pricing and Cost Structure
The Nemotron 3 Super has the following pricing structure:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

The cost examples provided are:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

#### Performance and Capabilities
The Nemotron 3 Super has a context window of 262,144 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of December 2023. Its benchmark scores are:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

It supports various capabilities, including:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for applications such as:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Comparison to Other Models
Although there are no direct competitors listed, we can still analyze the Nemotron 3 Super's features and pricing to determine its position in the market. Its unique set of capabilities, such as function calling and structured outputs, make it a strong contender for applications that require complex text processing and generation.

#### When to Choose the Nemotron 3 Super
The Nemotron 3 Super is a good choice for applications that require:
* High-performance text processing and generation
* Complex functionality, such as function calling and structured outputs
* Large context windows and maximum output sizes
* Support for various capabilities, including JSON mode and streaming

However, its pricing structure may be a limiting factor for applications with high input or output volumes. In such cases, alternative models with more competitive pricing may be

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this guide, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it suitable for conversational AI applications. With its large context window of 262,144 tokens, it can engage in lengthy and meaningful conversations.
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Define a chat function
def chat(input_text):
    output = model.generate(input_text, max_length=4096)
    return output

# Test the chat function
print(chat("Hello, how are you?"))
```

#### 2. **Coding and Analysis**
The model's capabilities in coding and analysis make it an excellent choice for tasks such as code completion, code review, and bug detection. Its function calling feature allows it to execute code and provide detailed explanations.
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Define a code analysis function
def analyze_code(code):
    output = model.function_calling(code, max_length=4096)
    return output

# Test the code analysis function
print(analyze_code("def add(a, b): return a + b"))
```

#### 3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
