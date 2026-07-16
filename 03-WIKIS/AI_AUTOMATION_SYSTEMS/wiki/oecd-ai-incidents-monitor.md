---
type: research
tags: [ai-automation, governance, risk-management, incidents, audit-vocabulary]
source: raw/OECD AI Incidents Monitor, an evidence base for trustworthy AI.md (captured 2026-07-09) + raw/2604.21412v3.pdf (Mengesha et al., 27 pp.) + raw/2604.23183v2.pdf (Gomez et al., 10 pp.); both papers reviewed in page-range chunks 2026-07-15
---

# OECD AI Incidents Monitor (AIM) — Live Evidence Base of AI Harms

**oecd.ai/en/incidents (beta).** The OECD's automated monitor of AI incidents and
hazards, built from public news sources (Event Registry data, Azure-processed,
AI-classified). **~16,300 incidents & hazards** catalogued at capture (July 9,
2026). Built for policymakers, but it doubles as a free, filterable,
continuously-updated catalog of *how AI deployments actually fail* — the
empirical companion to [[nist-ai-rmf]]'s risk vocabulary and the incident-history
check in the promoted vetting screen.

## How it classifies

- **AI Incident** — harm materialized, AI's role pivotal (jobs eliminated,
  wrongful bans, privacy violated, fraud completed).
- **AI Hazard** — credible potential harm, not yet realized (autonomous-weapons
  programs, systemic financial risk warnings, automation-driven job threats).
- Each entry is filterable by: AI principle violated · industry · **harm type** ·
  severity · affected stakeholders · **business function** · **autonomy level** ·
  AI task. Every entry carries a stated rationale for its classification and
  links to the underlying articles. One trend note from the OECD itself:
  incidents are *rising in absolute count but falling as a share of all AI news*.

## Failure classes worth keeping named (July 2026 sample)

| Incident | Failure class | Audit-relevant lesson |
|---|---|---|
| Discord AI moderation bug wrongfully bans 8,000+ users (spreadsheets flagged as harmful, **bypassing human review**) | False positives at scale, no review gate | The human-review-gate argument, with a number attached |
| Allianz cuts 1,500–1,800 jobs in AI claims/customer-service automation | Workforce displacement as incident | Role-redesign (not silent elimination) is what separates transformation from harm — the human-agent operating model's selling point |
| Flock license-plate AI misused by police for personal searches | Authorized system, unauthorized use | Access governance outlives deployment; usage auditing is part of the build |
| AI chatbots give inconsistent, demographically biased financial advice (UGA/Rome study) | Output bias in advice systems | Never ship advice-shaped output without QC sampling — [[nist-ai-rmf]] MEASURE in practice |
| Lawyer sanctioned for prompt injection hidden in a court filing (Brazil, detected by the court's own AI) | Adversarial input via documents | Prompt injection is a live, prosecuted, real-world attack — see [[mcp-security-and-authorization]] |
| Deepfake doctor videos target elderly patients; AI-generated fraud schemes (Madrid) | Synthetic-media fraud | Client-facing trust systems need provenance answers |
| Secret Network $4.7M bridge hack, AI-assisted exploit of old code | AI as attacker leverage | Aging code is now cheaper to exploit — maintenance retainers have a security dimension |

## Why this matters for this wiki / `.ROOT`

1. **Vetting-screen depth.** The promoted Category 10 vetting checklist asks
   about incident history — AIM is the *lookup table*: search a vendor/tool
   before recommending it, cite what surfaces.
2. **Audit vocabulary with receipts.** "What breaks if we automate this without
   a review gate?" now has named, dated, sourced answers (Discord's 8,000 bans
   is the one-liner). Pairs with [[nist-ai-rmf]]'s MAP/MEASURE functions when a
   client engagement needs formal risk language.
3. **Standing reference, not a feed to chase.** This wiki holds AIM as a
   *lookup resource*; horizon-scanning stays the Watchtower's job per its own
   cadence. If a pattern from AIM ever suggests a service opportunity, it routes
   through the castle gate like any other signal — eyes, not hands.
4. **The counter-file.** `.ROOT` mostly ingests capability evidence (what agents
   can do). AIM is the failure evidence (what deployments actually did wrong) —
   the balance a credible vendor-neutral advisor needs.

## 2026 method layer — counts are not trends

Two 2026 technical-governance papers turn AIM from a lookup catalog into a
more disciplined monitoring input. This is a **supporting-extension** claim
change: the earlier page remains valid, but raw incident counts are now
explicitly insufficient for trend claims.

Mengesha et al. show that a rising incident count can mean more reporting,
more deployed AI (exposure), more harm per use, or some combination. Their
SORT monitoring question makes four choices explicit: **Subject,
Opportunity, Risk event, Timeframe**. Analysts then estimate harm and exposure
separately, state evidence quality, and classify the trajectory:

| Exposure | Harm per exposure | Classification |
|---|---|---|
| rising | rising | Escalating |
| rising | falling | Mitigating |
| falling | rising | Concentrating |
| falling | falling | Receding |
| direction not defensible | direction not defensible | Unclassifiable / abstain |

The important audit discipline is principled abstention. News-derived AIM data
overrepresents visible, dramatic, English-language events and can fragment one
incident across articles. It is strong for examples and hypotheses; it is not
automatically a denominator-corrected risk rate.

Gomez et al. stress-test escalation logic against ten incidents and identify a
three-layer dependency: definitions, available data, and trigger logic. A gap
upstream creates downstream under-detection. Two recurring blind spots are
individual-event criteria that miss cumulative harm and discrete-event rules
that miss standing population-level conditions. Their eight checks cover AI
causation, scope, immediate triggers, pattern aggregation, harm category and
severity, cross-border propagation, irreversibility, and near misses.

### Client-audit use

For a vendor or workflow review, use AIM in three passes:

1. Look up named incidents and hazards for the tool, vendor, task, and sector.
2. Do not call the count a trend until exposure and reporting changes are
   considered through a SORT-style question.
3. Test whether the client's escalation rules can see clusters, near misses,
   cumulative harm, and ongoing conditions—not only one severe event at a time.

## Links to related pages

- [[nist-ai-rmf]] — the framework; AIM is the incident evidence it manages against
- [[mcp-security-and-authorization]] — the technical threat catalog beneath several AIM classes
- [[agent-vetting-worked-examples]] — where incident history feeds scoring rows
- [[work-trend-index-2024-2026]] — the adoption arc AIM is the shadow side of
