# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports its main strengths, which include high performance in coding, analysis, and multilingual tasks. Its capabilities in function calling, RAG (Retrieval-Augmented Generation), and agents make it suitable for complex applications. The model has demonstrated impressive benchmarks, scoring 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications. Developers can leverage Mistral Large 2 for tasks that require in-depth analysis, coding assistance, and advanced natural language processing.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples include $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached inputs can significantly reduce costs, as there is no charge for them. Similarly, batch inputs are also free, which can lead to substantial savings when making multiple API calls.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible to minimize costs. Since there is no charge for cached inputs, it is beneficial to use them for repeated or similar queries. This can be particularly useful in applications where the same or similar inputs are processed multiple times.

#### Batch API Savings
Batching API calls can also lead to significant cost savings. Although the pricing data does not specify a direct discount for batch inputs, the fact that batch inputs are free suggests that making multiple calls in a single batch can reduce the overall cost per call. This is because the cost of input tokens is waived for batch inputs.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. 

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process human language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, with higher scores indicating stronger performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications that require code execution and evaluation.
* The **MMLU** score (84.0) indicates that the model has a good understanding of human language, but may not be the best choice for tasks that require extremely high levels of language understanding.
* The **LMSYS Arena ELO** score (1225) suggests that Mistral Large 2 is a competitive model, but its ranking may vary depending on the specific task and application.

#### Pricing and Cost
The pricing for Mistral Large 2 is as follows:
* **Input**: $3.0 per

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its top competitor, GPT-4o, highlighting price differences, performance trade-offs, and scenarios where each model is the better choice.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-intensive tasks, GPT-4o is cheaper by $0.5 per 1M tokens. However, for output-intensive tasks, Mistral Large 2 is more cost-effective by $1.0 per 1M tokens.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While GPT-4o's benchmark scores are not provided, Mistral Large 2's scores indicate strong performance in coding, analysis, and multilingual tasks.

#### Capabilities and Limitations
Mistral Large 2 supports a wide range of capabilities, including:
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
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model by Mistral AI, offers a wide range of capabilities including text, vision, function calling, and more. With its impressive benchmarks and large context window, it's an ideal choice for various applications. Here, we'll explore the top 5 best use cases for Mistral Large 2, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, making it perfect for automating code reviews, generating boilerplate code, and even assisting in debugging.
   * Example: Using OpenRouter to integrate Mistral Large 2 for code completion:
   ```python
import openrouter

# Initialize OpenRouter with Mistral Large 2
model = openrouter.MistralLarge2()

# Define a coding prompt
prompt = "Write a Python function to sort a list of integers."

# Generate code using Mistral Large 2
code = model.generate_code(prompt)

print(code)
```

2. **Data Analysis**: With its strong analytical capabilities, Mistral Large 2 can help in data analysis, report generation, and even data visualization.
   * Example: Using OpenRouter to analyze data with Mistral Large 2:
   ```python
import openrouter
import pandas as pd

# Load data into a Pandas DataFrame
data = pd.read_csv("data.csv")

# Initialize OpenRouter with Mistral Large 2
model = openrouter.MistralLarge2()

# Define an analysis prompt
prompt = "Analyze the data and generate insights."

# Generate analysis using Mistral Large 2
analysis = model.generate_analysis(prompt, data)

print(analysis)
```

3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's ability to retrieve information, augment existing data,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
