# GPT-4o Mini API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to GPT-4o Mini
The GPT-4o Mini, released by OpenAI on 2024-07-18, is a budget-friendly model designed for developers. This model is not open-source and is positioned as a cost-effective solution for various applications. With a context window of 128,000 tokens and a maximum output of 16,384 tokens, GPT-4o Mini is suitable for a range of tasks, from chatbots to bulk processing. Its knowledge cutoff is 2023-10, ensuring it has a robust understanding of information up to that point.

### Architecture and Strengths
GPT-4o Mini boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, structured outputs, streaming, batch processing, and system prompts. Its strengths are reflected in its benchmark scores: MMLU (82.0), HumanEval (87.2), LMSYS Arena ELO (1218), and GSM8K (87.0). These scores indicate the model's proficiency in various areas, making it an attractive choice for applications such as classification, summarization, and content moderation. The pricing structure is as follows: $0.15 per 1M tokens for input, $0.6 per 1M tokens for output, $0.075 per 1M tokens for cached input, and $0.075 per 1M tokens for batch input.

### Use Cases and Cost Considerations
GPT-4o Mini is best suited for tasks like chatbots, classification, summarization, bulk processing, and simple coding. However, it may not be the ideal choice for complex reasoning, long document analysis, cutting-edge coding, or research tasks. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls (avg 500 tokens) cost $0.375, 10,000 calls cost $3.75, and 

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $0.075 |
| Batch Input | $0.075 |
| Batch Output | $0.3 |

## Pricing Analysis
### GPT-4o Mini Pricing Analysis
#### Overview
The GPT-4o Mini model, released by OpenAI on 2024-07-18, is a budget-friendly option with a tier classification of "budget". This analysis will break down the cost structure, explore scenarios where cached tokens and batch API calls can lead to savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for GPT-4o Mini is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.075 per 1M tokens** (50% discount compared to regular input)
* Batch Input: **$0.075 per 1M tokens** (50% discount compared to regular input)

#### Using Cached Tokens
Cached tokens can significantly reduce costs when the same input is used multiple times. With a 50% discount, cached input tokens cost **$0.075 per 1M tokens**, making them an attractive option for applications with repetitive input patterns.

#### Batch API Savings
Batching API calls can also lead to cost savings. By using batch input, the cost per 1M tokens is reduced to **$0.075**, which is 50% of the regular input cost. This makes batch processing an efficient way to handle large volumes of data.

#### Cost at Scale
To illustrate the cost implications of using GPT-4o Mini at scale, consider the following examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples demonstrate how the cost increases linearly with the number of API calls.

#### Comparison to Top Competitors
GPT-4

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 82.0 |
| HumanEval | 87.2 |
| LMSYS Arena ELO | 1218 |
| ARC | 91.6 |

## Benchmark Analysis
### Analysis of GPT-4o Mini Benchmark Performance
The GPT-4o Mini model, released by OpenAI on 2024-07-18, is a budget-friendly option with a unique set of capabilities and limitations. To understand its performance, we'll delve into the benchmark scores and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 82.0
* **HumanEval**: 87.2
* **LMSYS Arena ELO**: 1218
* **GSM8K**: 87.0

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across multiple tasks. A score of 82.0 suggests that GPT-4o Mini has a good understanding of language, but may struggle with more complex or nuanced tasks.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 87.2 indicates that GPT-4o Mini is capable of generating high-quality code, making it suitable for tasks like simple coding and content moderation.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it's pitted against other models. An ELO score of 1218 suggests that GPT-4o Mini is a strong competitor, but may not be the top performer in all scenarios.
* **GSM8K**: Measures the model's ability to reason and solve math problems. A score of 87.0 indicates that GPT-4o Mini has

## Competitor Comparison
### GPT-4o Mini Comparison Against Top Competitors
#### Introduction
The GPT-4o Mini, released by OpenAI on 2024-07-18, is a budget-friendly model with a unique set of features and pricing. This comparison will delve into the specifics of the GPT-4o Mini, its top competitors, and provide guidance on when to choose each model.

#### Pricing Comparison
The pricing for the GPT-4o Mini is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $0.075 per 1M tokens
* Batch Input: $0.075 per 1M tokens

In comparison, the top competitors have the following pricing:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output
* OpenAI: GPT-3.5 Turbo: $0.5/1M input, $1.5/1M output

The GPT-4o Mini offers a significant cost advantage, particularly for input tokens, with a price point 81.25% lower than Claude 3.5 Haiku and 70% lower than GPT-3.5 Turbo.

#### Performance Trade-offs
The GPT-4o Mini has the following benchmarks:
* MMLU: 82.0
* HumanEval: 87.2
* LMSYS Arena ELO: 1218
* GSM8K: 87.0

While the performance of the GPT-4o Mini is not provided for the competitors, the GPT-4o Mini's capabilities and limitations suggest it is well-suited for tasks such as chatbots, classification, summarization, and bulk processing.

#### Context and Limits
The GPT-4o Mini has the following context and limits:
* Context Window: 128,000 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2023-10

These limits suggest that the GPT-4o Mini is not suitable for tasks requiring complex reasoning, long document analysis, cutting-edge coding, or research tasks.

#### Capabilities and Use Cases
The GPT-4o Mini has a wide range of capabilities, including:
* text
* vision
* function_calling
* json_mode


## Best Use Cases
### Introduction to GPT-4o Mini
The GPT-4o Mini model, released by OpenAI on 2024-07-18, is a budget-friendly option with a tier classification of "budget". Although it is not open source, it offers a range of capabilities, including text, vision, function calling, and more. In this guide, we will explore the top 5 best use cases for GPT-4o Mini, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for GPT-4o Mini
Based on the model's capabilities and limitations, the following are the top 5 use cases for GPT-4o Mini:

1. **Chatbots**: GPT-4o Mini is well-suited for chatbot applications, with its ability to process text inputs and generate human-like responses.
2. **Classification**: The model's classification capabilities make it an excellent choice for tasks such as sentiment analysis, spam detection, and content moderation.
3. **Summarization**: GPT-4o Mini can be used to summarize long pieces of text, extracting key points and main ideas.
4. **Bulk Processing**: With its ability to process large volumes of data, GPT-4o Mini is ideal for bulk processing tasks such as data cleaning, data transformation, and data analysis.
5. **Simple Coding**: The model's function calling and JSON mode capabilities make it suitable for simple coding tasks, such as generating code snippets or modifying existing code.

### Code Integration Examples with OpenRouter
To integrate GPT-4o Mini with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define a function to call the GPT-4o Mini model
def call_gpt4o_mini(prompt):
    response = client.call_model(
        model="gpt-4

## Frequently Asked Questions


---
*Data verified: 2026-04-09 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
