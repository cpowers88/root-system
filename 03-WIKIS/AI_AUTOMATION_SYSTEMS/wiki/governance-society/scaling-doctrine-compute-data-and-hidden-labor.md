---
type: research
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, scaling, compute, training-data, labor, supply-chain, governance, evaluation, historical]
---

# Scaling Doctrine: Compute, Data, and Hidden Labor

**Summary**: Scaling laws turned frontier-model development into a predictable
capital-allocation strategy: more parameters, data, and compute could buy measurable
performance gains. That predictability attracted capital and produced GPT-scale
systems, but it also moved risk into the supply chain. More compute requires
specialized chips, cloud infrastructure, energy, and money; more data lowers
consent and quality barriers; broader data then requires more hidden human labor
to filter outputs. Model capability and externalized cost scale together unless
each input is governed explicitly.

**Source**: `raw/empireofAIDreamsandNightmares.pdf` (Karen Hao, *Empire of AI*,
2025), Chapter 5, “Scale of Ambition” (physical PDF pp. 119-138), reviewed as one
complete dense chapter chunk. Physical p. 139 is the Part II divider and Chapter 6
begins p. 140; boundaries visually verified.

**Last updated**: 2026-07-16

## Scaling Became Strategy

OpenAI's scaling thesis combined three observations:

- simple neural architectures could improve with more capacity;
- model loss changed smoothly with parameters, training data, and compute;
- those curves could forecast the resources needed for a target performance.

This made research legible to investors and infrastructure planners. Instead of
waiting for an unpredictable conceptual breakthrough, an organization could fund
a larger run and expect a measurable gain. GPT-1, GPT-2, and GPT-3 provided
increasingly persuasive demonstrations of that strategy.

The error is to turn an empirical regularity into a universal doctrine. A scaling
curve measures performance on selected objectives within a model family. It does
not prove that the system understands, that its data is lawful or representative,
that its outputs are safe, or that further scale is the best use of resources.

## The Frontier Supply Chain

```text
desired benchmark gain
  -> larger model and training run
  -> more GPUs and longer runtime
  -> cloud/chip/vendor dependency
  -> more capital and commercialization pressure
  -> larger training corpus
  -> lower provenance and quality thresholds
  -> more harmful/low-quality material
  -> more filtering, moderation, and preference labor
  -> external human and environmental cost
```

The Microsoft partnership supplied OpenAI with capital and a ten-thousand-GPU
supercomputer while making Azure its exclusive infrastructure. The arrangement
advanced capability and created mutual lock-in: OpenAI needed compute; Microsoft
needed frontier AI to close its infrastructure and product gap.

## Data Quantity Changes Data Governance

GPT-2 used a relatively selective web corpus. GPT-3 required far more data and
added Wikipedia, books, Reddit-linked material, and filtered Common Crawl. Later
runs broadened collection further. Hao reports alleged use of pirated book sources
and other scraped material; these claims are part of the book's sourced account and
should be checked against litigation and primary documentation before external
reuse.

The durable pattern is independent of any one dataset:

- quantity pressure weakens provenance review;
- absence of an explicit no-scrape signal is treated as permission;
- dataset composition becomes less knowable as scale grows;
- low-quality and hateful material rises with indiscriminate collection;
- output filtering is asked to compensate for input-governance failure.

## Hidden Labor Is Part of the Model

Large models do not emerge from compute and data alone. Contractors label,
compare, moderate, redact, and evaluate model behavior. When the corpus expands
from curated material to an internet-scale data swamp, the labor changes from
ordinary categorization to repeated exposure to violent, sexual, hateful, or self-
harm content.

RLHF and moderation may improve the product while concealing who absorbs the
cost. Any model inventory that records only architecture and benchmark scores is
therefore incomplete. Labor conditions, geography, pay, psychological exposure,
appeal mechanisms, and vendor chains are system properties.

## Scaling Review Gate

Before funding or adopting a larger model, require answers to:

1. Which deployed outcome improves with scale, and by how much?
2. Could better data, retrieval, tools, workflow design, or a smaller model achieve
   the same result?
3. What are the compute, energy, water, and infrastructure dependencies?
4. Can every major data source be named, licensed, removed, and audited?
5. What human work prepared and evaluated the model, under what conditions?
6. Does the safety method prevent harmful behavior or merely filter it after
   generation?
7. Does investor or vendor dependency change release timing or risk tolerance?

## Connects To

- [[enterprise-ai-adoption-and-production-roadmap]] - requires bounded value and
  evaluation evidence before expanding scale.
- [[openai-evals-and-red-teaming]] - each scaling and architecture change adds
  failure modes needing separate evaluation.
- [[reward-shaping-curiosity-and-safe-exploration]] - optimizing a measurable
  curve can displace the real objective.
- [[agentic-ai-industry-adoption-barriers]] - proprietary context, verification,
  and confidentiality remain deployment bottlenecks despite frontier scale.

## Limits and Next Source Chunk

This page covers the formation of the scaling system through Part I. Later parts
of the book contain the fuller labor, environmental, commercial, and governance
consequences; those remain a named chunk backlog and should update this page or
spawn a distinct supply-chain page only where the retrieval job differs.
