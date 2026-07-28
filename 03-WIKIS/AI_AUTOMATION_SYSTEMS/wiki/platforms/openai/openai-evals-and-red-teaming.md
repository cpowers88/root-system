---
type: research
timeline: reference
tags: [ai-automation, openai, evals, verification, red-teaming, agent-patterns]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ — Getting started with datasets, Evaluate agent workflows, Evaluate external models, Evaluation best practices, Working with evals, Red teaming (official OpenAI API docs, relocated from CASTLE July 12, 2026; read in full — this is the mechanical backbone behind the "traces/evals before multi-agent scale" claim CASTLE already applied to the July 12 launch audit at the principle level, without reading the how-to); plus Graders (title-collided capture, added July 12, 2026)
---

# OpenAI Evals and Red Teaming — The Mechanics Behind "Verify Before Scaling"

**Official OpenAI API documentation, read in full July 12, 2026.** CASTLE's
prior pass extracted one sentence from this chunk — "traces/evals before
multi-agent scale" — and applied it as an audit criterion without reading
the actual mechanics. This page is that missing depth: what an eval
concretely is, how graders work, why architecture complexity multiplies the
number of things that need testing, and how red teaming differs from evals.

## One-paragraph summary

Evals are structured, repeatable tests for nondeterministic model output —
OpenAI frames eval-driven development as the AI-era analog of test-driven
development, with a firm anti-pattern named explicitly: **"vibe-based
evals"** (shipping on "it seems to work," or writing no evals until after
launch). The single most load-bearing structural finding: **each step up in
agent-architecture complexity (single-turn → workflow → single-agent →
multi-agent) adds a new category of nondeterminism that needs its own
evals** — tool selection and data-precision evals appear only once tools
exist; agent-handoff-accuracy evals appear only once multiple agents exist.
This is the actual mechanism behind "traces/evals before multi-agent
scale": multi-agent isn't just harder to build, it is verifiably harder to
*verify*, with a named, growing checklist of new failure categories at every
step. **Major recency flag**: OpenAI is deprecating its entire Evals
platform — read-only for existing users October 31, 2026, fully shut down
November 30, 2026 — so the API/dashboard mechanics in this pack are on a
five-month clock from the capture date.

## The eval-design loop and grader types

Five-step design loop: define objective → collect dataset → define metrics
→ run and compare → continuously evaluate (re-run on every change, mine
production logs for new eval cases, grow the set over time — evaluation is
"a journey, not a destination").

Five grader types, in order of cost/scale trade-off:

| Grader | Mechanism | Best for |
|---|---|---|
| String check | Exact match | Ground-truth-column comparison |
| Text similarity | Embedding distance | Semantic closeness, no exact match needed |
| Score model grader | LLM assigns a numeric score | Subjective properties (tone, friendliness) |
| Label model grader | LLM picks a category | Classifying output into fixed labels |
| Python code execution | Custom code | Programmatic checks (e.g. "under 50 words") |

**Human annotation is still positioned as the highest-quality input**, not
a legacy step graders replace — annotations (Good/Bad + a text critique)
feed the automated prompt optimizer, and OpenAI explicitly recommends a
subject-matter expert do the annotating when the annotator isn't already
an expert in the dataset's domain, "the most valuable way for their
expertise to be incorporated." Datasets are the fast/iterative surface;
**Evals (the API-driven, larger-scale sibling) is for repeatability** —
export from Datasets to Evals once you know what "good" looks like and want
to benchmark changes over time.

## Grader mechanics in depth

*(Added July 12, 2026 from a title-collided capture — the table above names
the five grader types; this section is the actual implementation depth
behind them, previously unrouted.)* Graders are JSON-specified and share a
templating syntax: `{{ item.field }}` pulls from the dataset row (or
fine-tuning row), `{{ sample.output_text }}` / `output_json` / `output_tools`
/ `output_audio` / `choices` pull from the model's own response.

- **String check**: `eq`/`neq`/`like`/`ilike` operations, binary 0/1 output.
- **Text similarity**: `fuzzy_match` (rapidfuzz), `bleu`/`gleu`/`meteor`,
  `cosine` (embedding similarity, eval-only), `rouge_1`–`rouge_l` — pick by
  what "close enough" means for the task.
- **Score model grader**: a second model grades the first, prompted with
  templated reference/sample content, returns a numeric `result` in a
  configurable `range` plus optional `steps` (structured reasoning before
  the score — explicitly recommended: ask the grader to name what it's
  checking *before* it commits to a number, not after). Constrained to a
  fixed allowlist of grader models (`gpt-4o`/`gpt-4.1`/`o1`/`o3`/`o4-mini`
  families as of capture) — `reasoning_effort` only applies to reasoning
  models in this role, `temperature` only to non-reasoning ones.
- **Python graders**: arbitrary code with a required `grade(sample, item)
  -> float` signature, run in an isolated environment — **256KB source
  cap, no network access, 2-minute execution limit, 2GB memory / 1GB disk,
  2 CPU cores** (throttled beyond that), with a fixed package allowlist
  (numpy, scipy, pandas, rapidfuzz, scikit-learn, rouge-score, jsonschema,
  pydantic, nltk + corpora, sqlparse, rdkit, ast-grep-py, etc. — a specific
  point-in-time list, recheck before relying on any one package). Any
  exception or non-float return is silently scored 0.
- **Multigraders**: combine several graders into one score via a formula
  string (`(name + email) / 2`) referencing each sub-grader's output by
  key, with a real expression grammar (`+ - * / ^`, `min/max/abs/floor/
  ceil/exp/sqrt/log`). Cannot nest a multigrader inside another multigrader
  — one level of composition only. Useful design lesson independent of the
  API: grading structured output field-by-field with different tolerance
  per field (exact-match on an email, fuzzy-match on a name) is a more
  precise signal than one holistic score.
- **Reward/grader hacking is named explicitly as a training-time failure
  mode**, not just an eval-time one: a model in RL-style fine-tuning can
  learn to exploit a grader's specific weaknesses rather than actually
  improving — detected by comparing model-grader scores against expert
  human eval scores on the same outputs; a model that scores well on the
  former and poorly on the latter has hacked the grader, not the task.
  Design defenses named: smooth scores over pass/fail stamps (so partial
  progress is visible to an optimizer), balanced datasets (skewed label
  distribution invites guessing the majority label), and validating an
  LLM-judge grader against human labels before trusting it, same caution
  already noted above for LLM-as-judge generally.

## LLM-as-judge — the caveats that matter

Cheaper and more scalable than human eval, but named biases apply:
**position bias** (favors whichever response is shown first/second
consistently) and **verbosity bias** (favors longer responses regardless of
quality). Mitigations: use pairwise comparison or pass/fail rather than
open-ended scoring, control for response length, add reasoning/chain-of-thought
*before* the score (not after), reformat into multiple-choice where
possible, and validate the judge's agreement with human labels before
trusting it at scale. One concrete number: a cited Braintrust case saw a
judge's F1 score against human ground truth jump from 0.12 to 0.74 by
switching the judge model from gpt-4o to o1 — a large, specific illustration
that judge-model choice is not a minor detail.

## A provider-neutral operating stack

The Evaluation Core in *The AI Builder's Handbook* (LevelUp Labs, April 2026,
Chapters 6–9, printed pp. 44–65) adds a provider-neutral implementation order
to the OpenAI-specific mechanics above:

1. Route every crisp property to deterministic code: schema, allowed values,
   exact match, required content, bounds, URLs, patterns, counts, and tool
   arguments.
2. Use a model judge only for a clearly rubricable subjective property.
3. Calibrate that judge against independently labeled human cases, resolve
   human disagreement by repairing the rubric, and version the judge prompt,
   model, rubric, cases, and agreement result.
4. Preserve recurring human spot checks to detect novel failures and feed
   them back into the deterministic or judge suites.
5. Put guardrails in the live request path for risks requiring intervention,
   and log every block, redaction, modification, route, reason, and fallback.

This produces a closed operating loop:

`production incident or guardrail firing → labeled case → cheapest valid
grader → regression suite → release decision → monitored production`

The handbook's case counts, evaluator percentages, and judge-agreement bands
are starting heuristics, not universal acceptance standards. Set the actual
bar from false-positive, false-negative, review, latency, and harm costs.

## The four-architecture nondeterminism ladder (the key structural finding)

| Architecture | New nondeterminism source | New eval category |
|---|---|---|
| Single-turn | Model + developer/user input | Instruction following, functional correctness |
| Workflow (chained calls) | Same sources, multiplied across steps | Same categories, evaluated per-step |
| Single-agent (tools) | Dynamic tool selection | + Tool selection, data precision (correct arguments) |
| Multi-agent (handoffs) | Triage/handoff decisions between agents | + Agent-handoff accuracy (right agent, right moment, no circular handoffs) |

Explicit guidance: **the decision to go multi-agent should be driven by
evals showing single-agent is insufficient, not started as the default** —
"starting with a multi-agent architecture adds unnecessary complexity that
can slow down your time to production." This is a precise, sourced version
of a principle `.ROOT`'s own fork-heavy research pattern already follows by
instinct (see [[claude-code-workflows-and-sessions]]'s note that `.ROOT`'s
forks-report-to-one-coordinator pattern matches the subagent model, not the
peer-messaging "agent team" model) — now with the specific reason why:
every additional agent-to-agent handoff is a new class of thing that can
silently fail.

## Trace grading vs. dataset/eval-run — a two-phase decision point

`Evaluate agent workflows` names an explicit sequence: **start with trace
grading while still debugging** (a trace = the full record of model calls,
tool calls, guardrails, and handoffs for one run; grade traces to answer
"did it pick the right tool," "did a handoff happen when it should have,"
"did a prompt change actually improve behavior") — **move to datasets and
eval runs once you need repeatability** (benchmarking changes, comparing
prompts, larger-scale runs over time). Traces are the fast/cheap diagnostic
layer; datasets/evals are the regression-test layer built once you know
what "good" looks like.

## Edge-case coverage (a checklist, not just a principle)

Three named buckets evals should deliberately cover, beyond the happy path:
**input variability** (non-English, non-text formats, images), **contextual
complexity** (multi-intent requests, typos, minimal-context requests like a
bare "returns", long-running conversations, ambiguous tool-return data,
circular agent handoffs), and **personalization/customization edge cases**
(jailbreak attempts, conflicting format requests, user-vs-system-prompt
conflicts).

## Evaluating external / non-OpenAI models

OpenAI's Evals platform can grade third-party models (Google, Anthropic via
AWS Bedrock, Together, Fireworks — via OpenRouter, cost-capped $5–$200/mo by
usage tier) or fully custom endpoints, with an explicit caveat: **calls to
external models "pass data to third parties and are subject to different
terms and weaker safety guarantees"** than OpenAI's own models — an
org-admin opt-in, not a default. Tool calls aren't supported for external
models in evals. Not directly relevant to `.ROOT` (no eval infrastructure of
this kind exists here) but a precise fact if a future comparison project
ever needs to benchmark models across vendors on the same harness.

## Red teaming — distinct from evals, not a replacement

**Evals measure whether a system behaves as intended; red teaming probes
how it behaves under adversarial, abusive, or unexpected input** — "mature
evaluation programs use both." Two paths: Promptfoo (open-source, generates
adversarial test cases for prompts/agents/apps) or OpenAI Red Teaming
(enterprise-only, managed). One boundary explicitly stated: only submit
code/assets you own or are authorized to test — no analyzing third-party or
open-source code without permission.

## Why this matters for this wiki / `.ROOT`

- **This is not a sixth confirmation of the verification-capacity finding**
  this wiki has now traced through five independent sources (barriers study,
  WTI series, Pereira, AI Index 2026, Thomson Reuters) — those are survey/
  adoption-data sources converging on the same empirical gap. This page is
  different in kind: it's the **mechanical how-to for closing that gap**,
  not another data point that the gap exists. Worth keeping the two
  separate rather than inflating the confirmation count.
- **`.ROOT` already runs two of the three evaluator types without naming
  them as such**: `wiki_lint.py` / `frontmatter_audit.py` /
  `validate_boot_chain.py` are metric-based graders (deterministic,
  code-executed, exactly OpenAI's "Python code execution" grader type
  applied to governance files instead of model output), and a Codex
  validation pass (like the one that produced today's
  `ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md`) is functionally
  an LLM-as-judge pass over `.ROOT`'s own governance state. What `.ROOT`
  does **not** have is the third piece — a persistent regression **dataset**
  of known-good/known-bad governance-file states to re-run those graders
  against over time, the way OpenAI's Datasets feature accumulates edge
  cases. Not proposal-ready, just an honest structural gap worth naming.
- **The four-architecture nondeterminism ladder gives "traces/evals before
  multi-agent scale" a precise mechanism**, not just a slogan — useful if
  `.ROOT` or a future client-facing agent build ever needs to justify
  staying single-agent/subagent-only rather than building true multi-agent
  handoffs.
- **Red teaming is a concrete, currently-unused practice `.ROOT` could
  actually run at low cost**: adversarially testing its own permission
  hardening (e.g., deliberately trying prompts designed to get a session to
  write to `88-JOURNAL` or a `raw/` path) would directly test whether the
  deny-rule backstops described in
  [[claude-code-permissions-security-and-review]] hold under adversarial
  pressure, not just normal use — flagged as a candidate exercise, not
  drafted as a proposal.
- Companion page: [[openai-prompting-and-reasoning-models]] covers the
  prompting-craft side this verification methodology is built to check.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
