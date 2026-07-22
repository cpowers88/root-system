---
tags:
  - pathway
  - documents
stage: phase-3
timeline: reference
---

# Document Automation Pathway

> Extracting, generating, and routing the documents SMBs drown in — the most engineering-flavored and defensible build work.

## Purpose
Define the document and data-extraction service line: turning invoices, POs, contracts, intake forms, and reports from manual burdens into automated pipelines.

## Key Idea
Document handling is where SMB waste is most concentrated and most measurable: someone reads a PDF, re-types its contents into a system, files it, and later can't find it. Modern AI (vision-capable LLMs and purpose-built extraction) has made this genuinely solvable at SMB price points for the first time. The pathway covers three motions: **extract** (document → structured data), **generate** (data → document), and **route** (document → right place, right person, right system).

## Why It Matters
- **High, provable ROI:** document tasks have countable volumes and per-document minutes — the [[smb-ai-audit-method|audit math]] writes itself.
- **Deeply defensible:** an extraction pipeline wired into a client's accounting and operations is hard to rip out and hard for a cheap freelancer to replicate reliably.
- **Best fit for an engineering background:** accuracy thresholds, validation layers, and exception handling are real engineering problems — the moat is *reliability*, not access to AI. See [[north-star-alignment|North Star Alignment]].

## What Gets Sold (Typical Builds)
- **AP invoice processing:** vendor invoices (email/PDF/scan) → extracted line items → validated → pushed to QuickBooks/Xero → flagged exceptions to a human
- **PO and order-entry extraction:** customer POs in random formats → order system entries
- **Contract & lease abstraction:** key terms, dates, obligations extracted into a tracked register with renewal alerts
- **Intake form processing:** applications, claims, patient/client intake → structured records + document filing
- **Document generation:** proposals, contracts, work orders, compliance reports assembled from system data via templates
- **AI-assisted reporting:** raw operational data → drafted narrative reports (job summaries, board packets) for human review

## Delivery Notes (What Makes This Pathway Different)
- **Never promise 100% accuracy.** Design human-in-the-loop from day one: high-confidence documents flow straight through; low-confidence route to a review queue. Sell "95% of documents untouched by humans," not "no humans."
- **Validation layers are the product:** totals must reconcile, dates must parse, vendors must match the master list. The LLM is one component; the checking around it is the value.
- **Data sensitivity is real here** — financial and sometimes medical data. Have a straight answer on data handling, model providers, and retention before the client asks. See [[risks-and-failure-modes|Risks & Failure Modes]].

## Pricing
- Single document-type pipeline (e.g., AP invoices): **$5,000–$15,000** build
- Multi-document platform: **$15,000–$40,000**
- Volume-based ongoing component works well here: base retainer + per-document tier, since your monitoring cost scales with volume. See [[pricing-models|Pricing Models]].

## Practical Actions
- Build a working AP-invoice extraction demo (sample PDFs → structured output → spreadsheet/accounting push) — this one demo sells the whole pathway.
- Learn the document AI landscape hands-on: LLM vision APIs, plus one dedicated extraction service; know when each wins ([[tool-stack|Tool Stack]]).
- In audits, always count monthly document volume × handling minutes — it's routinely a five-figure annual number.

## Beginner Version
One document type, moderate volume, low blast radius — e.g., extracting supplier invoices into a review spreadsheet the bookkeeper approves before sync. Deliberately oversized human review at first; tighten as accuracy proves out.

## Intermediate Version
Single-document pipelines delivered with the full gate stack — deterministic validation, confidence routing to a review queue, sampling audits — and a trained client-side reviewer working the queue ([[agent-manager-job-design|AI Workflow Operator]]). Straight-through rate is measured and reported monthly; raising it safely is the retainer story.

## Advanced Version
Multi-document, multi-system pipelines with confidence scoring, automated reconciliation, exception dashboards, and SLAs on straight-through-processing rates. Vertical-specific packages (e.g., "subcontractor compliance-doc engine" for construction) sold as productized offers.

## Revenue Connection
Highest ticket sizes of the early pathways and the strongest lock-in per dollar delivered. A handful of document-automation clients on volume-based retainers materially stabilizes the P&L — key to the [[one-year-plan|One-Year Plan]] revenue mix.

## Human-Agent Management Connection
This pathway is the purest expression of [[quality-control-and-risk-gates|confidence routing]]: high-confidence documents flow straight through, low-confidence ones queue for a human — so the bookkeeper stops re-typing invoices and starts adjudicating exceptions. The calibration loop (accuracy data → gate relaxation → higher straight-through rate) is visible, reportable retainer work, and the client's reviewer is the textbook first [[agent-manager-job-design|operator role]].

## Risks / Failure Modes
- **Errors reaching the books** — the highest blast radius of the early pathways; validation layers and reconciliation checks are the product, not overhead.
- **Promising accuracy you can't measure** — never quote a straight-through rate before testing on the client's real document mix; formats in the wild are always worse than the samples.
- **Data-sensitivity improvisation** — financial and medical documents demand the written data-handling answer *before* the client asks ([[business-setup|Business Setup]] Tier 2).

## Related Pages
- [[workflow-automation-pathway|Workflow Automation Pathway]] — the pipelines documents flow through
- [[data-and-dashboard-pathway|Data & Dashboard Pathway]] — reporting on the extracted data
- [[internal-ai-assistants-pathway|Internal AI Assistants Pathway]] — assistants built on the document corpus you've structured
- [[retainer-model|Retainer Model]] — volume-based recurring revenue
