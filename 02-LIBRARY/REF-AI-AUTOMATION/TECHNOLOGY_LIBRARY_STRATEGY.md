---
type: strategy
tags: [now, ai-automation]
---

# TECHNOLOGY_LIBRARY_STRATEGY.md — The AI & Software Possibility Map
#AI #system #business
### Location: 02-LIBRARY\REF-AI-AUTOMATION\ | Referenced by: TechStackPriority.md and the TECHNOLOGY wiki
### Created: July 5, 2026 | Review: monthly (with SKILL_GAP_ANALYSIS.md)

---

## Why This File Exists

The permanent technology-capability goal, stated plainly:

> Know the full possibility space of AI and software well enough to walk
> into any business and name exactly what it needs — and what it does
> NOT need — so no dollar is wasted on the wrong tool.

That knowledge is the product in three forms:
- **Identify** — the audit finds the real problem and the right category of fix
- **Sell** — vendor-neutral advice a business owner can trust and act on
- **Make** — build only what the market genuinely doesn't already sell cheap

This file is the working map. The wiki refines raw knowledge; this file
holds the operational version Chris uses in audits, recommendations,
and skill planning. One page per concept lives in the wiki; the
compressed, sellable version lives here.

---

## The One Question Every Tool Must Answer

> Can this help a business reduce waste, improve workflow, clarify data,
> automate manual work, improve decisions, or increase profit?

If the answer is no — or the answer is yes but a cheaper layer below it
already does the job — the recommendation is no.

---

## The Recommendation Ladder — Cheapest Fix First

Work down this ladder on every problem found in an audit. Never skip a rung.
Most consultants sell from the bottom of the ladder up. Selling from the
top down is what makes the advice trustworthy — and repeatable.

```
1. ELIMINATE   — Does this step need to exist at all? (free)
2. SIMPLIFY    — Can the process be shortened before touching software? (free)
3. USE WHAT    — Is a tool they already pay for able to do this?
   THEY OWN      (Excel/Sheets, QuickBooks features, phone camera — free)
4. CONFIGURE   — Cheap off-the-shelf tool, used as designed ($10–100/mo)
5. INTEGRATE   — Connect existing tools: Make.com, n8n, Zapier, webhooks
6. BUILD LIGHT — Script, Flask tool, Airtable/Retool internal app
7. BUILD REAL  — Custom software. Last resort. Must beat every rung above
                 on total cost of ownership, not just purchase price.
```

**The cheapest software is the software you don't buy.**
A recommendation to NOT buy something is a deliverable — often the one
that earns the most trust and the retainer.

---

## The Possibility Map — 12 Categories

Twelve audit-usable categories that support the North Star's permanent capability
base. They are a possibility map, not a fixed curriculum or identity.
For each: the problem it solves, the signals a business needs it, the
signals money is about to be wasted, and representative tools by tier.

### 1. Field Data Capture
- **Problem:** Information born in the field dies before reaching the office.
- **Need signals:** Paper forms retyped later; photos trapped in text threads; "call the office to check" culture.
- **Waste signals:** Buying a $300/mo platform when a shared form + phone camera + folder convention solves it.
- **Tools:** Google Forms/Jotform → CompanyCam, Fulcrum → custom mobile form + SQLite/Postgres backend.

### 2. Job & Project Management
- **Problem:** Nobody can answer "where is this job right now?" without calls.
- **Need signals:** Whiteboard or memory is the schedule; double-booked crews; finished work not billed for weeks.
- **Waste signals:** Enterprise PM suites for a 10-person crew; a second PM tool because nobody set up the first.
- **Tools:** Trello/Sheets → Jobber, Buildertrend, ServiceTitan, Procore → custom dashboards on their data.

### 3. Business Intelligence & Dashboards
- **Problem:** Decisions made on gut because the numbers are scattered or stale.
- **Need signals:** Owner can't state job-level profit; monthly numbers arrive too late to act on.
- **Waste signals:** Power BI licenses when Looker Studio on a Sheet does it free; dashboards nobody opens.
- **Tools:** Looker Studio (free) → Power BI → custom Flask/Plotly reporting.

### 4. Process Automation
- **Problem:** Humans doing robot work — copy, paste, rename, re-enter, forward.
- **Need signals:** Same data typed into two systems; "every Friday I spend 3 hours on…" sentences.
- **Waste signals:** Automating a broken process (automation cements waste); brittle 40-step Zaps nobody can maintain.
- **Tools:** Make.com, Zapier → n8n (self-hosted, cheaper at volume) → Python scripts.
- **Rule:** Simplify first, then automate. Never automate rung 1–2 problems.

### 5. Data Storage & Retrieval
- **Problem:** The spreadsheet became the database and now it's breaking.
- **Need signals:** One giant Excel file everyone edits; version-named files (FINAL_v3_REAL); data lost when someone leaves.
- **Waste signals:** Paying for a database platform when the real problem is nobody agreed where files go.
- **Tools:** Sheets (fine longer than people admit) → Airtable → SQLite → PostgreSQL.

### 6. Communication & Coordination
- **Problem:** Decisions and commitments living in texts and voicemail.
- **Need signals:** "I never got that" disputes; customers asking for status because nobody tells them.
- **Waste signals:** Adding Slack AND Teams AND a portal — a new channel is a new place to lose things.
- **Tools:** Consolidate first. Then Slack/Teams → client portals (often built into tools from category 2).

### 7. Financial Operations
- **Problem:** Owner doesn't know which jobs make money until tax time.
- **Need signals:** No job costing; invoices sent late; receipts in a shoebox.
- **Waste signals:** New accounting software when QuickBooks is fine and the process around it is the problem.
- **Tools:** QuickBooks used properly → job-costing add-ons → custom reporting on QB data (API).

### 8. CRM & Client Pipeline
- **Problem:** Leads leak; follow-ups depend on memory.
- **Need signals:** "I forgot to call them back" revenue loss; no list of past customers to remarket to.
- **Waste signals:** Salesforce for a 5-person shop; any CRM without a defined follow-up process behind it.
- **Tools:** Sheet + calendar discipline → Airtable CRM, HubSpot free tier → industry CRM.

### 9. API & Integration Layer
- **Problem:** Tools that don't talk force humans to be the integration.
- **Need signals:** Double entry between two systems that both have APIs.
- **Waste signals:** Replacing two working tools with one expensive suite when a $20/mo connector fixes the gap.
- **Tools:** Native integrations → Make.com/Zapier connectors → REST API + webhooks (custom glue).
- **This is Chris's core build territory.** Small, high-value, defensible.

### 10. AI & Intelligent Automation
- **Problem:** Judgment-flavored grunt work: reading, extracting, drafting, classifying, summarizing.
- **What AI actually does well for an SMB today:**
  - Extract structured data from unstructured input (invoices, emails, photos, plans)
  - Draft first versions (quotes, follow-ups, job descriptions, reports)
  - Summarize long material (meeting notes, threads, documents)
  - Classify and route (leads, tickets, expenses)
  - Answer questions over the company's own documents
  - Agent workflows: multi-step tasks chained with checks (newest, highest risk/reward)
- **Need signals:** Skilled people spending hours reading/retyping/drafting; knowledge trapped in documents nobody searches.
- **Waste signals:** "We need AI" with no named workflow; AI bolted onto a process that should be eliminated (rung 1); chatbots nobody asked for; per-seat AI licenses for staff who won't use them.
- **Tools:** ChatGPT/Claude used well (train the team) → API-level integration (Anthropic/OpenAI) → LangChain/agent frameworks.
- **Rule:** AI is a layer on a working process, not a rescue for a broken one.
- **Agent-tool vetting screen:** before recommending or adopting an agent
  workflow, price risk as well as cost. Form factor sets the risk floor:
  chat-with-tools → enterprise agent builder → browser/computer-use agent.
  Check for: agent-specific safety evals, sandboxing/isolation, single-agent
  stop/pause controls, approval gates for sensitive actions,
  disclosure/identity behavior when interacting with third parties, and —
  when the target system isn't internet-reachable — whether the vendor has
  any no-inbound-port private-network bridge at all; coverage varies by
  vendor, and specific offerings should be reverified against current docs
  rather than assumed from memory. Builder
  platforms shift guardrail responsibility to the deploying business; count
  that as hidden ROI/liability cost. Failed checks are not automatic
  rejection — they raise the risk price of the recommendation. Source detail
  lives in `03-WIKIS\AI_AUTOMATION_SYSTEMS`.

### 11. Documentation & Knowledge Management
- **Problem:** The business lives in one person's head. That person can quit.
- **Need signals:** Only Mike knows how to close out a job; training a new hire takes months of shadowing.
- **Waste signals:** Wiki platforms when the problem is nobody writes anything; SOPs written once and never used.
- **Tools:** Google Docs SOPs + naming convention → Notion → AI-assisted SOP generation from recordings.

### 12. Custom Internal Tools
- **Problem:** A real, specific need no off-the-shelf tool serves — after rungs 1–5 are exhausted.
- **Need signals:** Genuinely unique workflow; integration glue with logic; heavy manual work with no vendor solution.
- **Waste signals:** Building what Jobber already sells for $39/mo. Ego builds. Anything the client can't operate after Chris leaves.
- **Tools:** Python scripts → Flask apps → Retool → full custom.
- **Rule:** Build last, build small, build maintainable.

---

## Selling the Map — How Knowledge Becomes Revenue

1. **The audit is the first product.** The map makes audit findings specific:
   not "you have communication problems" but "your job status lives in
   texts (category 6) and your foreman re-types it daily (category 4)."
2. **Vendor neutrality is the moat.** Software salesmen sell their product.
   Chris sells the ladder — including "don't buy anything." That is why
   the second call happens.
3. **Every recommendation ships with numbers:** cost, hours saved per week,
   payback period. A rec without ROI math is an opinion, not a deliverable.
4. **The retainer is maintenance of the ladder:** tools drift, processes
   grow back, new waste appears. The map makes the ongoing relationship
   legible to the client.

---

## Maintaining the Map — Cadence

- **Weekly (30 min max):** one landscape rep — study one category, one tool,
  or one real business use case. Feed notes to the wiki or straight here.
  Source: Clippings, wiki `priority/now` pages, ConstructionDive tech section.
- **Monthly:** review this file alongside SKILL_GAP_ANALYSIS.md. Reprioritize
  categories against the permanent capability base, current strategy, and live proof.
- **No orphan knowledge:** every category studied must connect to school,
  a client service, POL/tracker, or an audit scenario — same rule as skills.
- **Guard:** landscape study is preparation, not production. If map work
  displaces audit-methodology work or build sessions two weeks running,
  rebalance (this is the "landscape awareness becoming procrastination"
  risk from CHRIS.md, and the wiki-as-time-sink risk from NORTH_STAR.md).

---

## Current State — July 15, 2026

**Demonstrated movement:** Python Stage 1 is verified and Stage 2 is active. The
Academic Tracker V1 shipped on Python/SQLite and now waits for real course data around
July 25. Revenue Lab's bounded scanner exercised Python, SQLite, and a public API.
The first Make.com landscape rep was completed July 9. The Goal/TOC material and
construction-domain knowledge are available for audit work.

**Live gaps (in priority order):**
1. SQL remains the July monthly weak link; the next meaningful proof is using the
   tracker with verified real course data, not expanding V2 speculatively.
2. Category 3 (Looker Studio) still needs its first hands-on dashboard rep. Category
   4 (Make.com) has one landscape rep but not yet a reused recommendation pattern.
3. API use is no longer zero, but integration depth and vendor-neutral selection
   judgment remain early.
4. ROI math practice remains open; no real recommendation has yet been costed.

**Sequencing rule:** prerequisites and the monthly weak-link review guide the next
rep, but there is no permanent tool-by-tool lock. Prefer the smallest real project
or decision that exercises the live gap without displacing school or verified work.

---
*One file, one map. Wiki refines; this file operationalizes; audits sell it.*
*Last updated: July 15, 2026 (post-North-Star factual reconciliation; July 5 weak-link ranking preserved until the August monthly review) | Next review: August 1, 2026*
