# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an impressive architecture that supports capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require extensive context understanding.

### Technical Strengths and Use Cases
The strengths of Mistral Large 2 are evident in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in handling a variety of tasks, from mathematical and logical reasoning to coding and natural language understanding. Given its capabilities, Mistral Large 2 is best utilized for tasks such as coding, analysis, retrieval-augmented generation (RAG), and function calling, especially in multilingual contexts. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To put this into perspective, for 1,000 calls averaging 500 tokens, the cost would be $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Calls**: With batch input tokens being free, making batch API calls can significantly reduce the overall cost.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

To put this into perspective, assuming an average of 500 tokens per call, the cost per 1M tokens can be calculated as follows:
* **1,000 calls**: 500 tokens/call \* 1,000 calls = 500,000 tokens, costing **$6.0** (input: 500,000 tokens \* $3.0/1M tokens = $1.5, output: assuming 500,000 tokens \* $9.0/1M tokens = $4.5, total: $1.5 + $4.5 = $6.0)
* **10,000 calls**: 500 tokens/call \* 10,000 calls

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, boasts impressive benchmark scores. This analysis will delve into the MMLU, HumanEval, and Arena ELO scores, explaining their implications for real-world applications.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1225
* **GSM8K**: 93.0

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across multiple tasks. A score of 84.0 suggests that Mistral Large 2 is capable of handling complex language tasks with a high degree of accuracy.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. With a score of 92.0, Mistral Large 2 demonstrates exceptional coding capabilities, making it suitable for tasks that require generating code.
* **LMSYS Arena ELO**: Assesses the model's overall language understanding and generation capabilities in a competitive setting. An ELO score of 1225 indicates that Mistral Large 2 is a strong performer in this area.

#### Real-World Implications
The benchmark scores have significant implications for real-world use cases:
* **Coding and analysis**: Mistral Large 2's high HumanEval score makes it an excellent choice for coding tasks, such as generating code snippets or entire programs.
* **Multilingual support**: The model's strong MML

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will evaluate Mistral Large 2 against its top competitor, GPT-4o, focusing on pricing, performance, and use cases.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-intensive tasks, GPT-4o is 16.7% cheaper, while for output-intensive tasks, Mistral Large 2 is 10% cheaper.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

GPT-4o's benchmark scores are not provided, making a direct comparison challenging. However, Mistral Large 2's scores indicate strong performance in coding, analysis, and multilingual tasks.

#### Capabilities and Limitations
Mistral Large 2 supports:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks and capabilities, it's essential to understand the best use cases for this model.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding Assistance**: Mistral Large 2 achieves a high score of 92.0 on HumanEval, making it an excellent choice for coding tasks, such as code completion, code review, and code optimization.
2. **Complex Analysis**: With a context window of 131,072 tokens, Mistral Large 2 can handle large amounts of text data, making it suitable for complex analysis tasks, such as text summarization, sentiment analysis, and entity recognition.
3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2's ability to handle function calling and JSON mode makes it an excellent choice for RAG tasks, which involve retrieving information from external sources and generating text based on that information.
4. **Multilingual Support**: Mistral Large 2's multilingual capabilities make it an excellent choice for tasks that require support for multiple languages, such as language translation, language detection, and cross-lingual information retrieval.
5. **Agent-Based Systems**: With its ability to handle system prompts and function calling, Mistral Large 2 is well-suited for agent-based systems, such as chatbots, virtual assistants, and autonomous agents.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client("mistralai/mistral-large-2407")

# Define a function to call the model
def call_model(prompt):
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
