---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/data-mining, subject/adoption, subject/productization]
source_role: primary
use_cases: [tech-stack]
---

# Data Mining Adoption Chasm and Productization

## Source Status

Historical synthesis from `raw/DataMiningCrossingtheChasm.pdf`, a 35-page
presentation by Rakesh Agrawal describing IBM Quest/Intelligent Miner and the
transition from research technology to a mainstream product. The deck's exact
date is not established in the file; its XML DTD framing and product references
place it in an earlier data-mining era. Use its adoption mechanics, not its tool
or market claims, as current guidance.

## Adoption Groups Need Different Evidence

| Group | What they value | What fails with them |
|---|---|---|
| Innovators | Novel technology, access, experimentation | Expecting a complete product or strong profit |
| Early adopters | Strategic advantage and customization | Slow time to value |
| Early majority | Proven productivity, references, production fit | Research demos and specialist-only tools |
| Late majority | Complete, inexpensive, standard solutions | High integration or learning burden |
| Skeptics | Status quo and debunking hype | Abstract productivity claims |

The chasm appears between visionaries who tolerate missing pieces for advantage
and pragmatists who require evidence, integration, support, and predictable
operations. A technically successful prototype is not automatically a product.

## Quest-to-Product Lessons

The Quest research effort began from visionary needs and built scalable data-
mining operations. The original visionaries did not necessarily become the first
customers; prospects wanted proof, integration was difficult, technology looked
too specialized, and internal analytic groups resisted.

Early services engagements created the bridge:

1. apply the technology to real customer data;
2. learn which operations and outcomes matter repeatedly;
3. discover unanticipated uses and missing integration;
4. produce success evidence;
5. use those engagements to justify and shape productization;
6. combine research capabilities into a supported product.

This directly supports the Advisor-Builder productization rule: prove a pattern
through service delivery before turning it into software.

## What Mainstream Adoption Required

The deck argued for:

- embedding analytics in applications rather than leaving it stand-alone;
- coupling with existing databases and infrastructure;
- stable interfaces and portable model/data contracts;
- representative benchmarks;
- automatic parameter/algorithm selection;
- actionable delivery through the web;
- privacy-aware data handling and user control;
- domain knowledge to separate useful patterns from noise.

Many named technologies are historical, but the requirements remain recognizable:
workflow fit, interoperability, proof, reduced specialist burden, governance, and
actionability determine adoption more than algorithm novelty.

## Current Use

When evaluating an AI/data product, ask:

```text
Is this a research capability, a service-assisted solution, or a repeatable product?
What production reference proves it works in this workflow?
What integration and operating burden remains with the buyer?
Can a normal user act on the output without a specialist?
Which standards, ownership rules, and privacy controls make it portable and safe?
What service evidence justifies productization?
```

## Complete Chunk Ledger

| PDF range | Deck content | Disposition |
|---|---|---|
| 1-12 | Thesis, adoption lifecycle, chasm, visionary/pragmatist contrast | Ingested into adoption evidence table |
| 13-22 | Quest approach, services engagements, productization, Intelligent Miner, barriers | Ingested into Quest-to-product lessons |
| 23-35 | Standards, database coupling, benchmarks, automation, web, privacy, personalization, summary | Ingested as mainstream-adoption requirements with historical caveat |

## Related Pages

- [[crisp-dm-process-and-data-leakage|CRISP-DM Process and Data Leakage]]
- [[data-driven-decision-making-and-data-science-definition|Data-Driven Decision-Making]]
- [[business-experimentation-and-project-unicorn|Business Experimentation and Project Unicorn]]
