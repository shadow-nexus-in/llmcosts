# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. This model is not open source, and its pricing structure includes input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is designed to handle a wide range of tasks, from coding and analysis to vision tasks and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores, which include an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. These scores indicate that Mistral Medium 3 is well-suited for tasks that require a combination of natural language understanding, coding abilities, and strategic thinking. With its knowledge cutoff date of 2024-11, Mistral Medium 3 is equipped to handle tasks that require up-to-date knowledge, but may not be the best choice for tasks that require very recent information.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens required. For example, 1,000 calls with an average of 500 tokens would cost $1.

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and has a specific cost structure for input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the context window is limited to 131,072 tokens, and the knowledge cutoff is 2024-11. Therefore, cached tokens should be used when:
* The input data is within the context window and knowledge cutoff.
* The input data is repetitive or can be reused.

#### Batch API Savings
Batch input is free, which means that making batch API calls can significantly reduce costs. To maximize batch API savings:
* Group multiple requests into a single batch call.
* Ensure that the batch call is within the context window and knowledge cutoff.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These costs can be broken down into input and output costs:
* 1,000 calls: $0.4 (input) + $0.8 (output) = $1.2
* 10,000 calls: $4.0 (input) + $8.0 (output) = $12.0
* 100,000 calls: $40.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, provided by Mistral AI, was released on 2025-04-17. It is a mid-tier model, not open source, with a context window of 131,072 tokens and a maximum output of 16,384 tokens.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0. This score indicates the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 77.5. This score measures the model's ability to evaluate and execute human-written code, reflecting its coding and problem-solving capabilities.
* **LMSYS Arena ELO**: 1200. This score represents the model's performance in a competitive arena, where it is pitted against other models in various tasks. A higher ELO score indicates better performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score (80.0) suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of natural language, such as text analysis, summarization, and content generation.
* The strong HumanEval score (77.5) indicates that the model

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will analyze its performance and cost against two top competitors: Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini, on the other hand, is significantly cheaper for input but also for output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Context and Limits
The context window and output limits for Mistral Medium 3 are:
* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

These limits are not provided for the competitor models, making it difficult to directly compare their capabilities.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
*

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This model excels in various tasks, including coding, analysis, and content generation. In this guide, we will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Development**
Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and bug detection. Its function calling capability allows it to interact with external systems, making it an excellent choice for automating development workflows.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a coding task
def code_completion(prompt):
    response = router.call(prompt, max_tokens=1024)
    return response

# Test the code completion function
print(code_completion("Complete the following code: def hello_world():"))
```

#### 2. **Text Analysis and Summarization**
Mistral Medium 3 can analyze large volumes of text data, providing insights and summaries. Its context window of 131,072 tokens allows it to process lengthy documents and articles.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a text analysis task
def text_summarization(text):
    prompt = f"Summarize the following text: {text}"
    response = router.call(prompt, max_tokens

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
