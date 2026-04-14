# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a cutting-edge language model developed by Nvidia. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including but not limited to chat, text generation, coding, analysis, and summarization. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured as follows: input costs $0.1 per 1M tokens, and output costs $0.5 per 1M tokens, with no charges for cached input or batch input. This pricing model suggests that the cost of using the Nemotron 3 Super will primarily depend on the volume of input and output tokens. For example, 1,000 calls with an average of 500 tokens would cost $0.3, scaling up to $30.0 for 100,000 calls. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its strong capabilities in language understanding and generation.

### Use Cases and Competitors
Given its strengths in text generation, coding, and analysis, the Nemotron 3 Super is best suited for applications such as chatbots, content creation, programming assistance, and data analysis. Its ability to handle structured outputs and function calls also makes it suitable for complex pipelines and applications requiring precise data manipulation. Notably,

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
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost savings will depend on the output tokens, which are charged at $0.5 per 1M tokens.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These costs indicate a linear scaling of costs with the number of API calls.

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits should be taken into account when designing applications that utilize the NVIDIA Nemotron 3 Super.

#### Capabilities and Best Use Cases
The model has the following capabilities:
* **Text**: text generation and processing
* **Function Calling**: ability to call functions
* **JSON Mode**: support for

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
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0, indicating the model's ability to understand and perform various natural language tasks.
* **HumanEval**: Not available, which would have provided insights into the model's coding capabilities.
* **LMSYS Arena ELO**: A score of 1200, representing the model's competitive performance in a language modeling arena.
* **GSM8K**: Not available, which would have evaluated the model's math problem-solving skills.

#### Pricing
The pricing structure for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (not applicable)
* **Batch Input**: $None per 1M tokens (not applicable)

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 262,144 tokens, allowing for relatively long input sequences.
* **Max Output**: 4,096 tokens, suitable for generating short to medium-length text.
* **Knowledge Cutoff**: 2023-12, indicating that the model's training data only goes up to December 2023.

#### Capabilities and Best Use Cases
The

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on January 1, 2024. With its impressive capabilities and competitive pricing, it's essential to compare it with other top models in the market. However, since there are no direct competitors listed, we will provide a general overview of the Nemotron 3 Super's features, pricing, and performance trade-offs.

#### Pricing
The NVIDIA Nemotron 3 Super pricing is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance Trade-offs
The Nemotron 3 Super has a context window of **262,144 tokens** and a maximum output of **4,096 tokens**. Its knowledge cutoff is **2023-12**, which may limit its ability to provide information on very recent events. The model's benchmarks are:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**

#### Capabilities and Use Cases
The Nemotron 3 Super supports the following capabilities:
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
To give you a better idea of the costs involved, here are some examples:
* 1,000 calls (avg 500 tokens): **$0.3**
* 10,000 calls: **$3.0**
* 100,000 calls: **$30.0**

#### Choosing the Right Model
Since there are no direct competitors listed, the decision to choose the Nemotron 3 Super depends on your specific use case and requirements. If you need a model with a large context window, high output limit, and support for various capabilities, the Nemotron 3 Super may be a good choice. However, if you require a model with more recent knowledge or specific features not supported by the Nemotron 3 Super, you may need to consider other options.

### Conclusion
The NVIDIA Nemotron 3 Super is a powerful model with competitive pricing and impressive capabilities. While it may have

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful model released by Nvidia on 2024-01-01, with a standard tier and closed-source license. This model excels in various tasks, including chat, text generation, coding, analysis, rag pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Based on its capabilities, here are the top 5 best use cases for the NVIDIA Nemotron 3 Super:

1. **Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, the Nemotron 3 Super is ideal for generating long-form content, such as articles, stories, and dialogues.
2. **Coding and Function Calling**: The model's ability to perform function calling and generate structured outputs makes it suitable for coding tasks, such as code completion, code generation, and code analysis.
3. **Chat and Conversational AI**: The Nemotron 3 Super's capabilities in text generation and function calling make it an excellent choice for building conversational AI models, such as chatbots and virtual assistants.
4. **Analysis and Summarization**: With its high context window and ability to generate structured outputs, the model can be used for analyzing and summarizing large documents, such as research papers, articles, and reports.
5. **RAG Pipelines**: The Nemotron 3 Super's support for rag pipelines makes it suitable for tasks that require retrieving and generating text based on external knowledge sources.

### Code Integration Example with OpenRouter
To integrate the Nemotron 3 Super with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Define a function to generate text
def generate_text(prompt):
    #

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
