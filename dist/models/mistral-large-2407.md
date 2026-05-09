# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for complex, long-form text processing and generation. Its architecture supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates significant strengths in various benchmarks, achieving scores of 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These benchmarks highlight its proficiency in coding, analysis, and reasoning tasks. The model is best utilized for applications such as coding assistance, in-depth analysis, and tasks that require the integration of multiple functions or system prompts. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To put this into perspective, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mist

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached input and batch API calls.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This structure indicates that while input and output tokens are charged, using cached input or making batch API calls does not incur additional costs for the input tokens.

#### When to Use Cached Tokens
Cached tokens should be utilized when the same input is used multiple times. Since cached input is free, reusing input tokens can significantly reduce costs, especially in applications where the same prompts or similar inputs are frequently used.

#### Batch API Savings
Batching API calls can also lead to cost savings, as the input tokens for batch calls are not charged. This makes batch processing an efficient way to handle large volumes of data or tasks, minimizing the cost per call.

#### Cost at Scale
To understand the cost implications at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost increase with the number of calls, indicating that the cost per call remains constant regardless of the volume. This linear scaling suggests that the cost model is straightforward and predictable, making it easier to budget for large-scale applications.



## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and topics.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model arena, where higher scores indicate better performance.
* **GSM8K**: 93.0, evaluating the model's math problem-solving skills.

#### Real-World Implications
These benchmark scores suggest that Mistral Large 2 is:
* Suitable for tasks that require a deep understanding of language and the ability to generate coherent text, such as coding, analysis, and multilingual applications.
* Competitive in terms of code generation and problem-solving capabilities, as evidenced by its high HumanEval and GSM8K scores.
* A strong contender in large-scale language model competitions, as indicated by its LMSYS Arena ELO score.

#### Pricing and Cost Examples
The model's pricing is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cost examples

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, and multilingual applications.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, one of its top competitors, GPT-4o, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

This indicates that while GPT-4o is cheaper in terms of input costs, Mistral Large 2 is more cost-effective for output, with a $1.0 per 1M tokens difference.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores suggest that Mistral Large 2 excels in coding and analytical tasks, as well as multilingual applications. However, its performance in embeddings, bulk cheap processing, real-time sub-100ms applications, and vision-heavy tasks is not its strong suit.

#### Context and Limits
Mistral Large 2 has the following context and limits:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications imply that Mistral Large 2 is designed for applications requiring a large context window and moderate output size, with knowledge limited to data available up to 2024-07.

#### Choosing the Right Model
Based on the comparison, choose Mistral Large 2 for:
- Coding and analysis tasks that require a large context window and moderate output size
- Multilingual applications where its high GSM8K score is beneficial
- Applications that can leverage its function calling, JSON mode, streaming, and system prompts capabilities

On the other hand, consider GPT-4o for:
- Applications where input costs are a primary concern, given

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model provided by Mistral AI, offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its release on 2024-07-24, it has established itself as a powerful tool for various applications. Here, we will explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding and Analysis**
Mistral Large 2 excels in coding and analysis tasks, making it an ideal choice for developers and data analysts. Its high scores in HumanEval (92.0) and GSM8K (93.0) benchmarks demonstrate its proficiency in coding and mathematical problem-solving.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example coding task
input_prompt = "Write a Python function to calculate the area of a rectangle."
output = model.generate_text(input_prompt)
print(output)
```

#### 2. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Large 2's capabilities in RAG tasks make it suitable for applications that require retrieving information, augmenting it, and generating new content.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example RAG task
input_prompt = "Write a short story about a character who learns a new skill."
output = model.generate_text(input_prompt)
print(output)
```

#### 3. **Multilingual Support**
With its support for multiple languages, Mistral Large 2 is an excellent choice for applications that require text processing and generation in different languages.

```python
import openrouter

# Initialize Mistral Large 2

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
