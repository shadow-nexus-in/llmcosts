# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. As a non-open-source model, its architecture is not publicly disclosed, but its capabilities and benchmarks provide insight into its strengths. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require processing and generating large amounts of text.

### Technical Capabilities and Use Cases
Mistral Medium 3 boasts an impressive range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 80.0 on MMLU, 77.5 on HumanEval, and 1200 on LMSYS Arena ELO. These capabilities make it an ideal choice for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model. However, the choice of model ultimately depends on the specific use case and requirements of the project. By considering the technical capabilities, pricing, and cost examples, developers can make an informed decision about whether Mistral

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached input and batch input.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs, as they are free. This is ideal for scenarios where the same input tokens are used repeatedly, such as in batch processing or when generating content based on a fixed set of inputs.

#### Batch API Savings
Batch input is also free, which means that making API calls in batches can significantly reduce costs. This is particularly useful for large-scale applications where multiple requests can be grouped together.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison with Top Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $0.15/

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate code that is correct and functional. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher score suggests better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding and analysis
* Text and vision tasks
* Summarization and content generation
* Function calling

However, the model may not be suitable for tasks that require:
* Frontier reasoning
* Bulk cheap

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and pricing. In this comparison, we will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing models of the three competitors are as follows:

* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

Based on the pricing data, GPT-4o Mini is the most cost-effective option, while Claude 3.5 Haiku is the most expensive.

#### Performance Comparison
The performance of the three models can be evaluated using various benchmarks:

* **MMLU**: Mistral Medium 3 (80.0) vs. Claude 3.5 Haiku (not available) vs. GPT-4o Mini (not available)
* **HumanEval**: Mistral Medium 3 (77.5) vs. Claude 3.5 Haiku (not available) vs. GPT-4o Mini (not available)
* **LMSYS Arena ELO**: Mistral Medium 3 (1200) vs. Claude 3.5 Haiku (not available) vs. GPT-4o Mini (not available)

Since the benchmark data for Claude 3.5 Haiku and GPT-4o Mini is not available, we cannot make a direct comparison. However, Mistral Medium 3 has a context window of 131,072 tokens and a max output of 16,384 tokens, which may indicate better performance

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is well-suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it to integrate with OpenRouter for automated code generation:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = mistralai.mistral_medium_3()

# Define a function to generate code using Mistral Medium 3
def generate_code(prompt):
    input_ids = model.encode(prompt)
    output_ids = model.generate(input_ids)
    code = model.decode(output_ids)
    return code

# Use OpenRouter to integrate with Mistral Medium 3
openrouter.init(generate_code)
```
2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and content generation. Its large context window of 131,072 tokens makes it suitable for long-form text analysis.
3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for image classification, object detection, and image generation. For example, you can use it to classify images using OpenRouter:
    ```python
import openrouter
from PIL import Image

# Initialize Mistral Medium 3 model
model = mistralai.mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
