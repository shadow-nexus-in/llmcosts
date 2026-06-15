# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate outputs of up to 4,096 tokens.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance. With a context window of 262,144 tokens and the ability to generate up to 4,096 tokens of output, it is well-suited for tasks that require understanding and generating significant amounts of text, such as chat, text generation, coding, analysis, and summarization. The model also supports rag pipelines, indicating its ability to retrieve and generate text based on external knowledge sources. Its benchmark scores, such as an MMLU of 80.0 and an LMSYS Arena ELO of 1200, demonstrate its competence in various linguistic and logical tasks.

### Pricing and Cost Considerations
The pricing model for Mistral: Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs, examples are provided: 1,000 calls averaging 500 tokens cost $0.375, 10,000 calls cost $3.75, and 100,000 calls cost $37.5. With its unique set of capabilities and competitive pricing, Mistral: Mistral Small 4

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard, non-open source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is free, the primary cost driver is the output tokens. However, batching can still help reduce the overall cost by minimizing the number of API calls required, thus reducing the output token count.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

To further analyze the cost at scale, let's calculate the cost per 1M tokens for the given examples:
- Assuming an average of 500 tokens per call, 1,000 calls would be approximately 0.5M tokens.
- For 1,000 calls, the cost is $0.375, which translates to $0.75 per 1M tokens (0.375 / 0.5).
- For 10,000 calls, the cost is $3.75, which translates to $0.75 per 1M tokens (3.75 / 5).
- For 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive arena. A higher ELO score indicates better performance compared to other models.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance on specific tasks such as coding and mathematical problem-solving.

#### Real-World Implications
The benchmark performance of Mist

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general overview of the model's features, pricing, and capabilities, highlighting its strengths and potential use cases.

#### Model Overview
* **Model:** Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Performance and Capabilities
Mistral Small 4 has the following capabilities:
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12
* **Capabilities:** text, function_calling, json_mode, streaming, structured_outputs
* **Best For:** chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Benchmarks
The model's performance on various benchmarks is:
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral Small 4
Given the lack of direct competitors, Mistral Small 4 can be considered for a wide range of applications, including:
* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

When to choose Mistral Small 4:
* When a standard-tier model with a large context window is required
* When the application requires a balance between input and output pricing
* When the use case involves text, function calling, JSON mode, streaming, or structured outputs

Note that the absence of direct competitors makes it difficult to provide

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high MMLU score of 80.0, Mistral Small 4 is well-suited for chat and text generation applications, such as conversational AI and content creation.
2. **Coding and Analysis**: Its ability to perform function calling and structured outputs makes it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling makes it suitable for RAG (Retrieval-Augmented Generation) pipelines, which involve generating text based on retrieved information.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or live content creation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Generate text using the model
def generate_text(prompt):
    output = model.generate_text(prompt, max_output=4096)
    return output

# Perform function calling

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
