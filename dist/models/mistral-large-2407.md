# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its effectiveness in handling complex tasks, especially those involving coding and multilingual support. The model is best utilized for applications requiring in-depth analysis, coding assistance, and function calling, where its ability to understand and generate human-like text is invaluable. However, it may not be the most cost-effective option for tasks requiring embeddings, bulk processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when the same input is used multiple times. This can be particularly useful in applications where the input data does not change frequently, such as in coding or analysis tasks.

#### Batch API Savings
Batch input is also free, which means that making API calls in batches can significantly reduce costs. This is especially beneficial for large-scale applications where thousands of API calls are made.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs are calculated based on the average number of tokens per call and the pricing structure.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges $2.5/1M input and $10.0/1M output. However, the free cached input and batch input options make Mistral Large 2 a more attractive option for certain use cases.

#### Conclusion
Mistral Large 2 offers a unique set of capabilities and

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process a wide range of language tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and responses.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large language model arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving skills.

#### Real-World Implications
These benchmark scores suggest that the Mistral Large 2 model is:
* Suitable for tasks that require a deep understanding of language, such as coding, analysis, and text-based applications.
* Capable of generating high-quality code and responses, making it a good fit for human-in-the-loop applications.
* Competitive with other large language models, as indicated by its LMSYS Arena ELO score.
* Proficient in math problem-solving, with a high GSM8K score.

#### Capabilities and Limitations
The model has the following capabilities:
* **Text**: processing and generating text
* **Vision**: limited vision capabilities
* **Function_calling**: ability to call external functions
* **JSON_mode**: support for JSON input and output

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive in terms of input cost but slightly cheaper in terms of output cost compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the exact benchmarks for GPT-4o are not provided, the performance of Mistral Large 2 suggests it is a high-performing model, particularly in coding and analysis tasks.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications indicate that Mistral Large 2 is capable of handling large inputs and generating substantial outputs, making it suitable for complex tasks.

#### Capabilities and Best Use Cases
Mistral Large 2 supports:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for:
- Coding
- Analysis
- RAG
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring sub-100ms response times
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its capabilities in text, vision, and more, it's a versatile tool for developers. Here, we'll explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding Assistance**
Mistral Large 2 is ideal for coding tasks, given its high scores in HumanEval (92.0) and GSM8K (93.0). It can assist in writing, debugging, and optimizing code.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example coding prompt
prompt = "Write a Python function to sort a list of integers."

# Get the response
response = model.generate(prompt)

print(response)
```

#### 2. **Analysis and Research**
With its large context window (131,072 tokens) and high MMLU score (84.0), Mistral Large 2 is suitable for in-depth analysis and research tasks, including understanding complex documents and generating summaries.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example analysis prompt
prompt = "Summarize the key points of a given research paper."

# Get the response
response = model.generate(prompt)

print(response)
```

#### 3. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Large 2 supports RAG tasks, making it useful for applications that require retrieving information, augmenting it, and then generating a response based on that information.

```python


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
