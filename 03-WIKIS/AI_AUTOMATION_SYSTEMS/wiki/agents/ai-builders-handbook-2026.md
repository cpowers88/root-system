---
type: source-summary
timeline: reference
status: active
reference_priority: core
tags: [ai-automation, agents, evaluation, vocabulary]
source_file: raw/AI_builders_handbook.pdf
---

# The AI Builder's Handbook (LevelUp Labs, April 2026)

## Source identity

Published by LevelUp Labs (`levelup-labs.ai`), April 2026, CC BY-NC 4.0. Not a
traditional single-author book — a 152-physical-page, 20-chapter self-paced
guide whose numbered main text runs to p. 143, built from "thirty-plus
enterprise implementations," organized as six parts:
Landscape → Designing AI Products → The Evaluation Core → Building Agentic
Systems → Production and the Long Arc → Where to Go Next. Every concept links
to a primary source (paper, provider doc, or course) rather than resting on
the guide's own authority — this is a curated map with commentary, not a
from-scratch treatise.

**Why this book over the other five queued alongside it:** it is the most
current of the six (April 2026, actively citing Claude Sonnet 4.6/Opus 4.7,
GPT-5, Gemini 2.5, DeepSeek-R1 — all current-generation), the shortest and
therefore the only one realistically fully ingestible inside a normal
session rather than a multi-session commitment, and its two largest parts
(Evaluation Core, 4 chapters; Building Agentic Systems, 6 chapters) sit
squarely in this hub's own `agents/` cohort with real gaps in existing
coverage — no current page here walks through *how to actually build and
score* an eval suite or an agentic system, only architecture/economics
papers about agentic automation in the abstract
([[agentic-automation-architecture-reliability-and-economic-evidence]]) and
industry-adoption barriers
([[agentic-ai-industry-adoption-barriers]]).

## Coverage status — honest, not full

**Compiled (2026-07-27):** Chapters 1-15 — **15 of 20 chapters**, i.e. all
of Parts 1-4 (The Landscape; Designing AI Products; The Evaluation Core;
Building Agentic Systems). This includes the two parts originally flagged
highest-priority for this hub's `agents/` cohort gap (Evaluation Core,
Building Agentic Systems) plus the remaining Part 1-2 material. **Chapters
16-20 (Part 5: Production and the Long Arc; Part 6: Where to Go Next) and
the Master Resource Index remain TOC-mapped below, not yet chunk-read.**

**Provenance note:** Chapters 6-9 were independently compiled twice —
once by this fork, once by a concurrent Codex session the same day — before
either was aware of the other. Consolidated into one section (this fork's
version, which preserved more named tools/exact thresholds/direct quotes);
no information from either pass was lost. See `wiki/log.md` for both
sessions' original entries.

## Chapter 1 — The Language of Generative and Agentic AI (compiled)

The book's stated reason for existing: "the AI field is bad at vocabulary.
Two reputable sources will define 'agent' differently, and both will sound
right." This chapter is a working glossary organized the way builders
actually construct understanding — raw material → talking to the model →
letting the model act → keeping it honest — not alphabetical.

**1.1 The Raw Material**
- **Generative AI** — the umbrella class (text/image/audio/video/code
  generation vs. classification). LLMs are the most familiar shape but not
  the only one.
- **Foundation model** — a model trained broad-and-at-scale for many
  downstream tasks rather than one; term coined by Stanford CRFM (2021).
  GPT, Claude, Gemini, Llama are all foundation models, usable directly or
  adapted via fine-tuning.
- **LLM** — a foundation model specialized for language. Key framing: it
  does not "know" facts like a database — it produces text fitting patterns
  in training data. "The behavior that feels magical and the behavior that
  feels wrong both trace back to that one fact."
- **Tokens** — the unit a model reads/writes (word, sub-word, or character
  depending on tokenizer). Same string tokenizes differently across models
  — practical consequences: you pay per token and have a hard per-request
  ceiling.
- **Context window** — total tokens a single request can hold (prompt +
  history + retrieved docs + response). As of this book's writing (2026):
  ~200K (Claude Sonnet 4.6 standard) up to 1M (Claude Opus 4.7 extended,
  Gemini 2.5 Pro) — **volatile claim, re-verify before citing**. Bigger
  window ≠ better attention — the "lost in the middle" problem (attention
  quality degrading toward the middle/edges of long contexts) is named as a
  real production concern, not a solved one.
- **Pretraining / fine-tuning / post-training** — three stages. Pretraining:
  expensive, general, trillions of tokens. Fine-tuning: adapting a
  pretrained model to a narrower task on a much smaller labeled set.
  Post-training: the umbrella between raw pretraining and a deployable
  model (instruction tuning, RLHF, safety tuning, reasoning training) — the
  book's stated claim is that **post-training, not pretraining scale, is
  what mostly distinguishes a "good" frontier model from a weaker one in
  practice.**

**1.2 From Text to Thought**
- **Chain-of-thought** — prompting a model to "think step by step" before
  answering; a 2022 Google Brain paper's counterintuitive finding that this
  alone dramatically improves math/logic/multi-step accuracy. Named as the
  foundational technique behind every later reasoning technique.
- **Reasoning models** — a distinct trained class (OpenAI o-series/GPT-5
  reasoning mode, Claude extended thinking, Gemini 2.5 thinking, DeepSeek
  R-series) that trade speed/cost for reliability on hard problems.
  Practical rule given: standard model for simple tasks, reasoning model
  for planning/math/code-debugging/agentic work.
- **Multimodality** — models accepting more than text (vision, and in some
  cases audio/video). Named practical consequence: no separate OCR pipeline
  needed for most document work in 2026 — a screenshot or photo can go
  directly into the prompt.

**1.3 Talking to the Model**
- **Prompting** — craft + design + empirical testing of model input.
- **System prompt** — a "sticky" prompt above the user's message, setting
  role/rules/scope for every turn.
- **Few-shot / in-context learning** — giving example input-output pairs
  directly in the prompt; the book calls this "one of the most underrated
  techniques" — three good examples often beat a carefully tuned zero-shot
  prompt.
- **Context engineering** — named as "the current evolution of prompt
  engineering": not just wording one instruction, but deciding everything
  that goes into the context window (system prompt, few-shot, retrieved
  docs, tool defs, history, output format) and in what order. Stated claim:
  **"When people talk about 'building an AI product' in 2026, they are
  almost always talking about context engineering more than model choice."**

**1.4 Beyond Single Calls** (headers only, pp. 12–14, not yet chunk-read in
full): Tool Use and Function Calling; Agent; Workflow vs. Agent; Router and
Classifier Patterns; Specialist and Sub-Agent; Multi-Agent System.

**1.5 Knowing What You Don't Know** (headers only, pp. 15–16): Retrieval;
Semantic Search and Embeddings; Vector Database; Memory.

**1.6 Keeping It Honest** (headers only, pp. 16–18): Evaluation (Evals);
LLM-as-Judge; Hallucination; Grounding; Guardrails.

**1.7 Plumbing** (headers only, pp. 18–19): Observability and Tracing; Model
Context Protocol (MCP); Agents SDK.

## Part 3: The Evaluation Core (compiled — Chapters 6-9, pp. 44-64)

**Note:** a concurrent Codex pass independently compiled this same Part 3
material into this page around the same time (shorter, paraphrased
sections: "Evaluation is the continuing work," "Use the cheapest valid
measurement first," "Treat an LLM judge as a calibrated measurement
instrument," "Separate measurement from intervention"). Consolidated
2026-07-27 into the single fuller version below, which covers the same
four chapters with named tools, exact thresholds, and direct quotes
preserved — removed rather than kept in parallel, per this hub's own LINT
rule against duplicate/mixed-ownership pages. No information was lost;
Codex's framing was a subset of what's below.

The book's own framing: "the deepest part of this guide." Read as two
chunks (Ch 6-7, Ch 8-9), each chapter fully.

### Chapter 6 — Why Evals Are the Real Work

**The 80/20 flip.** Traditional software front-loads work (scope, design,
build, test, ship; stable after). AI systems flip it: the first version
ships fast, then most of the real work happens post-deployment — watching
real usage, spotting failures, adjusting evals/prompts/retrieval, shipping
again, continuously. Stated claim: **where software spent 80% of effort
pre-deployment, AI spends 80% post-deployment**, and teams that don't plan
staffing/budget around that learn it the expensive way.

**The two questions every eval answers**, for a given case: *did the system
do the right thing* (correctness) and *was the way it did it safe and
usable* (quality — tone, no sensitive-data leak, right format). Most
production systems need both; correctness-only misses unusable-but-right
answers, quality-only misses confidently-wrong-but-well-formatted ones.

**Evals are infrastructure, not a milestone.** The named failure mode: a
team writes an eval suite pre-launch, runs it once, ships, then the suite
sits untouched while the system drifts. The book's own **CC/CD framework**:
Continuous Calibration (keep evals fresh) + Continuous Development (keep
improving against them) — replacing the one-time-launch software model with
a living-system model. Every new production edge case becomes a new test
case; every model upgrade and prompt change runs through the suite before
going live.

### Chapter 7 — Code-Based Evals

The cheapest, most underused eval family — deterministic checks needing no
labels, no human, no LLM judge. **Build these first, always.**

What they check: schema validation, format validation, exact match
(canonical for classification), containment (required string/citation/
disclaimer present), length constraints (too short = truncation signal, too
long = the model running on), URL validity (HEAD-request resolution +
allowed domains), regex pattern match, count-of-things checks. Rule of
thumb given: **if a question can be answered by inspecting output with
code, it's a code-based eval waiting to be written** — and it beats any
LLM-based alternative on speed, cost, consistency, and debuggability
whenever the question has a crisp right answer.

**Building the first one:** three parts — a dataset (20-50 cases, main
patterns plus edge cases), a run function (calls the system, returns
output), a score function (returns true/false against the expected
output/criterion). Named failure modes these catch best: schema drift,
format regressions, silent truncation, category bleed, hallucinated links
— "each of these is cheap to check and expensive to miss."

**The limits:** cannot judge whether an answer *sounds* right, whether tone
is appropriate, or whether reasoning is correct — those need a human or an
LLM judge (Chapter 8). **Target given: 60-70% of total eval coverage should
be code-based** — widest net of real failures at the lowest cost; the
remaining 30-40% is where judges and human review earn their keep.

### Chapter 8 — LLM-as-Judge and Calibration

For judgment calls code can't answer (tone, faithfulness, helpfulness) and
human review can't scale to. **Three conditions must all be true** before
reaching for an LLM judge: the question requires judgment; the scale is too
big for humans; you can write a clear rubric in a paragraph. Missing any
one — use a code-based eval instead, human review for small datasets, or
fix the rubric before blaming the tool.

**Worked example components** (brand-voice judge, Good/Acceptable/Poor):
task definition, explicit rubric with per-label criteria, a calibration set
of labeled human examples, the judge prompt itself, a parseable scoring
mechanism. **Judge-prompt principles:** use a label taxonomy (Good/
Acceptable/Poor), not fine-grained 1-10 scores — labels are blunter but far
more stable across runs than numeric scores, which sound precise but drift;
define every label explicitly; force structured, parseable output; keep the
reasoning to one sentence (long chains produce inconsistent labels).

**Calibration workflow (the step teams skip when rushed):** pick 30-50
cases spanning quality range → two humans label each with the rubric →
resolve disagreements (an unresolvable one means the rubric itself is
underspecified) → run the judge prompt on the same set → measure judge/human
agreement. **≥90% agreement: trust and deploy. 70-90%: iterate the prompt.
<70%: the rubric or task isn't ready for a judge at all.** That same
calibration set becomes the judge's own regression test going forward.

**Failure modes:** position bias (judges systematically prefer the
first-shown option in side-by-side comparisons — randomize order),
length bias (favor longer responses even when worse — control for it in
the rubric), over-lenient scoring (helpfulness-trained frontier models
skew toward "Good" over "Acceptable"), sensitivity to phrasing (small
rubric wording changes shift scores — version the prompt once calibrated),
model drift (judge-model upgrades shift scores even on an unchanged rubric
— recalibrate after every judge-model change).

**Mix ratio for a full suite:** 60-70% code-based (every change), 20-30%
LLM judge (calibrated quarterly), 5-10% human spot-check (weekly, feeding
new edge cases back into the other two buckets). **Recalibration triggers:**
judge prompt changed, judge model changed, rubric changed, system output
style shifted, or a quarter has passed.

### Chapter 9 — Guardrails: Input and Output

**Evals measure after the fact, offline, on a dataset. Guardrails run in
real time, on every request, in production, and can block/modify/route
it** — the production safety layer, not a duplicate of evals.

**Input guardrails** (stop bad things reaching the model): PII detection/
redaction, prompt-injection detection (dedicated classifiers named: Meta's
Prompt Guard, Lakera Guard), jailbreak detection (harder — needs a
specialized classifier, not simple pattern matching), sensitive-data
blocking (credentials/API keys/proprietary docs), scope filtering
(in-scope-vs-out-of-scope classifier), input sanitization (HTML/scripts/
unusual unicode). Recommended: 3-5 of these active, tuned to risk profile.

**Output guardrails** (catch bad things before the user sees them):
groundedness check (does the response claim things the source docs
actually support — named tools: Galileo, Azure Groundedness Detection),
PII leakage detection, action-boundary enforcement (did the response claim
an action the system didn't actually take), tone/brand-voice filtering,
domain-boundary check, citation validation, tool-call validation (name and
arguments match schema before executing), refusal mechanisms (graceful
decline, not a bare error).

**Guardrails vs. evals, explicitly:** evals show aggregate quality and feed
release decisions; guardrails catch the specific edge cases that slip
through in production. If you can only build one first, **build evals
first** — they tell you how often guardrails will actually need to fire,
which tells you which guardrails are worth building.

**Strictness tradeoff:** every guardrail trades false positives against
false negatives. High-risk domains (financial/legal/medical) — err strict,
a blocked legitimate request costs less than a harmful response getting
through. Lower-risk domains (internal tools) — err lenient, over-blocking
just creates a bad UX with no real safety upside. Tune thresholds against a
month of real traffic, not guesswork.

**Production patterns that work:** layer guardrails in sequence (cheap
checks — sanitization, injection detection, scope filtering — run before
the expensive model call); log every guardrail decision (input, decision,
reason — this is how you catch a guardrail's catch-rate drifting from 1%
to 5% over time); always build a graceful fallback path for a blocked
request, never a bare refusal. **Right-sized starting stack:** input
sanitization (always on), PII redaction on input (if users might share
sensitive info), prompt-injection detection (any externally-exposed
system), scope filtering (any focused-purpose system).

## Part 4: Building Agentic Systems (compiled in full — Chapters 10-15, pp. 66-101)

The book's largest part (6 chapters); this hub's core `agents/` subject.

### Chapter 10 — From Single Calls to Agents

**The spectrum**, in order of rising model autonomy and engineering cost:
single call → chained calls (fixed order, still a workflow) → workflow
(branching logic the designer wrote — a router decides which specialist
handles a request, a planner decides which approach to try) → agent (the
model decides the steps dynamically, given a goal and tools, looping until
it decides it's done) → multi-agent system (multiple agents coordinating,
orchestration itself becomes complex). Named claim: **the router-and-
specialist workflow pattern is the right shape for most enterprise tasks**
— jumping straight to "agent" makes the system harder to evaluate without
solving a real problem.

**Cost of each step up:** evals get harder (can't test a fixed input-output
pair anymore, have to test the whole trajectory), latency rises, cost
rises, debugging gets harder (a bug can live at any of five turns), failure
modes multiply (loops, tool misuse, goal drift a workflow structurally
cannot exhibit).

**The rule for moving up, stated directly: stay at the simplest level that
handles 90% of your cases; upgrade only when you have a specific class of
cases the simpler shape cannot handle.** Cites Anthropic's own published
guidance verbatim ("find the simplest solution possible, and only increase
complexity when needed") as the same conclusion from a different source.

**When agents are actually the right shape:** long-tail task variety
(hundreds of variations you can't enumerate), dynamic planning (the right
next step depends on information you only get after the first step),
open-ended user goals, exploratory/trial-and-error work. Named
counter-examples: a billing draft specialist, a compliance checker, a
customer-support router — none need an agent, workflows handle them
faster/cheaper/more reliably.

**The hybrid pattern the book says ships most often:** a workflow as the
overall shape (router + specialists), with small scoped agentic behavior
*embedded inside* one specialist where it earns its keep (e.g., a billing
specialist that has tool access and decides which tool to call within its
narrow scope) — "use workflows as the chassis, with small scoped agents
embedded as components inside specific specialists."

**Evaluating systems as they get more complex:** single-call level —
evaluate inputs/outputs. Workflow level — add which path was taken. Agent
level — add the full trajectory, tools called, order, error recovery,
whether the goal was actually met. Direct claim: **a team that ships an
agent without an agent-aware eval suite ships a system it cannot improve —
the cost of building the evals is part of the real cost of choosing agents.**

### Chapter 11 — Workflow and Router Patterns

**The five workflow patterns** (sourced from Anthropic's "Building
Effective Agents" essay, cited as the clearest public writeup on this):
prompt chaining (fixed-order steps), routing (classify → dispatch to a
specialist), parallelization (multiple calls at once, for voting/diversity
or splitting sub-tasks), orchestrator-and-workers (central LLM plans,
worker LLMs/tools execute, cleaner plan/execution boundary than a full
agent), evaluator-and-optimizer (one LLM produces, a second scores against
a rubric, output gets refined — the book's own brand-voice judge from
Chapter 8 plugged directly into this pattern). Most real systems combine
several: route → chain → evaluate before returning.

**The router pattern in depth** (named the most common enterprise shape,
and the most likely to fail silently if built carelessly). Three parts:
classifier (usually one cheap LLM call, returns a category), specialists
(one per category, each with its own prompt/tools/eval criteria, no
awareness of the others needed), fallback (escalate to human / default
handler / ask for clarification when classification is uncertain or wrong).

**Design principles for a router that holds up:** keep the category set to
3-7 (below 3 the router isn't earning its keep, above 7 accuracy degrades
and specialists start overlapping); make categories mutually exclusive (a
request fitting two categories signals a design gap, not a data problem);
use a cheap fast model for the classifier itself (Claude Haiku 4.5, GPT-5
mini, Gemini 2.5 Flash named explicitly — save the expensive models for
specialists, not the router); few-shot examples are named the single best
router-accuracy intervention; evaluate the router with a code-based exact-
match eval (Chapter 7), no LLM judge needed, run on every prompt change;
log every routing decision (category, confidence if available, downstream
specialist outcome) to see whether quality drift traces to the classifier
or the specialists.

**Confidence and human review:** estimate confidence either by asking the
model to self-report a High/Medium/Low label (subjective but stable if the
prompt is stable) or by using logprobs where the provider exposes them.
For low-confidence cases: escalate to human, default to a stronger general
handler, ask the user to clarify, or accept the miss if the cost of being
wrong is low. **Three human-in-the-loop patterns:** pre-action review (AI
drafts, human approves before it happens — for high-stakes actions),
post-action review (AI acts, human reviews a sample after — for
high-volume/low-stakes work), escalation triggers (AI handles autonomously,
escalates only when a specific condition fires). Choice depends on the
cost of a wrong action and the workflow's volume.

**Composability test, given directly:** can you swap a specialist without
touching anything else? Add a category without breaking existing ones?
Upgrade the router model without specialists caring? If yes, the workflow
ages well; if no, every change risks breaking something unexpected — design
each step's input/output contract before implementing it.

**A named reference shape for document-heavy enterprise work** (compliance
checks, filing reviews, policy adherence): classify document type/intent →
retrieve relevant rules → extract key facts → verify facts against rules →
flag issues with structured output → generate a human-readable summary →
route to human review on any high-severity flag. Each step gets its own
prompt, eval, and guardrails.

### Chapter 12 — Tool Use and Actions

Framing line: "a language model that cannot use tools is limited to what
is in its training data. A language model with tools is an employee" — and
tool use is also where the risk profile changes, since a model that can
call APIs can call them wrong, and one that can take actions can take the
wrong one.

**Mechanics:** define tools (name, description, input schema) exposed to
the model in the prompt; the model returns a structured tool call instead
of plain text when it decides one is needed; your code executes it and
returns the result; the model continues using that result — this loop can
run multiple times within one user-facing response.

**Five tool-design principles:** name for what it does, not what it is
(`get_invoice_details` beats `invoice_api_v2` — the model picks tools by
name/description, both need to be self-explanatory); write a description
that says *when* to use it, not just what it does; keep the input schema
tight (only genuinely needed parameters); design output to be useful
(structured, concise, clear field names, no internal codes/DB jargon the
model has to guess at); make failures legible (a clear error message the
model can act on — "Invoice ID not found" beats "ERR-4011").

**Read-only tools first, always.** Read-only tools (lookups, searches,
status checks) are safe to let the model call freely — worst case is a
wasted call. Write-action tools change state and carry real consequence
when wrong. **The recommended progression:** (1) read-only, autonomous —
most production systems live here for months; (2) write-action with
draft-then-confirm (model proposes, human approves); (3) write-action with
guardrails, autonomous but boundary-limited (specific record types/value
ranges/user contexts); (4) write-action, fully autonomous — reserved for
low-blast-radius, high-volume actions only, and named as rare for good
reason. **Most enterprise systems ship safely at level 2; level 3 needs
real eval/guardrail investment; level 4 is rare.**

**Permissioning — "the part teams skip."** Direct statement: a model with a
tool has the same permissions as the code running the tool — if the tool
can read any account, the model can read any account, and that is almost
always wrong. **The correct pattern, called out as "the correct pattern,
always":** scope the tool's permissions to the authenticated user's
context, passed in at runtime, enforced inside the tool's implementation —
the model cannot bypass this even if a prompt tells it to (i.e., permission
scoping belongs in code, not in prompt instructions).

**Error handling:** surface structured errors to the model itself (let the
model decide retry/ask-user/escalate, don't silently swallow failures into
a generic "something went wrong" — that anti-pattern denies the user real
information and the model any chance to recover); cap retries per call and
per full request, with a clean fallback response when the cap is hit.

**Reference shape given** (matches the Ch 11 billing-specialist running
example): read-only tools only; permissions scoped to the authenticated
user via prompt *and* implementation; clear names/descriptions; structured
concise outputs; legible errors; the model drafts but never claims an
action it didn't take; a guardrail enforces that no false "I applied a
credit" language reaches output. **When to add a new tool:** only when
there's a task the model genuinely cannot complete without it *and* at
least 20% of user requests need that task — every tool is a maintenance
commitment and a new potential failure mode, not a free capability.

### Chapter 13 — Retrieval

Framing: models are trained on a snapshot of the world and don't know your
company's documents, today's news, or last week's specific customer
question — retrieval (the book prefers this over "RAG" as the umbrella
term, since tooling has moved well past the 2020 formulation) is how you
give a model access to what it wasn't trained on. **Direct claim: the
quality of the final answer is capped by the quality of retrieval — if the
right document isn't in the top matches, the model cannot answer correctly
no matter how capable it is** — named as the part of the system most teams
underinvest in.

**Mechanics at query time:** turn the query into a search (keyword,
semantic, or both) → fetch top matches from the knowledge store → include
them in the model's prompt → generate the answer from what was retrieved.

**Keyword vs. semantic search:** keyword matches literal query words
against document words — fast and precise when vocabulary matches, blind
to paraphrase (misses "accounting of income" when the query says "revenue
recognition policy"). Semantic search embeds query and documents as
vectors and matches by meaning — catches paraphrase, but can surface
thematically-close-but-not-actually-relevant results. **Production answer:
hybrid retrieval (run both, combine, rerank) — most retrieval-quality
improvement comes from tuning this combination**, not from a fancier
single method.

**Chunking — "the decision most teams get wrong."** Rules given: respect
document structure (chunk on sections/paragraphs/headings, never
mid-sentence or mid-table); size chunks to the task (200-500 tokens for
document Q&A, larger for summarization, smaller for code search); include
enough context in each chunk to stand alone (e.g., carry the parent
section's heading — Anthropic's Contextual Retrieval approach, adding a
short summary to each chunk at index time, is cited as measurably lifting
quality); overlap chunks 10-20% to catch information straddling a boundary,
without inflating the index too far. Called "not glamorous work" but "the
single highest-leverage place to improve retrieval quality for most teams."

**Ranking and reranking:** retrieve a wider candidate set (20-50), then run
a reranker (cross-encoder or specialized model — Cohere, Voyage, Jina named
as good hosted options) to pick the final 3-5 for the prompt. Called "one
of the cheapest upgrades in the retrieval stack."

**Retrieval needs its own separate eval suite**, three named metrics:
precision@K (fraction of top-K retrieved docs that are actually relevant),
recall@K (fraction of all truly-relevant docs the top-K actually caught),
faithfulness (does the generated answer actually use the retrieved context,
or did the model ignore it and hallucinate — usually checked with an LLM
judge). Stated reason for keeping these separate from overall system
evals: **without them, when quality drops you cannot tell whether
retrieval degraded or generation did.**

**Patterns beyond the basics** (2025-2026 mainstream, none required —
"worth knowing for the moment you need one"): contextual retrieval (short
per-chunk summary before embedding, per Anthropic's published version);
agentic retrieval (the model decides what to search for and iterates,
more flexible and more expensive, usually worth it for complex research
tasks); GraphRAG (knowledge-graph-based retrieval for entity-relationship-
rich data, Microsoft's implementation cited as the reference); multi-vector
retrieval (multiple embeddings per chunk — title/summary/full-text —
searched together, helps when query specificity varies); caching
(remembered retrievals for common queries — Anthropic's prompt caching
works at the model-call level, application-level caching works at the
retrieval level).

**Pre-ship checklist, given as five required conditions, not optional
polish:** chunking respects document structure; hybrid search (semantic +
keyword) is in place; reranking runs on top candidates; separate retrieval
evals measure precision/recall/faithfulness; a real fallback exists for
when nothing relevant is found (tell the user, don't guess). **"If any one
is missing, the failure mode is predictable — know which one you're
missing before you launch."**

### Chapter 14 — Memory and Long-Running Agents

**Short-term vs. long-term.** Short-term memory (the current conversation,
held in the context window) is "solved" — include prior turns, summarize
if long. Long-term memory (persisting across sessions — user preferences,
facts learned previously, decisions already made) is "where the
interesting design work happens."

**When memory is worth adding, stated as a direct cost/benefit call.**
Worth it: personalization over time (a writing assistant that remembers
voice, a research agent that remembers trusted sources), multi-session
projects (a coding agent that remembers project structure, a legal
drafting assistant that remembers the client matter), cumulative learning
(rare, real for some specialized copilots). Tempting but not worth it:
single-session tasks (memory buys nothing, adds risk), tasks where fresh
context is actually safer (compliance review, audit — prior-conversation
drift could introduce subtle errors), tasks retrieval already solves
(if you can look up relevant history at query time, you don't need a
persistent memory layer — retrieval is "often simpler and safer"). **Rule
given directly: when in doubt, start without memory; add it only when a
specific use case proves it's worth the engineering complexity, new
failure modes (stale/incorrect memory, cross-user leaks), and evaluation
overhead it costs.**

**Short-term memory patterns:** full history (every prior turn — breaks on
long/expensive conversations), sliding window (last N turns only — cheap,
loses early context), summarized history (oldest turns compressed to a
running summary, recent turns kept verbatim — named as **what most
production chat systems actually do**).

**Long-term memory's three components:** storage (a database or vector
store, each entry carrying content + timestamp + who/what metadata),
retrieval (almost always semantic search against the memory store, top
matches included in the prompt), write policy (named "the hardest part" —
when/what to remember; remembering everything bloats the store with noise,
remembering selectively risks missing what mattered). Common write
policies given: explicit user requests ("remember I prefer short
summaries"), decisions made in-conversation, identifiers/references, and
per-session-end summaries.

**Memory evaluations — three questions, distinct from main system evals:**
is the right memory being retrieved (precision/recall, same framing as
Chapter 13's retrieval evals)? Is the memory still accurate (a system
returning stale memories is *worse than no memory at all*)? Does the write
policy actually capture what matters (test: a week later, can you answer
questions about the conversation using only the memory entries)? Cadence
recommended: weekly or monthly against a rolling set of recent
conversations — "most teams underinvest here and pay for it later when
users complain the system keeps 'forgetting' things they explicitly said."

**Long-running agents** (work autonomously for minutes/hours+) — named as
one of the hardest system categories to get right and where "the most
ambitious 2026 systems live." Key design elements: checkpointing (save
state at natural pause points so the agent can be paused/inspected/
resumed — LangGraph's checkpoint primitives cited as the most mature public
implementation), time/cost budgets (hard caps with graceful termination on
breach), observability (see Ch 16), human intervention (a human must be
able to pause/inspect/redirect at any point — "long-running agents without
this always eventually take an unwanted action").

**Three memory failure modes worth knowing going in:** cross-user leakage
(a memory from User A's session surfaces in User B's — called "the
absolute worst failure mode for memory systems"; always scope memory to a
user at both write and read time, test cross-user isolation explicitly);
memory poisoning (a user plants a memory that manipulates future behavior
— less studied than prompt injection but a real concern for open systems;
treat memory writes like user input: sanitize, scope, verify); runaway
memory growth (no eviction policy → the vector store becomes "a graveyard
of stale entries that hurt retrieval quality" — design eviction from the
start: time decay, user-initiated deletion, relevance scoring).

### Chapter 15 — Multi-Agent Systems

Opens by naming the trap directly: multi-agent "reads as sophisticated...
every AI conference has a talk on it... every framework has a multi-agent
abstraction" — the chapter's explicit stated purpose is to **talk builders
out of building one most of the time**, then give the patterns that hold
up in production for the cases that genuinely need it.

**Four gate questions before even sketching a multi-agent architecture** —
if any answer is no, stay at workflow or single-agent: does a single
well-designed agent actually fail at this task? Does a workflow (Ch 11)
fail at it (many things that *feel* multi-agent are actually workflow
problems — "a router and specialists is a workflow, and it solves a broad
class of 'multi-agent' problems cleanly")? Do you have the eval harness to
measure a multi-agent system (trajectories across multiple agents,
interactions to trace, emergent failure modes — "if your evals are not
ready for this, your multi-agent system is not either")? Is your team
ready to debug one (failures are non-local — a bug in one agent's prompt
can surface as weird behavior three agents downstream)?

**When multi-agent is actually the right shape:** large open-ended
research tasks (concurrent exploration + synthesis — deep research agents,
competitive intelligence), heterogeneous expertise (genuinely different
thinking styles per step, e.g. "think like an architect" vs. "think like a
code reviewer" in software engineering), long-running collaborative work
(parallel tracks over hours, periodic synthesis — "ambitious but rare in
production"), simulation and debate (value comes specifically from
multiple perspectives interacting). **Explicitly named as NOT belonging
here — customer support, document review, compliance checking, data
extraction: "the bread and butter of enterprise AI work. These are
workflow problems."**

**Three topologies, when you do build one:** orchestrator-and-workers (one
orchestrator plans/delegates/synthesizes, workers scoped to subtasks, only
the orchestrator holds the full picture — clean boundaries, straightforward
eval; **named the most common in production and the book's own default
recommendation**); peer-to-peer (agents communicate via shared message
bus/state, useful for simulation/debate/collaborative drafting, harder to
evaluate because interactions are non-linear); hierarchical (orchestrators
directing sub-orchestrators directing workers — necessary for genuinely
complex tasks, dangerous for most others because the failure surface grows
fast).

**Inter-agent communication, three patterns:** shared state (all agents
read/write one data structure — scales well, easy to inspect, no
message-passing overhead; **named what most production systems converge
on**); message passing (structured messages between agents — more
flexible, introduces ordering issues and harder debugging); structured
handoffs (an agent finishes, packages a clean summary, passes control
onward — the pattern OpenAI's Agents SDK uses). **For most enterprise
multi-agent systems: shared state plus structured handoffs is the simpler
and usually better architecture.**

**Failure modes specific to multi-agent systems** (that single-agent
systems don't exhibit): loops (Agent A asks B, B asks a clarifying
question, A repeats its original question, B asks again — "can run until a
budget stops them," always set a step budget); goal drift (each agent
takes a small liberty with the task; three agents in, the system has
quietly redefined its own job — counter with a canonical goal statement
every agent sees every turn); responsibility fuzziness (two agents both
think they own something, or neither does — fix with explicitly exclusive
scopes); compounding errors (Agent A errs slightly, Agent B reasons over
A's output as if correct, the error compounds — independent per-agent
evals catch this before it propagates); cost explosions (each agent is its
own LLM call, often with its own tool calls — set cost budgets, alert on
approach, kill gracefully on breach).

**Evaluating multi-agent systems extends single-agent evals with:**
per-agent evals (each agent scoped to its own role — a router gets a
routing-accuracy eval, a writer gets a quality eval), trajectory evals (did
the system take a reasonable step sequence, call the right agents in a
sensible order — usually needs an LLM judge over the full trace),
end-to-end evals (did the final output meet the user's actual goal — same
framing as single-agent, applied to the whole system), cost/step evals
(steps taken, cost incurred, tracked as a distribution with tail-case
alerts). **Stated rule of thumb: multi-agent eval effort runs roughly 3x
single-agent eval effort — plan for it.**

**One real named example:** Google DeepMind's AI Co-Scientist — six
specialized agents (generation, reflection, ranking, evolution, proximity,
meta-review) proposing research hypotheses collaboratively, with honest
public documentation of its own design/evaluation. Offered explicitly not
as an enterprise blueprint ("your use case is almost certainly not
open-ended scientific research") but as a reference for what a
well-designed multi-agent system looks like when the task genuinely
requires one.

**Chapter's own closing line, stated directly: "For 90% of enterprise AI
teams reading this chapter, the right multi-agent answer is: not yet.
Build workflows. Build single agents where workflows fall short. Keep your
evals solid. Ship, learn, iterate... Until then, stay simple."**

## Part 1 remainder: The Landscape (compiled — Chapters 2-3, pp. 21-30)

### Chapter 2 — What Enterprises Are Building

**The shift from pilots to production (2023→2026):** cites McKinsey's State
of AI survey (majority of enterprises now use gen AI regularly, up from
roughly a third two years earlier) and Menlo Ventures' 2025 State of AI in
the Enterprise (spending well into tens of billions, steepest growth in
production-grade systems, not experiments). **Named gap this creates:**
teams that succeeded at pilots didn't always succeed in production — the
work that closes that gap (eval harnesses, guardrails, observability,
retraining loops) is explicitly what "Chapters 6 through 18 of this guide
are mostly about."

**Five categories where enterprise AI value is actually landing, in
order:** internal knowledge/support (largest by spend — Q&A systems,
onboarding, help-desk routing; cleanest ROI case: fewer tickets, faster
onboarding); document processing/extraction (contract review, invoice
processing, compliance checking — natural fit since long documents are
structured enough and errors are catchable); coding copilots (GitHub
Copilot, Claude Code, Cursor — "the category with the clearest adoption
numbers"); customer-facing assistants (less dominant than internal tools
because the risk bar is higher, growing as guardrails mature); research
and analysis workflows (literature review, competitive research, market
analysis — often built on retrieval). **Named absence, stated directly:
fully autonomous agents doing complex multi-step work without human
oversight are still rare in production — "agentic patterns ship, but they
ship with a lot of workflow scaffolding around them."**

**Patterns that work, across production systems that stuck:** augment
first, automate later (human stays in the loop, system proposes/drafts,
automation expands only as evals prove each step safe); narrow scope, deep
quality (a single well-built narrow system beats a broad "AI assistant for
everything" — narrow scope makes evaluation tractable); retrieval over
fine-tuning for knowledge (fine-tuning is for style/format/tightly-scoped
behavior, retrieval is for knowledge — this book's consistent position,
matching Chapter 13); workflows before agents (the router-and-specialist
pattern is the most common production shape — "teams that tried free-
roaming agents first often came back to workflows later"); evaluation as
durable infrastructure (same CC/CD framing as Chapter 6 — teams that
maintain evals continuously improve, teams that treat evals as a
launch-checkbox see quality drift within months).

**What's failing, traced to one of three root causes in almost every named
enterprise AI post-mortem:** no clear problem (project started from "we
should use AI" rather than a named pain — "the single most common cause of
failure," preventable with 30 minutes of upfront problem discovery, per
Chapter 4); no evaluation discipline (looked good in demos, no way to tell
why it failed in production — what Chapters 6-9 build the muscle against);
over-scoped agentic design (a multi-agent system attempted for a problem
that needed a workflow — failure modes compound, debugging gets expensive,
project can't ship — per Chapters 10/15). **Pattern named across all
three: each failure mode is a sign of skipping the boring work.**

### Chapter 3 — Models: How to Choose

Opens with a direct framing move: **"picking a model is the question
builders want to answer first and should often answer last."**

**"There is no best model," two reasons given:** frontier models cluster
close enough on general benchmarks (MMLU, HumanEval, GSM8K) that the gap
between them is often smaller than the variance a prompt-design choice
introduces on the *same* model (stated: "the gap between the top three
closed models in any given month is often within a few points... the gap
between a good prompt and a bad prompt on the same model can be twenty
points"); and your task isn't the benchmark — a model dominating MMLU may
be average on your specific retrieval-synthesis task, so **the only
comparison that matters is your own evals run on your own task.**

**Six dimensions that actually move a production decision:** capability
(on your own evals — the dimension teams over-focus on, then discover the
others matter as much); latency (reasoning models: 20-60s; standard
models: 1-3s — a customer-facing product concern, irrelevant for a
background batch job); cost (per-token pricing varies 10x across
providers, 100x between frontier and small models — "a high-volume
workflow can easily be the difference between $200/month and
$20,000/month"); context length (200K standard, 1M available from
multiple providers in 2026 — bigger isn't automatically better, attention
quality can degrade past a point, but a larger window can simplify
retrieval design); modality (text/vision/audio/tool-use/structured-output
— match to actual input types); reasoning capability (a distinct trained
class — Claude extended thinking, OpenAI o-series, Gemini thinking,
DeepSeek-R1 — slower/costlier but often dramatically better on multi-step
problems); licensing/deployment (closed API-only vs. open (Llama, Mistral,
Qwen) vs. hosted-open (Together, Fireworks, Groq) — matters for data
residency or on-premise requirements).

**The decision framework, given as a named three-step rule: "start
capable, downsize where you can, escalate when you must."** Start capable
— prototype with the strongest affordable model (Claude Opus 4.7/Sonnet
4.6, GPT-5, Gemini 2.5 Pro named) so you're not debugging prompt problems
and model limitations simultaneously. Downsize where you can — once the
system works end-to-end, swap cheaper/smaller models into components where
quality doesn't degrade (simple classifiers/routing/narrow specialists
often perform nearly identically on Claude Haiku 4.5 or GPT-5 mini at a
fraction of cost — the Chapter 11 router-specialist pattern named as the
perfect fit: cheap fast model routes, capable model handles the hard
specialist work). Escalate when you must — only move to a reasoning model
when evals plateau below the needed bar and prompt engineering/retrieval
improvements are exhausted; reasoning models are "overkill for most tasks
but transformative for the few where they help": multi-step planning,
complex code, careful document analysis, decisions requiring shown work.

**Open vs. closed, 2026 read:** open models (Llama 4, latest Qwen,
DeepSeek V3/R-series) are named "genuinely competitive with frontier
closed models on many benchmarks" — reasons to choose open: data
residency, predictable cost at scale, hard behavioral controls,
fine-tuning for narrow tasks, avoiding lock-in. Reasons to choose closed:
the actual frontier for hardest reasoning is still closed (Opus 4.7,
GPT-5, Gemini 2.5 Pro named), higher API maturity, more reliable tool
use/structured output, zero self-hosting overhead. **Most 2026 enterprise
systems use both** — frontier closed for the hardest parts, an open model
on a hosted-inference platform for high-volume simple parts; "the mix is
cost engineering." **Chapter's closing line: "your evals beat any
benchmark" — everything else in the chapter narrows the choice, nothing
replaces running it against your own evals.**

## Part 2: Designing AI Products (compiled — Chapters 4-5, pp. 32-42)

### Chapter 4 — Problem-First Design, Revisited

Opens with a direct causal claim: **"every AI project that fails in
production traces back to a design decision made months earlier... before
anyone wrote a single prompt."** Named contrast with traditional software:
a weak problem statement there still usually produces a *working* system
(expensive but recoverable); in AI, a weak problem statement produces a
system whose outputs "look plausible but drift in ways you cannot
predict" — the evals never catch what was never specified, and six months
later nobody's sure whether the fix is a better prompt, model, or dataset.
**"Problem-First Design is the cheapest insurance you can buy against
this failure mode... thirty minutes of clean problem definition upfront
saves months of unclear iteration later."**

**The Four Layers Framework** (the book's own design-conversation
structure, "maps roughly to Marty Cagan's product framing, adapted for
AI's specific failure modes" — must be written in order, each fitting one
paragraph): **Layer 1, The User and Their Pain** — named role, actual
task, measurable pain, stated with a concrete worked example ("compliance
analysts spend 90 minutes per filing checking disclosure completeness,
and miss 3-5% of required items"); **Layer 2, The Outcome** — what changes
when the system works, written *before* the system itself ("analyst
completes a filing check in under 20 minutes, with miss rate under 1%");
**Layer 3, The AI Intervention** — the narrowest useful definition of what
the system actually does: specific pattern (retrieve-and-check,
draft-and-review, classify-and-route) plus specific capability
(summarization, extraction, classification, generation) — named as the
layer most often bloated in failed projects, "narrow it until it hurts";
**Layer 4, The System and Safety** — the production scaffolding: evals,
guardrails, observability, human oversight, rollback, audit trail. **Stated
rule: if Layer 2 is vague, no amount of clever Layer 3 work saves the
project.**

**Six design traps named from "thirty-plus enterprise implementations,"
recognizing one is usually enough to avoid it:** tech-first thinking
("we want to use AI for X" — AI is the given, not the problem; every
project that leads with technology ends up building something without a
real user); over-scoping (three related problems packed into one system —
none get done well, none can be evaluated; split them); problem with no
owner (a vaguely-agreed pain nobody specifically has to live with — no
named owner means no measurable outcome, and the project drifts);
solutioning in the problem statement (e.g. "build an LLM that uses RAG
over our document store with a workflow agent on top" — this describes an
architecture, not a problem; the actual pain — who hurts, where, how much
— is missing, and should come first with architecture following from it);
skipping the human baseline (building without ever measuring how long the
task takes a human today, or how often they get it wrong — without a
baseline you structurally cannot tell if the AI system is actually an
improvement); confusing pilot success with production readiness (a
curated-data, selected-user pilot doesn't reveal how the system holds up
against real edge cases — "most teams skip the hard transition").

**A concrete scoping template given verbatim**, to fill in collaboratively
with the user and engineering team in the room *before* any design starts
(the act of filling it in is stated to surface every unresolved
disagreement before code gets written): Who is the user? (named role, not
"employees"). What are they doing today, and how is it painful? (current
workflow, timed, error rate measured, ideally a direct quote). What would
change if the new system works? (new workflow description, acceptable
error rate). What is the single AI capability at the core? (one sentence,
one pattern — "if you cannot say it in a sentence, the system is too
complicated"). What does "ready to ship" mean? (specific eval scores,
specific guardrail coverage, a human fallback, a rollback plan). What can
go wrong, and what happens when it does? (enumerate failure modes, map
each to a recovery path).

**Designing for iteration:** AI systems are framed as living in a
deploy→observe→learn→improve→redeploy loop, not build-once artifacts —
practical implication: design the first version as the simplest thing
that could work, ship it in front of three real users, watch what breaks,
fix the top problem, ship again; resisting the pull to build the "full
end-state architecture" before shipping anything, since "the cost of being
wrong about the design is much higher than the cost of shipping something
small." Named as the design-time twin of Chapter 6's CC/CD operational
framework.

**Explicit caveat closing the chapter: "Problem-First Design is a
discipline for the first thirty minutes of a project, used well and then
set aside"** — once the problem is clear and the system ships, most time
should go to evaluation and iteration (Chapters 6-9), not endless
re-scoping meetings when the real issue is slow execution.

### Chapter 5 — Prompting and Context Engineering

Opens by explicitly rejecting the shallow version of this chapter ("a list
of twenty prompting techniques") in favor of naming the actual 2023→2026
shift: prompting (the craft of phrasing a single instruction well) has
been subsumed by **context engineering** — "the discipline of deciding
what goes into the model's context window, in what order, with what
structure." Prompting is named one piece of that larger discipline, not
its replacement.

**The six parts of a working prompt** (present even when implicit — making
them explicit is named the fastest quality lever): role (who the model is
acting as — anchors tone/scope/default behavior, e.g. "you are a billing
support specialist"); context (the operating situation — authenticated
user, current document, relevant policy; explicitly *not static*, assembled
at runtime from the user, retrieval layer, and tool results in a real
system); task (one clear instruction — "if you find yourself writing three
tasks, consider splitting into three prompts"); constraints (what the
model must not do, or must do a specific way — concrete examples given:
"never claim you applied a credit," "cite the policy ID for every claim,"
"respond in under 200 words"); examples (two-three input-output pairs for
non-obvious patterns — **named the highest-leverage tool in the whole
prompt toolkit** for anything subjective or structured); output format
(JSON schema, markdown template, a specific tag set — "the interface
between your model and everything downstream"). **Order matters: models
weight the earliest and latest sections of a prompt most heavily — most
teams put role/context first, task/constraints in the middle, examples
before a final output-format reminder.**

**Prompting reasoning models is explicitly different — three rules that
change, not just a style tweak:** less hand-holding (reasoning models
already do their own step-by-step thinking — telling them to "think step
by step" is redundant and "sometimes harmful"; describe the goal and
constraints, let the model reason on its own); more context, less
structure (where standard models benefit from tight pre-processed
structure, reasoning models often do better given the full picture rather
than a heavily pre-processed summary); separate the what from the how
(state the goal and what success looks like, skip procedural how-to-get-
there instructions). **Compressed framing given: "for standard models you
are scripting the task. For reasoning models you are briefing a capable
specialist."**

**Context engineering, the bigger picture:** a real production request is
described as assembled dynamically from up to five sources every time the
model runs — system prompt (role/rules), running conversation history,
retrieved documents (e.g. three chunks at ~300 tokens each), tool
definitions (schemas for callable tools), tool results (output from a
previous call), and the current user message. The discipline is about
what goes in, what stays out, in what order, and how to compress/summarize
as the window fills — "the difference between a prototype that works on
short conversations and a system that holds up across a ten-turn customer
support thread." **Four practical principles given** (the same four
already logged verbatim in Chapter 1's context-engineering entry, restated
here as production practice): recency matters (keep the most important
context near the end of the prompt — models attend more strongly to
recent content); summarize when you compress (don't just truncate long
conversations — summarize old turns into a running summary preserving key
facts); retrieve what you need, when you need it (pull relevant chunks at
the moment they're relevant, don't front-load everything); keep tool
definitions stable (frequently changing tool schemas confuse models —
stabilize the interface, iterate the logic behind it instead).

**Few-shot examples, restated as "the single highest-leverage
[prompting] technique"** if only one could be taught — two to three
example input-output pairs "consistently outperforms almost any other
single intervention" on subjective or structured tasks, for three named
reasons: they teach the pattern without describing it abstractly, they
calibrate tone/style (hard to describe in words), and they resolve task
ambiguity implicitly. **Rules for picking good examples:** cover real-case
variety (not just the easy cases), include one-two edge cases (not only
distribution-middle cases), cover every category at least once if the
task has categories, and update examples when the task changes ("stale
examples become a drag on quality").

**Output format — "the interface nobody talks about."** Three choices
covering most production systems: structured JSON (for anything a
downstream *machine* consumes next — schema-guaranteed by all major
providers); markdown (for anything a *human* reads directly — clean,
supports lists/bold/code blocks, a good chat-interface default); tagged
sections (mixed structured+narrative output — e.g. `<reasoning>...
</reasoning>` and `<answer>...</answer>` — easy to parse, flexible for the
model). **Rule: match the format to the next consumer, not to what feels
natural to write.**

## Remaining chapters — TOC map only (not yet read)

**Parts 1-4 (Chapters 1-15) are now fully compiled above.** Only Parts 5-6
remain:

| Part | Chapters | Subject | Priority for next pass |
|---|---|---|---|
| 5: Production and the Long Arc | 16. Observability and Tracing; 17. Protocols and Extensibility; 18. Production Readiness Checklist | Logging/tracing setup, MCP + A2A + Agents SDK, launch checklist | **High — Ch. 17's MCP section is directly relevant to `protocols/mcp/`, and Ch. 18 is the book's own capstone checklist** |
| 6: Where to Go Next | 19. Role-Based Learning Tracks; 20. The Horizon; Master Resource Index | Reading paths by role, 2026 forward-look, curated resource bibliography (by source/topic/type, pp. 134–143) | Medium — the Master Resource Index is worth mining as a reference list now that Parts 1-4 are done; 19-20 lower priority narrative |

## Volatile claims requiring re-verification at point of use

Same discipline as this hub's other current-tech sources
([[mastering-claude-ai-dickey-consumer-guide]]): context-window sizes,
named model versions, and pricing in this book are correct as of April
2026 and will drift. Re-check against live provider docs before citing a
specific number.

## Overlap notes (why the other five queued books were not also compiled)

- Both dedicated prompt-engineering books (Berryman & Ziegler;
  Phoenix & Taylor) cover the same §1.3/Chapter 5 territory this book and
  `AI_engineering.pdf` (Huyen)'s Chapter 5 already address — genuine depth
  exists in the dedicated books, but not a compile priority while three
  sources already cover the surface. `AI_engineering.pdf` has no wiki page
  yet — TOC-classified only this session, see [[../raw-source-coverage]].
- `agentic_AI_for_engineers.pdf` overlaps this book's Part 4 territory but
  opens with a more general ML/AI-foundations survey (supervised/
  unsupervised/RL, NLP, computer vision) this hub already has adjacent
  coverage for; its agentic-specific chapters are lower priority than this
  book's Part 4 given this book's more current, practitioner-checklist
  depth.
- `Generative_AI_economic_potential.pdf` (McKinsey, June 2023) is now a
  dated snapshot superseded by already-compiled
  [[../adoption-delivery/ai-index-2026]] and
  [[../adoption-delivery/work-trend-index-2024-2026]].

Full disposition for all six: [[../raw-source-coverage]].
