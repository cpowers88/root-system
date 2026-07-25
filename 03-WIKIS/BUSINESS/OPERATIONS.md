---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [business, governance]
created: 2026-07-24
---

# BUSINESS_WIKI — OPERATIONS

## Function

Maintain a compounding evidence-and-method system for diagnosing business
problems, designing offers and delivery methods, testing economic claims, and
returning verified results to the current strategy.

This wiki supports a vehicle. It does not choose or govern the vehicle.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR\NORTH_STAR.md` |
| Adaptive capability and value outcomes | `01-NORTH_STAR\Goals & Milestones\` |
| Current business vehicle and assumptions | `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` |
| Business evidence, methods, offer components, and economic models | this wiki |
| Sequencing, test activation, and proof status | CASTLE and `NOW.md` |
| Reusable sanitized business assets | `05-BUSINESS\` |
| Active client-specific/private work | separate authorized client workspace |
| External material signals | Watchtower |

No file in this wiki MAY redefine the North Star, activate a business action,
change the current strategy, or claim market proof from generated material.

## Layers

```text
raw evidence -> maintained wiki knowledge -> bounded test -> measured outcome
     ^                 |                         |              |
 immutable       BUSINESS owns            CASTLE activates    owner returns
```

`raw\` is immutable. AI MUST NOT create, edit, move, rename, archive, or delete
anything under it without Chris explicitly authorizing the named exception.

## Operations

### INGEST

1. State the business question.
2. Read the source completely in bounded chunks when large.
3. Classify source tier, date, scope, limitations, and volatility.
4. Update an existing evidence or method page before creating a page.
5. Separate verified claim, source claim, inference, hypothesis, and unknown.
6. Record contradictions and supersession explicitly.
7. Update `wiki\index.md` when discovery changes.
8. Append the operation and source coverage to `wiki\log.md`.

### QUERY

1. Read `wiki\index.md`.
2. Load only the pages and evidence needed.
3. Answer with claim status and source traceability.
4. File the result only when it is durable, reusable, and has one clear owner.
5. Do not convert a conversation, idea, or estimate into strategy or proof.

### LINT

Check:

- unresolved links and orphan pages;
- duplicate owners and copied strategy;
- stale or undated prices, market claims, vendors, and regulations;
- contradictions and silently superseded claims;
- evidence pages without source traceability;
- methods without a measurable use test;
- scenarios presented as plans;
- templates stored in the wiki instead of the asset system;
- index-versus-tree drift; and
- field results that were never returned to their owner.

## Page contract

Every maintained knowledge page MUST identify:

1. `type`;
2. `timeline`;
3. `status` when operationally meaningful;
4. purpose and owned question;
5. claim/evidence status;
6. source or owner links;
7. use condition;
8. proof or falsification condition;
9. risks and limitations; and
10. related pages.

Use `stage` only for a stable classification. Never use it to copy live CASTLE
phase or current execution state.

## Evidence standard

- Prices, adoption rates, market sizes, legal/tax guidance, product
  capabilities, and vendor recommendations MUST include an as-of date and
  source.
- Vendor, affiliate, anecdotal, or self-reported evidence MUST be labeled.
- A forecast is a scenario until real outcomes calibrate it.
- Willingness to talk is not willingness to pay.
- A proposal is not revenue.
- Revenue is recorded only when received.
- A reusable asset is proven only through use or validated reuse.

## Action and safety

Business pages MAY explain an action. They MUST NOT authorize outreach,
publication, purchases, account creation, pricing commitments, filing,
contracts, client work, or use of private/client data.

Chris explicitly approves consequential action. CASTLE activates bounded tests.
Filled client artifacts never live in this wiki.

## Return packet

Every real test returns:

1. outcome;
2. evidence link;
3. affected strategy assumption or goal;
4. capability/status movement;
5. reusable-asset candidate;
6. system-learning candidate; and
7. next decision and review trigger.

## Close

A BUSINESS change is complete only when affected claims remain traceable,
navigation resolves, the log records the operation, active authority is not
duplicated, and the owner can retrieve the result in a fresh session.
