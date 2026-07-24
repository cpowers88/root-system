---
type: source-summary
timeline: reference
status: in-progress
tags: [castle, architecture, prompt-engineering, source-intake]
source: 03-WIKIS/AI_AUTOMATION_SYSTEMS/raw/promp_engineering_generative_AI_guide.pdf
created: 2026-07-24
---

# *Prompt Engineering for Generative AI* — Chunk Intake

## Source Identity and Review Method

- **Source:** James Phoenix and Mike Taylor, *Prompt Engineering for
  Generative AI: Future-Proof Inputs for Reliable AI Outputs*, O'Reilly,
  first edition (May 2024).
- **Physical extent:** 791 PDF pages.
- **Method:** complete physical-page traversal in chapter-aware consecutive
  chunks. Findings are written after each chapter closes so extraction is
  never mistaken for reading.
- **Character:** a practitioner-tutorial book built around worked
  ChatGPT/GPT-4 and Midjourney/Stable-Diffusion examples, code (Python,
  LangChain, vector databases), and a small set of named, reused principles.
  Very high proportion of page count is worked prompt/output pairs and code
  listings rather than dense prose — durable principles are extracted from
  around this scaffolding rather than the specific example text.
- **Volatility flag:** the book is explicitly model-and-vendor-anchored to
  GPT-4, Midjourney v6, and Stable Diffusion XL/AUTOMATIC1111 as of mid-2024.
  The authors themselves flag this ("within months these models may no
  longer be state of the art") — treat named tools, prices, context-window
  sizes, and specific model comparisons as dated snapshots, not current fact.
- **Raw boundary:** the original PDF remains unchanged.

## Coverage Ledger

| Unit | Physical pages | Status |
|---|---:|---|
| Front matter, praise, preface | 1–20 | Complete |
| Chapter 1 — The Five Principles of Prompting | 21–93 | Complete — 4 chunks |
| Chapter 2 — Introduction to LLMs for Text Generation | 94–~180 (est.) | Opened, not closed |
| Chapter 3 — Standard Practices for Text Generation | est. | Pending |
| Chapter 4 — Advanced Text Generation (LangChain) | est. | Pending |
| Chapter 5 — Advanced Text Generation with Vector Databases | est. | Pending |
| Chapter 6 — Introduction to Agents | est. | Pending |
| Chapter 7 — Standard Practices for Image Generation | est. | Pending |
| Chapter 8 — Advanced Text-to-Image Techniques | est. | Pending |
| Chapter 9 — Advanced Image Generation (AUTOMATIC1111 / Stable Diffusion Web UI) | est.–791 | Pending |

Chapter page boundaries beyond Chapter 2 are estimated from cross-references
seen in Chapter 1 (Chapter 4 = LangChain, Chapter 5 = vector databases,
Chapter 6 = agents, Chapters 7–9 = image generation) and are not yet
confirmed against the actual running heads — confirm on resumption rather
than trusting this table.

## Front Matter — Physical Pages 1–20

- First edition May 2024, copyright 2024 Saxifrage LLC / Just Understanding
  Data Ltd. Authors have worked with generative AI since the GPT-3 beta
  (2020).
- The authors' explicit thesis: early prompting "tricks and hacks" decayed as
  models improved, but a smaller set of principles proved stable across both
  text and image generation and across multiple model generations — the book
  is built to teach those, not the tricks.
- Examples assume paid access (OpenAI billing enabled, Midjourney
  subscription); code targets Python 3.9 with a GitHub-hosted
  `requirements.txt`.

## Chapter 1 — Physical Pages 21–93: The Five Principles of Prompting

### The Naming Problem as a Teaching Vehicle

- The chapter opens with a naive prompt ("list product names for shoes that
  fit any size") and diagnoses five concrete failure modes: vague direction,
  unformatted output, missing examples, no evaluation, no task division. Each
  failure maps 1:1 to one of the five principles — the principles are framed
  as *fixes for observed failure classes*, not an abstract taxonomy.
- The authors are explicit that LLMs are next-token predictors with
  temperature-controlled randomness: a naive prompt returns an "average of
  the internet," and the entire discipline of prompting is about shifting
  the probability mass toward the desired output.

### The Five Principles (as named, in the book's order)

1. **Give Direction** — describe the desired style in detail, or reference a
   relevant persona/role (e.g., "in the style of Steve Jobs"). Direction is
   the broadest, most commonly needed principle; too little direction is
   named as the more common failure than too much. Role-playing applies
   equally to image models (naming an artist reliably shifts style).
   Overlapping/conflicting direction (e.g., "stock photo" + "Van Gogh") can
   exceed what the model can jointly satisfy — resolve by dropping the
   less-important element, don't expect the model to reconcile a genuine
   conflict.
2. **Specify Format** — models are "universal translators" between formats
   (JSON/YAML/Markdown/code), and format drift (e.g., numbered list vs.
   comma-separated) is harmless for one-off use but breaks production
   parsers. JSON is preferred for API/machine consumption (validate with a
   standard parser, e.g., Python's `json`); YAML is a human-readable
   alternative. A parse failure is itself a usable trigger to retry or
   escalate. Format and Direction principles can clash (a supplied base image
   fights a requested output format) — the same drop-the-lesser-priority
   rule applies.
3. **Provide Examples** — zero-shot/one-shot/few-shot terminology, citing the
   GPT-3 paper's finding that even one example can move task accuracy from
   ~10% toward ~50% for some tasks. Named trade-off: more examples increase
   reliability but *reduce* creativity/diversity of output — a few
   well-chosen, diverse examples beat many similar ones. Cited research
   (Hsieh et al., 2023) found direction often outperforms examples and
   examples are harder to source well — try Give Direction first. For image
   models, the analogous move is supplying a base image (img2img).
4. **Evaluate Quality** — without a feedback loop you're "blind prompting,"
   fine for one-off use, risky for anything reused or in production. Concrete
   evaluation ladder given, cheapest to most rigorous: informal eyeballing →
   thumbs-up/thumbs-down logging (with worked ipywidgets/pandas code:
   randomize+blind the sample before rating to avoid bias, log to CSV,
   aggregate count/mean score by prompt variant) → 3/5/10-point scales →
   pairwise/Elo-style ranking (cites Chatbot Arena/lmsys) → programmatic
   ground-truth scoring where a reference answer exists. Named non-exhaustive
   list of *what* to evaluate for: cost, latency, call count, task
   performance vs. a real feedback/physics model, classification accuracy,
   reasoning/math correctness, hallucination rate, safety, refusal rate,
   adversarial/prompt-injection robustness, and output similarity (BLEU/ROUGE
   or embedding distance). For image models, the analogous method is
   *permutation prompting*: cross a small set of directions/formats, generate
   an image per combination, and lay results out in a comparison grid.
5. **Divide Labor** — task decomposition: chain multiple, smaller AI calls
   instead of asking one prompt to do everything at once; complexity and
   convolution correlate with less deterministic output and more
   hallucination. Two decomposition patterns are named: **meta-prompting**
   (use one model call to generate/improve a second call's prompt — cites
   Zhou 2022, "LLMs are human-level prompt engineers") and simple two-step
   self-evaluation (generate, then have the model rate/critique its own
   output — e.g., product-name ratings on clarity/memorability/uniqueness).
   Chain-of-thought ("let's think step by step") is presented as the
   single-prompt version of the same decomposition principle and is shown to
   materially change (and make more internally consistent) a model's own
   self-ratings. Progressive summarization (chunk → summarize each chunk →
   summarize the summaries) is given as the foundational example of chaining
   for content that exceeds a context window.

### Landscape Context Embedded in Chapter 1 (dated, volatile)

- Frames the book's competitive landscape as OpenAI/Anthropic/large tech
  vs. open-source (Hugging Face) — as of writing, Claude 2's 100K-token
  window and GPT-4's 128K-token variant are cited as the frontier, with
  Gemini 1.5's 1M-token window as the outlier. Explicitly flagged by the
  authors themselves as likely to be stale — treat as a 2024 snapshot only.
- Frameworks named as early/immature at time of writing: ReAct, BabyAGI,
  AgentGPT, Microsoft AutoGen — "still early and prone to errors... likely to
  be part of the next stage." LangChain is named as the tooling layer for
  chaining prompts/queries (detailed in Chapter 4).

### Chapter 1 Decision Contribution

**Keep:** CASTLE's existing preference for small, reversible, evidence-first
moves maps directly onto "give direction first, add examples/decomposition
only where direction under-performs" — this source independently supports
not over-engineering a prompt/instruction before testing the simplest fix.

**Add to the synthesis queue:** a named, versioned Five-Principles-style
checklist for `.ROOT`'s own AI-instruction authoring (direction, format,
examples, evaluation, task-division) as a lightweight lint target for
instruction files; a blind/randomized rating pattern (not just "looks right
to me") as the minimum bar before calling an instruction-file change
validated; explicit note that more/longer few-shot examples trade reliability
for creativity — relevant to how prescriptive CASTLE's own templates should
be; meta-prompting and self-critique as a cheap two-call pattern worth
naming explicitly if `.ROOT` ever automates instruction-file quality checks.

**Reject as default:** treating "add more examples" as a free reliability
lever (it has a creativity cost); treating any specific model/vendor/
context-window number in this source as current; adopting agent frameworks
(ReAct/BabyAGI/AutoGen) on this source's authority — the authors' own
framing marks them as immature at time of writing, and 2024-era immaturity
claims should not be imported into a 2026 architecture decision without
re-verification against a current source.

## Chapter 2 — Physical Pages 94+ (opened, not closed)

Chapter 2, "Introduction to Large Language Models for Text Generation,"
opens with tokens/tokenization (BPE mechanics worked through the "apple"
example), word embeddings/vector representations, and begins contrasting
BERT's encoder architecture with GPT's decoder architecture (Figure 2-2).
This is foundational NLP background, not yet judged for `.ROOT`-relevant
content — no decision contribution is recorded until the chapter closes.
**Do not treat this section as evidence for or against any design question.**

## Next Exact Action

Resume at physical page 94 (Chapter 2 opening) and continue consecutive
chapter-aware chunks through Chapter 2's close, then proceed chapter by
chapter through Chapter 9. Confirm the estimated chapter/page boundaries in
the Coverage Ledger against actual running heads as they're reached.
