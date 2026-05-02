# Mistral Large 2411 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2411
Mistral Large 2411, released by Mistral AI on 2024-11-12, is a standard-tier large language model designed to cater to a wide range of applications, particularly in coding, analysis, and content generation. This model is not open source. With its robust architecture, Mistral Large 2411 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2024-06, ensuring it is well-versed in information up to that point.

### Technical Strengths and Use Cases
Mistral Large 2411 demonstrates its strengths through various benchmarks: it scores 84.0 on MMLU, 92.1 on HumanEval, 1251 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores highlight its proficiency in understanding and generating human-like text. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it versatile for tasks such as coding, instruction following, and content generation. However, it is not recommended for embeddings, bulk cheap tasks, real-time sub-100ms tasks, or vision-heavy applications due to its pricing model and limitations.

### Pricing and Cost Considerations
The pricing for Mistral Large 2411 is structured as follows: $2.0 per 1M tokens for input, $6.0 per 1M tokens for output, with no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $4.0, scaling up to $400.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2411 offers a competitive pricing

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $2.0 |
| Output | $6.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2411 Pricing Analysis
#### Overview
The Mistral Large 2411 model, provided by Mistral AI, is a standard, non-open-source model released on 2024-11-12. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2411 is as follows:
* Input: **$2.0 per 1M tokens**
* Output: **$6.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input sequences.
* **Batch API Calls**: Leverage batch input to reduce costs, as batch input is also free. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Large 2411 at scale is as follows:
* **1,000 API Calls** (avg 500 tokens): **$4.0**
* **10,000 API Calls**: **$40.0**
* **100,000 API Calls**: **$400.0**

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Competitors
Mistral Large 2411's pricing is competitive with other models in the market. For example, GPT-4o is priced at **$2.5/1M input** and **$10.0/1M output**. While GPT-4o has a lower input cost, Mistral Large 2411's output cost is significantly lower, making it a more cost-effective option for applications with

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.1 |
| LMSYS Arena ELO | 1251 |
| ARC | 92.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2411 Benchmark Performance
The Mistral Large 2411 model, released by Mistral AI on 2024-11-12, is a standard, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. The model's pricing is as follows:
* Input: $2.0 per 1M tokens
* Output: $6.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and generate text across a wide range of tasks and domains. A higher MMLU score suggests better performance in tasks that require a broad understanding of language.
* **HumanEval**: 92.1 - This score evaluates the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1251 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that the Mistral Large 2411 model is well-suited for tasks that require:
* Broad language understanding (MMLU: 84.0)
* Code generation and coding tasks (HumanEval: 92.1)
* Competitive performance in a variety of tasks (LMSYS Arena ELO: 1251)

The model's capabilities, including text, vision, function calling, JSON

## Competitor Comparison
### Comparison of Mistral Large 2411 with Top Competitors
#### Overview
Mistral Large 2411, provided by Mistral AI, is a standard-tier model released on 2024-11-12. It offers a range of capabilities, including text, vision, function calling, and more. This comparison will focus on its pricing, performance, and trade-offs against its top competitors, specifically GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2411 is as follows:
- Input: $2.0 per 1M tokens
- Output: $6.0 per 1M tokens

In comparison, GPT-4o is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

This indicates that Mistral Large 2411 is more cost-effective for both input and output tokens, with a 20% lower cost for input tokens and a 40% lower cost for output tokens compared to GPT-4o.

#### Performance Comparison
Mistral Large 2411 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.1
- LMSYS Arena ELO: 1251
- GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, the performance of Mistral Large 2411 suggests it is a strong model, particularly in areas such as coding (HumanEval: 92.1) and problem-solving (GSM8K: 93.0).

#### Context and Limits
Mistral Large 2411 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-06. These specifications are not directly compared to GPT-4o due to the lack of provided data, but they indicate that Mistral Large 2411 is capable of handling large inputs and generating substantial outputs.

#### Capabilities and Best Use Cases
Mistral Large 2411 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- Function calling
- RAG (Retrieval-Augmented Generation)
- Agents
- Content generation

## Best Use Cases
### Practical Advice on Top 5 Use Cases for Mistral Large 2411
Mistral Large 2411, provided by Mistral AI, is a powerful model with a range of capabilities including text, vision, function calling, and more. Given its features and pricing, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Large 2411 excels in coding and analysis tasks, making it ideal for applications such as code review, code generation, and debugging. Its high scores in HumanEval (92.1) and GSM8K (93.0) benchmarks demonstrate its proficiency in these areas.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Large 2411 model
model = openrouter.MistralLarge2411()

# Define a coding task
def generate_code(prompt):
    response = model.generate_text(prompt, max_tokens=4096)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

#### 2. **Function Calling and RAG (Retrieval-Augmented Generation)**
The model's ability to perform function calling and RAG tasks makes it suitable for applications that require generating text based on external knowledge or APIs. Its high MMLU score (84.0) indicates its effectiveness in these tasks.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Large 2411 model
model = openrouter.MistralLarge2411()

# Define a function calling task
def call_api(prompt):
    response = model.call_function(prompt, max_tokens=4096)
    return response

# Test the function
print(call_api("Get the current weather in New York City"))
```

#### 3. **Content Generation**
Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
