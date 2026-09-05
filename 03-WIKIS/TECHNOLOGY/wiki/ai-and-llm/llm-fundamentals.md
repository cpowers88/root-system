---
domain: tech
type: concept
tags: [subject/ai]
timeline: now
status: wiki-only
---

# LLM Fundamentals: Pretraining, Fine-Tuning, and Emergence

**Summary**: What a Large Language Model actually is mechanically (a next-token predictor trained in two stages), and the two phenomena that make LLMs behave unlike traditional software — emergence and the "jagged" shape of their capabilities.

**Sources**: CoIntelligence.pdf (Chapter 1, "Creating Alien Minds")

**Last updated**: 2026-06-17

---

## What an LLM does, mechanically

Despite the hype, an LLM like ChatGPT is doing one thing: predicting the next token (a word or part of a word) given the text so far, then repeating that prediction one token at a time. It is "a very elaborate autocomplete." Where this gets powerful is scale — the original ChatGPT ran on 175 billion **weights**, learned parameters that encode statistical relationships between tokens, and no human programmed any individual weight (source: CoIntelligence.pdf).

LLMs are built in two stages:

1. **Pretraining** — unsupervised learning on a massive, largely uncurated text corpus (web pages, books, code, even oddities like the leaked Enron email corpus and amateur fiction). The model has no labeled "correct answers," just raw text to predict from. This stage is what costs over $100 million in compute for frontier models, and it produces a model with no ethical boundaries — it reflects back whatever was in its training data, including bias, error, and instructions for harm if asked (source: CoIntelligence.pdf).
2. **Fine-tuning**, most commonly via **Reinforcement Learning from Human Feedback (RLHF)** — human raters (often low-paid contract workers) score model outputs, and that feedback further trains the model to prefer "good" answers and avoid "bad" ones. This is what turns a raw pretrained model into something usable and (relatively) safe. See [[ai-alignment-and-ethics]] for the costs and limits of this process.

The Transformer architecture (Google, 2017, "Attention Is All You Need") made this practical by adding an **attention mechanism** — letting the model weigh which earlier words in a passage matter most for predicting the next one, instead of just reading left-to-right mechanically. This is the architectural shift that separates LLMs from earlier, clearly-robotic text generators like Markov chains (source: CoIntelligence.pdf).

## Emergence: capabilities nobody programmed in

Frontier LLMs display **emergence** — abilities (chess, empathy, multi-step reasoning, creative problem-solving) that were never explicitly trained for and that scientists don't fully understand the origin of. Mollick cites NYU's Sam Bowman: with hundreds of billions of internal connections invoked repeatedly per response, "any attempt at a precise explanation of an LLM's behavior is doomed to be too complex for any human to understand" (source: CoIntelligence.pdf). This is the core reason LLMs don't behave like traditional software: traditional software is predictable because a human designed every rule; LLMs develop capabilities nobody designed.

## The Jagged Frontier

Capability is not evenly distributed across tasks that look similarly difficult to a human. Mollick's example: GPT-4 can pass the bar exam and ace AP Calculus, but fails a trivial tic-tac-toe puzzle that any child could solve — while writing a flawless tic-tac-toe *program*. There is no way to predict in advance which side of this invisible boundary (the "Jagged Frontier") a given task falls on; you have to test it directly (source: CoIntelligence.pdf). This is elaborated as Principle 1 in [[four-rules-for-co-intelligence]].

## Connects to

- [[co-intelligence-mollick]] — source tracker
- [[ai-alignment-and-ethics]] — what fine-tuning is actually trying to fix, and where it falls short
- [[four-rules-for-co-intelligence]] — the Jagged Frontier is the direct justification for "always invite AI to the table" and experiment task-by-task
- [[theory-of-constraints]] — like a production system's bottleneck, an LLM's real limits can't be reasoned out abstractly; both require direct, empirical probing of the actual system rather than assumptions about how it "should" behave
- [[ai-developer-tools-landscape-2026]] — "hallucinated code" flagged there as a tool risk is this page's hallucination phenomenon, just observed at the application layer instead of the model layer
