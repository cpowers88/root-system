---
type: contract
timeline: reference
register: ai-directive
tags: [governance, wikis]
created: 2026-08-11
status: live
---

# Wiki Shared Layer — the rules every `03-WIKIS` hub relies on

### Load when working inside any `03-WIKIS` hub or CASTLE's wiki. `AGENT.md` § Wiki Shared Layer points here.

One copy lives here; every hub's `OPERATIONS.md` relies on it instead of
re-copying it. Moved out of `AGENT.md` on 2026-08-11 because these eight rules
apply only inside a hub, while `AGENT.md` is read in full by every session in
every tool — they were 12% of a payload most sessions never used. The
`## Wiki Shared Layer` heading remains in `AGENT.md` as a pointer, because 26
files across the vault reference that anchor by name and a heading that
disappears is its own failure class.

---

1. **Raw is immutable.** Read from a wiki's `raw\`; never modify, delete,
   rename, or reorganize it without Chris's explicit instruction. Extracted
   material goes into that wiki's `wiki\`.

   > **DO NOT DEDUPE `raw\` ON HASH.** Measured 2026-08-11 across all 2,277
   > non-journal `.md` files: seven files in `03-WIKIS\SYSTEMS\raw\` hold only
   > two articles between them (one set of 4 identical, one set of 3). This is
   > **not** a duplication bug to clean up — it is *capture loss*. The clipper
   > pre-filled each note's name from whichever browser tab was active, then
   > re-extracted the body at save time, so the **filename** is from the intended
   > source and the **body** is from a different one. Five sources were never
   > captured at all and exist as a filename and nothing else: "Eight Principles
   > of Good Data Management", "Data Management for Researchers", "13 Project
   > management", "Why Trust Science", and the O'Dea talk.
   >
   > **The filenames are the only surviving record of what is missing.** A
   > hash-based cleanup would delete that evidence and make the loss permanent
   > and invisible. The correct repair is to reconcile filename against
   > frontmatter `title`/`source` and build a recovery list — deleting nothing.
   > Open as flag #97; full analysis in `Session_Logs\System Update Log\
   > 2026-08-11_ROOT_COUNCIL_REVIEW\COUNCIL_RECONCILED_VERDICT.md` § Data loss.
2. **Large-source chunking.** Never extract a long PDF, book, or multi-part
   source in one pass. Work in chunks small enough to hold fully (10–15
   pages or one chapter/section); synthesize only after every chunk is
   read; record the page ranges covered in `log.md`.
3. **Session start (minimum).** Read the wiki's `wiki\index.md` and the
   last 3 `log.md` entries; state the session goal in one sentence.
4. **Session close (minimum).** Update `log.md`; update `index.md` if pages
   changed; state the next action in one sentence.
5. **Update over create.** Check whether a source strengthens, corrects, or
   extends an existing page before creating a new one.
6. **Never silently overwrite a claim.** Before replacing a claim, classify
   the change as a temporal update, context-dependent variant, or true contradiction.
   When a new source contradicts an existing page, flag it on the page
   (supersedes/contradicts X — source, date) instead of quietly replacing it.
7. **Recency markers on volatile claims.** Prices, versions, and adoption
   stats that age carry "(as of YYYY-MM, source)".
8. **Lint pass.** At the monthly review, or on request, scan for orphan
   pages, dead wikilinks, contradictions, stale superseded claims, and
   index-vs-live-tree mismatch; log findings and fix per normal flag
   priority. After creating or editing wiki frontmatter, also run
   `python 00-BRAIN\scripts\frontmatter_audit.py --baseline 00-BRAIN\scripts\frontmatter_baseline.json`
   and resolve every new finding before close.
9. **Verify captures on content, not existence (added 2026-08-30, Chris-approved).**
   A file routed from `77-INBOX` — a D2L export, a web capture, a converted
   document — is not filed until the *filed copy* passes three checks:
   **(a) open it and read it** — a body that is page chrome, a session-timeout
   shell, or an `<iframe>` tag with no content is an empty capture, not a source;
   **(b) count its structure against the live original** — sections, numbered
   tasks, rubric items, options ("three options" listing two is how one defect
   was caught); **(c) never assert a fact from the filed copy alone when the
   claim is about graded work** — re-open the original. A capture that fails any
   check is filed with `status: incomplete-capture` in frontmatter and named in
   the session close, never left looking whole. *Why this is a rule and not
   advice: seven aid defects in eleven days (2026-08-19 → 08-29), five of them
   introduced or concealed at filing, each one teaching wrong facts about graded
   work until caught — evidence recorded in `04-SCHOOL\miss-log.md` § aid
   defects. The pattern's common shape: a source verified on one property
   (it exists, it has the right name) and then trusted on another (its content).*

---

Academic integrity for course-support wikis (PYTHON, PHYSICS, EDUCATION) is
governed once, in `AGENT.md` § Academic Integrity — not restated here.

*Prior history: the July 9 version of this rule set was condensed into a
run-on paragraph during the July 10 `AI_Agent.md`→`AGENT.md` split, dropping the
`§ Wiki Shared Layer` anchor; restored as a numbered section 2026-07-24.*
