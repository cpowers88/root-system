---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/spreadsheet-modeling, subject/or-practice, subject/operations-research]
---

# The Art of Modeling with Spreadsheets

**Summary**: Practical modeling craft, not a mathematical technique — a Plan-Build-Test-Analyze process for actually building a working spreadsheet model of a real decision problem, plus the changing-cells/output-cells distinction that keeps a model organized and debuggable. This is the "how do you actually build the thing" chapter, complementary to every mathematical model already ingested from this book.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 21 ("The Art of Modeling with Spreadsheets"), the Everglade Co. cash-flow-planning worked example — physical ~1100 of the chapter

**Last updated**: 2026-07-13**

---

## The Plan-Build-Test-Analyze Process

A four-stage discipline for building a spreadsheet model of any real decision problem, illustrated with a cash-flow/loan-sizing example (Everglade Co. deciding how much to borrow, long-term vs. short-term, to maintain a minimum cash reserve while maximizing the final cash balance):

1. **Plan**: define the problem and gather data (what decisions, what constraints, what objective — the same three questions any LP formulation starts with, see [[linear-programming-formulation-and-graphical-solution]]); visualize what the finished answer should look like *before* building anything (what numbers will actually go in the final report); do some calculations by hand on a small trial case, both to clarify what formula an output cell actually needs and to have a known-correct answer for later verification; sketch the spreadsheet's layout on paper before touching Excel.
2. **Build**: start with a small-scale version of the model, then expand to full scale once the small version is verified working.
3. **Test**: try different trial solutions to check the model's internal logic actually behaves as expected.
4. **Analyze**: evaluate proposed solutions and/or run an optimizer (Solver) against the finished model. If the solution reveals a flaw in the model itself, loop back to Plan or Build rather than patching around it.

## Changing Cells vs. Output Cells: The Key Organizing Distinction

**Changing cells** hold the actual decision variables — values that don't depend on anything else in the model, and that an optimizer is free to adjust. **Output cells** hold everything *computed from* the changing cells (and data cells) — results, not decisions. **A common modeling mistake**: including a computed quantity (like a resulting cash balance) as a "changing cell" because it changes based on decisions — but a changing cell must be an independent input, not a dependent result. Getting this distinction right is what makes a spreadsheet model both correct (an optimizer can only adjust genuine decision variables) and readable (a reviewer can immediately see what's being decided vs. what's being calculated).

**Practical layout advice**: sketch blocks for data cells, changing cells, and output cells *before* building — data at the top/left, flowing logically toward the objective cell; use a consistent row/column structure (e.g., one row per time period) so all related quantities share common headers rather than being scattered arbitrarily across the sheet.

## Why Hand Calculations Matter

Doing a small hand-calculated example before building the full spreadsheet serves two purposes: (1) it clarifies exactly what formula an output cell needs (working through "ending balance = starting balance + cash flow + loans − interest − paybacks" by hand makes the eventual cell formula obvious), and (2) it provides a known-correct answer to verify the finished spreadsheet against — plug the same trial numbers into the built model and confirm it reproduces the hand-calculated result before trusting it for anything else.

## Key Takeaways

- Spreadsheet modeling craft is a real, distinct skill from the mathematical modeling covered elsewhere in this wiki — a mathematically correct model built with a poor spreadsheet structure is still hard to trust, debug, or hand off.
- The changing-cells/output-cells distinction isn't just organizational tidiness — conflating a decision variable with a computed result is a genuine formulation error, not just a style issue.
- Hand-calculating a small trial case before building the full model serves double duty: it clarifies the needed formulas *and* provides a verification check for the finished spreadsheet.
- "If the solution reveals inadequacies in the model, return to Plan or Build" — treating a bad result as a signal to revisit the model's structure, not just a number to report, is the discipline that prevents shipping a subtly broken deliverable.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — the Plan stage's three defining questions (decisions, constraints, objective) are the same ones any LP formulation starts from.
- Every other page in this OR ingest — this chapter's craft applies to building a working spreadsheet implementation of any of the mathematical models already covered (LP, inventory, forecasting, decision analysis, etc.).

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | This is the actual delivery-mechanism skill for turning any OR model already ingested into a working client deliverable |
| Current usefulness | 4 | Directly applicable to literally any spreadsheet-based deliverable, not tied to a specific OR technique |
| KSU support | 3 | Practical/applied content rather than theory-heavy; less commonly emphasized in intro-OR coursework than the mathematical chapters |
| Tech-stack relevance | 5 | This is the direct, practical skill of building any Excel-based (or equivalent) OR deliverable — maximally applicable |
| Business audit value | 4 | A well-structured, verifiable spreadsheet model is itself part of what makes an audit deliverable credible and maintainable by the client after the engagement ends |
| Data/workflow value | 3 | Not data-dependent itself — it's the discipline for organizing whatever data any specific model needs |
| Reading urgency | 3 | Genuinely useful, broadly applicable craft knowledge, distinct in kind from the mathematical content around it |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Actually building any client-facing spreadsheet deliverable (from any OR model in this wiki) — Plan-Build-Test-Analyze, with the changing-cells/output-cells distinction kept clean throughout.

**Use when**:
Building a spreadsheet implementation of any decision model for a client, especially one that needs to be verifiable and maintainable after the engagement ends (not just a one-off internal calculation).

**Do not use when**:
The model is genuinely a one-off scratch calculation with no need for client handoff or long-term maintainability — the full discipline is overkill for a quick internal check.

**Fast retrieval query**:
`subject/spreadsheet-modeling` + `subject/or-practice` — or search "Plan Build Test Analyze" / "changing cells output cells" / "sketch spreadsheet layout"

## North Star Connection

- How this applies to the audit business: this is the actual craft skill for turning any of the mathematical models already ingested into a working, verifiable, client-handoff-ready spreadsheet deliverable — the discipline that separates a credible audit tool from a fragile one-off calculation.
- Track relevance: Business — directly relevant to how every audit deliverable actually gets built and handed to a client, regardless of which underlying OR technique it implements.
- Possible future Second Brain use: Yes — this discipline (changing/output cell separation, Plan-Build-Test-Analyze) should become a standing checklist applied to every spreadsheet-based capability-library tool going forward, not a one-off reference.
