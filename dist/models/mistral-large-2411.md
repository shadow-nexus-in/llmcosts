# Mistral Large 2411 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2411
Mistral Large 2411, provided by Mistral AI, is a standard-tier model released on 2024-11-12. This model is not open source. From an architectural standpoint, Mistral Large 2411 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2024-06, indicating that its training data includes information up to June 2024. With capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, this model is highly versatile.

### Strengths and Use Cases
The main strengths of Mistral Large 2411 are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.1, LMSYS Arena ELO at 1251, and GSM8K at 93.0. These scores suggest that the model excels in coding, analysis, and function calling tasks, among others. It is best utilized for applications such as coding, analysis, function calling, RAG (Retrieval-Augmented Generation), agents, content generation, and instruction following. However, it is not recommended for tasks requiring embeddings, bulk cheap tasks, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2411 is as follows: $2.0 per 1M input tokens and $6.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens cost $4.0, 10,000 calls cost $40.0, and 100,000 calls cost $400.0. In comparison to its top competitor, GPT-4o, which charges $2.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $2.0 |
| Output | $6.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2411
#### Overview
Mistral Large 2411 is a standard, non-open-source model provided by Mistral AI, released on 2024-11-12. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2411 is as follows:
* Input: **$2.0 per 1M tokens**
* Output: **$6.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can significantly reduce overall costs.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$4.0**
* **10,000 calls**: **$40.0**
* **100,000 calls**: **$400.0**

To estimate costs at scale, we can extrapolate from these examples. Assuming an average of 500 tokens per call, we can calculate the cost per 1M tokens:
* **1,000 calls**: 500 tokens/call \* 1,000 calls = 500,000 tokens, costing **$4.0** (or **$8.0 per 1M tokens**)
* **10,000 calls**: 500 tokens/call \* 10,000 calls = 5,000,000 tokens, costing **$40.0** (or **$8.0 per 1M tokens**)
* **100,000 calls**:

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.1 |
| LMSYS Arena ELO | 1251 |
| ARC | 92.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2411 Benchmark Performance
#### Overview
Mistral Large 2411, a model provided by Mistral AI, demonstrates strong performance across various benchmarks. This analysis will delve into the MMLU, HumanEval, and Arena ELO scores, explaining their implications for real-world use cases.

#### Benchmark Scores
The model achieves the following benchmark scores:
* **MMLU: 84.0** - The MMLU (Measuring Massive Multitask Language Understanding) score evaluates a model's ability to understand and generate text across a wide range of tasks. A higher score indicates better performance. With a score of 84.0, Mistral Large 2411 demonstrates strong language understanding capabilities.
* **HumanEval: 92.1** - The HumanEval score assesses a model's ability to generate code that passes human evaluation. A higher score indicates better performance. With a score of 92.1, Mistral Large 2411 shows excellent code generation capabilities.
* **LMSYS Arena ELO: 1251** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other. A higher score indicates better performance. With a score of 1251, Mistral Large 2411 demonstrates strong competitive performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With high HumanEval and MMLU scores, Mistral Large 2411 is well-suited for coding and analysis tasks, such as code generation, code review, and data analysis.
* **Function Calling and RAG**: The model's strong performance

## Competitor Comparison
### Comparison of Mistral Large 2411 with Top Competitors
#### Overview
Mistral Large 2411 is a standard-tier model offered by Mistral AI, released on 2024-11-12. It is not open-source and has a specific set of capabilities and limitations. In this comparison, we will evaluate Mistral Large 2411 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2411 and GPT-4o is as follows:
* Mistral Large 2411:
	+ Input: $2.0 per 1M tokens
	+ Output: $6.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2411 is cheaper than GPT-4o for both input and output tokens. For example, for 1,000 calls with an average of 500 tokens, the cost would be:
* Mistral Large 2411: $4.0
* GPT-4o: $5.0 (input) + $10.0 (output) = $15.0 per 1M tokens, which would be approximately $7.5 for 1,000 calls with 500 tokens.

#### Performance Comparison
The performance of Mistral Large 2411 is measured by the following benchmarks:
* MMLU: 84.0
* HumanEval: 92.1
* LMSYS Arena ELO: 1251
* GSM8K: 93.0

In contrast, the performance of GPT-4o is not provided in the data. However, based on the pricing, it can be inferred that GPT-4o may offer better performance, but at a higher cost.

#### Capabilities and Limitations
Mistral Large 2411 has the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* Function calling
* RAG
* Agents
* Content generation
* Instruction following

However, it is not suitable for tasks that require:
* Embeddings
* Bulk cheap tasks
*

## Best Use Cases
### Practical Advice on the Top 5 Best Use Cases for Mistral Large 2411
Mistral Large 2411, a model provided by Mistral AI, is a powerful tool with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing structure, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Large 2411 excels in coding and analysis tasks, making it an ideal choice for applications that require generating or understanding code. For example, you can use it to create a code completion tool:
```python
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-large-2411")

# Define a function to generate code
def generate_code(prompt):
    response = model.generate(prompt, max_tokens=4096)
    return response

# Test the function
prompt = "Write a Python function to sort a list of integers"
print(generate_code(prompt))
```
**Cost Estimate:** Assuming an average of 500 tokens per call, 1,000 calls would cost $4.0.

#### 2. **Function Calling and RAG (Retrieval-Augmented Generation)**
Mistral Large 2411 supports function calling and RAG, making it suitable for tasks that require retrieving and generating text based on external knowledge. For example:
```python
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-large-2411")

# Define a function to retrieve and generate text
def retrieve_and_generate(prompt):
    response = model.generate(prompt, max_tokens=4096, function_calls=True)
    return response

# Test the function
prompt = "Write a short story about a character who learns a new skill"
print(retrieve_and_generate(prompt))
```
**

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
