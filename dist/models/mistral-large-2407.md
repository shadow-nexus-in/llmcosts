# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its architecture is designed to handle a wide range of tasks, from coding and analysis to multilingual support and function calling. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex, data-intensive applications.

### Strengths and Use Cases
Mistral Large 2 demonstrates exceptional performance across various benchmarks, including MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). Its primary strengths lie in its ability to handle coding, analysis, and function calling tasks with high accuracy. The model is best utilized for applications that require in-depth analysis, coding assistance, and multilingual support. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy workloads. With its pricing structure, developers can expect to pay $3.0 per 1M input tokens and $9.0 per 1M output tokens, making it a premium option for high-value applications.

### Pricing and Competitiveness
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 100,000 calls would amount to $600.0. In comparison to its top competitor, GPT-4o, which offers input and

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
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached inputs)
- **Batch Input**: $None per 1M tokens (suggesting no specific discount for batched inputs, but costs are calculated based on input and output tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there's no additional cost for cached inputs, it's beneficial to use cached tokens whenever possible to minimize input costs.
- **Batch API Savings**: Although there's no explicit discount for batch inputs, processing requests in batches can reduce the overhead and potentially lower the average cost per call by minimizing the number of API calls needed.

#### Cost at Scale
Given the average cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

We can observe a linear scaling of costs with the number of calls. This suggests that the cost per call remains constant, with no economies of scale evident from the provided data.

#### Competitor Comparison
Comparing Mistral Large 2 with GPT-4o:
- **Input Cost**: Mistral Large 2 is priced at $3.0 per 1M tokens, while GPT-4o is priced at $2.5 per 1M tokens. GPT-4o offers a

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher score suggests better performance in understanding and generating human-like language.
* **HumanEval**: 92.0 - This score measures the model's ability to generate correct code based on human-written prompts. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1225 - This score represents the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better overall performance.
* **GSM8K**: 93.0 - This score measures the model's ability to solve math problems, with a higher score indicating better math reasoning capabilities.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is a highly capable model, particularly in coding and

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores are not directly comparable to GPT-4o without its benchmark data. However, Mistral Large 2's high scores suggest strong performance in various tasks, including coding, analysis, and multilingual support.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring sub-100ms responses
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Large 2
Mistral Large 2, a premium model by Mistral AI, offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. Given its strengths and pricing, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Large 2 excels in coding tasks with a high HumanEval score of 92.0. It can be used for code analysis, code completion, and code review. 
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example code completion task
prompt = "Complete the following Python function: def greet(name):"
response = model.complete_code(prompt)
print(response)
```

#### 2. **RAG (Retrieval-Augmented Generation) Tasks**
With its high MMLU score of 84.0, Mistral Large 2 is suitable for RAG tasks that require generating text based on retrieved information.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example RAG task
prompt = "Write a short story about a character who discovers a hidden world."
response = model.generate_text(prompt, rag=True)
print(response)
```

#### 3. **Multilingual Support**
Mistral Large 2 offers multilingual support, making it an excellent choice for applications that require text processing in multiple languages.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example multilingual task
prompt = "Translate the following text from English to Spanish: Hello, how are you?"
response = model.translate_text(prompt, target_language

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
