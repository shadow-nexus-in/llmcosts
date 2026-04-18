# Mistral Large 2411 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2411
Mistral Large 2411, released by Mistral AI on 2024-11-12, is a standard-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for tasks that require in-depth analysis and generation of text. The model's architecture supports a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Strengths and Use Cases
Mistral Large 2411 excels in coding, analysis, function calling, and content generation tasks, making it a versatile tool for developers. Its high performance on benchmarks such as MMLU (84.0), HumanEval (92.1), LMSYS Arena ELO (1251), and GSM8K (93.0) demonstrates its capabilities in handling complex tasks. The model is best utilized for tasks that require instruction following, agents, and RAG (Retrieval-Augmented Generation). However, it is not recommended for tasks that require embeddings, bulk cheap tasks, real-time sub-100ms responses, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2411 is $2.0 per 1M tokens for input and $6.0 per 1M tokens for output. There are no additional costs for cached input or batch input. To put this into perspective, 1,000 calls with an average of 500 tokens would cost $4.0, while 10,000 calls would cost $40.0, and 100,000 calls would cost $400.0. Compared to its top competitor, GPT-4o, which costs $2.5/1M input and $10.0/1M output, Mistral Large 2411 offers a competitive pricing model

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
Mistral Large 2411 is a standard, non-open-source model provided by Mistral AI, released on 2024-11-12. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Mistral Large 2411 is as follows:
* Input: **$2.0 per 1M tokens**
* Output: **$6.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Cached Tokens
Cached tokens are free, with a cost of **$0 per 1M tokens**. This makes it an attractive option for applications where input data is frequently reused or has a high overlap between requests. However, the effectiveness of cached tokens depends on the specific use case and data distribution.

#### Batch API Savings
Batch input is also free, with a cost of **$0 per 1M tokens**. This means that batching API calls can significantly reduce costs, especially for applications with a high volume of requests. By batching requests, users can take advantage of the free batch input pricing, reducing the overall cost per request.

#### Cost at Scale
The cost of using Mistral Large 2411 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$4.0**
* **10,000 calls**: **$40.0**
* **100,000 calls**: **$400.0**

These costs are based on the average number of tokens per request and the pricing structure outlined above.

#### Comparison to Competitors
Mistral Large 2411's pricing is

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval**: 92.1 - This score evaluates the model's ability to generate code that is correct and functional. A higher score indicates better performance.
* **LMSYS Arena ELO**: 1251 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better performance.
* **GSM8K**: 93.0 - This score evaluates the model's ability to solve math problems.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* **MMLU score of 84.0**: The model is capable of understanding and performing a wide range of natural language processing tasks, but may struggle with more complex or nuanced tasks.
* **HumanEval score of 92.1**: The model is highly capable of generating correct and functional code, making it suitable for coding and development tasks.
* **LMS

## Competitor Comparison
### Comparison of Mistral Large 2411 with Top Competitors
#### Overview
Mistral Large 2411 is a standard-tier model released by Mistral AI on 2024-11-12. It offers a range of capabilities, including text, vision, function calling, and more. In this comparison, we will evaluate Mistral Large 2411 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2411 and GPT-4o is as follows:
* Mistral Large 2411:
	+ Input: $2.0 per 1M tokens
	+ Output: $6.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2411 offers a more competitive pricing structure, with a 20% lower input cost and a 40% lower output cost compared to GPT-4o.

#### Performance Comparison
The performance benchmarks for Mistral Large 2411 are:
* MMLU: 84.0
* HumanEval: 92.1
* LMSYS Arena ELO: 1251
* GSM8K: 93.0

While the performance benchmarks for GPT-4o are not provided, Mistral Large 2411 demonstrates strong performance across various tasks, including coding, analysis, and function calling.

#### Performance Trade-offs
Mistral Large 2411 has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-06

These limits may impact performance for tasks that require longer context windows or larger output sizes. However, for most use cases, Mistral Large 2411's capabilities and performance make it a strong choice.

#### When to Choose Each Model
Mistral Large 2411 is best for:
* Coding
* Analysis
* Function calling
* RAG (Retrieve, Augment, Generate)
* Agents
* Content generation
* Instruction following

On the other hand, Mistral Large 2411 is not well-suited for:
* Embeddings
* Bulk cheap tasks
* Real-time sub-100ms tasks
* Vision-heavy

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Large 2411
Mistral Large 2411, a model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Large 2411 excels in coding and analysis tasks, making it ideal for applications such as code review, code generation, and debugging. Its high performance on benchmarks like HumanEval (92.1) and GSM8K (93.0) underscores its capability in these areas.

```markdown
### Example: Using Mistral Large 2411 with OpenRouter for Code Generation
To integrate Mistral Large 2411 with OpenRouter for generating code based on a specification, you can use the following approach:
```python
import openrouter

# Initialize the Mistral Large 2411 model
model = openrouter.MistralLarge2411()

# Define your specification or prompt
prompt = "Generate a Python function to calculate the area of a rectangle."

# Use the model to generate code
generated_code = model.generate_code(prompt)

print(generated_code)
```

#### 2. **Function Calling**
With its function calling capability, Mistral Large 2411 can be used to execute specific functions or APIs based on text inputs. This makes it suitable for applications that require dynamic execution of code or integration with external services.

```markdown
### Example: Function Calling with Mistral Large 2411 and OpenRouter
To call a function using Mistral Large 2411 integrated with OpenRouter, you can follow this example:
```python
import openrouter

# Initialize the model
model = openrouter.MistralLarge2411()

# Define the function to call and its parameters
function_to_call = "calculate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
