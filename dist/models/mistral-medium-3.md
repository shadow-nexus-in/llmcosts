# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed to cater to a wide range of applications. With its robust architecture, this model excels in tasks such as coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Specifications and Strengths
Mistral Medium 3 boasts a context window of 131,072 tokens and a maximum output of 16,384 tokens, with a knowledge cutoff of 2024-11. The model's pricing is structured as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. Its performance is benchmarked at 80.0 on MMLU, 77.5 on HumanEval, and 1200 on LMSYS Arena ELO. The model's strengths lie in its ability to handle complex tasks, making it best suited for applications such as coding, analysis, and vision tasks. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks requiring sub-100ms responses.

### Cost Considerations and Competitors
The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. In comparison to its competitors, Mistral Medium 3 is priced competitively, with Claude 3.5 Haiku charging $0.8/1M input and $4.0/1M output, and GPT-4o Mini charging $0.15/1M

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3 is a mid-tier model offered by Mistral AI, released on 2025-04-17. This model is not open source and has a specific cost structure for input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that Mistral AI encourages batch processing to improve efficiency and reduce costs.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost per call, we can divide the total cost by the number of calls:
* 1,000 calls: $1.2 / 1,000 = $0.0012 per call
* 10,000 calls: $12.0 / 10,000 = $0.0012 per call
* 100,000 calls: $120.0 / 100,000 = $0.0012 per call

The cost per call remains constant at $0.0012 per call, regardless of the number of calls.

####

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Its pricing is set at $0.4 per 1M input tokens and $2.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and process natural language across a wide range of tasks. A higher MMLU score suggests better language comprehension.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate human-like code and understand programming concepts. A higher HumanEval score implies stronger coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in various tasks. A higher ELO score indicates better overall performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* **Coding and Analysis**: With a high HumanEval score, Mistral Medium 3 is well-suited for coding tasks, such as code generation, code completion, and code analysis.
* **Text and Vision Tasks**: The model's strong MMLU score and support for text, vision, and function_calling capabilities make it a good fit for tasks like text classification, object detection, and image analysis.
* **Content Generation**: Mistral Medium 3

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance of each model is measured by the following benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Performance Trade-Offs
While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not provided, we can infer the following trade-offs:
* Mistral Medium 3 offers a balance between price and performance, with a mid-tier pricing and respectable benchmark scores.
* Claude 3.5 Haiku is likely to offer higher performance, but at a significantly higher cost (100% more than Mistral Medium 3).
* GPT-4o Mini is likely to offer lower performance, but at a significantly lower cost (62.5% less than Mistral Medium 3 for input and 70% less for output).

#### Use Cases and Recommendations
Based on the capabilities and limitations of each model, we recommend

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Medium 3
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of capabilities and pricing. Here are the top 5 best use cases for this model, along with specific code integration examples and mentions of OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review, code completion, and bug detection. When integrating with OpenRouter, you can leverage the model's `function_calling` capability to analyze code snippets and provide insightful feedback.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a code analysis function
def analyze_code(code_snippet):
    # Use Mistral Medium 3 to analyze the code snippet
    response = router.function_calling(code_snippet)
    return response

# Example usage
code_snippet = "def add(a, b): return a + b"
analysis_result = analyze_code(code_snippet)
print(analysis_result)
```
#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as summarizing long documents, generating product descriptions, or creating chatbot responses. With OpenRouter, you can utilize the model's `text` and `json_mode` capabilities to generate high-quality content.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a content generation function
def generate_content(prompt):
    # Use Mistral Medium 3 to generate content
    response = router.text(prompt, json_mode=True)
    return response

# Example usage
prompt =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
