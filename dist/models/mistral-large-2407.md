# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed for a wide range of applications, including coding, analysis, and multilingual support. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores highlight its proficiency in coding, analysis, and other complex tasks. The model is best utilized for applications such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To illustrate the cost implications, consider that 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers a competitive pricing model, especially considering its robust capabilities

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can take advantage of the free batch input pricing.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): **$6.0**
* 10,000 calls: **$60.0**
* 100,000 calls: **$600.0**

To estimate the cost of using Mistral Large 2, we can use the following formula:
Cost = (Number of Input Tokens / 1,000,000) \* $3.0 + (Number of Output Tokens / 1,000,000) \* $9.0

For example, if we make 1,000 calls with an average of 500 input tokens and 200 output tokens, the total cost would be:
Cost = (500,000 / 1,000,

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is designed for various tasks, including coding, analysis, and function calling, with capabilities in text, vision, and more.

#### Pricing
The pricing for Mistral Large 2 is as follows:
- Input: **$3.0 per 1M tokens**
- Output: **$9.0 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has a context window of **131,072 tokens**, a maximum output of **4,096 tokens**, and a knowledge cutoff of **2024-07**.

#### Benchmarks
The model's performance is measured by the following benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 84.0
  - MMLU scores indicate a model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher score suggests better performance in tasks requiring broad language understanding.
- **HumanEval**: 92.0
  - HumanEval scores reflect a model's ability to write correct and functional code based on human-provided specifications. Higher scores indicate better coding capabilities.
- **LMSYS Arena ELO**: 1225
  - LMSYS Arena ELO scores measure a model's competitive performance in various language tasks against other models. A higher ELO score signifies superior performance and adaptability in diverse linguistic challenges.
- **G

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities and performance metrics. To understand its value proposition, we'll compare it with its top competitor, GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o for input tokens, but slightly cheaper for output tokens.

#### Performance Trade-offs
The performance of Mistral Large 2 is measured by the following benchmarks:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the performance metrics for GPT-4o are not provided, we can infer that Mistral Large 2 offers strong performance across various tasks, including coding, analysis, and multilingual support.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Agents
* Multilingual support
* Function calling

On the other hand, it is not recommended for tasks that require:
* Embeddings
* Bulk cheap processing
* Real-time sub-100ms processing
* Vision-heavy tasks

#### Cost Examples
To illustrate the cost of using Mistral Large 2, consider the following examples:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Choosing the Right Model
When deciding between Mistral Large 2 and GPT-4o, consider the following factors:
* **Input and output token costs**: If your application requires a large number of input tokens, G

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even learn from code examples.
   - **Example**: Using OpenRouter to integrate Mistral Large 2 for automated code completion.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.Model("mistralai/mistral-large-2407")

   # Define a coding prompt
   prompt = "Write a Python function to sort a list of integers."

   # Generate code using Mistral Large 2
   response = model.generate(prompt)
   print(response)
   ```

2. **Analysis and Research**: With its strong analysis capabilities, Mistral Large 2 can be used for in-depth analysis of texts, research papers, or any form of written content.
   - **Example**: Analyzing a research paper using Mistral Large 2 through OpenRouter.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.Model("mistralai/mistral-large-2407")

   # Load a research paper text
   with open("research_paper.txt", "

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
