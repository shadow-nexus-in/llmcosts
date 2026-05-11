# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its suitability for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is well-suited for tasks that require extensive contextual understanding and detailed responses. Its capabilities in text generation, coding, analysis, and summarization make it an ideal choice for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. The pricing model for Mistral Small 4 includes input costs of $0.15 per 1M tokens and output costs of $0.6 per 1M tokens, with no charges for cached or batch inputs.

### Pricing and Performance
In terms of performance, Mistral Small 4 has a benchmark score of 80.0 on the MMLU test and an LMSYS Arena ELO score of 1200. While it does not have direct competitors listed, its pricing and performance metrics provide a clear picture for developers looking to integrate this model into their applications. For example, 1,000 calls with an average of 500 tokens would cost $0.375, making it a viable option for projects with moderate to high usage. With its balanced performance and pricing, Mistral Small 4 is a consideration for developers seeking a reliable language model for their projects, especially those focused on text-based applications

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input is free, utilize this feature whenever possible to reduce input costs.
* **Batch API calls**: With batch input being free, grouping API calls together can significantly reduce overall costs.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples demonstrate a linear cost increase with the number of API calls. To estimate costs at scale, we can use the following calculations:
* **Average cost per call**: $0.375 / 1,000 calls = $0.000375 per call
* **Average cost per token**: Assuming an average of 500 tokens per call, the cost per token is $0.000375 / 500 tokens = $0.00000075 per token

Using these estimates, we can calculate the cost for a large number of API calls:
* **1 million calls (avg 500 tokens)**: 1,000,000 calls \* $0.000375 per call = $375
* **10

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure for input and output tokens.

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

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores representing better performance. The LMSYS Arena ELO score of 1200 is a measure of the model's overall strength, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
For real-world use, the benchmark scores can be interpreted as follows:
* The MMLU score of 80.0 suggests that the model is

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance trade-offs. This will help users understand when to choose this model and what to expect from it.

#### Model Overview
The Mistral: Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. It has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral: Mistral Small 4 model is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To give users a better idea of the costs involved, here are some examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance Trade-Offs
The Mistral: Mistral Small 4 model has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

These scores indicate that the model has a moderate level of performance. The MMLU score of 80.0 suggests that the model is capable of handling a wide range of tasks, but may not excel in any particular area. The LMSYS Arena ELO score of 1200 indicates that the model has a moderate level of competitiveness in the LMSYS Arena benchmark.

#### When to Choose Mistral: Mistral Small 4
Based on its features and pricing, the Mistral: Mistral Small 4 model is a good choice for users who:
* Need a standard, non-open-source model for chat, text generation, coding

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4 is a powerful language model provided by Mistralai, released on 2024-01-01. This model is classified as a standard, non-open source model. In this guide, we will explore the top 5 best use cases for Mistral: Mistral Small 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral: Mistral Small 4
Based on the capabilities and best-for categories, the top 5 use cases for Mistral: Mistral Small 4 are:

1. **Chat**: Mistral: Mistral Small 4 can be used to generate human-like responses in chat applications.
2. **Text Generation**: This model can be used for text generation tasks such as writing articles, creating content, and more.
3. **Coding**: Mistral: Mistral Small 4 can assist with coding tasks such as code completion, code review, and debugging.
4. **Analysis**: This model can be used for text analysis tasks such as sentiment analysis, entity recognition, and topic modeling.
5. **Summarization**: Mistral: Mistral Small 4 can be used to summarize long pieces of text into concise and meaningful summaries.

### Code Integration Examples with OpenRouter
Here are some code integration examples using OpenRouter:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the model and input parameters
model = "mistralai/mistral-small-2603"
input_text = "Hello, how are you?"

# Generate a response using the chat capability
response = client.generate(
    model=model,
    input=input_text,
    capability="chat"
)

print(response)

# Define a function to call using the function_calling capability
def add(a, b):
    return a + b

#

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
