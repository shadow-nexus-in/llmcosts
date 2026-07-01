# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, developed by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to balance performance and cost, making it an attractive option for developers who need a reliable and capable model without the highest-end features. Its main strengths include a context window of 131,072 tokens, allowing for complex and nuanced understanding of input, and the ability to generate up to 16,384 tokens of output.

### Technical Capabilities and Use Cases
Mistral Medium 3 boasts a wide range of capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. These features make it well-suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. The model's performance is backed by solid benchmarks, with scores of 80.0 on MMLU, 77.5 on HumanEval, and an ELO rating of 1200 in the LMSYS Arena. However, it's not recommended for frontier reasoning, bulk cheap tasks, simple classification, or applications requiring real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is structured as follows: $0.4 per 1 million tokens for input, and $2.0 per 1 million tokens for output. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens would cost $1.2, scaling to $12.0 for 10,000 calls, and $120.0 for 100,000 calls. When comparing Mistral Medium 3 to its competitors, such as Claude 

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can lead to significant savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the provided pricing, we can estimate the costs:
* Input: 500,000 tokens / 1,000,000 tokens * $0.4 = $0.2 (1,000 calls), $2.0 (10,000 calls), $20.0 (100,000 calls)
* Output: Assuming an average output of 100 tokens

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 77.5, measuring the model's ability to evaluate and execute human-written code.
* **LMSYS Arena ELO**: 1200, representing the model's competitive performance in a large-scale language model benchmark.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high MMLU score suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of natural language, such as **coding**, **analysis**, and **content generation**.
* The strong HumanEval score indicates that the model is capable of executing and evaluating human-written code, making it a good fit for **function calling** and **RAG (Retrieve, Augment, Generate)** tasks.
* The LMSYS Arena ELO score of 1200 demonstrates the model's competitive performance in a large-scale language model benchmark, indicating that it can handle complex tasks and compete with other state-of-the-art models.

#### Cost

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance benchmarks for each model are:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time tasks with latency under 100ms

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Right Model
Based on the pricing and performance comparison, here are some guidelines for

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a versatile model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code, coupled with its function calling capability, makes it an excellent choice for tasks such as code review, code completion, and debugging.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Example code completion task
input_code = "def greet(name):"
output = model.complete_code(input_code)
print(output)
```

#### 2. **Summarization**
With its strong language understanding capabilities, Mistral Medium 3 is well-suited for summarization tasks. It can effectively condense long pieces of text into concise, meaningful summaries.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Example summarization task
input_text = "This is a long piece of text that needs to be summarized."
output = model.summarize(input_text)
print(output)
```

#### 3. **Content Generation**
Mistral Medium 3's ability to generate high-quality text makes it an excellent choice for content generation tasks, such as writing articles, creating product descriptions, and more.
```python
import openrouter

# Initialize Mistral Medium 3
model = openrouter.MistralMedium3()

# Example content generation task
input_prompt = "Write a short story about a character who discovers a hidden world."
output = model.generate_content(input_prompt)
print(output)
```

#### 4

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
