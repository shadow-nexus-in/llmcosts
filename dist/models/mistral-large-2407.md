# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require extensive contextual understanding and the ability to process large amounts of information.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports multiple capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate that Mistral Large 2 is particularly adept at tasks that require complex reasoning and coding abilities. It is best utilized for applications such as coding, analysis, retrieval-augmented generation (RAG), and multilingual tasks. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, scaling up to $600.0 for 100,000 calls. Compared to competitors like GPT-4o, which charges $2.5/

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and has a unique cost structure.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch API calls can also help reduce costs. With batch input being free, making batch API calls can significantly lower the overall cost of using the model.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of API calls \* Average tokens per call \* Input cost per token) + (Number of API calls \* Average output tokens per call \* Output cost per token)

Assuming an average of 500 tokens per call and 4,096 output tokens per call (max output), we can calculate the cost as follows:
* 1,000 API calls: (1,000 \* 500 \* $3.0/1M) + (1,000 \* 4,096 \* $9.0/1M) = $6.

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and understand programming concepts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that Mistral Large 2 is:
* Suitable for coding and analysis tasks, with a high HumanEval score indicating strong programming capabilities.
* Effective in multilingual applications, given its high performance across various benchmarks.
* Capable of handling function calling, JSON mode, and streaming, making it a versatile model for various use cases.
* Not ideal for embeddings, bulk cheap processing, or real-time applications requiring sub-100ms response times.

#### Cost Analysis
The pricing model is based on input and output tokens, with examples:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, and multilingual applications.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input tokens, but slightly cheaper in terms of output tokens.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the exact benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o will depend on the specific use case and the importance of each benchmark.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These limits should be considered when choosing a model, especially for applications requiring longer context windows or more up-to-date knowledge.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual applications
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap applications
- Real-time applications with latency under 100ms
- Vision-heavy applications

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it ideal for automated code generation, code review, and code optimization. For example, when using OpenRouter for routing network packets, you can integrate Mistral Large 2 to generate optimized routing configurations:
    ```python
import openrouter
from mistralai import MistralLarge2

# Initialize Mistral Large 2 model
model = MistralLarge2()

# Define a function to generate routing configurations
def generate_routing_config(network_topology):
    # Use Mistral Large 2 to generate optimized routing configurations
    config = model.generate_code(network_topology)
    return config

# Use OpenRouter to route network packets
router = openrouter.OpenRouter()
router.route_packets(generate_routing_config(network_topology))
```

2. **Analysis and Research**: With its strong analysis capabilities, Mistral Large 2 is suitable for research tasks, such as data analysis, scientific paper summarization, and research paper generation. For instance, you can use Mistral Large 2 to analyze network traffic patterns using OpenRouter:
    ```python
import openrouter
from mistralai import MistralLarge2

# Initialize Mistral Large 2 model
model = MistralLarge2()

# Define a

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
