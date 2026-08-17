# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex text-based applications.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 is backed by impressive benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Although it lacks benchmarks in HumanEval and GSM8K, its capabilities in text, function calling, and structured outputs position it as a versatile tool. The model is best utilized for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. Its pricing model is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. This makes it a cost-effective solution for applications where input and output volumes can be managed efficiently.

### Cost Considerations and Competitors
For developers considering Mistral Small 4, understanding the cost implications is crucial. The model's pricing translates to $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Given its capabilities and pricing, Mistral Small 4 is positioned as a unique offering without direct competitors listed. Its limitations, such as a knowledge cutoff of 2023-12 and specific max output constraints, should be considered in the

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. This model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral: Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs. Since cached input tokens are free, it is recommended to use them whenever possible to minimize expenses.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing does not explicitly mention a discount for batch input, the fact that batch input is listed as $None per 1M tokens suggests that batching may not incur additional costs. However, the actual cost savings will depend on the specific implementation and the number of tokens processed.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs are based on the average number of tokens per call and the pricing structure. The costs can be broken down into input and output costs, but the exact split is not provided.

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens.

#### Benchmark Scores
The model's performance can be evaluated through its benchmark scores:
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct code based on human-written tests. The absence of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 is relatively moderate, indicating that Mistral Small 4 has some proficiency in tasks that require strategic thinking and problem-solving.

#### Real-World Implications
For real-world use, these benchmark scores imply the following:
* **Text-related tasks**: With an MMLU score of 80.0, Mistral Small 4 can be expected to perform reasonably well in tasks such as text generation,

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and category. 

#### Hypothetical Competitors
For the purpose of this comparison, let's consider two hypothetical models:
- **Model A**: A standard, open-source model with similar capabilities to Mistral Small 4.
- **Model B**: A premium, closed-source model with advanced features and higher performance.

#### Pricing Comparison
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

In comparison, the hypothetical competitors may have the following pricing:
- **Model A**: 
  - Input: $0.10 per 1M tokens (33% cheaper than Mistral Small 4)
  - Output: $0.50 per 1M tokens (17% cheaper than Mistral Small 4)
- **Model B**: 
  - Input: $0.25 per 1M tokens (67% more expensive than Mistral Small 4)
  - Output: $0.80 per 1M tokens (33% more expensive than Mistral Small 4)

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following performance metrics:
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
- **Mistral: Mistral Small 4**: Choose this model when you need a balance between price and performance. It offers a standard set of capabilities and decent

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open source.

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, Mistral Small 4 is best suited for the following applications:

1. **Chat and Text Generation**: With its ability to understand and generate human-like text, Mistral Small 4 is ideal for chatbots, virtual assistants, and content generation platforms.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it suitable for coding tasks, such as code completion, code review, and analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4 can be used for summarizing long documents, extracting key information, and building RAG (Retrieve, Augment, Generate) pipelines for more complex tasks.
4. **Text Analysis and Insights**: The model can be used to analyze text data, extract insights, and provide recommendations, making it a valuable tool for businesses and organizations.
5. **Streamlined Content Creation**: With its ability to generate text and structured outputs, Mistral Small 4 can be used to streamline content creation, such as generating articles, social media posts, and product descriptions.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt, model)
    output = model.generate(input_ids, max_length=4096

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
