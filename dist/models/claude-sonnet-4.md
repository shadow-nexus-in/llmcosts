# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive architecture that supports a wide range of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require in-depth analysis and generation of lengthy content.

### Technical Strengths and Use Cases
Claude Sonnet 4 demonstrates exceptional performance across various benchmarks, including MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). Its strengths make it an ideal choice for applications such as coding, analysis, agents, long document analysis, RAG, computer use, research, and writing. However, it is not recommended for tasks like embeddings, real-time sub-100ms responses, bulk cheap tasks, or image generation. The model's pricing structure is as follows: $3.0 per 1M tokens for input, $15.0 per 1M tokens for output, $0.3 per 1M tokens for cached input, and $1.5 per 1M tokens for batch input.

### Cost Considerations and Competitors
To give developers a better understanding of the costs involved, consider the following examples: 1,000 calls with an average of 500 tokens would cost $9.0, while 10,000 calls would cost $90.0, and 100,000 calls would cost $900.0. In comparison to its top competitors, Claude Sonnet 4 is priced higher than GPT-4o ($2.5/1M input, $10.0

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
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost at scale for this model.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* **Input**: $3.0 per 1M tokens
* **Output**: $15.0 per 1M tokens
* **Cached Input**: $0.3 per 1M tokens
* **Batch Input**: $1.5 per 1M tokens

#### When to Use Cached Tokens
Cached input tokens are significantly cheaper than regular input tokens, at $0.3 per 1M tokens. This represents a **90% discount** compared to regular input tokens. It is recommended to use cached tokens when possible, especially for repeated or similar input sequences.

#### Batch API Savings
Batch input tokens are priced at $1.5 per 1M tokens, which is a **50% discount** compared to regular input tokens. Using the batch API can lead to substantial cost savings, especially for large-scale applications or when processing multiple inputs simultaneously.

#### Cost at Scale
The cost of using Claude Sonnet 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $9.0
* **10,000 calls**: $90.0
* **100,000 calls**: $900.0

To put this into perspective, assuming an average input size of 500 tokens, the cost per call would be:
* **1,000 calls**: $9.0 / 1,000 calls = $0.009 per call
* **10,000 calls**: $90.0 / 10,000 calls = $0.009 per call
* **100,000 calls**: $

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Performance Analysis
#### Model Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities, including text, vision, tool use, and more, making it suitable for tasks like coding, analysis, and research.

#### Pricing
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 90.5 - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 93.7 - This score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance in coding-related tasks.
* **LMSYS Arena ELO**: 1340 - This score represents the model's performance in a competitive arena, where it is pitted against other models. A higher score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Claude Sonnet 4 is a high-performance model suitable for tasks that require:
* Strong language understanding (MMLU: 90.5)
* Accurate code evaluation and execution (HumanEval:

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
Claude Sonnet 4 has a context window of 200,000 tokens and a max output of 64,000 tokens. The model has achieved the following benchmark scores:
* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

While the pricing for Claude Sonnet 4 is higher than its competitors, its performance is also superior. The choice between Claude Sonnet 4 and its competitors will depend on the specific use case and the trade-off between cost and performance.

#### When to Choose Each Model
* **Claude Sonnet 4**: Choose this model for tasks that require high performance, such as coding, analysis, and research. The model's capabilities, including text, vision, and tool use, make it well-suited for complex tasks.
* **GPT-4o**: Choose this model for tasks that require a balance between cost and performance. GPT-4o is 20-33% cheaper than Claude Sonnet 4, but its performance may not be as high

## Best Use Cases
### Practical Advice for Claude Sonnet 4
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its impressive benchmarks (MMLU: 90.5, HumanEval: 93.7, LMSYS Arena ELO: 1340, GSM8K: 98.2) and capabilities (text, vision, tool_use, json_mode, streaming, batch_processing, system_prompts, extended_thinking, computer_use), it is best suited for tasks such as coding, analysis, agents, long_document_analysis, rag, computer_use, research, and writing.

#### Top 5 Best Use Cases for Claude Sonnet 4
1. **Coding and Code Analysis**: Claude Sonnet 4 excels in coding tasks, making it an ideal choice for code review, code generation, and code analysis. Its high HumanEval score (93.7) demonstrates its proficiency in coding tasks.
2. **Long Document Analysis**: With a context window of 200,000 tokens, Claude Sonnet 4 can analyze long documents, making it suitable for tasks such as document summarization, text analysis, and research paper analysis.
3. **Research and Writing**: Claude Sonnet 4's capabilities in text, vision, and computer_use make it an excellent choice for research and writing tasks, such as generating research papers, articles, and blog posts.
4. **Agent Development**: Claude Sonnet 4's support for agents, system_prompts, and extended_thinking makes it a great choice for developing intelligent agents that can interact with users and perform complex tasks.
5. **Computer Use and Automation**: Claude Sonnet 4's capabilities in computer_use and tool_use enable it to automate tasks, interact with computers, and perform complex computations, making it an excellent choice for tasks such as data processing and automation.

#### Code Integration Example with OpenRouter
To

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
