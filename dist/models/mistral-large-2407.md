# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 output tokens, making it suitable for complex and detailed responses. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports multiple capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These capabilities and performance metrics make Mistral Large 2 best suited for tasks such as coding, analysis, and applications requiring advanced natural language understanding and generation. However, it's not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified pricing for cached input or batch input. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers competitive pricing for

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.
- **Batch API Savings**: Although the pricing does not explicitly mention a discount for batch inputs, the fact that batch input is listed as $0 per 1M tokens suggests that batching can be an effective way to save on costs. However, the actual savings would depend on the implementation and how the model processes batched inputs.

#### Cost at Scale
Given the cost examples provided:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with the number of API calls. To estimate costs for different scenarios, we can use the average cost per call. For 1,000 calls with an average of 500 tokens, the cost is $6.0, which translates to $0.006 per call.

#### Competitor Comparison
Comparing Mistral Large 2 with GPT-4o:
- **Mistral Large 2 Input**: $3.0 per 1M tokens

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

#### Interpretation of Benchmarks
The benchmarks provide insight into the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: A score of 92.0 measures the model's ability to generate code that is correct and functional. This score indicates that the model is highly proficient in coding

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In comparison, its top competitor, GPT-4o, is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens.

| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

#### Performance Trade-offs
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its performance benchmarks are as follows:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the performance benchmarks of GPT-4o are not provided in the data. However, based on the pricing, GPT-4o may offer a more cost-effective solution for input-intensive tasks, while Mistral Large 2 may be more suitable for output-intensive tasks.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

Assuming an average of 500 tokens per call, the cost of using GPT-4o can be estimated as follows:
- 1,000 calls (avg 500 tokens): $5.0 (input) + $10.0 (output) = $15.0 (assuming 1:1 input:output ratio)
- 10,000 calls

## Best Use Cases
### Practical Advice on Top 5 Use Cases for Mistral Large 2
Mistral Large 2, a premium model by Mistral AI, offers a wide range of capabilities including text, vision, function calling, and more. With its impressive benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0) and features, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Development**
Mistral Large 2 excels in coding tasks, making it an ideal choice for developers. Its `function_calling` capability allows for seamless integration with external code. 
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Use the model for coding tasks
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Example usage
prompt = "Write a Python function to sort a list of integers."
code = generate_code(prompt)
print(code)
```

#### 2. **Analysis and Research**
With its high MMLU score (84.0), Mistral Large 2 is well-suited for analysis and research tasks. Its `text` capability enables in-depth text analysis.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Use the model for text analysis
def analyze_text(text):
    response = model.generate(f"Analyze the following text: {text}")
    return response

# Example usage
text = "The impact of climate change on global economies."
analysis = analyze_text(text)
print(analysis)
```

#### 3. **RAG (Ret

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
