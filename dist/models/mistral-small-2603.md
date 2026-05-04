# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From a technical standpoint, Mistral Small 4 boasts an architecture that supports a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens. Its capabilities include handling text, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for various applications.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to perform well in chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for developers looking to integrate AI capabilities into their applications. The model's performance is backed by benchmarks such as an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its potential for handling complex tasks. However, it's essential to note the knowledge cutoff of 2023-12, which might limit its ability to handle very recent information or trends.

### Pricing and Cost Examples
The pricing for Mistral Small 4 is straightforward, with input costing $0.15 per 1M tokens and output at $0.6 per 1M tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens would cost $0.375, scaling up to $3.75 for 10,000 calls, and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 presents itself as a unique offering in the

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1 million tokens
- **Output**: $0.6 per 1 million tokens
- **Cached Input**: No charge
- **Batch Input**: No charge

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no charge for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is listed as having no charge, the actual cost savings come from optimizing the input and output token counts. By batching API calls, users can reduce the number of calls needed, thereby lowering the overall cost.

#### Cost at Scale
The provided cost examples illustrate the cost-effectiveness of Mistral Small 4 at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples demonstrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant.

#### Cost Calculation
To understand the cost structure better, let's calculate the cost per token:
- **Input Cost**: $0.15 per 1 million tokens = $0.00000015 per token
- **Output Cost**: $0.6 per 1 million tokens = $0.0000006 per token

Assuming an average output of 500 tokens per call (as in the 1,000 calls example), the total cost per call can be broken down into input and output

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
- Input: **$0.15 per 1M tokens**
- Output: **$0.6 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
- Context Window: **262,144 tokens**
- Max Output: **4,096 tokens**
- Knowledge Cutoff: **2023-12**

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is measured by the following scores:
- **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) score is a measure of a model's ability to understand and perform a wide range of natural language tasks. A higher score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a good level of language understanding.
- **HumanEval: None**: HumanEval is a benchmark that measures a model's ability to generate code that passes unit tests. The lack of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly.
- **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO score is a measure of a model's performance in a

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and with similar capabilities. 

#### Hypothetical Competitors
For the purpose of this comparison, let's consider two hypothetical models: 
- **Model A**: A standard, open-source model with similar capabilities to Mistral Small 4.
- **Model B**: A premium model with advanced capabilities and higher pricing.

#### Pricing Comparison
The pricing for Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

In comparison, the hypothetical competitors may have the following pricing:
- **Model A**: 
  - Input: $0.10 per 1M tokens (33% cheaper than Mistral Small 4)
  - Output: $0.4 per 1M tokens (33% cheaper than Mistral Small 4)
- **Model B**: 
  - Input: $0.30 per 1M tokens (100% more expensive than Mistral Small 4)
  - Output: $1.2 per 1M tokens (100% more expensive than Mistral Small 4)

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

In comparison, the hypothetical competitors may have the following performance metrics:
- **Model A**: 
  - MMLU: 70.0 (12.5% lower than Mistral Small 4)
  - LMSYS Arena ELO: 1000 (16.7% lower than Mistral Small 4)
- **Model B**: 
  - MMLU: 90.0 (12.5% higher than Mistral Small 4)
  - LMSYS Arena ELO: 1400 (16.7% higher than Mistral Small 4)

#### When to Choose Each Model
Based on the pricing and performance comparison, here are some guidelines on when to choose each model:
- **Mistral Small 4**: Choose this model when you need a balance between price and performance. It is suitable for applications such as chat, text generation, coding, analysis, and summarization.
- **Model A

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its ability to perform function calling and generate structured outputs makes it an excellent choice for coding and analysis tasks.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling enables it to be used in RAG (Retrieval-Augmented Generation) pipelines, which are useful for tasks like question answering and text generation.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or sentiment analysis.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    output = model.generate_text(prompt, max_length=4096)
    return output

# Use the function to generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
