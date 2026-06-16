# GPT-4o API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to GPT-4o
The GPT-4o model, released by OpenAI on 2024-05-13, is a premium, non-open-source language model designed to provide advanced capabilities for developers. With a context window of 128,000 tokens and a maximum output of 16,384 tokens, GPT-4o is well-suited for complex tasks that require extensive input and output processing. Its knowledge cutoff is 2024-04, ensuring that it has been trained on a vast amount of data up to that point.

### Architecture and Strengths
GPT-4o boasts an impressive array of capabilities, including text, vision, function calling, JSON mode, structured outputs, streaming, and batch processing. Its strengths are reflected in its benchmark scores, which include an MMLU score of 88.7, a HumanEval score of 90.2, an LMSYS Arena ELO score of 1295, and a GSM8K score of 96.1. These scores demonstrate GPT-4o's exceptional performance in coding, analysis, and other complex tasks. The model is priced at $2.5 per 1M input tokens, $10.0 per 1M output tokens, with discounts available for cached input and batch input at $1.25 per 1M tokens.

### Use Cases and Cost Considerations
GPT-4o is best suited for tasks such as coding, analysis, summarization, vision tasks, function calling, content generation, and data extraction. However, it is not recommended for simple classification, embeddings, bulk cheap tasks, or real-time tasks that require sub-100ms response times. The cost of using GPT-4o can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $6.25, while 10,000 calls would cost $

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $2.5 |
| Output | $10.0 |
| Cached Input | $1.25 |
| Batch Input | $1.25 |
| Batch Output | $5.0 |

## Pricing Analysis
### GPT-4o Pricing Analysis
#### Overview
The GPT-4o model, released by OpenAI on 2024-05-13, is a premium, non-open source model with a unique pricing structure. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and calculate the cost at scale for 1k, 10k, and 100k API calls.

#### Cost Structure
The pricing for GPT-4o is as follows:
* Input: **$2.5 per 1M tokens**
* Output: **$10.0 per 1M tokens**
* Cached Input: **$1.25 per 1M tokens**
* Batch Input: **$1.25 per 1M tokens**

#### Using Cached Tokens
Cached tokens can significantly reduce costs. If the input is likely to be repeated, using cached tokens can save **50%** of the input cost, from **$2.5 per 1M tokens** to **$1.25 per 1M tokens**.

#### Batch API Savings
Batching API calls can also lead to cost savings. The batch input price is **$1.25 per 1M tokens**, which is **50%** of the regular input price. This can be beneficial for large-scale applications where multiple inputs can be batched together.

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): **$6.25**
* 10,000 calls: **$62.5**
* 100,000 calls: **$625.0**

To calculate the cost at scale, we can use the following formula:
Cost = (Number of Calls \* Average Tokens per Call \* Input Price per Token) + (Number of Calls \* Average Output Tokens per Call \* Output Price per Token)

Assuming an average of 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 88.7 |
| HumanEval | 90.2 |
| LMSYS Arena ELO | 1295 |
| ARC | 96.4 |

## Benchmark Analysis
### GPT-4o Benchmark Performance Analysis
#### Model Overview
The GPT-4o model, provided by OpenAI, was released on 2024-05-13 as a premium, non-open-source model. 

#### Pricing
The pricing for GPT-4o is as follows:
* Input: **$2.5 per 1M tokens**
* Output: **$10.0 per 1M tokens**
* Cached Input: **$1.25 per 1M tokens**
* Batch Input: **$1.25 per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **128,000 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-04**

#### Benchmark Performance
The benchmark performance of GPT-4o is as follows:
* MMLU: **88.7**
* HumanEval: **90.2**
* LMSYS Arena ELO: **1295**
* GSM8K: **96.1**

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 88.7 indicates strong performance in this area.
* **HumanEval**: Evaluates the model's ability to generate code that is correct and functional. A score of 90.2 suggests that GPT-4o is highly proficient in coding tasks.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, where it is pitted against other models

## Competitor Comparison
### GPT-4o Comparison with Top Competitors
#### Overview
GPT-4o, released by OpenAI on 2024-05-13, is a premium, non-open source model that offers a range of capabilities, including text, vision, function calling, and more. This comparison will focus on the pricing, performance, and use cases of GPT-4o against its top competitors.

#### Pricing Comparison
The pricing for GPT-4o is as follows:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens
* Cached Input: $1.25 per 1M tokens
* Batch Input: $1.25 per 1M tokens

In comparison, OpenAI o1, a top competitor, is priced at:
* Input: $15.0 per 1M tokens
* Output: $60.0 per 1M tokens

GPT-4o offers a significant cost savings, with input costs 83.3% lower and output costs 83.3% lower than OpenAI o1.

#### Performance Trade-offs
GPT-4o has demonstrated strong performance on various benchmarks:
* MMLU: 88.7
* HumanEval: 90.2
* LMSYS Arena ELO: 1295
* GSM8K: 96.1

While the performance of OpenAI o1 is not provided, the significant cost difference between the two models suggests that GPT-4o may offer a more cost-effective solution for many use cases.

#### Context and Limits
GPT-4o has the following context and limits:
* Context Window: 128,000 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-04

These limits are not directly comparable to OpenAI o1, as the data is not provided. However, GPT-4o's large context window and max output make it suitable for a wide range of applications.

#### Capabilities and Use Cases
GPT-4o offers a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Structured outputs
* Streaming
* Batch processing
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Agents
* Summarization
* Vision tasks

## Best Use Cases
### Introduction to GPT-4o
The GPT-4o model, released by OpenAI on 2024-05-13, is a premium, non-open-source language model. With its impressive capabilities and benchmarks, it is best suited for tasks such as coding, analysis, and vision tasks.

### Top 5 Best Use Cases for GPT-4o
Based on its capabilities and benchmarks, here are the top 5 best use cases for GPT-4o:

1. **Coding and Function Calling**: GPT-4o excels in coding tasks, with a HumanEval score of 90.2. It can be used for code completion, code review, and even function calling.
2. **Analysis and Summarization**: With its high MMLU score of 88.7, GPT-4o is well-suited for analysis and summarization tasks. It can be used to analyze large documents and summarize key points.
3. **Vision Tasks**: GPT-4o has capabilities in vision tasks, making it a great choice for image classification, object detection, and image generation.
4. **Content Generation**: With its high GSM8K score of 96.1, GPT-4o is well-suited for content generation tasks such as writing articles, creating stories, and even generating dialogue.
5. **Data Extraction**: GPT-4o's capabilities in structured outputs and json_mode make it a great choice for data extraction tasks, such as extracting data from unstructured text.

### Code Integration Examples with OpenRouter
To integrate GPT-4o with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the GPT-4o model
model = openrouter.GPT4o()

# Define a function to call the model
def call_model(prompt):
    response = model.generate(prompt)
    return response

# Call the model with a prompt
prompt

## Frequently Asked Questions


---
*Data verified: 2026-04-09 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
