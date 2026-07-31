---
type: reference
timeline: reference
status: source-capture
title: Credits
slug: credits
description: Understand how credits work in Make, how different features consume them, and how to monitor your usage
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/aij4Le3bEHQVM9X7VLRNz_1.png
docTags: 
createdAt: 2025-08-04T07:26:09.076Z
---

:::hint{type="warning"}
Credits have replaced operations as the term for Make's billing unit. Your existing plan and pricing, including the cost of buying credits, remain unchanged. The cost of credits[ varies by plan](https://www.make.com/en/pricing).&#x20;

How credits are used:

- **Non-AI apps**: 1 operation equals 1 credit.&#x20;
- **Third-party AI apps like OpenAI, Anthropic Claude, and Gemini**: 1 operation equals 1 credit. Credits for modules with automatic AI provider connections also include token usage.&#x20;
- **Built-in AI apps:** Varies by connection type:
  - **Make’s AI Provider (all plans)**: Credits are based on tokens and operations. Make’s AI Provider is available in [Make AI Agents](docId\:MDyjgeEIIRrXMd607V1xg) and [Make AI Toolkit](docId\:CfGqHRAekfeXyGbyOW_wC).&#x20;
  - **Custom AI provider connection (paid plans)**: With custom AI provider connections, such as OpenAI or Anthropic Claude, credits are based on operations. You pay your provider directly for tokens.
  - **Automatic AI provider connection (all plans)**: [Make AI Web Search](docId\:bffuREdPz8IIQcEVE9VvX) and [Make AI Content Extractor](docId\:gV6ZATMkaRnAqCTIK1MAx) use an AI provider of Make's choice. Credits are based on tokens, operations, and other usage-based factors.
:::

In this guide to credits in Make, learn about how credits work and the different types of credit usage.&#x20;

::embed[]{url="https://www.youtube.com/watch?v=ufYhY5WgEnw"}

## **What are credits?**

Credits are the currency you buy and consume to use Make. Only features triggered by scenario runs (apps, modules, and some in-app features) or the AI agent’s chat use credits.&#x20;

Your credit usage can vary based on the number of operations, tokens, and other usage-based factors.&#x20;

:::hint{type="info"}
Credits and operations are separate terms because they serve different purposes: credits help you track how much you’re spending, and [operations](docId\:ZR2rWmILMJ_19R85MlAwM) show the outcome of your activities on the platform.&#x20;
:::

In Make, credit usage is either fixed or dynamic:

- [Fixed credit usage](docId\:hh-nrTakEqakBmg63UUiN): Apps use a set number of credits per run.&#x20;
- [Dynamic credit usage](docId\:hh-nrTakEqakBmg63UUiN): Some AI and advanced apps use a varying number of credits per run based on actual consumption.

Whether a feature has fixed or dynamic credit usage depends on its processing complexity, whether it uses AI, and the connection type.&#x20;

## Fixed credit usage

With fixed credit usage, modules consume credits based on a set rate. By default, 1 operation equals 1 credit. ﻿That rate is constant regardless of input or data transfer size. Most apps consume credits on a fixed basis.

For example, running the **Google Drive&#x20;**> **Upload a File** module always uses 1 credit per file upload, regardless of the file size.&#x20;

**Exceptions**

Some [Make AI Content Extractor](docId\:gV6ZATMkaRnAqCTIK1MAx) modules with fixed credit usage consume more than the default 1 credit per operation due to their processing complexity.&#x20;

Features using more than the default 1 credit have a unique tag. In the example below, the modules consume 2 or 10 credits per operation.

::Image[]{src="https://app.archbee.com/api/optimize/oAyFj2GHlBeBVWF5OAir2/sB2AteiLPcczpbbHlxLbb-20250916-134543.png" size="60" width="535" height="430" position="center" darkWidth="535" darkHeight="430" showCaption="false"}

You can find detailed examples of fixed credit usage in [Credits by module type](docId\:LZASgxrjtBcJOk6vF0RKR).

## Dynamic credit usage

With dynamic credit usage, modules consume a different number of credits per run based on actual usage rather than a fixed rate.&#x20;

The most common factor affecting credit usage is token consumption. Tokens are the unit that AI providers use to measure and charge for usage. They vary depending on the amount of information processed: more interactions, longer prompts, larger files, and longer responses all increase token usage. In English, [1 token equals around 4 characters](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them), and 100 tokens equal about a paragraph.&#x20;

Other factors that can determine credit usage include file size, page count, or processing time.

Features with dynamic credit usage have unique tags:

- **Tokens:** Credits based on tokens and/or embedding tokens consumed (and operations in some cases)
- **File size:** Credits based on file size processed
- **Per page:** Credits based on pages processed
- **Run time:** Credits based on processing time

In the example below, the modules use credits based on tokens.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/Q31995ot4OZzZRNwsMBrJ-HvnGTUzKzYLk24J1PHdF8-20250827-093443.png" size="50" width="539" height="439" position="center" showCaption="false"}

For a list of all dynamic credit usage features, see [Credits by feature](docId\:LZASgxrjtBcJOk6vF0RKR).

## Credit usage for AI features

When you use **third-party AI app modules that require you to create a connection,&#x20;**&#x73;uch as Anthropic Claude or OpenAI, you pay Make for credits based on operations and your AI provider for tokens.&#x20;

Make's **built-in AI apps** and **third-party AI app modules that don't require creating a connection** can follow a different credit usage logic. They include the following apps:

- [Make AI Agents](docId\:MDyjgeEIIRrXMd607V1xg)
- [Make AI Toolkit](docId\:CfGqHRAekfeXyGbyOW_wC)
- [Make AI Web Search](docId\:bffuREdPz8IIQcEVE9VvX)
- [Make AI Content Extractor](docId\:gV6ZATMkaRnAqCTIK1MAx)
- The **Simple Text Prompt&#x20;**&#x6D;odule in [OpenAI](https://apps.make.com/openai-modules#KZlO8), [Google Gemini AI](https://apps.make.com/gemini-ai#ntuH-), [Groq](https://apps.make.com/groq#tncyO), and [Anthropic Claude](https://apps.make.com/anthropic-claude#ilAhA) apps.&#x20;

These apps consume credits differently based on their connection type:

- **Make's AI Provider**: Credits are based on operations and tokens.
- **Custom AI provider connection**: You pay Make for credits based on operations, and the AI provider for tokens.&#x20;
- **Automatic AI provider connection**: In apps without an option to select an AI provider, credits are based on tokens, operations, and other usage-based factors.&#x20;

### **Make's AI Provider**

Make's AI Provider is available to users on all plans in **Make AI Agents** and **Make AI Toolkit**.&#x20;

With Make's AI Provider, Make handles the connection to an AI provider for you. You don't need to create an account with providers like OpenAI or Anthropic. You pay Make for credits used based on tokens and operations.&#x20;

Choose between Make's tiered models (Small, Medium, and Large) or models from providers like OpenAI and Anthropic Claude.&#x20;

:::ExpandableHeading
**Token usage with Make's AI Provider**

When you use Make's AI Provider, credits vary based on two factors: the tokens consumed and the model selected. Each model uses credits based on the number of input tokens (from the prompt) and output tokens (from the response) consumed in each scenario run.

After a run, you can view the tokens used in that run in a module's output bubble.

**Small, Medium, and Large**

| **Model tier** | **Model**                              | **Tokens**              |
| -------------- | -------------------------------------- | ----------------------- |
| Small          | GPT-5 nano &#xA;with minimal reasoning | 5,000 tokens per credit |
| Medium         | GPT-5 nano&#xA;with low reasoning      | 3,500 tokens per credit |
| Large          | GPT-5 mini                             | 1,500 tokens per credit |

**All other models**

| **AI provider**  | **Model**                                     | **Input tokens**         | **Output tokens**       |
| ---------------- | --------------------------------------------- | ------------------------ | ----------------------- |
| OpenAI           | GPT-5.4 nano                                  | 4,520 tokens per credit  | 723 tokens per credit   |
| OpenAI           | GPT-5.4 mini                                  | 1,205 tokens per credit  | 200 tokens per credit   |
| OpenAI           | GPT-5.4 with up to&#xA;272,000-token context  | 361 tokens per credit    | 60 tokens per credit    |
| OpenAI           | GPT-5.4 with over&#xA;272,000-token context   | 180 tokens per credit    | 40 tokens per credit    |
| OpenAI           | GPT-5.2                                       | 516 tokens per credit    | 64 tokens per credit    |
| OpenAI           | GPT-5.1                                       | 723 tokens per credit    | 90 tokens per credit    |
| OpenAI           | GPT-5                                         | 723 tokens per credit    | 90 tokens per credit    |
| OpenAI           | GPT-5 mini                                    | 3,616 tokens per credit  | 452 tokens per credit   |
| OpenAI           | GPT-5 nano                                    | 18,080 tokens per credit | 2,260 tokens per credit |
| Anthropic Claude | Opus 4.6                                      | 181 tokens per credit    | 36 tokens per credit    |
| Anthropic Claude | Opus 4.5                                      | 181 tokens per credit    | 36 tokens per credit    |
| Anthropic Claude | Haiku 4.5                                     | 904 tokens per credit    | 181 tokens per credit   |
| Anthropic Claude | Sonnet 4.5                                    | 301 tokens per credit    | 60 tokens per credit    |
:::

:::hint{type="info"}
The models used for Make's AI Provider and their token-to-credit conversion rates are subject to change as newer models become available.&#x20;
:::

### Custom AI provider connection

Custom AI provider connections are available to users on paid plans. &#x20;

You can select from custom AI provider connections like OpenAI, Anthropic, and Gemini to link to your accounts with these providers, using API keys and other methods. You pay Make for credit usage based on operations, and pay your AI provider for token usage.

### Automatic AI provider connection

Some AI features don't provide an option to select and create a connection to an AI provider. They connect automatically to one, so you don't need to set up an account with a provider. You pay Make for credits based on tokens, operations, and other usage-based factors.

These features include:

- [Make AI Web Search](docId\:bffuREdPz8IIQcEVE9VvX)
- [Make AI Content Extractor](docId\:gV6ZATMkaRnAqCTIK1MAx)
- &#x20;The **Simple Text Prompt&#x20;**&#x6D;odule in [OpenAI](https://apps.make.com/openai-modules#KZlO8), [Google Gemini AI](https://apps.make.com/gemini-ai#ntuH-), [Groq](https://apps.make.com/groq#tncyO), and [Anthropic Claude](https://apps.make.com/anthropic-claude#ilAhA) apps

For more information on the credit usage of any of the features mentioned, including credit-to-tokens conversion rates, refer to their documentation.&#x20;



## **Buying extra credits&#x20;**

If you run out of credits before the next billing cycle starts, you can upgrade your subscription, buy extra credits, or enable extra credits auto-purchasing. To learn more about these options, refer to [Extra credits](docId:2ZcWIdBk-UaMtP2X2_7kj).
