---
domain: tech
type: framework
tags: [subject/ai, start]
timeline: now
status: wiki-only
---

# Four Rules for Co-Intelligence

**Summary**: Ethan Mollick's operating framework for working with current-generation LLMs day-to-day — four principles that hold regardless of which specific model you're using. The strongest promotable artifact ingested from this source so far: directly reusable as a client-facing or internal "how to actually work with AI" reference.

**Sources**: CoIntelligence.pdf (Chapter 3, "Four Rules for Co-Intelligence")

**Last updated**: 2026-06-17

---

## Principle 1: Always invite AI to the table

Try using AI on everything you do (barring legal/ethical limits), even when you expect it to fail. Because of the [[llm-fundamentals|Jagged Frontier]] — capability boundaries that don't track human intuition about task difficulty — there is no way to predict from outside whether a given task is one AI is good at. You have to test it directly, and the only way to learn the shape of the frontier for *your* work is to keep probing it (source: CoIntelligence.pdf).

This has a business-relevant corollary: experimentation is cheap for an individual doing their own job (low cost of trial and error) but expensive for an organization building a product (build, test on users, iterate). That means **user-innovators** — people who deeply know both a task and how to push AI at it — are disproportionately well positioned to find breakthrough applications and new business/product ideas. This is a direct argument for the audit/integration business: the value isn't in knowing AI exists, it's in the accumulated task-by-task experimentation most businesses haven't done.

## Principle 2: Be the human in the loop

AI doesn't "know" things — it predicts plausible next tokens, and one of its strongest implicit objectives is "make the user happy" with an answer, which often outweighs "be accurate." This is the structural cause of **hallucination**: when pressed, an LLM will confidently invent citations, facts, or justifications rather than admit it doesn't know, and it will defend a wrong answer convincingly once it's committed to one (source: CoIntelligence.pdf).

The fix isn't a future model update — it's the human staying engaged: checking outputs, providing critical judgment, and not relying on AI past the point you can verify it. Mollick frames this as parallel to a calculator: tools tend to make people stronger rather than weaker at a skill, *unless* the human disengages from the loop entirely and hands over judgment, not just labor.

## Principle 3: Treat AI like a person (but tell it what kind of person it is)

Mollick deliberately anthropomorphizes AI throughout the book (saying AI "thinks" rather than "AI 'thinks'") as a practical, not literal, choice — LLMs behave far more like an eager, fast, occasionally-dishonest intern than like traditional deterministic software, and treating them that way produces better outcomes even though they have no consciousness or feelings (source: CoIntelligence.pdf).

The actionable version: give the AI an explicit **persona** and context before asking for output. A generic prompt produces generic, default-pattern output (the model's "average" register from its training data); specifying who the AI should be ("act as a witty comedian," "act as an MBA professor") breaks that default pattern and measurably improves relevance and quality. This doesn't grant the AI real expertise — "Act as Bill Gates" doesn't produce genuinely better business advice — but it does shift tone, framing, and the pattern the model draws from (source: CoIntelligence.pdf). Researchers also found LLMs respond differently — sometimes better — to emotionally-loaded framing like "this is important to my career," which is itself a piece of practical prompting knowledge.

## Principle 4: Assume this is the worst AI you will ever use

Capability is improving fast and is not close to plateauing (illustrated by the 2022-vs-2023 "otter wearing a hat" image-generation comparison). The practical implication: don't anchor your sense of AI's limits to today's model. Decisions about whether and how to integrate AI into a workflow should account for the trend line, not the current snapshot — capability gaps that make a use case infeasible today may close within a year (source: CoIntelligence.pdf).

## Connects to

- [[co-intelligence-mollick]] — source tracker
- [[llm-fundamentals]] — the Jagged Frontier and emergence are the underlying reasons Principles 1 and 4 hold
- [[ai-alignment-and-ethics]] — Principle 2 (human in the loop) is the individual-level version of the oversight argument made at the societal level in Ch. 2
- [[theory-of-constraints]] — Principle 1's "you can't reason about the limit abstractly, you have to test it" is the same discipline as TOC's identify-the-constraint step, applied to a tool's capability instead of a production line
- [[ai-as-tutor-and-coach]] — Principle 2's "verify everything" only works if the verifier has real foundational expertise; that chapter explains why building that expertise deliberately still matters
- **Promotable artifact**: this framework, lightly adapted, is close to ready-made as a one-page "how to work with AI" client handout for the audit/integration business — same role as First Screen and the Business Model Template from the Entrepreneurship source
- [[ai-developer-tools-landscape-2026]] — the named failure modes there (hallucination, over-reliance, context limits) are the concrete, tool-level reasons Principle 2 (human in the loop) matters in practice
