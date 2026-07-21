# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These specifications and pricing make Mistral Small 4 a competitive choice for developers looking for a robust language model for various applications, including chatbots, text generation, and coding assistance.

### Use Cases and Cost Considerations
Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. However, its limitations and lack of direct competitors mean that developers should carefully evaluate their needs against the model's capabilities. The cost of using Mistral Small 4 can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

This indicates that input and output tokens are the primary cost drivers, while cached and batch inputs are not charged.

#### Usage Scenarios
To optimize costs, consider the following scenarios:
* **Use cached tokens when possible**: Since cached input tokens are free, leveraging this feature can significantly reduce costs, especially for repeated or similar inputs.
* **Batch API calls**: With batch input being free, grouping multiple inputs into a single API call can lead to substantial savings, especially for high-volume use cases.

#### Cost at Scale
The provided cost examples illustrate the scaling costs for Mistral Small 4:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples demonstrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant.

#### Calculating Costs
To estimate costs for a specific use case, consider the average number of input and output tokens per call. With an input cost of $0.15 per 1M tokens and an output cost of $0.6 per 1M tokens, the total cost can be calculated as follows:
* **Input cost**: (number of input tokens / 1,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

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

The MMLU score of 80.0 indicates the model's ability to understand and process natural language. A higher MMLU score generally corresponds to better language understanding capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment. ELO scores are used to rank models based on their performance, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
For real-world use, the Mistral Small 4 model's benchmark performance suggests that it is

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Mistral: Mistral Small 4 model is a standard-tier model provided by Mistralai, released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for the Mistral: Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
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
The Mistral: Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the Mistral: Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

### Choosing the Mistral: Mistral Small 4 Model
Since there are no direct competitors listed, the decision to choose the Mistral: Mistral Small 4 model depends on the specific requirements of your project. Consider the following factors:
* **Context Window**: If your application requires a large context window, the Mistral: Mistral Small 4 model may be a good choice, with a context window of 262,144 tokens.
* **Output Requirements**: If your application requires a moderate output size,

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This model is not open-source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities, the top 5 best use cases for Mistral: Mistral Small 4 are:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral: Mistral Small 4 is ideal for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's capability for function calling and structured outputs makes it suitable for coding tasks and analysis of complex data.
3. **Summarization**: Mistral: Mistral Small 4 can be used for summarizing long pieces of text into concise, meaningful summaries.
4. **RAG Pipelines**: The model's support for JSON mode and streaming makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from external sources and generating text based on that information.
5. **OpenRouter Integration**: For tasks that require routing or integrating with other systems, Mistral: Mistral Small 4 can be used in conjunction with OpenRouter to create complex workflows.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral: Mistral Small 4 with OpenRouter using Python:
```python
import requests

# Set up the API endpoint and credentials
endpoint = "https://api.mistralai.com/mistral-small-2603"
api_key = "YOUR_API_KEY"

# Define a function to call the model
def call_model(prompt):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
