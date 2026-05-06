# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive set of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require extensive analysis and generation of content.

### Technical Strengths and Use Cases
Claude Sonnet 4's architecture is designed to excel in various tasks, as evidenced by its benchmark scores: MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). Its primary strengths lie in coding, analysis, agents, long document analysis, RAG, computer use, research, and writing. However, it is not recommended for tasks such as embeddings, real-time sub-100ms responses, bulk cheap tasks, or image generation. The model's pricing structure includes input ($3.0 per 1M tokens), output ($15.0 per 1M tokens), cached input ($0.3 per 1M tokens), and batch input ($1.5 per 1M tokens), with examples of costs for 1,000 calls (avg 500 tokens) at $9.0, 10,000 calls at $90.0, and 100,000 calls at $900.0.

### Comparison and Cost Considerations
When comparing Claude Sonnet 4 to its top competitors, such as GPT-4o and DeepSeek R1, developers should consider the trade-offs between cost and performance. GPT-4o offers input at $2.5/1M and output at $10.0/1M

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $15.0 |
| Cached Input | $0.3 |
| Batch Input | $1.5 |
| Batch Output | $7.5 |

## Pricing Analysis
### Claude Sonnet 4 Pricing Analysis
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$15.0 per 1M tokens**
* Cached Input: **$0.3 per 1M tokens**
* Batch Input: **$1.5 per 1M tokens**

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens when possible, as they are significantly cheaper (**$0.3 per 1M tokens**) compared to regular input tokens (**$3.0 per 1M tokens**). This can lead to a **90% reduction in input costs**.
* **Batch API**: Utilize batch API calls to reduce input costs. Batch input tokens are priced at **$1.5 per 1M tokens**, resulting in a **50% reduction in input costs** compared to regular input tokens.

#### Cost at Scale
The cost of using Claude Sonnet 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$9.0**
* **10,000 calls**: **$90.0**
* **100,000 calls**: **$900.0**

To estimate the cost at scale, we can calculate the cost per call:
* Assuming an average of 500 tokens per call, the input cost per call is **$3.0 / 1,000,000 tokens \* 500 tokens = $0.0015 per call**.
* The output cost per call is **$15.0 / 1

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Performance Analysis
The Claude Sonnet 4 model, released by Anthropic on 2025-05-22, is a premium, non-open-source model with a unique set of capabilities and pricing. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Scores
The Claude Sonnet 4 model has achieved the following benchmark scores:
* **MMLU: 90.5** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 90.5 indicates that Claude Sonnet 4 has excellent language understanding capabilities, making it suitable for tasks that require complex text analysis.
* **HumanEval: 93.7** - The HumanEval benchmark assesses a model's ability to generate human-like text based on a given prompt. A score of 93.7 suggests that Claude Sonnet 4 can produce high-quality, coherent text that is similar to human-written content.
* **LMSYS Arena ELO: 1340** - The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1340 indicates that Claude Sonnet 4 is a strong competitor, capable of holding its own against other models in the arena.

#### Real-World Implications
The benchmark scores have significant implications for real-world use:
* **Language Understanding**: With a high MMLU score, Claude Sonnet 4 is well-suited for

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium language model released on 2025-05-22. This model offers a range of capabilities, including text, vision, and tool use, making it suitable for tasks such as coding, analysis, and research.

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
Claude Sonnet 4 has the following performance metrics:
* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

While the performance metrics for GPT-4o and DeepSeek R1 are not provided, the pricing difference suggests that Claude Sonnet 4 may offer better performance, but at a higher cost.

#### Context and Limits
Claude Sonnet 4 has the following context and limits:
* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

These limits may affect the suitability of Claude Sonnet 4 for certain tasks, such as long-document analysis or tasks that require a large context window.

#### When to Choose Each Model
* Choose Claude Sonnet 4 for:
	+ Tasks that require high-performance and advanced capabilities, such as coding, analysis, and research.
	+ Tasks that require a large context window or max output.
* Choose GPT-4o for:
	+

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, provided by Anthropic, is a premium model released on 2025-05-22. It offers a range of capabilities including text, vision, tool use, and more, making it suitable for tasks such as coding, analysis, and research. In this guide, we will explore the top 5 best use cases for Claude Sonnet 4, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Claude Sonnet 4
#### 1. **Coding and Software Development**
Claude Sonnet 4 excels in coding tasks, thanks to its high scores in HumanEval (93.7) and LMSYS Arena ELO (1340). You can use it for code review, code generation, and debugging.

```markdown
### Example: Code Generation with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter for code generation, you can use the following code:
```python
import openrouter

# Initialize the model
model = openrouter.ClaudeSonnet4()

# Define the prompt
prompt = "Generate a Python function to calculate the area of a rectangle."

# Generate the code
response = model.generate_code(prompt)

# Print the response
print(response)
```

#### 2. **Long Document Analysis**
With a context window of 200,000 tokens, Claude Sonnet 4 is well-suited for long document analysis. You can use it to summarize documents, extract key points, and perform sentiment analysis.

```markdown
### Example: Document Summarization with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter for document summarization, you can use the following code:
```python
import openrouter

# Initialize the model
model = openrouter.ClaudeSonnet4()

# Define the document
document = "Your long document text here."

# Summarize the document
response

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
