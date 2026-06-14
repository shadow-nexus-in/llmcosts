# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium large language model (LLM) released on 2025-05-22. This model is not open source, indicating that its internal architecture and training data are proprietary. The architecture of Claude Sonnet 4 is designed to handle a wide range of tasks, including text and vision processing, tool use, and computer interactions. Its capabilities include text, vision, tool_use, json_mode, streaming, batch_processing, system_prompts, extended_thinking, and computer_use.

### Technical Specifications and Use Cases
Claude Sonnet 4 has a context window of 200,000 tokens and can generate up to 64,000 tokens as output. Its knowledge cutoff is 2025-03, meaning it has been trained on data up to that point. The model excels in tasks such as coding, analysis, agents, long_document_analysis, rag, computer_use, research, and writing, as evidenced by its high benchmark scores: MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). However, it is not suitable for embeddings, real-time tasks requiring sub-100ms responses, bulk cheap tasks, or image generation. The pricing model for Claude Sonnet 4 includes input costs of $3.0 per 1M tokens, output costs of $15.0 per 1M tokens, with discounts for cached input ($0.3 per 1M tokens) and batch input ($1.5 per 1M tokens).

### Cost Considerations and Competitors
To understand the cost implications of using Claude Sonnet 4, consider the following examples: 1,000 calls averaging 500 tokens cost $9.0, scaling to $90.0 for 10,000 calls and $900.0 for 100

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $15.0 |
| Cached Input | $0.3 |
| Batch Input | $1.5 |
| Batch Output | $7.5 |

## Pricing Analysis
### Pricing Analysis for Claude Sonnet 4
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$15.0 per 1M tokens**
* Cached Input: **$0.3 per 1M tokens** (10% of regular input cost)
* Batch Input: **$1.5 per 1M tokens** (50% of regular input cost)

#### Optimal Usage Scenarios
* **Cached Tokens**: Use cached input tokens when possible, as they offer a significant reduction in cost (90% savings compared to regular input tokens). This is ideal for scenarios where the input data is repetitive or can be reused.
* **Batch API Savings**: Utilize batch input for large-scale API calls, as it provides a 50% discount on input costs. This is suitable for applications that require processing large volumes of data in batches.

#### Cost at Scale
The cost of using Claude Sonnet 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$9.0**
* **10,000 calls**: **$90.0**
* **100,000 calls**: **$900.0**

These costs are based on the average token count per call and do not take into account the potential savings from using cached input or batch processing.

#### Comparison to Competitors
Claude Sonnet 4's pricing is competitive with other premium models:
* **GPT-4o**: $2.5/1M input, $10.0/1M output (20-33% cheaper than Claude Sonnet 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Analysis
#### Overview
The Claude Sonnet 4 model, developed by Anthropic, is a premium, non-open-source language model released on 2025-05-22. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world applications.

#### Benchmark Scores
The Claude Sonnet 4 model has achieved the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 90.5
* **HumanEval**: 93.7
* **LMSYS Arena ELO**: 1340
* **GSM8K**: 98.2

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks and domains. A score of 90.5 suggests that Claude Sonnet 4 has a high level of language understanding.
* **HumanEval**: Evaluates the model's ability to write code that passes a set of unit tests. A score of 93.7 indicates that the model is highly proficient in coding tasks.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1340 suggests that Claude Sonnet 4 is a strong competitor in the language model arena.

#### Real-World Implications
The benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With a high HumanEval score, Claude Sonnet 4 is well-suited for coding tasks

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, provided by Anthropic, is a premium language model released on 2025-05-22. This model offers a range of capabilities, including text, vision, and tool use, making it suitable for tasks such as coding, analysis, and research.

#### Pricing Comparison
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

In comparison, the top competitors have the following pricing:
* GPT-4o:
	+ Input: $2.5 per 1M tokens (20% cheaper than Claude Sonnet 4)
	+ Output: $10.0 per 1M tokens (33% cheaper than Claude Sonnet 4)
* DeepSeek R1:
	+ Input: $0.55 per 1M tokens (81.7% cheaper than Claude Sonnet 4)
	+ Output: $2.19 per 1M tokens (85.4% cheaper than Claude Sonnet 4)

#### Performance Trade-offs
Claude Sonnet 4 has the following benchmarks:
* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

While the exact benchmarks for GPT-4o and DeepSeek R1 are not provided, Claude Sonnet 4's high scores suggest it may offer better performance in certain tasks. However, this comes at a higher cost.

#### Context and Limits
Claude Sonnet 4 has the following context and limits:
* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

These limits may affect the model's performance in certain tasks, such as long-document analysis or research.

#### When to Choose Each Model
* **Claude Sonnet 4**: Choose for tasks that require high-performance, premium capabilities, and are willing to pay a higher cost. Suitable for coding, analysis, agents, long-document analysis, and research.
* **GPT-4o**: Choose for tasks that require a

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its impressive capabilities and high benchmark scores, it's an ideal choice for various applications. Here, we'll explore the top 5 best use cases for Claude Sonnet 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Claude Sonnet 4
#### 1. **Coding and Analysis**
Claude Sonnet 4 excels in coding and analysis tasks, with a high HumanEval score of 93.7. You can leverage its capabilities for code review, debugging, and optimization.

```python
import openrouter

# Initialize Claude Sonnet 4 model
model = openrouter.ClaudeSonnet4()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Get the response
response = model.generate(task)

# Print the response
print(response)
```

#### 2. **Long Document Analysis**
With a context window of 200,000 tokens, Claude Sonnet 4 is well-suited for long document analysis. You can use it to summarize, extract insights, or perform sentiment analysis on large documents.

```python
import openrouter

# Initialize Claude Sonnet 4 model
model = openrouter.ClaudeSonnet4()

# Define a document analysis task
task = "Analyze the sentiment of a 10-page document and provide a summary."

# Load the document
document = open("document.txt", "r").read()

# Get the response
response = model.generate(task, document)

# Print the response
print(response)
```

#### 3. **Research and Writing**
Claude Sonnet 4's high LMSYS Arena ELO score of 1340 makes it an excellent choice for research and writing tasks. You can

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
