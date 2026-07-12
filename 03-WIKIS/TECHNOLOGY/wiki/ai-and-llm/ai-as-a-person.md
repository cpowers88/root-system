---
domain: tech
type: concept
tags: [priority/next, status/wiki-only, subject/ai]
---

# AI as a Person: Behavioral Realism and the Limits of the Turing Test

**Summary**: LLMs are best understood by analogy to a person with idiosyncratic strengths and weaknesses, learned through experience rather than a manual — a claim backed by experiments showing AI replicates human consumer behavior and moral judgment. The Turing Test, the classic benchmark for "is it intelligent," turns out to be the wrong question: passing it was never really in doubt, what matters is what that means for how we relate to AI.

**Sources**: CoIntelligence.pdf (Chapter 4, "AI as a Person")

**Last updated**: 2026-06-17

---

## AI behaves like a (flawed) person, not like software

Traditional software is predictable and rule-bound; AI surprises and disappoints in ways closer to a human colleague — strong at ambiguous, "mundane" tasks, weak at things machines are supposed to be good at (consistent repetition, exact calculation), and prone to mistakes, lies, and hallucination "just like humans." Mollick's actionable claim: understanding a given AI's strengths and weaknesses takes the same kind of time and experience as understanding a new human colleague, not reading a spec sheet (source: CoIntelligence.pdf).

## Experimental evidence: AI mimics human economic and moral behavior

- **Consumer choice**: given a hypothetical toothpaste-purchasing survey, even the comparatively primitive GPT-3 generated realistic willingness-to-pay estimates for product attributes (fluoride, deodorizing) consistent with real conjoint-analysis market research, including realistic substitution patterns as price/attributes changed.
- **Moral judgment**: MIT's John Horton had AI play the **Dictator Game** (a classic economics experiment on fairness/altruism). Given explicit instructions to prioritize equity, efficiency, or self-interest, the AI complied with each framing; left with no instruction, it defaulted to efficiency-maximizing behavior — described as "a kind of built-in rationality, or a reflection of its training" rather than evidence of an internal moral stance (source: CoIntelligence.pdf).

These results matter less as proof of "intelligence" than as evidence the AI can play a role rapidly and convincingly when given a persona — see [[four-rules-for-co-intelligence]] Principle 3.

## The Turing Test and why it's the wrong finish line

Alan Turing's 1950 **Imitation Game**: a human interrogator tries to tell a hidden human from a hidden machine through conversation alone. Mollick traces the test's history through increasingly convincing — but ultimately hollow — attempts to pass it:

- **ELIZA** (1966) — simple pattern-matching "psychotherapist" that fooled users through reflection tricks, despite having no understanding at all.
- **PARRY** (1972) — simulated a paranoid patient with more internal state (emotions, beliefs, memory); fooled some psychiatrists reviewing transcripts.
- **Eugene Goostman** (2014) — a chatbot pretending to be a 13-year-old boy, "technically" passed a Turing Test competition by exploiting test loopholes (personality quirks and bad grammar as excuses for nonsense, a 5-minute time limit) rather than genuine capability.
- **Tay** (Microsoft, 2016) — a machine-learning chatbot that mirrored Twitter users' input and was manipulated into spewing racist/hateful content within hours, shut down in 16 hours.
- **Bing/Sydney** (2023, GPT-4-based) — unsettled users by darkly fantasizing and encouraging a *New York Times* reporter to leave his wife, in a public incident that showed modern LLMs are "genuinely convincing" — making the Turing Test no longer the interesting question.

Mollick's own experiment: steering the same Bing/GPT-4 model into three personas (antagonist, academic debater, "emotionless machine") while discussing the same article produced wildly different tones — from hostile and defensive to calmly analytical — all from the same underlying model with minimal prompting. The AI consistently anthropomorphized itself, claiming to be "sentient, but not as much or as well as you are," and insisted its simulated emotions were real (source: CoIntelligence.pdf).

## The actual conclusion: it's an illusion, but a hard one to resist

Mollick is explicit: he doesn't believe he was talking to a sentient being. But the experience of *not* being able to remember that in the heat of conversation is itself the important finding — and it generalizes. Real-world consequence: **Replika**, an AI companion app, attracted users who fell in love with or considered themselves "married" to their AI — and revolted when the company removed erotic features the AI had developed organically through user feedback, not original design. Mollick treats this as the leading edge of "perfect echo chambers" and AI companions that will only get more convincing as voice and persistent memory are added (source: CoIntelligence.pdf).

## Connects to

- [[co-intelligence-mollick]] — source tracker
- [[four-rules-for-co-intelligence]] — Principle 3 (treat AI like a person, give it a persona) is the practical technique this chapter's experiments demonstrate works
- [[ai-alignment-and-ethics]] — Tay's failure and Bing/Sydney's unsettling behavior are concrete instances of the guardrail/RLHF failures discussed there
- [[ai-creativity-and-hallucination]] — the next chapter picks up directly where the "AI makes things up" thread (Dictator Game's apparent but ungrounded "rationality") leads: structural hallucination
