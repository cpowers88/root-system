---
type: evidence-report
status: approved-internal-proof
tags: [revenue, content, youtube, research]
created: 2026-07-14
timeline: now
---

# YouTube Outlier Scanner — First Findings
### Review artifact | July 14, 2026 | Status: internal proof approved; no launch decision

## Chris Decision — July 14, 2026

Chris approved moving forward with the practical AI/software tutorial path,
with AI-for-small-business as the companion angle. The CASTLE gate passes the
next **internal** phase only: add topic ranking and snapshot velocity to the
scanner, run a one-month validation loop inside the existing weekly technology-
landscape rep, and prepare one private 8–12 minute tutorial proof from the live
scanner build. Public channel creation, posting, monetization, affiliates, paid
tools, and kids content remain outside authorization.

**Research-depth and scope amendment:** Chris increased the default depth to
**up to 100**, then clarified that the primary 100 must come from the combined
relevant market—not only `Claude Code tutorial`. Exact-topic reports are now
drilldowns beneath the cross-topic market report.

The defined market contains 36 searches across practical AI, software tutorials,
software/app reviews, small-business AI, and adult-facing family technology.
The completed scan produced 2,615 deduplicated raw candidates. A transparent
title relevance gate removed 502 obvious mismatches, leaving 2,113 candidates
for review. The overall top 100 by views contains 50 long-form videos and 50
Shorts; rank 100 has 891,117 views. Category matches within those 100 are:
practical AI 81, software tutorials 21, small-business AI 9, software reviews 2,
and family technology 2. Counts overlap when one video matches multiple topics.

Strict relevance is not final classification. It catches known ambiguity such
as Minecraft results for `Obsidian tutorial`, but full-content review is still
required before calling a candidate reproducible or worth making.

Execution brief:
`00-BRAIN\Session_Logs\Report Archive\YT_SCANNER_TOPIC_REPORT_AND_PRIVATE_PROOF_EXECUTION_BRIEF_2026-07-14.md`

## Decision This Report Supports

Chris is considering whether content can be made as a byproduct of the technology
stack and real systems he is already learning and building. This report does
**not** authorize a channel, posting, monetization, affiliates, or a kids channel.
It records the first public-data evidence for a later CASTLE review.

## Data Location and Method

Raw public API results are stored locally in
`02-LIBRARY\.PROJECTS\YT_Outlier_Scanner\scanner.db`:

- `discoveries` — wide-net search results: exact video title, channel, publish
  date, views, subscriber count when public, and views/subscriber.
- `channels` / `videos` — deep-harvest data for the initial channel samples,
  with Shorts and long-form separated.

Discovery searches covered videos published in the last 180 days. Each search
returns recent, relevant public YouTube results; it is a sample, not the entire
market. Results were read on July 14, 2026 and view counts will continue to change.

The scanner uses three different signals:

1. **Total views** — evidence that a subject is attracting attention.
2. **Views per subscriber** — evidence that a specific video broke out beyond
   its channel's ordinary reach. It is a discovery signal, not proof of income.
3. **Measured view velocity** — change in views between real observations at
   least 24 hours apart. It remains `n/a` until that evidence exists.

## Scan A — Desk-Based Software Tutorials

Initial deep sample: Kevin Stratvert, Jeff Su, and Howfinity (600 videos), with
Marques Brownlee (200 videos) as a product-review benchmark.

| Sample | Long-form breakout rate | Shorts breakout rate | Read |
|---|---:|---:|---|
| Software tutorials | 24.2% (95/393) | 17.4% (36/207) | Strong attention and repeatable desk-based formats. |
| Tech reviews | 0.7% (1/140) | 11.7% (7/60) | Depends heavily on access to new products and an established review operation. |

High-performing tutorial angles included free tool alternatives, Claude Code and
Claude AI beginner walkthroughs, practical Gmail/Canva/phone fixes, and specific
tool comparisons. This supports tutorials based on real work Chris is already
doing; it does not support copying titles or generic AI filler.

## Scan B — Practical AI Tutorials

**Queries:** `Claude Code tutorial`, `ChatGPT tutorial`, `AI automation tutorial`,
`AI tools for beginners`.

| Query | Videos | Median views | Top views | Channels under 200k subscribers |
|---|---:|---:|---:|---:|
| Claude Code tutorial | 92 | 453,286 | 5,208,546 | 39% |
| ChatGPT tutorial | 93 | 332,562 | 10,668,177 | 46% |
| AI automation tutorial | 92 | 385,875 | 2,660,185 | 34% |
| AI tools for beginners | 90 | 383,150 | 10,108,075 | 21% |

### Leading-Ten Excerpt — `Claude Code tutorial` From the 100-Row Set

| # | Views | Channel | Published | Video title |
|---:|---:|---|---|---|
| 1 | 5,208,546 | Claude | 2026-05-05 | What is Claude Code? |
| 2 | 2,110,949 | Nick Saraev | 2026-02-12 | CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026) |
| 3 | 1,864,962 | Dan Martell | 2026-05-21 | Learn 97% of Claude in Under 16 Minutes |
| 4 | 1,595,606 | Danny Why | 2026-05-30 | Claude Code Just Changed YouTube Forever! |
| 5 | 1,586,103 | 100x Engineers | 2026-04-06 | Don't upload PDFs to Claude, Use this instead! |
| 6 | 1,567,929 | Samin Yasar | 2026-04-06 | Claude Just Changed the Stock Market Forever! (Tutorial) |
| 7 | 1,487,636 | Ayushman Pandita | 2026-04-06 | Full Claude Tutorial for Beginners - Become A Pro In Just 30 Minutes! |
| 8 | 1,374,245 | Tech With Tim | 2026-02-27 | Claude Code - Full Tutorial for Beginners |
| 9 | 1,372,896 | Claude | 2026-02-27 | What are skills? |
| 10 | 1,178,240 | Sandeep Swadia | 2026-05-22 | How To Use Claude Better Than 99% Of People |

The recurring *formats* are beginner explanations, full walkthroughs, surprising
mistakes/workarounds, new-feature explainers, and concrete outcomes. The strong
fit is original content grounded in a real build: a school-tracker lesson, an
API/SQLite workflow, or an AI feature tested on a genuine business/family/school
problem. `ChatGPT tutorial` results were heavily mixed with photo-editing prompt
Shorts, so that subcategory is not evidence of a durable fit.

## Scan C — AI for Small-Business Workflows

**Queries:** `AI for small business`, `ChatGPT for small business`, `small business automation`, `AI CRM small business`.

| Query | Videos | Median views | Top views | Channels under 200k subscribers |
|---|---:|---:|---:|---:|
| AI for small business | 94 | 298,559 | 3,937,818 | 35% |
| ChatGPT for small business | 88 | 1,852 | 886,079 | 77% |
| Small business automation | 80 | 3,101 | 781,898 | 85% |
| AI CRM small business | 84 | 1,229 | 766,164 | 85% |

The broad query has substantial attention but is noisy. The cleaner evidence is
the specific operational problem: setting up Claude for a small business,
comparing AI receptionists, CRM workflows, and showing AI inside a contractor's
operation. This has lower broad reach than AI tutorials but much stronger
alignment with the North Star's advisor-builder service path.

## Scan D — Parent-Facing Technology and Family Systems

The broad pass (`AI for parents`, `parenting technology`, `educational apps for
kids parents`, `parental controls tutorial`) was polluted by viral novelty,
unrelated entertainment, and fake/aspirational AI-device Shorts.

The narrower pass used `Google Family Link tutorial`, `screen time app for parents`,
`parental control apps review`, and `family calendar app tutorial`.

| Query | Videos | Median views | Top views | Channels under 200k subscribers |
|---|---:|---:|---:|---:|
| Google Family Link tutorial | 94 | 5,698 | 38,326,218 | 73% |
| Screen time app for parents | 88 | 6,532 | 6,168,657 | 73% |
| Parental control apps review | 81 | 4,037 | 244,686 | 80% |
| Family calendar app tutorial | 83 | 1,068 | 337,647 | 84% |

There is a modest, practical market for screen-time walkthroughs, parental-control
comparisons, and family digital-command-center content. The Family Link query
remains polluted by bypass/removal content. This supports an adult-facing
family-systems angle only; it does **not** support a child-directed channel.

## Cross-Scan Read

| Candidate direction | Evidence read | Fit with existing work | Status for review |
|---|---|---|---|
| Practical AI/software tutorials | Strongest attention and best repeatable desk format | Direct Python/API/AI learning overlap | Leading research candidate |
| AI for small-business workflows | Narrower attention; stronger business relevance | Direct advisor-builder and construction/real-estate overlap | Strong companion angle |
| Parent-facing family systems | Smaller, authentic material; query quality needs work | Genuine lived experience, not core tech-stack work | Secondary/optional angle |
| Kids channel | No valid market/profit/compliance case researched | Separate production and compliance business | HOLD |

## Proposed Staying-Current Loop (Not Yet an Operating Commitment)

1. Monitor official release notes for tools already in Chris's stack: Claude,
   ChatGPT/Codex, Google Workspace/Gemini, Python, and selected automation tools.
2. When a relevant feature/change lands, run a 30- to 90-day discovery scan using
   that exact feature phrase.
3. Rank up to 100 by total views and views/subscriber, then deeply review the
   strongest and most relevant subset.
4. Make an original tutorial only when Chris has used the feature on a live project
   or real workflow that week.
5. Preserve periodic view snapshots before adding a future `views-per-day` ranking;
   a single public view count cannot measure true velocity.

## Scanner Limits and Needed Review

- YouTube search relevance is imperfect; every query needs manual classification.
- Public views are attention signals, not revenue, demand, or repeatability.
- Search samples favor recently indexed/popular videos; they are not a full census.
- The scanner stores exact discovery rows and now ranks up to 100 by total views,
  views/subscriber, publish date, and—after qualifying repeat snapshots—measured
  views/day without a manual database query.
- Scanner quota output is an operational guardrail; Google Cloud Console remains
  the source of truth for quota usage.

## Human Classification Packet

The canonical
[top-100 classification worksheet](../../../02-LIBRARY/.PROJECTS/YT_Outlier_Scanner/TOP_100_CLASSIFICATION_WORKSHEET.md)
is generated from `market-report`'s same views-ranked, all-format, strict-relevance
market universe. It contains 100 deduplicated mechanical-evidence rows and a second
table with 100 blank human-only classification rows. Scanner categories and matched
topics are search provenance, not niche or relevance judgments.

On July 16, an explicitly non-human AI pre-screen was added without changing the
blank classification table. It used titles and search provenance only to test one
operating question: could Chris make an original video by recording work already
happening with little additional production? The advisory screen returned 16 `Y`,
38 `?`, and 46 `N` rows and converted the strongest patterns into seven original
recording angles. It is triage, not watched-video evidence or market validation.

Chris may review the 16 `Y` rows first and run one private proof without completing
the full classification. All 100 human rows still require Chris's observed labels
before any market-wide or format-separated conclusion is produced. AI must not fill
those cells, reinterpret `?`, or turn this review into a channel, publishing,
revenue, or title decision.

## Approved Internal Next Phase

1. Add topic-ranking output and snapshot-based velocity to the scanner.
2. Conduct a one-month validation scan inside the existing weekly technology-
   landscape rep.
3. Run one private proof from the scanner build, capped at 90 added minutes, and
   measure production time and usefulness.
4. Return to review before any public action. Stop/park Lane A if the production
   footprint cannot fit school and family reality.

No external action is authorized by this report.
