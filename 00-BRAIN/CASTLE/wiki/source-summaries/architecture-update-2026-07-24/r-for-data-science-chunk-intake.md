---
type: source-summary
timeline: reference
status: complete
tags: [castle, architecture, data-science, reproducibility, source-intake]
source: 03-WIKIS/TECHNOLOGY/raw/r_for_data_science.pdf
created: 2026-07-24
---

# *R for Data Science* — Chunk Intake

## Source Identity and Review Method

- **Source:** Hadley Wickham and Garrett Grolemund, *R for Data Science:
  Import, Tidy, Transform, Visualize, and Model Data*, O'Reilly, first
  edition (December 2016; copyright 2017).
- **Physical extent:** 520 PDF pages (front/back matter plus 483 numbered
  book pages).
- **Method:** complete PDF-page traversal in ~20-page consecutive chunks,
  written up after each chapter closes.
- **Character:** a specific-tool tutorial (R, the tidyverse, RStudio) rather
  than an architecture text. Most content is R syntax, package APIs, and
  RStudio keyboard shortcuts with no `.ROOT` architecture relevance — this
  report says so plainly per chapter rather than manufacturing a connection.
  The transferable material is concentrated in a few conceptual sections:
  the layered-grammar composability idea (Ch. 1), tidy-data's definition of a
  well-formed unit of evidence (expected in Ch. 9), and the *Workflow:
  Projects* chapter on paths, working directories, and reproducibility
  (Ch. 6) — flagged in the coverage ledger as the two remaining
  highest-relevance targets.
- **Raw boundary:** the original PDF remains unchanged; read-only via the
  Read tool.

## Coverage Ledger

| Unit | PDF pages | Status |
|---|---:|---|
| Front matter (cover, TOC, preface) | 1–28 | Complete |
| Chapter 1 — Data Visualization with ggplot2 | 29–61 | Complete |
| Chapter 2 — Workflow: Basics | 63–67 | Complete |
| Chapter 3 — Data Transformation with dplyr | 69–103 | Complete |
| Chapter 4 — Workflow: Scripts | 104–107 | Complete |
| Chapter 5 — Exploratory Data Analysis | 108–136 | Complete |
| Chapter 6 — Workflow: Projects | 138–143 | Complete (architecture-relevant) |
| Chapter 7 — Tibbles with tibble | 145–166 | Complete |
| Chapter 8 — Data Import with readr | 166–187 | Complete |
| Chapter 9 — Tidy Data with tidyr | 187–196 | Complete |
| Chapters 10–13 — relational data, strings, factors, dates/times | 197–286 | Complete |
| Chapters 14–17 — pipes, functions, vectors, iteration | 287–370 | Complete |
| Chapters 18–20 — model basics, building, many models | 371–448 | Complete |
| Chapters 21–24 — R Markdown and communication | 449–507 | Complete |
| Back matter and index | 508–520 | Complete |

## Front Matter — PDF Pages 1–28

- Standard O'Reilly front matter, acknowledgments, and a "What You Won't
  Learn" section: the book explicitly excludes big data, Python/Julia, and
  non-rectangular data, and commits to depth-first single-tool mastery over
  breadth. No `.ROOT` architecture relevance; this is a book-scoping
  decision, not a transferable system principle.
- **One durable framing device:** the book's own five-stage pipeline —
  Import → Tidy → Transform → (Visualize ⇄ Model) → Communicate, wrapped in
  Program — is a plain-language precedent for "evidence must move through
  ordered stages before it counts as knowledge." It parallels, at a much
  smaller and single-analyst scale, `.ROOT`'s System Loop; it is a naming
  precedent, not new evidence for CASTLE's specific stage boundaries.
- Confirms hypothesis-generation (exploration) and hypothesis-confirmation
  (preregistered, single-use-of-data) are genuinely different modes and
  should not be conflated — relevant echo of CASTLE's DIVERGE/CONVERGE
  distinction (`AGENT.md § Work Modes`), independent corroboration rather
  than new information.

### Front Matter Decision Contribution

**Keep:** DIVERGE/CONVERGE as already-adequate for the
explore-vs-confirm distinction this book also makes.

**Add to the synthesis queue:** none — the pipeline framing corroborates the
existing System Loop naming rather than adding a new mechanism.

**Reject as default:** none activated yet.

## Chapter 1 — Data Visualization with ggplot2 (PDF pages 29–61)

- Almost entirely `ggplot2` syntax (aesthetics, geoms, facets, stats,
  position adjustments, coordinate systems) — no direct `.ROOT` architecture
  relevance.
- **One transferable idea:** the "layered grammar of graphics" — any plot
  decomposes into exactly seven orthogonal parameters (data, geom, mapping,
  stat, position, coordinate system, facet), and composing those parameters
  can build "any plot you can imagine" from one small template. This is a
  concrete worked example of a durable architecture pattern CASTLE already
  values elsewhere (per `AI_builders_handbook` and `AI_engineering` intakes
  this same batch): a small orthogonal parameter set that composes instead
  of a large enumerated case list. Supporting, not new — a third
  independent domain (statistical graphics) landing on the same
  small-orthogonal-grammar shape as agent tool contracts and prompt/context
  engineering.

### Chapter 1 Decision Contribution

**Keep:** preference for small orthogonal parameter sets over large
enumerated option lists, wherever CASTLE already leans that way.

**Add to the synthesis queue:** none new — this is corroborating evidence
for an existing candidate principle, not a distinct mechanism.

**Reject as default:** none — chart-specific syntax not evaluated for
relevance.

## Chapter 2 — Workflow: Basics (PDF pages 63–67)

- Pure R mechanics: assignment (`<-`), object naming (`snake_case`
  recommended), calling functions, RStudio autocomplete/history shortcuts.
  No architecture relevance.
- **One general observation, not R-specific:** "there's an implied contract
  between you and \[the tool\]: it will do the tedious computation for you,
  but in return you must be completely precise in your instructions" — a
  restatement of why deterministic tools need exact, versioned inputs, a
  point already made more rigorously by the `AI_engineering` intake this
  batch (structured-output/validation findings). Not new.

### Chapter 2 Decision Contribution

**Keep / Add / Reject:** none activated — chapter has no material bearing
on the architecture question.

## Chapter 3 — Data Transformation with dplyr (PDF pages 69–103)

- Covers the five core verbs (`filter`, `arrange`, `select`, `mutate`,
  `summarize`) plus `group_by()` and the pipe operator. Almost entirely
  R/package syntax with no direct `.ROOT` architecture relevance.
- **Two general (non-R-specific) points worth naming:** (1) the pipe
  operator's stated justification — sequential, left-to-right, imperative
  "then" steps are easier to read than nested function calls or many named
  intermediate variables — is a plain interface-readability argument,
  already covered more rigorously elsewhere; (2) "whenever you aggregate,
  always carry a count of the underlying observations, or you'll draw
  conclusions from tiny, noisy samples" is a concrete data-quality
  discipline. It weakly echoes CASTLE's evidence-sufficiency concerns but is
  not new information — a specific statistical-analysis instance of "don't
  treat sparse or unrepresentative evidence as a settled fact."

### Chapter 3 Decision Contribution

**Keep / Add / Reject:** none activated — no distinct mechanism for
`.ROOT`; the count-before-concluding point is filed as weak corroboration
only.

## Chapter 4 — Workflow: Scripts (PDF pages 104–107)

- RStudio script-editor mechanics (keyboard shortcuts, running expressions
  vs. whole scripts). No architecture relevance. One line worth noting only
  as a restated norm: never put machine-specific setup calls
  (`install.packages()`, `setwd()`) inside a script meant to be shared,
  because it silently breaks on someone else's machine — a plain instance
  of the portability principle Chapter 6 develops properly.

## Chapter 5 — Exploratory Data Analysis (PDF pages 108–136)

- Defines EDA as an explicit iterative loop: generate questions → answer by
  visualizing/transforming/modeling → use answers to refine or generate new
  questions. States plainly that EDA "is not a formal process with a strict
  set of rules... more than anything, a state of mind," and that investigating
  data quality is itself EDA, not a separate cleaning step performed before
  it.
- The two organizing questions the whole chapter is built on — "what
  variation occurs within a variable?" and "what covariation occurs between
  variables?" — are a durable, tool-independent frame for any exploratory
  evidence pass, not specific to R.
- Gives the formal vocabulary this book uses for a well-formed data unit,
  ahead of Chapter 9's full treatment: *variable* (a measurable quantity),
  *value* (its state at one measurement), *observation*/*case* (one set of
  jointly measured values), *tabular data* is *tidy* when each value has its
  own cell, each variable its own column, each observation its own row.
- **Outlier/unusual-value discipline, stated as an explicit rule:** don't
  drop rows with implausible values by default (dropping one bad measurement
  can silently drop the whole observation, and doing this reflexively can
  erase most of a low-quality dataset); prefer replacing the specific bad
  value with an explicit missing marker; re-run the analysis with and
  without the questionable values, and if the conclusion changes materially,
  you must find and disclose the cause before proceeding — never drop
  without justification. This is a genuinely transferable evidence-handling
  principle: don't silently discard anomalous evidence, quantify its effect,
  and disclose rather than default to deletion. It corroborates (independent
  domain, does not originate) `.ROOT`'s existing contradiction-flagging and
  raw-immutability postures.
- Patterns are treated explicitly as candidate explanations to interrogate,
  not conclusions: "could this be coincidence? how strong is it? does it
  hold in every subgroup?" — a plain skepticism checklist for any observed
  correlation, again a corroborating rather than new idea next to
  `AI_engineering`'s hallucination/evaluation findings this same batch.

### Chapter 5 Decision Contribution

**Keep:** contradiction/uncertainty flagging over silent overwrite or silent
deletion (`AGENT.md § Wiki Shared Layer` rule 6) — this chapter is an
independent domain confirming the same discipline is standard data-science
practice, not merely a `.ROOT`-specific convention.

**Add to the synthesis queue:** none new — reinforcing evidence only.

**Reject as default:** treating an observed pattern as confirmed without
checking whether it survives removing outliers, changing subgroup, or
questioning coincidence.

## Chapter 6 — Workflow: Projects (PDF pages 138–143)

This is the chapter flagged in advance as architecture-relevant, and it
earns the flag — it is a small, explicit reproducibility contract that
maps closely onto `.ROOT`'s own file-safety rules (`AGENT.md § File Safety`)
and the path-move-integrity question Phase 5 of the governing instructions
raises via Flag #83.

- **"What is real?"** — the source (scripts, and by extension any
  human-authored instructions or extracted wiki text) is the durable
  artifact; derived, in-memory session state is disposable and must be
  reproducible from source, never the other way around. The book's
  concrete practice is disabling workspace-state persistence entirely so
  you are forced to keep everything important in the reproducible script,
  not the ephemeral session — the record must never live somewhere it can
  silently vanish or drift from the source that generated it.
- **Path discipline, stated as an explicit rule with a reason:** never use
  absolute, machine-specific paths in shared material — they "hinder
  sharing: no one else will have exactly the same directory configuration
  as you"; use paths relative to a defined project root instead, and never
  change global working-directory state from inside a script. This is the
  same failure class as `.ROOT`'s path-move-integrity concern (Flag #83):
  content that hardcodes its own location breaks the moment the location
  changes, silently, for every downstream reference.
- **Bundle a unit of work at its natural boundary, once, and don't split
  it across untracked locations:** "keep all the files associated with a
  project together — input data, scripts, results, figures... everything
  you need is in one place, cleanly separated from all other projects."
  This is a plain precedent for CASTLE's per-wiki ownership boundary and
  for keeping a source-intake batch (like this one) self-contained under
  one dated folder rather than scattered.
- **Reproducibility is verified, not assumed:** the worked example insists
  the reader actually quit and relaunch the tool, confirm the working
  directory is restored from the project file rather than memory, and
  confirm the same script regenerates the same output file. A generated
  figure is proof of nothing on its own; being regenerable from source on a
  cold start is the actual acceptance test — directly on point for the
  governing instructions' "a fresh session could reproduce the reasoning
  without oral history" quality-gate line.

### Chapter 6 Decision Contribution

**Current design claim under test:** `.ROOT`'s raw immutability and
`WHERE_IT_GOES.md` placement authority already forbid path drift and
scattered project files.

**Supporting evidence:** this chapter, independently, in a different tool
ecosystem, converges on the same three rules — durable source over
disposable session state, no hardcoded absolute paths, and one bundled
location per unit of work — for the same underlying reason (silent breakage
on relocation or on a fresh machine/session).

**Challenging evidence:** none — no contradiction found; this chapter did
not surface a case where `.ROOT`'s existing posture is insufficient.

**Verdict:** keep current design; treat as corroboration, not a new
requirement.

**Smallest proposed change:** none required by this source alone. If the
architecture synthesis ultimately proposes a path-move/reference-integrity
validator (per Phase 5's Flag #83 discussion), this chapter is citable
supporting precedent that the underlying failure mode (hardcoded location →
silent breakage on move) is a known, named problem in reproducible-analysis
practice generally, not a `.ROOT`-specific quirk.

**Owner:** CASTLE (cross-realm tooling question, not a domain-wiki claim).

**Acceptance test:** n/a — no change proposed from this source alone.

**Return path:** cite alongside Flag #83 if/when the synthesis report
addresses the path-move-integrity validator question.

**What would reverse the verdict:** a later chapter or source showing a
case where strict relative-path/no-shared-session-state discipline
actively breaks a legitimate `.ROOT` workflow — not encountered so far.

## Chapter 7 — Tibbles with tibble (PDF pages 145–166)

- Tibbles are an opinionated variant of R's data frame (no silent type
  coercion, no renamed variables, no auto-generated row names, clearer
  truncated printing, stricter `$`/`[[` access that warns on typos instead
  of silently partial-matching). Entirely a language/package implementation
  detail — confirmed, not merely expected, to have no `.ROOT` architecture
  relevance.

## Chapter 8 — Data Import with readr (PDF pages 166–187)

- Covers `read_csv()` and sibling parsers, type-inference heuristics,
  encodings (UTF-8 vs. legacy), locales for numbers/dates, and writing back
  to disk. Almost entirely R/package mechanics.
- **One transferable point, stated as an explicit recommendation, not
  R-specific:** the type-inference heuristic samples only the first 1,000
  rows to guess each column's type; this can silently produce a wrong
  schema when a rare case (a stray non-numeric value, a date format) only
  appears later in the file. The book's fix is to always pin down and
  supply the full column specification explicitly rather than trust the
  inferred one, and to use a strict mode that errors on any parsing failure
  rather than silently continuing. This is a specific, concrete instance of
  a general principle already established more rigorously by this batch's
  `AI_engineering` intake (versioned, explicit configuration over trusted
  defaults) — corroborating, not new.
- Also names the general risk of format round-tripping: writing to CSV
  loses column type information, so re-reading requires re-declaring or
  re-inferring the schema every time — a plain instance of "a serialization
  format can silently drop information the next reader needs unless the
  schema travels with the data, or is version-pinned separately."

### Chapter 8 Decision Contribution

**Keep / Add / Reject:** none activated — no distinct new mechanism;
filed as corroboration for explicit-over-inferred configuration, a
principle CASTLE's synthesis queue already carries from `AI_engineering`.

## Chapter 9 — Tidy Data with tidyr (PDF pages 187–196)

The other chapter flagged in advance as architecture-relevant, and the
strongest single conceptual payload in the book — this is the formal
version of what Chapter 5 previewed informally.

- **The three tidy-data rules, stated as strictly interdependent (you
  cannot satisfy only two of three):** each variable has its own column,
  each observation its own row, each value its own cell. The same
  underlying facts can be represented in many structurally different but
  logically equivalent tables; only one of those representations is
  "tidy," and untidy alternatives usually arise either because a human
  optimized the layout for data entry rather than for machine
  transformation, or because no one applied a consistent schema at all.
  This is a precise, formal argument for a principle CASTLE already
  practices informally: a fact should have exactly one owning
  representation, and any other view of it should be a deterministic
  derivation, not an independently maintained parallel copy. It is a
  clean, transferable justification (not new evidence, but a sharper
  articulation) for why `.ROOT` treats domain wikis as owning their facts
  and forbids competing sources of truth or duplicated placement authority.
- **Explicit vs. implicit missing-ness is a genuine, transferable
  distinction:** a value can be missing because a cell is flagged absent
  (explicit), or because a valid combination simply never appears in the
  record at all (implicit — "the absence of a presence" vs. "the presence
  of an absence"). Which representation you're looking at can make an
  implicit gap invisible until you deliberately check for it (e.g., by
  reshaping the data so every expected combination gets a row). This maps
  onto a real CASTLE gap-detection concern: a coverage ledger that only
  lists what *was* processed cannot by itself reveal a source that was
  never listed at all — the absence has to be checked against an
  independent expected-set, not just read off the ledger's own rows. Worth
  carrying into the synthesis as a named test for any future coverage-ledger
  or intake-tracking design: does it only show explicit gaps, or can it
  also surface implicit ones (an expected source category with zero
  entries, silently)?
- **The closing caveat is itself a durable governance point:** "messy" is
  explicitly named as a pejorative oversimplification — tidy data is
  presented as the right *default*, not a universal mandate. Alternative,
  non-tidy structures are legitimate when they have real performance/space
  advantages or established domain conventions. This directly parallels
  the caution CASTLE's own governing instructions already apply to
  standardization proposals generally: prefer one canonical shape by
  default, but do not force it where a bounded, justified exception is
  cheaper and safer than conformance.
- The worked case study (untidying a real WHO tuberculosis dataset:
  redundant identifier columns, values encoded into column names,
  inconsistent naming needing a targeted string fix before parsing) is a
  concrete demonstration that real-world data virtually never arrives
  tidy and reaching a tidy form is normally a deliberate multistep pipeline,
  not a one-shot operation — a minor, generic point about intake effort
  rather than a distinct architecture claim.

### Chapter 9 Decision Contribution

**Current design claim under test:** `.ROOT` requires one owning
representation per fact (domain-wiki ownership; CASTLE forbids competing
sources of truth), and requires coverage/source ledgers to track intake
status.

**Supporting evidence:** the tidy-data rules are a rigorous, independently
sourced formalization of "one fact, one canonical shape, other views are
derived" — real corroboration, sharper than anything else in this batch on
that specific point.

**Challenging evidence:** the explicit/implicit missing-value distinction
surfaces a real gap-detection weakness worth testing: does any existing
`.ROOT` coverage ledger (e.g., `SYSTEMS\wiki\raw-source-coverage-and-intake-status.md`,
named as the pattern to follow in the governing instructions) only record
sources it already knows about, with no independent check for a source
category that should exist but has zero entries? That is an open question
this source raises but cannot answer — it did not itself audit any live
`.ROOT` ledger.

**Verdict:** keep the one-fact-one-owner principle (strong corroboration);
**test** whether existing coverage ledgers can surface implicit
(zero-entry) gaps, not only explicit (logged-but-incomplete) ones.

**Smallest proposed change:** none from this source alone; if the
synthesis report evaluates coverage-ledger design, add an explicit check
for "categories/sources that should be represented but have no ledger row
at all," not just "rows marked incomplete."

**Owner:** whichever wiki's coverage ledger is evaluated; CASTLE if the
ledger pattern itself is standardized.

**Acceptance test:** a coverage ledger passes if a reviewer can list, from
the ledger plus an independent expected-source-set, both (a) sources logged
as incomplete and (b) sources not logged at all.

**Return path:** carry into Phase 2/3 of the governing instructions'
per-wiki coverage-ledger sweep as an explicit test question, not a
standalone finding.

**What would reverse the verdict:** evidence that every existing `.ROOT`
coverage ledger already cross-checks against an independent expected-source
list (in which case this is already handled and not a gap).

## Chapters 10–13 — PDF Pages 197–286

- Relational joins require explicit keys/cardinality. Duplicate keys multiply
  rows; unmatched keys silently discard facts. A reference audit must identify
  duplicate targets and unresolved references.
- Filtering joins distinguish testing a relationship from mutating a record;
  validators should report before changing.
- Regex anchors match text boundaries, not meaning. Heading integrity needs
  parsed Markdown identity/link resolution, not substring search alone.
- Factors/dates mainly add the reminder to record order, locale, and time zone.

## Chapters 14–17 — PDF Pages 287–370

- Functions give repeated logic one named implementation and contract.
- Iteration should preserve keys and per-item failures.
- Pipes clarify linear sequence but become harder with branches/side effects;
  use named state at consequential branches.
- Most content is R syntax and adds no architecture mechanism.

## Chapters 18–20 — PDF Pages 371–448

- A model is a simplified representation; residuals/held-out cases show what it
  misses. Architecture categories need concrete routing tests and exceptions.
- Many-model workflows keep data, model, metrics, and identifiers together.
- Statistical mechanics are out of scope; no new `.ROOT` role is proposed.

## Chapters 21–24 — PDF Pages 449–507

- R Markdown is one plain-text source combining prose, executable code, and
  generated results. Reader views are derived rather than parallel truth.
- YAML is a machine-readable control surface separate from prose. This supports
  frontmatter/register metadata for consequential instructions.
- Cached chunks are unsafe when only their own code is tracked. Dependencies
  and external-file versions must invalidate the cache.
- Parameterized reports reuse one source against declared inputs.
- The lab-notebook workflow records successes, failures, and reasoning, then a
  clean full render verifies reproducibility outside the interactive session.
- Long-term reproducibility also requires environment/package versions.

## Coverage Declaration

- **Fully examined:** all 520 physical pages, front matter through Chapters
  1–24 and back matter.
- **Material contributions:** Chapters 5, 6, 9, 10, 11, and 21–24.
- **Confirmed low-relevance spans:** Chapters 1–4, 7–8, and 12–20 are mostly
  R/tidyverse mechanics; only transferable findings were activated.
- **Remaining uncertainty:** this 2017 source carries strongest weight for
  reproducibility, canonical source, dependencies, keys, joins, and literate
  computing—not agent architecture.
