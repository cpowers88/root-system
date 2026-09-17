---
type: template
tags:
  - template
  - delivery
stage: phase-2
timeline: reference
---

# Scope of Work Template

Signed at kickoff of every project, referencing your MSA ([[business-setup|Business Setup]], Tier 2). This is the document that protects the margin, the timeline, and the relationship — [[fulfillment-system|Fulfillment System]], stage 1. If a dispute ever starts with "but I thought...", the answer lives here or the template needs improving.

---

# Statement of Work #[N] — [Project Name]
Under the Master Service Agreement dated [date] between [Your Company] and [Client Company].

## 1. Deliverables
*Numbered, specific, testable. "A working automation that..." not "automation support."*
1. [Deliverable]: when [trigger], the system [action], with [error handling behavior]. Acceptance: [the test the client will run].
2. ...
3. System documentation + training recordings ([X] videos, ≤5 min each)
4. 30-day post-launch support (bug fixes and adjustments to delivered scope; not new features)

## 2. Explicitly Out of Scope
*The most valuable section. Name the adjacent things they might assume are included:*
- [e.g., Migration of historical data prior to [date]]
- [e.g., Changes to the accounting system's chart of accounts]
- [e.g., Workflows for the [X] department]
- Anything not listed in §1. New requests are welcomed via Change Request (§6).

## 3. Success Metrics & Baseline
| Metric | Baseline (measured [date]) | Target |
|---|---|---|
| [e.g., minutes per quote] | | |
| [e.g., leads receiving same-hour response] | | |

*Baselines recorded NOW, at kickoff. No baseline, no provable result, no [[05-BUSINESS/03-Case Studies/CASE_STUDY_TEMPLATE|case study]].*

## 4. Client Responsibilities
Delays in these extend the timeline day-for-day:
- Access/credentials to [systems] by [date] (via password manager invite — no credentials over email)
- [Named person] available for questions with ≤[2] business-day response
- Decision-maker sign-off at: design approval, pre-launch acceptance test
- Sample/historical data: [specifics] by [date]

## 5. Timeline & Payment
| Milestone | Date | Payment |
|---|---|---|
| Kickoff (this SOW signed) | | 50% — $[X] |
| Build complete → acceptance testing | | — |
| Launch + handoff | | 50% — $[X] |

Third-party software: [list, est. monthly cost] — contracted and billed in Client's name; Client owns all accounts and data.

## 6. Change Requests
Any addition or modification to §1 is quoted in writing (even at $0) and appended to this SOW on approval. Verbal requests are honored as conversations, not commitments.

## 7. Ownership, Access & Support
- All systems built under this SOW run in Client-owned accounts; Client owns the workflows and data. [Your Company] retains ownership of pre-existing templates, internal tooling, and general know-how.
- On completion, admin access documented and held by: [Client person] + [Your Company] (for support).
- After the included 30-day support window, maintenance is available under a support agreement ([separate one-pager]) or ad hoc at $[X].

**Agreed:**
[Client] ______ date ______ · [Your Company] ______ date ______

---

## Internal Pre-Signature Checklist (delete from client copy)
- [ ] Every deliverable has an acceptance test a non-technical client can run
- [ ] Out-of-scope list written for THIS client's likely assumptions, not copied from the last SOW
- [ ] Baselines scheduled for kickoff week, owner assigned
- [ ] Timeline includes client-dependency buffer (their delays are the #1 slip cause)
- [ ] Retainer conversation queued for the handoff agenda ([[retainer-model|Retainer Model]])
