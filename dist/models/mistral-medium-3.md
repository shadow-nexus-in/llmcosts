# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed for a wide range of applications. This model is not open source. From an architectural standpoint, Mistral Medium 3 boasts a context window of 131,072 tokens and can generate up to 16,384 tokens as output. Its knowledge cutoff is 2024-11, ensuring it has a broad and up-to-date understanding of the world up to that point.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its capabilities, which include text, vision, function calling, JSON mode, streaming, and system prompts. This versatility makes it best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, it's positioned to handle complex tasks efficiently. However, it's not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms.

### Benchmarks and Cost Considerations
Mistral Medium 3 has demonstrated its performance through various benchmarks, achieving scores of 80.0 on MMLU, 77.5 on HumanEval, and an ELO rating of 1200 on LMSYS Arena. While its performance on GSM8K is not available, its overall capabilities and pricing make it a competitive option in the market. For example, making 1,000 calls with an average of 500 tokens each would cost $1.2, scaling to $12.0 for 10,000 calls and $120.0 for 100,000 calls. Compared to competitors like Claude 3.5 Haiku and GPT-4o Mini

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible to minimize costs.
- **Batch API**: With batch input being free, batching API calls can significantly reduce overall costs, especially for large-scale operations.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs can be broken down further based on the input and output pricing:
- Assuming an average of 500 tokens per call, 1,000 calls would amount to 500,000 tokens. At $0.4 per 1M tokens for input, this would cost $0.2 for input. Without specific output token counts, we cannot directly calculate output costs, but the total cost of $1.2 for 1,000 calls suggests significant output costs.
- For 10,000 and 100,000 calls, the costs scale linearly, indicating that the pricing model is consistent and predictable.

#### Comparison with Competitors
Mistral Medium 3's pricing is compared to its top competitors:
- **

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, a model provided by Mistral AI, offers a balance of performance and cost for various real-world applications. Released on 2025-04-17, this mid-tier model is not open source.

#### Pricing
The pricing structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications include:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
Mistral Medium 3's performance is measured through several benchmarks:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates strong performance across various tasks, suggesting Mistral Medium 3 can handle complex language understanding tasks effectively.
* **HumanEval (77.5)**: HumanEval assesses a model's coding abilities by evaluating its capacity to write correct and functional code based on given prompts. A score of 77.5 shows that Mistral Medium 3 has good coding capabilities, making it suitable for tasks like coding and analysis.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score reflects a model's competitive performance

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the price differences, performance trade-offs, and use cases for Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is priced between Claude 3.5 Haiku and GPT-4o Mini, offering a balance between cost and performance.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
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

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
To illustrate the cost implications, consider the following examples

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this mid-tier model offers a balance between performance and cost. Here, we'll explore the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding tasks, such as code completion, code review, and code analysis. Its ability to understand and generate code makes it an ideal choice for developers.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Use Mistral Medium 3 for code completion
def complete_code(prompt):
    response = router.generate(text=prompt, max_tokens=512)
    return response

# Example usage
prompt = "Complete the following code: def hello_world():"
print(complete_code(prompt))
```

#### 2. **Summarization and Content Generation**
With its strong language understanding capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks, such as article summarization, text rewriting, and content creation.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Use Mistral Medium 3 for article summarization
def summarize_article(article):
    response = router.generate(text=article, max_tokens=256)
    return response

# Example usage
article = "This is a sample article..."
print(summarize_article(article))
```

#### 3. **Vision Tasks

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
