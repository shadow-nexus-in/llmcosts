# Claude 3.5 Haiku API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude 3.5 Haiku
Claude 3.5 Haiku, developed by Anthropic, is a standard-tier model released on 2024-11-04. This model is not open-source. Its architecture is designed to handle a variety of tasks, including text and vision processing, with capabilities such as JSON mode, streaming, batch processing, and system prompts. The model's context window can handle up to 200,000 tokens and can generate a maximum output of 8,192 tokens, with a knowledge cutoff date of 2024-07.

### Technical Strengths and Use Cases
Claude 3.5 Haiku demonstrates its strengths through various benchmarks: it achieves an MMLU score of 81.4, a HumanEval score of 88.1, an LMSYS Arena ELO of 1220, and a GSM8K score of 92.0. These metrics indicate the model's proficiency in tasks that require understanding and generating human-like text. It is best suited for applications such as chatbots, text classification, summarization, coding assistance, and high-volume tasks. However, it may not perform optimally in tasks requiring complex reasoning, frontier coding, embeddings, or bulk cheap tasks.

### Pricing and Cost Considerations
The pricing for Claude 3.5 Haiku is as follows: $0.8 per 1M tokens for input, $4.0 per 1M tokens for output, $0.08 per 1M tokens for cached input, and $0.4 per 1M tokens for batch input. To give developers a better understanding of the costs, examples are provided: 1,000 calls with an average of 500 tokens cost $2.4, 10,000 calls cost $24.0, and 100,000 calls cost $240.0. When comparing with top competitors like GPT-4o Mini and Llama 3

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.8 |
| Output | $4.0 |
| Cached Input | $0.08 |
| Batch Input | $0.4 |
| Batch Output | $2.0 |

## Pricing Analysis
### Pricing Analysis for Claude 3.5 Haiku
#### Overview
The Claude 3.5 Haiku model, provided by Anthropic, offers a range of capabilities including text, vision, and tool use, making it suitable for applications such as chatbots, classification, and coding assistance. This analysis will delve into the cost structure, the benefits of using cached tokens, batch API savings, and the cost at scale for this model.

#### Cost Structure
The pricing for Claude 3.5 Haiku is as follows:
- **Input**: $0.8 per 1M tokens
- **Output**: $4.0 per 1M tokens
- **Cached Input**: $0.08 per 1M tokens, representing a 90% discount over regular input costs
- **Batch Input**: $0.4 per 1M tokens, offering a 50% reduction compared to standard input pricing

#### Using Cached Tokens
Cached tokens can significantly reduce costs, especially for applications where the same input sequences are repeated. With a cost of $0.08 per 1M tokens, cached input is 10 times cheaper than regular input. This makes it an attractive option for high-volume tasks where input redundancy is high.

#### Batch API Savings
For batch processing, the cost per 1M tokens is $0.4, which is half the cost of regular input. This pricing tier is beneficial for applications that can process inputs in batches, as it offers a direct 50% cost savings over the standard input rate.

#### Cost at Scale
To understand the cost implications at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $2.4
- **10,000 calls**: $24.0
- **100,000 calls**: $240.0

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 81.4 |
| HumanEval | 88.1 |
| LMSYS Arena ELO | 1220 |
| ARC | 92.0 |

## Benchmark Analysis
### Claude 3.5 Haiku Benchmark Performance Analysis
#### Overview
The Claude 3.5 Haiku model, released by Anthropic on 2024-11-04, is a standard, non-open-source model with a context window of 200,000 tokens and a maximum output of 8,192 tokens. Its pricing structure includes input, output, cached input, and batch input costs.

#### Pricing Structure
The pricing for Claude 3.5 Haiku is as follows:
* Input: **$0.8 per 1M tokens**
* Output: **$4.0 per 1M tokens**
* Cached Input: **$0.08 per 1M tokens**
* Batch Input: **$0.4 per 1M tokens**

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU: 81.4** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval: 88.1** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score suggests better performance in coding assistance and programming tasks.
* **LMSYS Arena ELO: 1220** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher ELO score indicates better overall performance and adaptability.

#### Real-World Implications

## Competitor Comparison
### Comparison of Claude 3.5 Haiku with Top Competitors
#### Overview
Claude 3.5 Haiku, offered by Anthropic, is a standard-tier model with a release date of 2024-11-04. It is not open-source and has a specific set of capabilities and limitations. This comparison will delve into the pricing, performance, and use cases of Claude 3.5 Haiku against its top competitors, GPT-4o Mini and Llama 3.1 70B Instruct.

#### Pricing Comparison
The pricing for each model is as follows:
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
	+ Cached Input: $0.08 per 1M tokens
	+ Batch Input: $0.4 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens
* **Llama 3.1 70B Instruct**:
	+ Input: $0.52 per 1M tokens
	+ Output: $0.75 per 1M tokens

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* **Claude 3.5 Haiku**:
	+ MMLU: 81.4
	+ HumanEval: 88.1
	+ LMSYS Arena ELO: 1220
	+ GSM8K: 92.0
* **GPT-4o Mini** and **Llama 3.1 70B Instruct** benchmarks are not provided, making a direct comparison challenging. However, we can infer their performance based on their pricing and intended use cases.

#### Capabilities and Limitations
Claude 3.5 Haiku has the following capabilities and limitations:
* **Capabilities**: text, vision, tool_use, json_mode, streaming, batch_processing, system_prompts
* **Best for**: chatbots, classification, summarization, rag, coding_assistance, high_volume_anthropic
* **Not good for**: complex_reasoning, frontier_coding, embeddings, bulk_cheap_tasks
* **Context Window**: 200,000 tokens
*

## Best Use Cases
### Introduction to Claude 3.5 Haiku
The Claude 3.5 Haiku model, provided by Anthropic, is a powerful tool with a wide range of capabilities, including text, vision, and tool use. With its standard tier and release date of 2024-11-04, it offers a context window of 200,000 tokens and a maximum output of 8,192 tokens.

### Top 5 Best Use Cases for Claude 3.5 Haiku
Based on its capabilities and benchmarks, the top 5 best use cases for Claude 3.5 Haiku are:

1. **Chatbots**: Claude 3.5 Haiku's high performance in human-like conversation tasks makes it an ideal choice for building chatbots.
2. **Classification**: With its strong performance in text-based tasks, Claude 3.5 Haiku can be used for classification tasks such as sentiment analysis and topic modeling.
3. **Summarization**: Claude 3.5 Haiku's ability to process large amounts of text makes it suitable for summarization tasks, such as summarizing long documents or articles.
4. **Coding Assistance**: Claude 3.5 Haiku's high score in HumanEval (88.1) makes it a good choice for coding assistance tasks, such as code completion and code review.
5. **High-Volume Anthropic Tasks**: Claude 3.5 Haiku's capabilities in batch processing and streaming make it suitable for high-volume tasks that require processing large amounts of data.

### Code Integration Examples with OpenRouter
To integrate Claude 3.5 Haiku with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Claude 3.5 Haiku model
model = openrouter.Claude35Haiku()

# Define a function to process text data
def process_text(text):
    # Use the model to process the text
    output = model(text)
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
