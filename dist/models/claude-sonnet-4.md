# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive architecture, with a context window of 200,000 tokens and a maximum output of 64,000 tokens. Its knowledge cutoff is 2025-03, ensuring it has a robust understanding of information up to that point. Claude Sonnet 4 is designed to excel in various tasks, including text and vision processing, tool usage, and batch processing, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The model's technical strengths are reflected in its benchmark scores: MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). These scores indicate that Claude Sonnet 4 is particularly well-suited for tasks such as coding, analysis, and long document analysis. Its capabilities extend to system prompts, extended thinking, and computer use, making it an ideal choice for research and writing applications. However, it is not recommended for tasks that require embeddings, real-time responses under 100ms, bulk cheap tasks, or image generation. The pricing structure for Claude Sonnet 4 includes $3.0 per 1M input tokens, $15.0 per 1M output tokens, $0.3 per 1M cached input tokens, and $1.5 per 1M batch input tokens.

### Cost Considerations and Competitors
To give developers a better understanding of the costs involved, example pricing for Claude Sonnet 4 includes $9.0 for 1,000 calls (avg 500 tokens), $90.0 for 10,000 calls, and $900.0 for 100,000 calls. In comparison to its top competitors, Claude Sonnet 4 is priced higher than GPT

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
- **Cached Tokens**: Use cached input tokens when possible, as they offer a significant discount ($0.3 per 1M tokens) compared to regular input tokens ($3.0 per 1M tokens). This is ideal for scenarios where the input data does not change frequently.
- **Batch API Savings**: Utilize batch input for bulk operations to save on costs. Batch input is priced at $1.5 per 1M tokens, which is 50% of the regular input price.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $9.0
- **10,000 calls**: $90.0
- **100,000 calls**: $900.0

To calculate the cost per call, we can use the provided cost examples:
- **1,000 calls**: $9.0 / 1,000 calls = $0.009 per call
- **10,000 calls**: $90.0 / 10,000 calls = $0.009 per call
- **100,000 calls**: $900.0 / 100,000 calls = $0.009 per call

Assuming an average of 500 tokens

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
The Claude Sonnet 4 model, released by Anthropic on 2025-05-22, is a premium, non-open-source model with a context window of 200,000 tokens and a maximum output of 64,000 tokens. Its pricing is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$15.0 per 1M tokens**
* Cached Input: **$0.3 per 1M tokens**
* Batch Input: **$1.5 per 1M tokens**

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU: 90.5** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate human-like language across a wide range of tasks. A higher score indicates better language understanding capabilities.
* **HumanEval: 93.7** - The HumanEval benchmark assesses a model's ability to generate code that is both correct and readable. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO: 1340** - The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment, with higher scores indicating better performance.
* **GSM8K: 98.2** - The GSM8K benchmark evaluates a model's ability to reason and solve math problems.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **MMLU score (90.5)** indicates that Claude Sonnet 4 is well

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium language model released on 2025-05-22. This model is not open-source and offers a range of capabilities, including text, vision, and tool use. In this comparison, we will evaluate Claude Sonnet 4 against its top competitors, GPT-4o and DeepSeek R1, in terms of pricing, performance, and use cases.

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
The performance of each model can be evaluated using various benchmarks:
* **Claude Sonnet 4**:
	+ MMLU: 90.5
	+ HumanEval: 93.7
	+ LMSYS Arena ELO: 1340
	+ GSM8K: 98.2
* **GPT-4o** and **DeepSeek R1** benchmark scores are not provided.

#### Context and Limits
The context window and limits for Claude Sonnet 4 are:
* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

#### Capabilities and Use Cases
Claude Sonnet 4 is best suited for:
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
* 1,000 calls (avg 500 tokens): $9

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its robust capabilities in text, vision, and tool use, it is best suited for tasks such as coding, analysis, and long document analysis.

### Top 5 Best Use Cases for Claude Sonnet 4
1. **Coding and Software Development**: Claude Sonnet 4 excels in coding tasks, thanks to its high scores in HumanEval (93.7) and GSM8K (98.2). It can be integrated with OpenRouter for automated code review and generation.
   ```python
   import openrouter
   from transformers import AutoModelForCausalLM, AutoTokenizer

   # Initialize Claude Sonnet 4 model and tokenizer
   model = AutoModelForCausalLM.from_pretrained("anthropic/claude-sonnet-4")
   tokenizer = AutoTokenizer.from_pretrained("anthropic/claude-sonnet-4")

   # Define a function to generate code using Claude Sonnet 4 and OpenRouter
   def generate_code(prompt):
       inputs = tokenizer(prompt, return_tensors="pt")
       outputs = model.generate(**inputs)
       return tokenizer.decode(outputs[0], skip_special_tokens=True)

   # Example usage
   prompt = "Write a Python function to sort a list of integers."
   print(generate_code(prompt))
   ```

2. **Long Document Analysis**: With a context window of 200,000 tokens, Claude Sonnet 4 is ideal for analyzing long documents. It can be used for tasks such as text summarization and document classification.
   ```python
   import openrouter
   from transformers import AutoModelForSequenceClassification, AutoTokenizer

   # Initialize Claude Sonnet 4 model and tokenizer
   model = AutoModelForSequenceClassification.from_pretrained("anthropic/claude-

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
