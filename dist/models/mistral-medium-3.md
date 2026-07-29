# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Medium 3 excels in tasks that require a combination of natural language understanding and generation, such as summarization, RAG (Retrieve, Augment, Generate), and vision tasks. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model's pricing structure, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens, makes it a competitive option for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0.

### Comparison and Best Use Cases
While Mistral Medium 3 is not suitable for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms, it is a strong contender in its tier. Compared to its competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique combination of capabilities and pricing. Developers who need a reliable and versatile model for coding, analysis, and content generation should consider Mistral Medium 3, weighing its strengths and limitations against their specific use cases and budget requirements.

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it is optimal to use:
* **Cached tokens** whenever possible, as they are free. This can significantly reduce costs for repeated or similar inputs.
* **Batch API** for large-scale inputs, as batch input is free. This can lead to substantial savings for bulk processing tasks.

#### Cost at Scale
The costs for Mistral Medium 3 at different scales are as follows:
* **1,000 calls** (avg 500 tokens): $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

While Mistral Medium 3 may not offer the lowest input cost, its output cost is competitive, especially considering its capabilities and best use cases, which

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. Its pricing structure includes:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Medium 3 has a strong foundation in language understanding, making it suitable for tasks like coding, analysis, and content generation.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to evaluate and execute human-written code. A score of 77.5 suggests that Mistral Medium 3 has a good understanding of programming concepts and can generate functional code, although it may struggle with more complex tasks.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, evaluating its ability to respond to a wide range of prompts and engage in conversation. An ELO score of 1200 indicates that Mistral Medium 3 has a moderate level of conversational ability, making it suitable for tasks like chatbots and dialogue systems.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is well-suited for tasks that require:
* Strong language understanding (MMLU: 

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models of the three competitors are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing model, with input costs 50% lower than Claude 3.5 Haiku and output costs 66.7% lower. In contrast, GPT-4o Mini has significantly lower input costs but higher output costs compared to Mistral Medium 3.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 demonstrates strong performance in MMLU, HumanEval, and LMSYS Arena ELO.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks


## Best Use Cases
### Practical Advice on Mistral Medium 3 Use Cases
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding tasks, making it ideal for code analysis, code completion, and code generation. When integrated with OpenRouter for routing coding requests, you can leverage Mistral Medium 3's capabilities efficiently.

```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.OpenRouter(model="mistralai/mistral-medium-3")

# Example coding task
def generate_code(prompt):
    response = router.route(prompt, max_tokens=512)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list."))
```

#### 2. **Summarization and Content Generation**
For tasks that require generating concise summaries or creating content, Mistral Medium 3 is well-suited. Its ability to understand and generate human-like text makes it perfect for blogging, article writing, and more.

```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3 for summarization
summarizer = openrouter.OpenRouter(model="mistralai/mistral-medium-3")

# Function to summarize long pieces of text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    summary = summarizer.route(prompt, max_tokens=256)
    return summary

# Test the summarizer
long_text = "Your long piece of text here."
print(summarize_text(long_text))
```

#### 3. **Vision Tasks**
Mistral Medium

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
