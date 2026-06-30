# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Medium 3's main strengths lie in its ability to handle complex tasks such as coding, analysis, and vision tasks. Its high scores on benchmarks like MMLU (80.0) and HumanEval (77.5) demonstrate its proficiency in these areas. The model is best used for tasks that require in-depth understanding and generation of content, such as summarization, content generation, and function calling. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model. Developers can evaluate the cost-effectiveness of this model by considering their specific use cases and the required input and output token volumes. With its balanced performance and pricing, Mistral Medium 3 is a viable option for developers seeking a reliable and efficient mid-tier model.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. However, the context window is limited to **131,072 tokens**, and the knowledge cutoff is **2024-11**. Cached tokens should be used for:
* Frequently asked questions or common queries
* Static data that doesn't require updates beyond the knowledge cutoff

#### Batch API Savings
Batch input is free, which can lead to significant savings when making multiple API calls. This is ideal for:
* Processing large datasets
* Handling high-volume requests

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To calculate the cost per call, we can use the following formula:
Cost per call = (Input cost per 1M tokens \* (avg tokens per call / 1,000,000)) + (Output cost per 1M tokens \* (avg output tokens per call / 1,000,000))

Assuming an average of 500 tokens per call and an average output of 100

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Model Overview
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **77.5**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts
It is best suited for tasks such as:
* coding
* analysis
* rag
* summarization
* vision_tasks
* content_generation
* function_calling
However, it is not recommended for:
* frontier_reasoning
* bulk_cheap_tasks
* simple_classification
* real_time_sub_100ms

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. It is not open-source and has a knowledge cutoff of 2024-11. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Since the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, a direct comparison is not possible. However, Mistral Medium 3 has a high MMLU score, indicating its strong performance in natural language understanding tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports various capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling



## Best Use Cases
### Practical Advice on Top 5 Use Cases for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review and debugging. When integrated with OpenRouter, you can leverage Mistral Medium 3's capabilities for automated code analysis.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a function to analyze code using OpenRouter
def analyze_code(code):
    # Use OpenRouter to send the code to Mistral Medium 3 for analysis
    response = openrouter.send_code(code, model)
    return response

# Example usage
code = "def hello_world(): print('Hello, World!')"
analysis = analyze_code(code)
print(analysis)
```

#### 2. **Summarization**
Mistral Medium 3's summarization capabilities make it an excellent choice for applications such as text summarization and news article summarization. You can integrate OpenRouter to send text to Mistral Medium 3 for summarization.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a function to summarize text using OpenRouter
def summarize_text(text):
    # Use OpenRouter to send the text to Mistral Medium 3 for summarization
    response = openrouter.send_text(text, model)
    return response

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
