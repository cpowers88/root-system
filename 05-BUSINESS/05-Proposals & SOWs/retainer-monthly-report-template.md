---
type: template
tags:
  - template
  - retainer
stage: phase-3
timeline: reference
---

# Retainer Monthly Report Template

One page, sent to every retainer client every month — [[retainer-model|Retainer Model]]'s retention tool. Its job is making invisible work visible: monitoring, prevented failures, and accumulated value. Automate the data population early ([[tool-stack|Tool Stack]]); assembling these by hand across ten clients destroys retainer margin.

---

# Systems Report — [Client] · [Month Year]
**Plan:** [Tier name] · **Systems under management:** [N]

## Health Summary
| System | Status | Runs this month | Issues |
|---|---|---|---|
| [Lead intake automation] | 🟢 Healthy | [1,240] | 0 |
| [Quote assembly] | 🟢 Healthy | [214] | 1 (resolved, see below) |
| [Invoice pipeline] | 🟡 Watch | [156] | [API deprecation upcoming — action planned] |

## What We Fixed Before You Noticed
*The section that renews retainers. Every intervention, however small:*
- [Date]: [e.g., CRM API update broke lead routing at 6:42am; alert fired, fixed by 8:15am — zero leads lost]
- [Date]: [e.g., quote template error on 3-line-item edge case; patched, affected quote resent]

## Improvements Made This Month
*Tier 2+: enhancement hours applied:*
- [e.g., Added supplier B to the invoice extraction pipeline]
- Enhancement hours: [used]/[included] — *[if consistently maxed: "we're hitting the ceiling of this tier — worth discussing the next one"]*

## Value Scoreboard (Cumulative)
| | This month | Since start |
|---|---|---|
| Automated task runs | | |
| Estimated hours saved | [runs × baseline minutes] | |
| Estimated labor value | @ $[loaded rate]/hr | **$[X]** |

*Keep the math conservative and consistent with the original [[smb-ai-audit-method|audit]] baselines — this number should be unimpeachable, because it's the number that makes the renewal conversation unnecessary.*

## Next Month
- [Planned maintenance/updates]
- [Recommended next improvement + why]
- [Anything needed from you: access, decision, 15 minutes]

Questions? [Reply / book time: link]

---

## Internal (strip before sending)
- [ ] Actual hours spent this client this month: ___ (→ margin tracking, re-tier trigger at >130% of tier for 2 consecutive months)
- [ ] Expansion signals noticed (new pain mentioned, new hire, new system bought): ___ → log in CRM
- [ ] Quarterly mini-audit due? ([Tier 2+] — schedule it)
