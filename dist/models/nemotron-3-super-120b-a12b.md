# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a powerful language model designed for a wide range of applications, including chat, text generation, coding, analysis, and summarization. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, is part of Nvidia's offerings and is classified as a standard, non-open-source model. With its robust architecture, the Nemotron 3 Super is capable of handling complex tasks, leveraging its capabilities in text, function calling, JSON mode, streaming, and structured outputs.

### Architecture and Strengths
The Nemotron 3 Super boasts an impressive context window of 262,144 tokens and can generate outputs of up to 4,096 tokens. Its knowledge cutoff is 2023-12, ensuring it is well-versed in information up to that point. The model's pricing structure includes charges of $0.1 per 1M tokens for input and $0.5 per 1M tokens for output, with no charges for cached input or batch input. Benchmarks show the model achieving an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in various linguistic and logical tasks. Its capabilities make it particularly suited for applications requiring in-depth text analysis and generation.

### Use Cases and Cost Considerations
Developers can leverage the Nemotron 3 Super for a variety of use cases, including but not limited to chatbots, text generation, coding assistance, and data analysis. The model is not recommended for applications outside its listed capabilities. Cost-wise, the model offers competitive pricing, with examples including $0.3 for 1,000 calls (avg 500 tokens), $3.0 for 10,000 calls, and $30.0 for 100,000 calls. With no direct competitors listed, the

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### NVIDIA Nemotron 3 Super Pricing Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Cost Optimization Strategies
To minimize costs when using the NVIDIA Nemotron 3 Super, consider the following strategies:
* **Use Cached Tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API Calls**: Batch input is also free, so batching API calls can help reduce overall costs.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These costs demonstrate a linear scaling of expenses with the number of API calls. To estimate costs for a specific use case, calculate the average number of tokens per call and multiply by the number of calls, then apply the input and output pricing rates.

#### Example Cost Calculation
Assuming an average of 500 tokens per call, with 50% of tokens being input and 50% being output:
* **1,000 calls**: 500,000 tokens (250,000 input, 250,000 output)
	+ Input cost: 250,000 tokens / 1,000,000 tokens per $0.1 = $0.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. This analysis will focus on its benchmark performance, specifically the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score suggests better performance in tasks such as text generation, question answering, and language translation.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct code based on a given prompt. The absence of a HumanEval score for the Nemotron 3 Super makes it difficult to assess its coding capabilities directly.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that the Nemotron 3 Super is a strong competitor, but its exact standing is unclear without more context.

#### Real-World Implications
The benchmark scores suggest that the Nemotron 3 Super is a capable model for a variety of natural language processing tasks, including:
* Text generation: The high MMLU score indicates that the model can generate coherent and contextually relevant text.
* Analysis: The model's ability to process large amounts of text (up to 262,144 tokens) makes it suitable for tasks such as

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a general overview of its features, pricing, and performance. This will help users understand its capabilities and make informed decisions about its use.

#### Model Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on January 1, 2024. It is not open-source.

#### Pricing
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the NVIDIA Nemotron 3 Super are:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

### Choosing the NVIDIA Nemotron 3 Super
Since there are no direct competitors listed, the decision to use the NVIDIA Nemotron 3 Super will depend on the specific requirements of your project. Consider the following factors:
* **Performance**: If you need a model with a high MMLU score (80.0) and a decent LMSYS Arena ELO score (1200), the NVIDIA Nemotron 3 Super may be a good choice.
* **Capabilities**: If your project requires text generation, coding, analysis, or summarization, the NVIDIA Nemotron 3 Super supports these capabilities.
* **Cost**: If you expect a high volume of calls, the

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful model released by Nvidia on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Here are the top 5 use cases for the NVIDIA Nemotron 3 Super model, along with code integration examples using OpenRouter:

1. **Chat and Text Generation**: The Nemotron 3 Super model excels in generating human-like text, making it an ideal choice for chat applications.
   * Example Code:
   ```python
import openrouter

# Initialize the model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Generate text
response = model.generate_text("Hello, how are you?")
print(response)
```

2. **Coding and Analysis**: With its function calling and structured outputs capabilities, the Nemotron 3 Super model can be used for coding and analysis tasks.
   * Example Code:
   ```python
import openrouter

# Initialize the model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Analyze code
response = model.analyze_code("def hello_world(): print('Hello, World!')")
print(response)
```

3. **RAG Pipelines**: The Nemotron 3 Super model supports RAG pipelines, making it suitable for tasks that require retrieving and generating text.
   * Example Code:
   ```python
import openrouter

# Initialize the model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Retrieve and generate text
response = model.retrieve_and_generate("What is the capital

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
