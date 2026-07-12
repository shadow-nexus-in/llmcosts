# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, is part of the standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. The model's pricing is based on input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. There are no charges for cached input or batch input. Benchmarks show the model scoring 80.0 on MMLU and 1200 on LMSYS Arena ELO, demonstrating its capabilities. The model is best suited for applications such as chat, text generation, coding, analysis, and summarization.

### Use Cases and Cost Considerations
Developers can leverage the Nemotron 3 Super for various applications, including chatbots, content generation, and code analysis. However, its suitability for certain tasks is yet to be determined, as indicated by the absence of direct competitors and some benchmark scores. To plan usage, developers can consider the cost examples provided: 1,000 calls averaging 500 tokens cost $0.3, scaling to $3.0 for 10,000 calls and $30.0 for 100,000 calls. Understanding

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
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and batch API savings for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input sequences.
* **Batch API Calls**: Leverage batch input to reduce costs. Although the pricing is listed as $0 per 1M tokens, this can lead to significant savings by minimizing the number of API calls.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at various scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$0.3**
* **10,000 API calls**: **$3.0**
* **100,000 API calls**: **$30.0**

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Context and Limits
When using the NVIDIA Nemotron 3 Super, consider the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These constraints can impact the model's performance and suitability for specific applications.

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:


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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score is a measure of a model's ability to understand and perform a wide range of natural language processing tasks. A score of 80.0 indicates that the NVIDIA Nemotron 3 Super has a high level of language understanding, capable of handling complex tasks with a good degree of accuracy. This score suggests the model is suitable for applications requiring comprehensive language comprehension, such as text generation, analysis, and summarization.

- **HumanEval Score: None**
  The HumanEval score evaluates a model's ability to generate correct code based on human-written tests. The absence of a HumanEval score for the NVIDIA Nemotron 3 Super means its coding capabilities, while listed as a capability, are not benchmarked in this context. This does not necessarily indicate poor performance but rather a lack of data for this specific metric.

- **LMSYS Arena ELO Score: 1200**
  The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, often involving tasks that require strategic thinking and problem-solving. An ELO score of 1200 suggests that the NVIDIA Nemotron 3 Super has a moderate level of competence in such tasks. For real-world applications, this score implies

## Competitor Comparison
### Comparison of NVIDIA: Nemotron 3 Super with Top Competitors
Since there are no direct competitors listed for the NVIDIA: Nemotron 3 Super, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of the Nemotron 3 Super and make informed decisions about its adoption.

#### Model Overview
The NVIDIA: Nemotron 3 Super is a standard-tier model released on January 1, 2024. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: December 2023
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the NVIDIA: Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Performance
The model's performance is measured by the following benchmarks:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

#### Cost Examples
To help users estimate the costs of using the Nemotron 3 Super, here are some examples:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Choosing the Nemotron 3 Super
Given the lack of direct competitors, the Nemotron 3 Super is a strong option for users who require a model with advanced capabilities such as function calling, JSON mode, and streaming. Its high context window and max output make it suitable for applications that require generating long pieces of text or analyzing large amounts of data.

However, users should consider the following factors when deciding whether to choose the Nemotron 3 Super:
* **Cost**: The model's pricing may be a barrier for users with limited budgets or high-volume usage requirements.
* **Performance**: While the model's benchmarks are impressive, users should evaluate its performance on their specific use cases to ensure it meets

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities and competitive pricing, it's an attractive choice for various applications. Here are the top 5 best use cases for this model, along with code integration examples using OpenRouter.

### Top 5 Use Cases
#### 1. **Chat and Text Generation**
Nemotron 3 Super excels in chat and text generation tasks, thanks to its large context window of 262,144 tokens and ability to generate up to 4,096 tokens of output. You can use it to build conversational AI models or generate high-quality text content.
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Generate text based on a prompt
prompt = "Write a story about a character who discovers a hidden world."
response = model.generate_text(prompt, max_tokens=2048)
print(response)
```
#### 2. **Coding and Function Calling**
The model's ability to perform function calling and generate structured outputs makes it suitable for coding tasks, such as code completion, code review, and bug detection.
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Call a function to generate code
function_call = "def greet(name: str) -> str:"
response = model.call_function(function_call, max_tokens=512)
print(response)
```
#### 3. **Analysis and Summarization**
Nemotron 3 Super can be used for text analysis and summarization tasks, such as extracting key points from a document or summarizing a long piece of text.
```python
import openrouter

#

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
