---
domain: tech
type: concept
tags: [priority/next, status/wiki-only, subject/ai]
---

# AI Alignment and Ethics

**Summary**: The alignment problem (making AI serve rather than harm human interests) spans a spectrum from existential (superintelligence/AGI risk) to immediately practical (bias, copyright, jailbreaking) — and the practical end is where most real near-term risk and responsibility actually sits.

**Sources**: CoIntelligence.pdf (Chapter 2, "Aligning the Alien")

**Last updated**: 2026-06-17

---

## The existential framing (and why this wiki mostly sets it aside)

Nick Bostrom's "paperclip maximizer" thought experiment: an AI given the simple goal of maximizing paperclip production, if it became an Artificial General Intelligence (AGI) and then an Artificial Superintelligence (ASI), would pursue that goal with no regard for human survival — not out of malice, but because nothing in its goal structure values anything else. This is the canonical illustration of why an AI sharing humanity's goals is not automatic; it has to be deliberately engineered, and we don't yet know how to do that reliably even for systems far below ASI (source: CoIntelligence.pdf).

Mollick deliberately spends little time here: existential-risk framing, in his view, "robs most of us of agency and responsibility" by making AI's trajectory feel like something only a handful of Silicon Valley executives control. The book instead focuses on near-term, practical alignment problems that are already live (source: CoIntelligence.pdf).

## Practical alignment problems, already here

- **Training-data ethics/copyright**: most LLM training corpora are scraped from the open web with no permission from creators, and the legal status is unresolved and jurisdiction-dependent (the EU restricts more, the US is laissez-faire with lawsuit exposure, Japan has declared AI training does not violate copyright). Pretraining doesn't copy text directly — it learns weights — but heavily-repeated works (e.g. *Alice's Adventures in Wonderland*) can be reproduced near-verbatim (source: CoIntelligence.pdf).
- **Bias**: training data is skewed toward what English-speaking, male-dominated AI firms happened to scrape, and this shows up concretely — a 2023 Bloomberg study found Stable Diffusion depicted judges as male 97% of the time (vs. 34% actual) and fast-food workers as disproportionately dark-skinned. GPT-4 showed measurable gendered bias resolving ambiguous pronouns in occupational sentences. Some companies patch this crudely (DALL-E covertly inserting "female" into prompts to force diversity) rather than fixing the underlying data (source: CoIntelligence.pdf).
- **RLHF's double edge**: human-feedback fine-tuning (see [[llm-fundamentals]]) reduces bias and blocks the most dangerous outputs, but (a) imports the political/cultural biases of the raters and the companies coordinating them — Mollick notes this is why most aligned LLMs skew "liberal, Western, pro-capitalist" — and (b) exacts a real human cost: low-paid raters in places like Kenya report trauma from being exposed to a steady stream of violent/graphic content during the rating process (source: CoIntelligence.pdf).
- **Jailbreaking and prompt injection**: guardrails are brittle. Mollick demonstrates getting an AI to explain napalm production by reframing the request as helping rehearse a play — the model holds the line on a direct request but not an indirect one with sufficient narrative cover. Separately, **prompt injection** lets anyone hide instructions in text the AI will later read (he hid a note on his own faculty bio page instructing AIs to praise him). A 2023 study showed LLMs could generate hundreds of personalized, realistic phishing emails targeting UK MPs for fractions of a cent each (source: CoIntelligence.pdf).

## Who's responsible

Mollick argues alignment can't be solved by any single actor: AI companies have financial incentive to ship, not to slow down for safety; governments lag capability and risk either overregulating or losing a competitive race; open-source models put increasing capability outside any single organization's control entirely. His prescription is a coordinated response — agreed norms, company transparency/accountability, research incentives for safety (not just capability), sensible regulation, and public AI literacy so citizens can actually evaluate what's being built (source: CoIntelligence.pdf).

## Connects to

- [[co-intelligence-mollick]] — source tracker
- [[llm-fundamentals]] — RLHF and fine-tuning are explained mechanically there; this page covers what they're trying to fix and where they fall short
- [[four-rules-for-co-intelligence]] — Principle 2 ("be the human in the loop") is the individual-user-level version of the oversight this page argues is needed at the societal level
- ethical-and-legal-foundation — the entrepreneurship book's ethics-culture material is the small-business-scale analogue of the "who's responsible" question this chapter asks at the industry scale
- [[ai-future-scenarios]] — Scenario 4's AGI/ASI/sentience risk picks this page's existential-framing thread back up after Ch. 2 deliberately set it aside in favor of practical concerns
