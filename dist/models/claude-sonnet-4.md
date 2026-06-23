# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive set of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require extensive analysis and generation of content.

### Technical Architecture and Strengths
The architecture of Claude Sonnet 4 is designed to handle complex tasks with ease, as evidenced by its high benchmark scores: MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). These scores demonstrate the model's exceptional performance in areas such as coding, analysis, and long document analysis. The model's primary strengths lie in its ability to process and generate high-quality text, making it an ideal choice for applications such as coding, research, writing, and computer use. With its extensive capabilities and impressive performance, Claude Sonnet 4 is a top-tier model for developers seeking a reliable and powerful tool for their projects.

### Pricing and Use Cases
Claude Sonnet 4 is priced at $3.0 per 1M input tokens, $15.0 per 1M output tokens, $0.3 per 1M cached input tokens, and $1.5 per 1M batch input tokens. This pricing structure makes it suitable for applications where high-quality output is essential, but may not be the most cost-effective option for bulk or low-latency tasks. The model is best used for tasks such as coding, analysis, and long document analysis, but is not recommended for embeddings, real-time sub-100ms tasks, or bulk cheap tasks.

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
The Claude Sonnet 4 model, provided by Anthropic, offers a premium tier with a specific pricing structure. This analysis will break down the cost structure, explore the use of cached tokens, batch API savings, and calculate the cost at scale.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$15.0 per 1M tokens**
* Cached Input: **$0.3 per 1M tokens**
* Batch Input: **$1.5 per 1M tokens**

#### When to Use Cached Tokens
Cached tokens are significantly cheaper than regular input tokens, with a price difference of **$2.7 per 1M tokens**. It is recommended to use cached tokens when possible, especially for repeated or similar input queries.

#### Batch API Savings
Batch input tokens are priced at **$1.5 per 1M tokens**, which is **$1.5 per 1M tokens** cheaper than regular input tokens. This pricing encourages the use of batch processing for large-scale API calls.

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): **$9.0**
* 10,000 calls: **$90.0**
* 100,000 calls: **$900.0**

To calculate the cost at scale, we can estimate the cost per call based on the average number of tokens per call. Assuming an average of 500 tokens per call, the cost per call would be:
* 1,000 calls: **$9.0 / 1,000 calls = $0.009 per call**
* 10,000 calls: **$90.0 / 10,000 calls = $0.009 per call**
* 100,000 calls: **

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Performance Analysis
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The Claude Sonnet 4 model has achieved the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 90.5
* **HumanEval**: 93.7
* **LMSYS Arena ELO**: 1340
* **GSM8K**: 98.2

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 90.5 suggests that Claude Sonnet 4 has a high level of language understanding.
* **HumanEval**: Evaluates the model's ability to generate code that passes human-written tests. A score of 93.7 indicates that Claude Sonnet 4 is proficient in coding tasks.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1340 suggests that Claude Sonnet 4 is a strong competitor.

#### Real-World Implications
The benchmark scores have significant implications for real-world use:
* **Coding and Analysis**: With high scores in HumanEval and MMLU, Claude Sonnet 4 is well-suited for coding, analysis, and research

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium language model released on 2025-05-22. This model offers a range of capabilities, including text, vision, and tool use, making it suitable for tasks such as coding, analysis, and research. In this comparison, we will examine Claude Sonnet 4's pricing, performance, and trade-offs against its top competitors, GPT-4o and DeepSeek R1.

#### Pricing Comparison
The pricing for each model is as follows:

* **Claude Sonnet 4**:
	+ Input: $3.0 per 1M tokens
	+ Output: $15.0 per 1M tokens
	+ Cached Input: $0.3 per 1M tokens
	+ Batch Input: $1.5 per 1M tokens
* **GPT-4o**:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens
* **DeepSeek R1**:
	+ Input: $0.55 per 1M tokens
	+ Output: $2.19 per 1M tokens

#### Performance Comparison
Claude Sonnet 4 demonstrates strong performance across various benchmarks:

* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

While the performance of GPT-4o and DeepSeek R1 is not provided, Claude Sonnet 4's benchmarks suggest it is a high-performing model.

#### Context and Limits
Claude Sonnet 4 has the following context and limits:

* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

#### Capabilities and Use Cases
Claude Sonnet 4 is suitable for a range of tasks, including:

* Coding
* Analysis
* Agents
* Long document analysis
* RAG
* Computer use
* Research
* Writing

However, it is not recommended for:

* Embeddings
* Real-time sub 100ms tasks
* Bulk cheap tasks
* Image generation

#### Cost Examples
The estimated costs for using Claude Sonnet 4 are:

* 1

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its robust capabilities, including text, vision, and tool use, it is best suited for tasks such as coding, analysis, and research. This guide will explore the top 5 best use cases for Claude Sonnet 4, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Claude Sonnet 4
1. **Coding and Development**: Claude Sonnet 4 excels in coding tasks, thanks to its high HumanEval score of 93.7. It can be used for code generation, code review, and debugging.
2. **Long Document Analysis**: With a context window of 200,000 tokens, Claude Sonnet 4 is ideal for analyzing long documents, such as research papers, books, and reports.
3. **Research and Writing**: The model's capabilities in text and computer use make it an excellent tool for research and writing tasks, including generating articles, summaries, and reports.
4. **Analysis and Agents**: Claude Sonnet 4's high MMLU score of 90.5 and LMSYS Arena ELO of 1340 make it suitable for complex analysis tasks and building intelligent agents.
5. **RAG (Retrieve, Augment, Generate) Tasks**: The model's ability to retrieve information, augment existing knowledge, and generate new content makes it well-suited for RAG tasks.

### Code Integration Example with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Claude Sonnet 4 model
model = openrouter.Model("anthropic/claude-sonnet-4")

# Define a function to generate code using the model
def generate_code(prompt):
    inputs = openrouter.Input

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
