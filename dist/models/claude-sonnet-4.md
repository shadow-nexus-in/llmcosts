# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive array of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require in-depth analysis and generation of lengthy content.

### Technical Architecture and Strengths
The architecture of Claude Sonnet 4 supports a wide range of applications, from coding and analysis to agents and long document analysis. Its strengths are reflected in its benchmark scores: MMLU at 90.5, HumanEval at 93.7, LMSYS Arena ELO at 1340, and GSM8K at 98.2. These scores indicate a high level of performance across various tasks, making Claude Sonnet 4 a top choice for developers seeking a reliable and powerful model. However, it's essential to note that this model is not ideal for tasks such as embeddings, real-time sub-100ms responses, bulk cheap tasks, or image generation.

### Pricing and Use Cases
The pricing for Claude Sonnet 4 is as follows: $3.0 per 1M tokens for input, $15.0 per 1M tokens for output, $0.3 per 1M tokens for cached input, and $1.5 per 1M tokens for batch input. For example, 1,000 calls with an average of 500 tokens would cost $9.0, while 10,000 calls would cost $90.0, and 100,000 calls would cost $900.0. Compared to its top competitors, such as GPT-4o and DeepSeek R1, Claude Son

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
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $15.0 per 1M tokens
- **Cached Input**: $0.3 per 1M tokens
- **Batch Input**: $1.5 per 1M tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Use cached input tokens when possible, as they offer a significant discount of $0.3 per 1M tokens, which is 10% of the regular input price and 20% of the batch input price.
- **Batch API Savings**: Utilize batch processing for input tokens to save 50% compared to regular input pricing.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls** (avg 500 tokens): $9.0
- **10,000 calls**: $90.0
- **100,000 calls**: $900.0

To estimate the cost at scale, we can calculate the cost per 1M tokens for each scenario:
- Assuming an average of 500 tokens per call, 1,000 calls would be approximately 0.5M tokens.
- For 10,000 calls, this would be approximately 5M tokens.
- For 100,000 calls, this would be approximately 50M tokens.

However, the provided cost examples do not directly correlate with the input/output pricing structure. To better understand the cost at scale, let's consider the input/output pricing:
- **1M input tokens**: $3.0


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Analysis
The Claude Sonnet 4 model, released by Anthropic on 2025-05-22, is a premium, non-open-source model with a unique set of capabilities and pricing. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Scores
The Claude Sonnet 4 model has achieved the following benchmark scores:
* **MMLU: 90.5** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 90.5 indicates that Claude Sonnet 4 has a high level of language understanding, making it suitable for tasks that require complex text analysis.
* **HumanEval: 93.7** - The HumanEval benchmark assesses a model's ability to generate human-like text. A score of 93.7 suggests that Claude Sonnet 4 can produce high-quality, coherent text that is similar to human-generated content.
* **LMSYS Arena ELO: 1340** - The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1340 indicates that Claude Sonnet 4 is a strong competitor, capable of outperforming many other models in various tasks.

#### Real-World Implications
The benchmark scores have significant implications for real-world use:
* **Coding and Analysis**: Claude Sonnet 4's high MMLU and HumanEval scores make it an excellent choice for coding

## Competitor Comparison
### Comparison of Claude Sonnet 4 with Top Competitors
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities including text, vision, tool use, and more, making it suitable for tasks like coding, analysis, and research. This comparison will delve into the pricing, performance, and use cases of Claude Sonnet 4 against its top competitors, GPT-4o and DeepSeek R1.

#### Pricing Comparison
The pricing models of these competitors are as follows:

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

#### Performance Trade-offs
Claude Sonnet 4 boasts impressive benchmarks:
- MMLU: 90.5
- HumanEval: 93.7
- LMSYS Arena ELO: 1340
- GSM8K: 98.2

While specific benchmark scores for GPT-4o and DeepSeek R1 are not provided, the general trend in the industry suggests that higher-priced models often correlate with better performance. However, the choice between these models should also consider the specific needs of the project, such as the required context window, max output, and knowledge cutoff.

#### Context and Limits
- **Claude Sonnet 4**: 
  + Context Window: 200,000 tokens
  + Max Output: 64,000 tokens
  + Knowledge Cutoff: 2025-03
- **GPT-4o** and **DeepSeek R1**'s context and limits are not specified, but these factors are crucial in determining the suitability of a model for particular tasks.

#### Capabilities and Best Use Cases
Claude Sonnet 4 is best for:
- Coding
-

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its impressive benchmarks, including an MMLU score of 90.5 and a HumanEval score of 93.7, it's well-suited for tasks that require advanced understanding and generation capabilities.

### Top 5 Best Use Cases for Claude Sonnet 4
Given its capabilities and limitations, here are the top 5 best use cases for Claude Sonnet 4, along with code integration examples using OpenRouter:

1. **Coding and Analysis**:
   Claude Sonnet 4 excels in coding tasks, with a high HumanEval score. It can be used for code review, code generation, and analysis.
   ```python
   import openrouter

   # Initialize Claude Sonnet 4 model
   model = openrouter.ClaudeSonnet4()

   # Generate code based on a prompt
   prompt = "Create a Python function to sort a list of integers."
   response = model.generate(prompt)
   print(response)
   ```

2. **Long Document Analysis**:
   With a context window of 200,000 tokens, Claude Sonnet 4 is ideal for analyzing long documents, such as research papers or books.
   ```python
   import openrouter

   # Initialize Claude Sonnet 4 model
   model = openrouter.ClaudeSonnet4()

   # Analyze a long document
   document = "Your long document text here."
   summary = model.summarize(document)
   print(summary)
   ```

3. **Research and Writing**:
   Claude Sonnet 4's capabilities in text generation and understanding make it a great tool for research and writing tasks, such as generating research papers or articles.
   ```python
   import openrouter

   # Initialize Claude Sonnet 4 model
  

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
