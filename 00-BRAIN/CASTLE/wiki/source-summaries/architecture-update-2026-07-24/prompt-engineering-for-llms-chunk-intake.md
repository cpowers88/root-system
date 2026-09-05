---
type: source-summary
timeline: reference
status: complete
tags: [castle, architecture, prompt-engineering, markdown, source-intake]
source: 03-WIKIS/AI_AUTOMATION_SYSTEMS/raw/Prompt_engineering_LLMs.pdf
created: 2026-07-24
---

# *Prompt Engineering for LLMs* — Chunk Intake

## Source Identity and Review Method

- **Source:** John Berryman and Albert Ziegler, *Prompt Engineering for LLMs:
  The Art and Science of Building Large Language Model-Based Applications*,
  O'Reilly, first edition (November 2025; copyright 2025). Both authors were
  founding/early engineers on GitHub Copilot.
- **Physical extent:** 282 PDF pages.
- **Method:** complete physical-page traversal in chapter-aware consecutive
  chunks. Findings recorded after each chapter closes so extraction is never
  mistaken for reading.
- **Character:** practitioner synthesis from the team that shipped one of the
  first industrial-scale LLM products. Explanatory framing (the "Little Red
  Riding Hood principle," the "playwriting" metaphor) is original to this book
  and durable; specific model names, prices, and context-window sizes are
  dated to late 2024/2025 and volatile.
- **Raw boundary:** the original PDF remains unchanged.

## Coverage Ledger

| Unit | Physical pages | Status |
|---|---:|---|
| Front matter and preface | 1–20 (PDF) | Complete |
| Part I / Ch.1 — Introduction to Prompt Engineering | printed 1–13 | Complete |
| Ch.2 — Understanding LLMs | printed 15–43 | Complete |
| Ch.3 — Moving to Chat | printed 45–64 | Complete |
| Ch.4 — Designing LLM Applications | printed 65–83 | Complete |
| Ch.5 — Prompt Content | printed 87–121 | Complete |
| Ch.6 — Assembling the Prompt | printed 123–146 | Complete |
| Ch.7 — Taming the Model | printed 147–166 | Complete |
| Ch.8 — Conversational Agency | printed 169–197 | Complete |
| Ch.9 — LLM Workflows | printed 199–221 | Complete |
| Ch.10 — Evaluating LLM Applications | printed 223–243 | Complete |
| Ch.11 — Looking Ahead | printed 245–252 | Complete |
| Index | printed 253–262 | Not applicable (reference index, no findings) |

**All 282 physical pages traversed. Book intake complete.**

Note: this book's "physical pages" in the ledger above are the printed page
numbers stamped on each page (distinct from raw PDF page indices, which run
~18 higher due to cover/TOC/preface front matter).

## Front Matter — Preface

- Central thesis, stated explicitly and repeated as the book's organizing
  principle: "At their core, LLMs are just text completion engines that mimic
  the text they see during training." Every technique in the book is framed as
  a consequence of this one fact.
- Three-part structure: foundations (how LLMs/chat/tools actually work),
  core techniques (sourcing content, assembling prompts, controlling
  completions), and advanced craft (agents, workflows, evaluation).

## Chapter 1 — Introduction to Prompt Engineering (printed 1–13)

- History arc: seq2seq (information-bottleneck decoder) → attention →
  transformer (2017) → GPT (2018, decoder-only, pretrain+finetune) → GPT-2/3
  (few-shot emergent capability, the actual birth of prompt engineering as a
  discipline) → ChatGPT/RLHF.
- Defines four escalating sophistication levels of prompt engineering: (1)
  thin wrapper around raw user input; (2) augmenting/modifying user input with
  retrieved context; (3) stateful, multi-turn interaction; (4) tool-using,
  agentic applications with autonomy over goals. This ladder is a clean,
  reusable framework for classifying any given LLM feature's maturity.
- Explicit non-fabrication test worth carrying into CASTLE evaluation
  practice: "Could a human expert who knows all the relevant general knowledge
  by heart complete the prompt in a single go without backtracking, editing,
  or note-taking?" — a fast sanity check for whether a capability is realistic
  to ask of a single-pass LLM call.

## Chapter 2 — Understanding LLMs (printed 15–43)

- LLMs are trained to mimic their training set's statistical continuation
  patterns, not to answer questions; the practical corollary is "don't ask how
  a reasonable person would reply — ask what a document starting with this
  prompt would most likely continue with."
- **Truth bias:** an LLM completing a prompt tends to assume the prompt's
  premises are true and will rarely self-correct a false premise mid-document,
  because self-correcting documents are rare in training data. This cuts both
  ways: it enables deliberate counterfactual/hypothetical framing, but it is a
  concrete hazard for any programmatically constructed prompt that might
  contain an unintended false or nonsensical claim — the model will not flag
  it.
- Tokenization creates three durable, model-agnostic failure classes worth
  encoding as a design checklist: (1) deterministic tokenizers make typos
  visible as broken token sequences but make sub-token manipulation (letter
  reversal, counting letters, capitalization transforms) unreliable — push
  these operations to pre/post-processing instead of asking the model to do
  them; (2) autoregressive, one-token-at-a-time generation means the model
  cannot pause, backtrack, or silently revise a token already emitted —
  mistake-correction must be supplied by the surrounding application, not
  expected from the model; (3) this same one-token-at-a-time constraint is why
  chain-of-thought works at all — a model has no internal monologue, so
  "thinking" only happens by literally writing tokens the subsequent
  generation can then condition on.
- Autoregressive generation is also why models can fall into repetition
  traps (each token in a pattern makes continuing the pattern more likely than
  breaking it) — mitigation is detect-and-filter or temperature-based
  randomization, not a prompt instruction.
- Temperature is a documented, actionable spectrum, not a single "creativity"
  dial: 0 for correctness/determinism-sensitive single answers; 0.1–0.4 for a
  small nudge toward an alternative when the top token isn't much more likely;
  0.5–0.7 when many independent varied solutions are wanted; 1.0 to mirror the
  true training-set distribution; >1 only for deliberately "weirder than
  training data" output. High temperature degrades over a long generation
  because the model starts mimicking the errors it just emitted as if they
  were part of the pattern — a compounding-error dynamic, not a one-off
  glitch.
- The transformer's attention mechanism is presented as a strict directional
  constraint with architecture-level consequences: information only flows
  left-to-right (backward) and bottom-to-top through layers (a fixed number of
  "reasoning steps" per generated token, "dumbward" per this book's term).
  This is the mechanical reason a single LLM call cannot do open-ended
  multi-hop reasoning without either enough layers or an externally-imposed
  multi-step (chain-of-thought / multi-call) structure.

## Chapter 3 — Moving to Chat (printed 45–64)

- Base models are unsafe and format-unpredictable for direct application use:
  equally capable of completing benign or harmful documents, and prone to
  completing a question with more questions rather than an answer, since raw
  internet text rarely has that structure.
- RLHF pipeline documented as base model → supervised fine-tuning (SFT, ~13k
  hand-authored documents) → reward model (trained on ~33k human-ranked
  completion pairs) → PPO-optimized RLHF model constrained to not diverge far
  from SFT output. This is dated, GPT-3-era data (2023 paper), presented as an
  illustrative mechanism, not current industry practice — treat exact document
  counts as historical, not current.
- **HHH alignment** (helpful, honest, harmless) is the named target property
  set. Notable non-obvious finding: honesty is the hardest of the three to
  train via imitation, because a human labeler writing an "ideal" completion
  cannot know exactly what the base model does or doesn't already know —
  labelers either supply answers exceeding the model's actual knowledge
  (teaching confident fabrication) or hedge on things the model is actually
  certain of (teaching false uncertainty). RLHF's reward-model step partially
  escapes this because the reward model ranks the *SFT model's own*
  completions rather than human-authored ones, so the training signal is
  keyed to the model's actual internal knowledge boundary rather than a human
  labeler's guess at it.
- **Alignment tax:** RLHF-style tuning toward helpful/honest/harmless can
  measurably reduce raw task capability on some natural-language tasks;
  mitigated in practice by mixing original base-model training data back in
  during alignment tuning.
- ChatML (or equivalent chat-formatting layers) is presented as a genuine
  architecture control, not cosmetic: because the special role/turn-boundary
  tokens are reserved and stripped from user-supplied text before assembly,
  a user cannot inject literal `<|im_start|>`-style control tokens into the
  conversation — a concrete, load-bearing example of how format-level
  separation (not prompt wording) is what prevents a whole class of prompt
  injection. Direct, explicit finding for CASTLE: **never let user-controlled
  content be concatenated into the system/instruction message** — doing so
  reopens exactly the injection surface the chat-format boundary exists to
  close.
- Comparative loss from moving to fine-tuned chat/instruct models versus raw
  completion: degraded raw-capability edge cases (an aging-out "alignment
  tax"), loss of fine control over exact output boundaries (chat models chat
  around an answer instead of stopping exactly at it), and loss of "the
  breadth of human diversity" in completions (RLHF-trained assistants are
  uniformly polite by design, which is sometimes the wrong tool — e.g.,
  generating deliberately raw/unfiltered natural-language sample data, or
  domains like law enforcement/medicine where an assistant refusing to discuss
  a topic is actively unhelpful).
- **"Prompt engineering as playwriting"** — a durable framing device: the
  chat transcript the model sees (system/user/assistant/tool turns) is a
  *different conversation* than the one the human end-user experiences, and
  it is authored by multiple "playwrights" simultaneously (the prompt
  engineer's boilerplate, the human user's actual words, the model's own
  generated turns, and any external API/tool results spliced in). Useful
  vocabulary for CASTLE instruction design: separate "what the human said" from
  "what the model was shown," since an application routinely fabricates
  synthetic user/assistant turns the end user never sees.

## Chapter 4 — Designing LLM Applications (printed 65–83)

- The application is formally a transformation **loop**: user problem →
  (feedforward pass) → prompt → completion → (transform back) → solution/UI
  update. A single request/response is the degenerate one-iteration case; chat
  is the loop run repeatedly with retained state; agentic workflows are the
  loop with internal branching and an embedded tool-execution sub-loop.
- Four simultaneous criteria a well-built prompt must satisfy, stated as a
  checklist: (1) closely resembles training-set document shape ("Little Red
  Riding Hood principle" — don't stray from the path the model was trained
  on); (2) includes all information actually needed to solve the problem; (3)
  leads the model toward generating a solution rather than more elaboration
  of the problem; (4) has a well-defined stopping point. For completion-style
  (non-chat) models, criteria 3 and 4 require deliberate engineering (a
  worked homework-style example, a `stop` sequence anchored to a predictable
  markdown structure like `\n#`); chat-tuned models satisfy 3 and 4
  "for free" via their fine-tuning, at the cost of the application author
  losing fine control over exactly where the response ends.
- Feedforward pass is decomposed into four named stages: context retrieval →
  snippetization → snippet scoring/prioritizing → prompt assembly. This maps
  directly onto CASTLE's return-path vocabulary and is a candidate common
  frame for describing any wiki's intake pipeline.
- Complexity dimensions that push an application beyond the single-pass case:
  more persisted state (conversation memory, truncation/summarization when it
  overflows budget), more external context (RAG — retrieval augmented
  generation, against a search index built over material unavailable at
  training time), deeper reasoning (chain-of-thought — forcing the "thinking"
  into visible generated tokens since the model has no internal monologue),
  and tool/agency loops (the model choosing when and how to call external,
  effectful APIs).
- **Evaluation is explicitly bifurcated:** offline evaluation (pre-ship,
  simulated proxies for user satisfaction — for code, "does the test suite
  still pass" is a strong proxy; for open-ended text, LLM-as-judge or human
  review) versus online evaluation (post-ship telemetry). Two sharp negative
  findings worth preserving: (a) explicit user feedback (thumbs up/down) is
  systematically biased — low response rate, skewed toward frustrated users —
  and should not be trusted as a primary quality signal; (b) implicit
  behavioral signals (e.g., Copilot's chosen key metric, completion
  *acceptance rate*) must be chosen because they are shown to correlate with
  the actual outcome that matters (user productivity), not because they are
  easy to log — a metric with no demonstrated link to the real outcome is a
  vanity metric regardless of how "behavioral" it looks.

## Chapter 5 — Prompt Content (printed 87–102, in progress)

- Core distinction: **static content** (task-invariant — instructions,
  clarifications, boilerplate, few-shot examples) versus **dynamic content**
  (instance-specific — the actual user/task context, different every call).
  The line is sometimes genuinely ambiguous and the book concedes this; the
  practical resolution is "hardcoded text in your application is static,
  anything pulled from a variable source is dynamic/context."
- Explicit-instruction guidance: phrase rules positively ("do X") rather
  than as prohibitions, give a reason rather than a bare command, and avoid
  absolutes — the claimed reasoning is that these forms are simply more
  common in the training distribution the model was fine-tuned to follow, not
  a claim about model "understanding." No source citation is given for this
  specific guidance in the chapter; treat as the authors' practitioner
  opinion, not an established finding.
- Few-shot prompting is presented as implicit instruction with three named,
  concrete drawbacks, each independently useful as a checklist for any CASTLE
  prompt/template design that embeds examples: (1) **scales poorly with
  growing context** — many verbose per-user examples can blow the prompt
  budget and get confusing even to a human reader, so few-shot is best suited
  to clarifying one narrow aspect (e.g., output format) rather than the whole
  task; (2) **anchoring bias** — the numeric/qualitative range spanned by the
  examples itself teaches the model an implied distribution (e.g., examples
  of "old" names skew all associated years earlier), so examples should
  deliberately span the *actual* expected range, including edge cases,
  rather than only "typical" cases; (3) **spurious incidental patterns** —
  unintentional structure in the example *order* (ascending numbers,
  "easy cases first, hard cases/failures last") gets picked up and continued
  by the model as if it were a rule, so example order should be deliberately
  randomized/shuffled unless the order itself is the intended lesson.
- Dynamic-context gathering is scoped by three practical constraints:
  **latency** (how much time the feedforward pass actually has, tied to what
  triggers it — background/non-user-facing calls can afford slow, thorough
  retrieval; live typing-assistance cannot), **preparability** (can a piece of
  context be computed/cached in advance of the request that needs it), and
  **comparability** (once gathered, candidate context snippets need a scoring
  method — priority tiers plus within-tier scores — to be triaged into the
  token budget; this scoring/triage step is deferred to Chapter 6 in the
  source).

## Chapter 5 (concluded, printed 102–121)

- RAG's core mechanism formalized: retrieval is a search problem over
  snippetized documents, scored by relevance (similarity to a query string).
  **Chekhov's gun fallacy** is a named, reusable failure mode: because
  training data is full of narratively-tight documents where every detail
  matters, an LLM tends to over-weight and over-interpret *any* retrieved
  snippet placed in the prompt as though it must be relevant — irrelevant
  retrieved context is not neutral filler, it actively misleads. This is a
  direct argument for retrieval precision over recall in any CASTLE
  return-path design: a wrong or marginal snippet surfaced to an AI reader is
  worse than no snippet.
- Lexical retrieval (Jaccard similarity, TF-IDF/BM25) versus neural retrieval
  (embeddings) is a real, current trade-off, not a solved question: lexical
  is transparent, debuggable, and tunable field-by-field but fails on
  synonyms/paraphrase; neural matches on meaning across wording/language but
  is an opaque failure mode when a document doesn't match a query and it's
  unclear why. Recommendation to keep: don't discard lexical retrieval by
  default — its debuggability has independent value for a governed system
  like CASTLE where "why did this surface" must be answerable.
- Snippetizing criteria (three-part, reusable checklist): stay under the
  embedding model's token window; size the chunk so it holds one and only one
  idea (a chunk spanning multiple topics produces a vector "between" both,
  serving neither); size it appropriately for its eventual placement in a
  prompt. Splitting on natural boundaries (paragraph/section) is preferred
  over fixed-size sliding windows because it avoids mid-idea truncation.
- **Hierarchical summarization** is presented with an explicit, named risk:
  the **rumor problem** — every summarization pass is a lossy compression,
  and each additional hierarchy level compounds the chance of the "telephone
  game" distorting the original meaning. Practical mitigation is keeping
  summaries generous rather than stingy at each level, and being aware that
  cost scales with the *original* text's total token count regardless of
  hierarchy depth (as long as each summary stays much smaller than its
  source). Directly relevant to any CASTLE design that would summarize wiki
  content recursively (e.g., page → index → cross-hub synthesis) — each
  additional summarization layer is a place a claim can silently drift from
  its source, which argues for the existing "flag contradictions instead of
  silently overwriting" rule already in `AGENT.md § Wiki Shared Layer`.
- **General versus specific summaries**: summarizing is lossy in a
  task-relevant way — a general summary of a post might drop the one detail
  a specific downstream question actually needed. General summaries are
  reusable across applications/models; specific (question-aware) summaries
  are more useful but must be redone whenever the question changes. This maps
  onto a real CASTLE design question (Phase 5 of the governing instructions
  file): a durable wiki page is closer to a "general summary" (reusable,
  stable) while a CASTLE decision report is closer to a "specific summary"
  (tuned to one question, not reusable, and must be redone rather than
  patched if the question changes).

## Chapter 6 — Assembling the Prompt (printed 123–146)

- **In-context learning** (recent information has outsized influence) and the
  **lost middle phenomenon** (information in the middle of a long prompt is
  used less effectively than the beginning or end) combine into what the book
  names the **Valley of Meh** — a real, model-general degradation zone in the
  middle of long prompts. Two named, actionable mitigations: place the
  highest-value elements outside the middle (start or end), and keep the
  overall prompt as short as possible so the "middle" is small. Directly
  applicable to CASTLE/wiki page design: don't bury the most decision-critical
  claim in the middle of a long page — lead or trail with it.
- The **sandwich technique** — stating the actual question/instruction both
  before and after the bulk of the context — is presented as the standard
  mitigation for long-context refocus loss. This is a concrete, adoptable
  pattern for any long CASTLE prompt/instruction file: restate the core ask
  at both the top and the bottom.
- Named three-part relationship model for combining prompt elements:
  **position** (order), **importance** (priority tier plus fine-grained
  score, independent of position — the introduction is usually high-importance
  despite being early, contradicting the naive assumption that recency alone
  drives importance), and **dependency** (requirements between elements that
  must both be present, and incompatibilities where two versions of the same
  content are mutually exclusive alternatives). Framed as a 0-1 knapsack-style
  optimization problem when the assembled prompt exceeds the token budget.
  Two prototype algorithms given (additive-greedy build-up vs.
  subtractive-greedy prune-down) with an explicit caveat that these are
  starting sketches, not finished tools — a fair template for any CASTLE
  scanner/validator: name the constraint precisely, prototype something
  minimal, expect to replace it as real cases surface.
- **Elastic prompt elements** — retrievable content authored in multiple
  lengths (full chapter → paragraph-elided → two-sentence-with-ellipsis) so
  an assembly step can ask "what's the longest version that fits the budget"
  rather than a binary include/exclude decision. A genuinely new idea for
  CASTLE's own return-path design: a wiki finding could be authored with a
  short/medium/long variant so a downstream consumer (a report, an index
  entry) pulls exactly the granularity it has room for, instead of an
  all-or-nothing link.
- Document-format guidance: Markdown is recommended specifically for
  analytic-report-style prompts because its heading hierarchy lets sections be
  rearranged or omitted while preserving structure, it renders directly for
  human display, and a table-of-contents section can double as both an
  outline and a chain-of-thought scratchpad (e.g., a `# Ideas` / `# Analysis`
  section the model is allowed to reason messily in, followed by a
  `# Conclusion` a downstream parser extracts cleanly) and as a stop-sequence
  anchor (`# Appendix` marking the end). This is a specific, actionable
  argument for why CASTLE's Markdown-heavy wiki convention is a genuinely
  good fit for AI-authored/AI-consumed content, not just a human-legibility
  choice.
- Structured-document formats (XML, YAML, JSON) each have concrete,
  non-obvious trade-offs worth preserving as a selection table: XML tolerates
  long/multiline content without escaping but needs open/close tag discipline;
  YAML is compact and precise for structured fields but indentation-sensitive
  and easy to break with pasted content; JSON needs escaping (newlines,
  quotes) which becomes a real failure risk for long-form text arguments, but
  is the best-supported format for tool/function-calling APIs specifically
  because providers (OpenAI named) invest disproportionate effort making
  their models emit valid JSON since their own tools API depends on it.
- Anthropic's Claude Artifacts prompt is used as a concrete, current
  worked example of a structured document (XML tags, an internal
  "think-before-acting" `antThinking` block gating whether to actually
  invoke the mechanism) — the source explicitly states this was reconstructed
  by a third party (@elder_plinius) from extracted prompts, not published
  documentation, so treat the exact tag names as illustrative rather than
  a stable contract.

## Chapter 7 — Taming the Model (printed 147–166)

- Completion anatomy is decomposed into five named zones worth using as
  vocabulary for any CASTLE output-format spec: preamble (before the real
  answer — sometimes wasteful, sometimes load-bearing when it's genuine
  chain-of-thought reasoning), recognizable start/end (needed for reliable
  parsing), and postscript/fluff (RLHF-trained politeness/hedging tacked on
  after the answer).
- **Long preambles can be a virtue, not a defect**, specifically when the
  preamble is genuine step-by-step reasoning — the source shows a concrete
  side-by-side example where forcing a long reasoning preamble produces the
  *correct* answer and a short-preamble/no-reasoning version produces a
  *wrong* answer to the identical question. This directly qualifies any
  blanket "prefer concise output" rule: concision should target fluff, not
  reasoning.
- Concrete technique for eliminating unwanted fluff: ask for the direct
  answer in a fixed early position (e.g., "1. [answer]") and relegate
  disclaimers/background/caveats to explicitly labeled *later* numbered
  sections — this reliably banishes fluff from before the answer even when it
  can't be eliminated from the response altogether.
- **Logprobs** (per-token log-probabilities the model already computed,
  retrievable at no extra inference cost from most hosted APIs) enable three
  concrete, reusable techniques: (1) **confidence scoring** — averaging
  per-token probability (not raw logprob) across a completion is described as
  empirically predictive of output quality, validated in production at
  GitHub Copilot, and usable as a threshold gate for auto-accept /
  flag-for-review / retry-with-bigger-model / never-interrupt-the-user
  decisions; (2) **calibration** — a model's own confidence threshold rarely
  matches the operationally desired threshold, so a constant offset
  (equivalent to a fitted logistic-regression bias term, sometimes exposed
  directly as a `logit_bias` API parameter) can be tuned against
  ground-truth data to shift the effective decision boundary; (3) **critical-point
  detection** — requesting logprobs on the *input* prompt itself (not just the
  completion) surfaces unexpectedly low-probability tokens, which is a
  legitimate, cheap typo/anomaly detector for the prompt text itself, worth
  filing as a candidate mechanical pre-flight check for any long
  auto-generated CASTLE prompt or instruction file. Caveat: logprobs are not
  perfectly deterministic (can vary by roughly ±1 across identical calls due
  to floating-point/deployment variance), so tests built on them must be
  written to tolerate that noise.
- The **classification-via-logprobs** technique has one sharp, non-obvious
  failure mode worth preserving verbatim as a design warning: if two
  candidate answers happen to share a common first token (e.g., "North
  America" and "Northeast Asia" both start with "North"), the model's
  token-by-token probability mass on that shared first token combines across
  both answers, which can make the model surface the less-likely full answer
  as if it were most probable. **Design rule: when using a fixed short list of
  classification labels, ensure every label is distinguishable by its very
  first token**, or the raw next-token probability is not a valid stand-in
  for the joint sequence probability.
- **Model-choice framework**, ordered by the source's stated importance:
  intelligence, speed, cost, ease of use, functionality (chat/tool
  use/logprobs/multimodal support), special requirements (open-source,
  data residency, on-prem). Explicit durable advice: don't hard-bake a model
  choice into application code; treat model selection as swappable
  (LiteLLM named as a unifying-API example). Specific provider names/rankings
  in this section (current in 2024–2025) are volatile and should not be
  treated as a standing recommendation.
- **Fine-tuning decision ladder**, reusable as a general escalation frame
  independent of specific tools: if current models already solve the task
  adequately, don't fine-tune; if the task is fundamentally unstable (the
  correct answer changes too fast), fine-tuning won't help either — wait for
  it to stabilize or solve it with retrieval instead; otherwise the right
  fine-tuning depth (full fine-tune / parameter-efficient tuning such as LoRA
  / soft-prompting) is set by how many good training examples exist and how
  deep the needed behavior change is. Named trade-off: full fine-tuning can
  teach genuinely new domain knowledge but costs weeks/thousands of examples;
  LoRA reshapes existing behavior/formatting/priors cheaply (hours-to-days,
  hundreds-to-thousands of examples) but doesn't teach new facts; soft
  prompting is cheapest but narrowest.
- The **Little Red Riding Hood principle gets a fine-tuning-specific
  addendum**: a fine-tuned model still has its *original* pretraining path
  latent underneath the new fine-tuned path, and a prompt that accidentally
  resembles the original-training document shape can cause the model to
  "forget" its fine-tuning and revert to base behavior. Design implication:
  a fine-tuned or heavily-instructed system's prompts must be checked against
  resembling the *wrong* prior document shape, not just checked for
  resembling *a* plausible document shape.

## Chapter 8 — Conversational Agency (printed 169–182)

- Motivating gap for agency: a bare chat model cannot access privileged/live
  information, cannot reliably do arithmetic at scale, and cannot take any
  real-world action — it can only talk. Tool usage is introduced as the fix:
  the application defines callable functions (JSON-schema described,
  TypeScript-style in the actual internal prompt OpenAI constructs), the
  model emits a structured invocation, the application executes the real
  function and appends the result back into the message list as a new turn.
- Worked example reconstructs OpenAI's actual internal ChatML representation
  of tool definitions and invocations (system message containing a
  `namespace functions { ... }` TypeScript-style block; invocation as
  `<|im_start|>assistant to=functions.NAME` followed by a JSON argument
  object). Explicitly labeled as the authors' own reverse-engineered
  reconstruction, not documented behavior — treat exact token/tag syntax as
  illustrative and dated, not a stable API contract to build against.
- Tool calling is explicitly reduced back to the book's core thesis: it is
  *not* a structurally different model capability, it is the same
  next-token document-completion mechanism wearing API-level "syntactic
  sugar" — the model is sequentially deciding who-speaks / whether-to-call-a-
  tool / which-tool / which-argument / what-value / when-done, one
  classification-like token-choice at a time. Reinforces this book's single
  recurring analytical move: any seemingly-special LLM capability should
  first be explained as "what does this look like as document completion,"
  before reaching for a different explanatory model.
- **Tool-definition guidelines**, phrased as reusable rules for designing any
  tool/function surface an LLM will call (directly relevant if CASTLE or a
  wiki ever exposes callable tools to an AI agent): keep the number of
  available tools small and the domain partitioned with minimal overlap
  (more tools/ambiguity measurably increases confusion); give tools and
  arguments meaningful, self-documenting camelCase-style names (not
  lowercase-concatenated); never paste a raw web/REST API spec directly into
  a tool definition — it is over-parameterized for a model's limited
  attention and needs simplifying; when integrating with a public API the
  model already knows from training, preserve its existing naming/shape
  rather than inventing a new one, since the model's prior knowledge
  transfers; keep tool output free of "just-in-case" extra content, since
  models can be distracted by irrelevant fields in a tool response exactly as
  they can by irrelevant retrieved context (an extension of Chapter 5's
  Chekhov's-gun-fallacy finding to tool outputs specifically).
- **Argument hallucination** is named explicitly: when a required argument's
  correct value isn't actually present in context, the model will often
  fabricate a plausible-looking placeholder rather than surface the gap.
  Two named mitigations, both with the same shape as this book's recurring
  "constrain the model's opportunity to guess" theme: omit the argument
  entirely from the tool definition when the application already knows the
  value (removing the model's ability to decide it at all), or explicitly
  instruct the model to ask the user when uncertain (weaker — the source
  admits models "often won't").
- **Dangerous tool execution is a named, hard safety rule, not a
  judgment call**: never let a model itself execute a consequential,
  side-effecting action on a mere promise (in its own prompt-visible
  reasoning) to double-check first — the source states plainly that a model
  instructed this way "guarantees" it will eventually skip the check.
  The correct control point is the application layer intercepting the tool
  call and requiring explicit human sign-off before the real side-effecting
  API executes, never the model's own restraint. This is a precise,
  independently-sourced confirmation of a boundary `.ROOT` already treats as
  non-negotiable (AGENT.md's consequential-action human-approval list) —
  useful as external corroborating evidence, not a new finding.
- **Chain-of-thought reasoning** is introduced (through its originating 2022
  paper) as the mechanical fix for the no-internal-monologue constraint
  established back in Chapter 2: forcing the "thinking" into visible
  generated tokens before the final answer measurably improved accuracy on
  both commonsense (StrategyQA, ~69%→~76%) and math (GSM8K, ~20%→~60%)
  benchmarks in the source paper's own reported figures — these specific
  percentages are dated to the original 2022 paper/model (PaLM 540B) and
  should be treated as illustrative of the *effect's existence and rough
  size*, not current state-of-the-art numbers. A follow-on technique
  ("Let's think step-by-step" as a zero-shot trigger phrase, no curated
  few-shot examples needed) is noted as a materially simpler way to get the
  same effect.

## Chapter 8 (concluded, printed 183–197)

- **ReAct** (think→act→observe loop, interleaving reasoning tokens with tool
  calls and their results) is presented with its original paper's own reported
  numbers as a genuinely negative-then-positive finding worth preserving
  faithfully rather than simplified: on HotpotQA, ReAct with only in-prompt
  examples (no fine-tuning) actually performed *worse* than plain
  chain-of-thought at every model size the paper tested, because a few
  in-context examples were not sufficient to teach reliable tool-reasoning
  interleaving. Only after fine-tuning on a modest ~3,000 examples did ReAct
  on a small model overtake standard/chain-of-thought prompting on much larger
  vanilla models. Direct, source-qualified lesson: **a reasoning/tool-loop
  pattern's value is not intrinsic to the pattern — it depends on whether the
  model has actually been conditioned (via examples or tuning) to execute it
  well**, and a naive few-shot version can underperform a simpler baseline.
  Specific percentages (69%→76% commonsense, 20%→60% math, 71% vs. 45%
  ALFWorld success rates) are this paper's own reported figures (2022-era
  models), dated and illustrative of relative effect size, not current
  performance to expect from present-day models.
- Three related advanced reasoning/action patterns are named as extensions
  beyond ReAct, each with a distinct mechanism worth keeping as vocabulary:
  **plan-and-solve** (devise the full plan before executing any step, vs.
  ReAct's interleaved think-act-observe); **Reflexion** (review completed work
  after the fact against a checkable outcome — the source is explicit that
  this only works for undoable/re-triable actions, e.g., failing unit tests,
  not for irreversible real-world actions); **branch-solve-merge** (run N
  independent solver attempts, ideally from differing perspectives/prompts,
  then have a separate merging pass combine them into one better answer).
- **Agent context is formally decomposed into four named parts** — preamble
  (system-level behavior/tool setup), prior conversation (all completed
  turns), artifacts (structured data objects attached to a message, distinct
  from prose — e.g., a flight-search result), and the current exchange (the
  live request plus any tool calls/results generated while handling it) — with
  the explicit rule that only the assistant's *final* response (not
  intermediate tool-calling turns) becomes part of the next turn's prior
  conversation. This is a clean, reusable vocabulary for describing what
  belongs in a CASTLE session's carried-forward context versus what should be
  compacted or dropped between turns.
- Named, unresolved trade-off on artifact management (the source is explicit
  it has "no one-size-fits-all answer" here): include full artifact content
  every turn (safest but consumes budget and risks the Chekhov's-gun-fallacy
  distraction from Chapter 5), let the model request more detail on demand via
  a `details()`-style drill-down tool (an idea the authors flag as untested
  by them), or fall back to plain RAG-style retrieval over the artifact.
  Directly analogous to the CASTLE question of how much of a source-summary
  page to surface in an index versus require a follow-up read for.
- **Consequential action authorization is reinforced with a concrete UI
  pattern**, not just a policy statement: the source's own worked example
  shows an agent about to book a $5,400 flight to North Korea and states
  plainly that *any* tool call with "a remote chance of being dangerous" needs
  explicit per-call user authorization, distinct from a one-time blanket
  permission — corroborates (does not newly establish) the human-approval
  boundary already in `AGENT.md`.
- UX guidance treats agent transparency as a design requirement, not a nicety:
  users should be able to inspect exactly which tool was called with which
  arguments and what it returned, and — where an argument was wrong — correct
  and resubmit it rather than only being able to accept/reject the whole
  turn. Relevant if CASTLE ever surfaces agent/tool activity to Chris in a UI
  rather than only in a log.

## Chapter 9 — LLM Workflows (printed 199–221)

- Opens with an explicit **strength-vs-generality trade-off framework**: a
  bare conversational agent is maximally general (can discuss anything) but
  weak at any specific complex multi-step task; a workflow trades away
  generality (built for one specific goal) for much higher reliability on
  that goal. AGI is framed as the unrealized point where both are high
  simultaneously. This is a clean, reusable two-axis frame for classifying
  any AI feature CASTLE considers building — including a fast test for
  overreach: if a single conversational agent is being asked to reliably
  complete a long multi-step business process end to end, that is evidence
  the feature needs workflow structure, not better prompting.
- The chapter's running worked example (an LLM pipeline that scrapes
  storefronts, invents a plug-in idea per store, and cold-emails the owner)
  is explicitly framed by the authors as ethically dubious ("nutty,"
  unsolicited automated outreach) even while used as a technically
  interesting case study — worth flagging as the source's own acknowledged
  limitation: technical feasibility and demonstrated real-world outcomes here
  do not establish that the technique was a responsible use of it, and CASTLE
  should not treat this example's outcome as validating unsolicited-contact
  patterns generally.
- **A conversational agent given an entire open-ended multi-step goal at
  once was shown to fail concretely** in the source's own test — vague plans,
  form-letter output with unfilled template variables (`[your_name]`),
  no actual capacity to execute the plan — even when given the necessary
  tools. The stated reason: shoving an entire goal into one agent means the
  system message must carry every edge case as a "strong suggestion" with no
  structural enforcement, and there's no way to process discrete units of
  work in isolation. Negative finding, directly reusable: **tool access
  alone does not substitute for decomposing a multi-step goal into discrete,
  independently-verifiable tasks.**
- **Five-step workflow-construction method**, reusable as a general design
  checklist independent of the book's toy example: define goal → specify
  tasks (with explicit input/output schema per task, not just a description)
  → implement tasks (verified correct in isolation before wiring together) →
  implement/connect the full workflow → optimize. The explicit schema-first
  emphasis (Tables 9-1/9-2 style field/datatype/example definitions) is a
  concrete, adoptable pattern for defining any CASTLE-facing task boundary.
- **Task implementation is explicitly not always an LLM call** — the source
  states plainly that traditional code, a classical ML classifier (BERT
  named), or human review can and should replace an LLM task wherever it is
  more dependable, cheaper, or faster; "whenever possible, avoid using LLMs."
  This directly reinforces the "smallest useful solution" principle already
  governing `.ROOT` — a CASTLE workflow should default to non-LLM
  implementation per task unless the task specifically needs open-ended
  generation.
- **Workflow topology has three named shapes with real trade-offs**: pipeline
  (strict sequential chain — simplest, but forces awkward pass-through
  coupling when a downstream task needs an upstream task's input that a
  middle task doesn't itself need); DAG (directed acyclic graph — same tasks,
  richer fan-out/fan-in connectivity, still simple to reason about because
  a task can run once all its upstream dependencies finish); cyclic graph
  (allows failure information to loop back to an earlier task for retry —
  explicitly flagged as adding real complexity: state that a DAG never needs
  to retain must now be preserved across the loop, every task must anticipate
  receiving failure-annotated input, and retry-count tracking is required to
  prevent infinite cycling). Direct, explicit recommendation: **default to
  the DAG, only add a cycle for a demonstrated retry need, and keep any
  necessary recursion hidden inside a single task rather than hoisted to
  workflow level.**
- **Reflexion at the task level** is described as the concrete mechanism for
  workflow self-correction: an analysis step (a deterministic check, a
  compiled-code/unit-test run, or an LLM-as-judge review) produces a report;
  if it flags failure, a new prompt combining the original requirements, the
  failed attempt, and the failure report is issued as a retry. This is a
  specific, implementable version of a generic "self-correcting task" pattern
  worth citing precisely rather than paraphrasing as "the AI checks its own
  work."
- Batch versus streaming workflow processing is named as an orthogonal
  design axis (a known/finite set of items processed at once vs. an
  open-ended, continuously arriving stream) — batch is simpler to build and
  reason about; streaming suits real-time/low-latency needs but adds
  complexity. No specific recommendation given beyond "either can be right for
  the same underlying task."
- **Advanced/agent-driven workflows are explicitly framed by the authors as
  the frontier, not yet stable or dependable** — letting an LLM itself drive
  task routing, spawn tasks dynamically, or maintain long-lived per-asset
  "stateful task agents" (a persistent agent tied to one evolving artifact,
  e.g., one file in a codebase, that reacts to change notifications from
  peer agents) trades predictability for flexibility. The source's own
  explicit recommendation, stated plainly in the chapter conclusion: **default
  to a traditional deterministic pipeline/DAG with LLM-implemented tasks;
  reach for agent-driven or stateful-agent workflow control only when the
  basic approach has a demonstrated, specific flexibility gap** — a direct,
  source-endorsed instance of the same "smallest useful solution, escalate on
  demonstrated need" principle already used elsewhere in this intake and
  already governing `.ROOT`'s own evolution policy.

## Chapter 10 — Evaluating LLM Applications (printed 223–243)

- Opens with a durable, source-authored framing that generalizes past any
  specific book example: evaluation can target three distinct things — the
  model, an individual interaction (one prompt/completion pass, "unit-test"
  granularity), or the whole application loop ("regression-test" granularity)
  — and a mature evaluation suite needs both granularities, not just one:
  whole-loop tests for architecture-level changes, single-pass unit tests for
  prompt/parameter tuning (since aggregate loop-level noise can drown out a
  small prompt effect).
- **Offline evaluation is laid out as an explicit maturity ladder**, reusable
  as a general adoption path for any AI feature: ad hoc playground tinkering
  → **example suite** (5–20 hand-picked representative inputs, run through a
  script, diffed by eye — deliberately *not* automated pass/fail, explicitly
  valuable before any quality criteria even exist) → full **evaluation
  harness** (hundreds-to-thousands of examples, automated scoring, needed once
  statistical power matters). Direct implication for CASTLE: a small,
  hand-curated example suite is a legitimate, low-cost first evaluation step
  for a new AI-facing feature — it doesn't need to wait for a "real" test
  suite to have value.
- **Sample-sourcing options are named with an explicit circularity warning**:
  mined historical records (best when they exist in volume), live app
  telemetry (only exists post-launch, decays as the app changes, and is
  biased toward *inputs* the app already handles rather than covering novel
  cases), or LLM-synthesized examples (fast and scalable, but carries a
  named, concrete risk — **if the same model that generates the test examples
  also produces or judges the candidate solutions, the evaluation is
  structurally biased toward that model** — a precise, reusable caution for
  any CASTLE self-evaluation loop that would use one AI to both create and
  grade test material).
- **Solution-evaluation methods are ranked by difficulty, each with a
  concrete selection criterion**: gold-standard matching (exact or partial —
  partial-match aspect selection is explicitly framed as a hard, deliberate
  choice: pick an aspect that reliably distinguishes real failure from benign
  variation, avoiding both "too strict, nothing passes" and "too loose,
  nothing meaningful is measured"); functional testing (execute the output
  and check an objective proxy — e.g., does generated code still pass the
  original repo's own unit tests, which the source's own Copilot case study
  used); LLM assessment (for genuinely open-ended natural-language quality
  with no gold standard).
- **LLM-as-judge has a specific, non-obvious bias correction documented**: a
  model asked to grade its *own* output directly is measurably worse
  (self-referential biases, RLHF's tendency to over-defer to any hint of
  user doubt) than the same model asked to grade a nominally third-party
  response — even when it's actually grading itself, framing the assessment
  as evaluating someone else's work produces more objective results. This is
  a specific, actionable implementation detail for any CASTLE self-review
  step that has an AI check its own prior output.
- **SOMA** (Specific questions, Ordinal scaled answers, Multi-Aspect
  coverage) is presented as the source's named, complete recipe for
  disciplined LLM-as-judge assessment: ask about one specific, independently
  verifiable aspect at a time rather than a vague "is this good"; use an
  ordinal scale (e.g., 1–5) with an explicit written description of what each
  point means, never a bare yes/no, because yes/no invites inconsistent
  private thresholds; decompose "goodness" into named, separately-scored
  aspects (e.g., intent-correctness vs. execution-correctness vs.
  appropriate restraint) rather than one aggregate score, since a single
  completion can be right on one axis and wrong on another simultaneously.
  Also specifies the judge must see the evaluation rubric/aspects *before*
  the example to grade, since the model reads once and cannot backtrack —
  order matters mechanically, not just stylistically. This is a complete,
  directly adoptable template for any CASTLE-designed AI self-assessment
  step (e.g., grading a wiki chunk-intake's own completeness).
- **Human-grounding requirement, stated as a hard methodological check**: LLM
  assessment is only trustworthy once validated against human judgment, and
  because humans themselves disagree with each other, the correct test is not
  "does the model match one human" but "does adding the model into a pool of
  several human graders change the *pool's* measured inter-rater disagreement"
  (Kendall's Tau named as the standard statistic) — a model within the normal
  human-to-human disagreement range is acceptable; a model that increases
  disagreement beyond that range is not. Durable, precise standard worth
  citing exactly rather than paraphrasing as "compare to a human."
- **Online evaluation's five-tier metric hierarchy** (most to least direct):
  direct feedback (explicit user rating — reaffirms Chapter 4's finding that
  this is intrusive and response-biased, with the added nuance that
  *contrastive* feedback, "which of these two is better," yields a cleaner
  signal than "rate this" but is more intrusive still, so it fits an
  assistant users already deliberately engage, not an ambient/background
  feature); functional correctness (did the concrete outcome objectively
  occur — code compiles, ticket confirmed); user acceptance (did the user act
  on the suggestion — a "did the user click" signal that only proves a
  suggestion looked promising, not that it was actually correct or valuable);
  achieved impact (the deeper, delayed, harder-to-measure question of
  real downstream benefit); incidental metrics (latency, session length, and
  similar signals with no fixed direction of "good," valuable mainly as
  investigation triggers on unexpected change, not standalone quality
  proof). Explicit, source-stated recommendation to generalize: **acceptance
  or impact metrics should be the primary target where available; direct
  feedback is the fallback only when neither can be measured; incidental
  metrics are always worth tracking as guardrails regardless.** The book's
  own reported Copilot finding is used as direct evidence that acceptance
  metrics can correlate more strongly with real productivity gain than more
  "sophisticated" downstream impact metrics — an argument for not assuming
  the more complex-sounding metric is automatically the better one.
- A/B testing is presented with one practical, generalizable methodological
  trap: comparing "already-updated users" against "not-yet-updated users" as
  proxies for treatment/control is invalid, because users who update quickly
  differ behaviorally from those who don't; the valid design compares only
  users who have *already* received an update, split randomly between the
  two variants.

## Chapter 11 — Looking Ahead (printed 245–252)

- Multimodality section: mechanically, image/video content is projected into
  the same embedding space as text tokens and processed by the same
  transformer architecture already covered in Chapter 2 — reinforcing this
  book's core recurring move (new-seeming capability = same mechanism,
  different input encoding). Concretely dated, secondary observations: public
  concern about approaching exhaustion of usable public text training data
  is named as a real driver toward multimodal training (image/video content
  as a fresh, much larger data source) — this is the authors' framing of a
  live, unresolved industry debate as of the book's writing (2025), not a
  settled fact, and should be treated as such if cited onward.
- **"Stateful objects of discourse"** is the source's own coined term for
  Anthropic's Claude Artifacts feature: a persistent, in-place-editable
  object (code, SVG, document) that a conversation can refer back to and
  revise, as distinct from a chat transcript's ordinary flow of ephemeral
  turns. The authors are explicit that this is new (introduced "as we were
  wrapping up this book") and still has concrete, named limitations worth
  preserving as a design checklist for any equivalent artifact system: the
  whole object is regenerated from scratch on every edit rather than
  patched (a scaling concern for large objects); the UI/model assumes only
  one active artifact at a time, with no clean way to reference or juggle
  several simultaneously; and there's no mechanism for the human to directly
  edit the artifact and have that edit flow back into the model's
  understanding of its current state — only "ask the assistant to fix it."
  This is a fair, source-grounded pointer to the exact class of gap CASTLE's
  own "elastic snippet" / evolving-page conventions would need to solve
  cleanly if a wiki page is treated as a persistent, jointly-edited object
  rather than a repeatedly-regenerated one.
- Benchmark saturation is named as a structural evaluation problem, not
  incidental noise: as models improve and as benchmark content leaks into
  subsequent training corpora (even unintentionally, via web mentions), a
  previously-discriminating benchmark stops being able to distinguish real
  capability differences. Named mitigations: continual benchmark refresh, and
  algorithmically-generated, non-memorizable test families (ARC-AGI cited as
  the example) that can always mint new, never-seen instances. Directly
  relevant caution for any CASTLE-internal capability benchmark: a fixed,
  reused internal test set will eventually stop being a meaningful signal
  once the same model (or its successors) have effectively "seen" it via
  repeated internal use, and periodic refresh or generative test variation
  should be planned for, not treated as a one-time setup cost.
- Closing two-lesson summary, stated by the authors as the book's actual
  thesis in miniature: (1) LLMs remain nothing more than text-completion
  engines mimicking training-set patterns — the Little Red Riding Hood
  principle (match established document/format patterns) is the single
  most-repeated actionable consequence throughout the book; (2) "empathize
  with the model" — five named, concrete behavioral facts to design around:
  LLMs are easily distracted by irrelevant content (Chekhov's-gun-fallacy,
  restated one final time as a closing principle); LLMs need the prompt to be
  human-decipherable or they will likely also struggle with it; LLMs need
  explicit instructions and examples, not implied intent; LLMs are not
  psychic and only know what the prompt/tools supply; LLMs have no internal
  monologue, so visible reasoning must be explicitly elicited.

### Decision Contributions So Far

**Keep:** raw evidence immutability, human validation, bounded/small trials,
business-outcome-first measurement (all independently reinforced by this
source's evaluation chapter).

**Add to the synthesis queue:** a four-level prompt-engineering maturity
ladder (thin wrapper → augmented input → stateful → agentic) as a
classification tool for any CASTLE-facing AI feature; an explicit
static-vs-dynamic content tagging convention for prompt/template design; a
hard rule against concatenating user-controlled text into a system/instruction
message (concrete prompt-injection boundary); a feedforward-pipeline vocabulary
(context retrieval → snippetization → scoring/prioritizing → assembly) as a
common frame for wiki intake pipelines; a requirement that any chosen
telemetry/success metric have a demonstrated link to the real outcome, not
just ease of logging; explicit-instruction phrasing guidance (positive,
reasoned, non-absolute) as a style rule for governance/instruction files
themselves, since AGENT.md and this instruction file are exactly this genre of
document; anchoring-bias and order-bias checks for any few-shot-style example
set embedded in a shared prompt/skill.

**Reject as default:** trusting explicit user feedback (thumbs up/down) as a
primary quality signal; treating a demo/single interaction as evidence a
sub-token or multi-hop-reasoning task is reliable without engineered
scaffolding; letting example order in a template go unrandomized when order
itself carries no intended meaning; pasting a raw REST/web API spec directly
into a tool/skill definition instead of simplifying it; allowing a model's
own "I'll double-check first" promise to substitute for an application-layer
human-approval gate on a consequential action.

**Additional adds (Chapters 5–8):** Chekhov's-gun-fallacy naming for
over-weighted irrelevant retrieved context/tool output; a lexical-vs-neural
retrieval trade-off table (transparency/debuggability vs. semantic recall)
for any CASTLE search/retrieval design; the "rumor problem" as a named risk
for recursive/hierarchical summarization, reinforcing the existing
contradiction-flagging rule; general-summary (reusable, stable) vs.
specific-summary (tuned, must-redo-not-patch) as vocabulary for
distinguishing a durable wiki page from a one-off CASTLE decision report; the
Valley of Meh / sandwich technique as concrete guidance for where to place
the highest-value claim in a long page or prompt; position/importance/
dependency as a three-part vocabulary for prioritizing content under a size
budget; elastic (multi-length) content authoring as a candidate return-path
mechanism; Markdown's heading-hierarchy/TOC structure as a specifically
good fit for AI-authored and AI-consumed governance content, independent of
human readability; the five-zone completion vocabulary (preamble/
start/end/postscript) plus the finding that long reasoning preambles can be
correct and desirable, not wasted tokens; logprob-based confidence/
calibration/critical-point techniques as candidate mechanical pre-flight
checks; the shared-first-token classification-label pitfall; the
model-choice and fine-tuning decision ladders as reusable escalation frames;
tool-definition guidelines (small partitioned tool sets, self-documenting
names, no raw API pastes, no just-in-case extra output fields) for any
CASTLE-exposed agent tool; argument-hallucination mitigation by omitting
already-known arguments from a tool's definition.

**Additional adds (Chapters 9–11):** the strength-vs-generality two-axis frame
for classifying any proposed AI feature; schema-first task definition as the
CASTLE task-boundary convention; "avoid LLMs by default" as a source-stated
preference reinforcing `.ROOT`'s smallest-useful-solution principle; DAG as
the default workflow topology, cycles only for a demonstrated retry need;
task-level Reflexion as a concrete self-correction mechanism; agent-driven/
stateful-agent workflow control reserved for a demonstrated flexibility gap,
not a default; the offline-evaluation maturity ladder (playground → example
suite → harness); the LLM-generating-its-own-test-data circularity risk; the
third-party-framing bias correction for LLM self-assessment; SOMA (specific
questions, ordinal scale, multi-aspect coverage, rubric-before-example
ordering) as a complete adoptable template for any CASTLE AI self-assessment
step; the pool-disagreement (Kendall's Tau) test for validating an AI judge
against human graders; the acceptance/impact-metric-over-direct-feedback
preference; the A/B "already-updated users only" methodological fix;
benchmark saturation/leakage as a reason to refresh or vary any internal
CASTLE capability test rather than reuse a fixed set indefinitely; "stateful
objects of discourse" named limitations (whole-object regeneration,
single-object assumption, no direct human edit path) as a gap-checklist for
any CASTLE design treating a wiki page as a persistent jointly-edited object.

**Reject as default (Chapters 9–11, additional):** giving a single
conversational agent an entire multi-step goal and expecting reliable
completion from tool access alone; using the same model to both generate
synthetic test examples and grade candidates against them without disclosing
the shared-model bias risk; comparing "updated" vs. "not-yet-updated" users
as an A/B proxy; treating a fixed internal benchmark as permanently valid.

## Coverage Statement

All 282 physical PDF pages traversed this run, front matter through the
Chapter 11 conclusion (printed pages 1–252), in chapter-aware chunks; the
index (printed 253–262) was read but contains no extractable findings
(reference material only). No chapter or section was skipped or sampled.
Every finding above is grounded in text actually read this run, not inferred
from the table of contents or prior training knowledge of this book.
Model/provider names, prices, benchmark scores, and framework
recommendations (LangChain, AutoGen, CrewAI, specific 2022-2025 paper
results) are flagged inline as dated/volatile and should be reverified before
being cited as current in any downstream CASTLE decision. Durable,
transferable findings — Little Red Riding Hood principle, truth bias,
Chekhov's-gun-fallacy, static/dynamic content separation,
position/importance/dependency prompt assembly, the offline/online
evaluation ladder, SOMA, and the strength-vs-generality workflow frame —
carry no such volatility flag and are usable as-is in the CASTLE architecture
synthesis.
