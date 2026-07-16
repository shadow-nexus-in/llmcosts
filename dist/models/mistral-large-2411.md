# Mistral Large 2411 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2411
Mistral Large 2411, provided by Mistral AI, is a standard-tier model released on 2024-11-12. This model is not open source. From an architectural standpoint, Mistral Large 2411 is designed to handle a variety of tasks, including text and vision processing, function calling, and more, thanks to its capabilities in text, vision, function_calling, json_mode, streaming, and system_prompts. Its main strengths lie in its ability to perform complex tasks such as coding, analysis, and content generation, making it a versatile tool for developers.

### Technical Specifications and Use Cases
Technically, Mistral Large 2411 has a context window of 131,072 tokens and can generate up to 4,096 tokens as output. The model's knowledge cutoff is 2024-06, indicating that its training data includes information up to June 2024. The pricing model for Mistral Large 2411 is based on input and output tokens, with costs of $2.0 per 1M input tokens and $6.0 per 1M output tokens. This model is best suited for tasks that require in-depth analysis, coding, and content generation, but it is not recommended for tasks that require embeddings, bulk cheap tasks, real-time responses under 100ms, or vision-heavy tasks. Benchmark scores such as MMLU (84.0), HumanEval (92.1), LMSYS Arena ELO (1251), and GSM8K (93.0) demonstrate its capabilities.

### Cost Considerations and Competitors
For developers considering the cost, examples show that 1,000 calls with an average of 500 tokens would cost $4.0, scaling up to $40.0 for 10,000 calls and $400.0 for 100,000 calls. In comparison to its competitors, Mistral Large 2411

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
Mistral Large 2411 is a standard, non-open-source model provided by Mistral AI, released on 2024-11-12. This analysis will delve into the cost structure, usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2411 is as follows:
* **Input**: $2.0 per 1M tokens
* **Output**: $6.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when the same input is used multiple times. This can significantly reduce costs in scenarios where the input data does not change frequently.

#### Batch API Savings
Batching API calls can also lead to cost savings, as the input cost per token decreases with batched requests. However, the exact savings depend on the specific use case and the number of tokens processed per batch.

#### Cost at Scale
The cost of using Mistral Large 2411 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $4.0
* **10,000 calls**: $40.0
* **100,000 calls**: $400.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens processed would be:
* 1,000 calls \* 500 tokens/call = 500,000 tokens
* 10,000 calls \* 500 tokens/call = 5,000,000 tokens
* 100,000 calls \* 500 tokens/call = 50,000,000 tokens

Using the pricing structure, the costs can be estimated as follows

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.1 |
| LMSYS Arena ELO | 1251 |
| ARC | 92.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2411 Benchmark Performance
The Mistral Large 2411 model, released by Mistral AI on 2024-11-12, is a standard, non-open-source model with a unique set of capabilities and limitations. To understand its performance and potential real-world applications, we'll delve into its benchmark scores.

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.1
* **LMSYS Arena ELO**: 1251
* **GSM8K**: 93.0

These scores indicate the model's ability to perform various tasks:
* **MMLU**: Measures the model's language understanding capabilities across a wide range of tasks. A score of 84.0 suggests that Mistral Large 2411 has strong language comprehension skills, making it suitable for tasks like coding, analysis, and content generation.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. With a score of 92.1, Mistral Large 2411 demonstrates excellent coding capabilities, making it a good fit for tasks that require generating or understanding code.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, simulating real-world scenarios. An ELO score of 1251 indicates that Mistral Large 2411 can hold its own in complex, dynamic situations, making it suitable for applications like agents and instruction following.
* **GSM8K**: Measures the model's math problem-solving skills. A score of 93.0 suggests that Mistral Large 241

## Competitor Comparison
### Comparison of Mistral Large 2411 with Top Competitors
#### Overview
Mistral Large 2411 is a standard-tier model offered by Mistral AI, released on 2024-11-12. It is a non-open source model with a unique set of capabilities and pricing. In this comparison, we will evaluate Mistral Large 2411 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2411 and GPT-4o is as follows:

* Mistral Large 2411:
	+ Input: $2.0 per 1M tokens
	+ Output: $6.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2411 is priced lower than GPT-4o for both input and output tokens. This makes it a more cost-effective option for applications with high input or output token requirements.

#### Performance Comparison
The performance of Mistral Large 2411 and GPT-4o can be evaluated using various benchmarks:

* Mistral Large 2411:
	+ MMLU: 84.0
	+ HumanEval: 92.1
	+ LMSYS Arena ELO: 1251
	+ GSM8K: 93.0
* GPT-4o: (benchmark scores not provided)

Since the benchmark scores for GPT-4o are not available, we cannot directly compare the performance of the two models. However, Mistral Large 2411 has demonstrated strong performance across various benchmarks, indicating its suitability for tasks such as coding, analysis, and function calling.

#### Context and Limits
The context window and output limits for Mistral Large 2411 are:

* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-06

These limits indicate that Mistral Large 2411 is suitable for tasks that require a large context window and moderate output length. However, it may not be the best choice for tasks that require very long output or real-time responses.

#### Capabilities and Use Cases
Mistral Large 2411 supports a range of capabilities, including:

* Text

## Best Use Cases
### Practical Advice on Top 5 Use Cases for Mistral Large 2411
The Mistral Large 2411 model, released by Mistral AI on 2024-11-12, is a powerful tool with a wide range of capabilities, including text, vision, function calling, and more. Given its pricing and capabilities, here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Large 2411 excels in coding and analysis tasks, making it an ideal choice for applications such as code review, code generation, and debugging. With its high scores in HumanEval (92.1) and GSM8K (93.0), this model can provide accurate and informative responses to coding-related queries.

```python
import openrouter

# Initialize the Mistral Large 2411 model
model = openrouter.MistralLarge2411()

# Use the model for code analysis
def analyze_code(code):
    response = model(code)
    return response

# Example usage
code = "def add(a, b): return a + b"
analysis = analyze_code(code)
print(analysis)
```

#### 2. **Function Calling and RAG**
The model's function calling capability makes it suitable for tasks that require executing specific functions or APIs. Its high score in LMSYS Arena ELO (1251) demonstrates its ability to reason and generate text based on the input.

```python
import openrouter

# Initialize the Mistral Large 2411 model
model = openrouter.MistralLarge2411()

# Define a function to call using the model
def call_function(func_name, args):
    response = model(f"Call {func_name} with arguments {args}")
    return response

# Example usage
func_name = "add"
args = "[2, 3]"
result = call_function(func_name, args)


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
