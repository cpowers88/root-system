---
type: project
tags: [parked, project]
---

# TCG POS SYSTEM — Scoping Document
#TCG #projects 
## Status: PENDING COMMITMENT | Do Not Build Until This Is Complete
### Last updated: May 23, 2026

---

## THE OPPORTUNITY
A contact has indicated they could get 100 TCG (trading card game) retail stores to sign up if the system is "done right."

**This is an opportunity, not a commitment.**

Do not write a single line of TCG code until the scoping conversation has produced written answers to every question below.

---

## SCOPING CONVERSATION — GET ANSWERS TO ALL OF THESE

### The Contact
- **Name:**
- **Role:** (store owner? distributor? industry connection?)
- **Date of conversation:**
- **How they know you:**

### The Commitment Question
- Did they offer to pay for the product or connect you to stores that would?
- What exactly did "100 stores" mean — their own customers? Their network? A guess?
- Would they sign a letter of intent, even informal?

### The Product Questions
**Features — what does "done right" mean exactly?**
- [ ] Inventory management (what types of cards — singles, sealed, graded?)
- [ ] Point of sale (cash, card, store credit?)
- [ ] Customer accounts / loyalty program?
- [ ] Trade-in / buylist management?
- [ ] Online sales integration (TCGPlayer, eBay)?
- [ ] Tournament management?
- [ ] Reporting and analytics?
- [ ] Multi-store / chain support?
- [ ] Mobile POS?

**What do stores use TODAY?**
- Current POS systems in use:
- Biggest pain with current systems:
- What would they switch for immediately?

### The Business Questions
- What would a store owner pay per month for a great POS? ($49? $99? $199?)
- What would the contact's role be — referral partner? White-label? Revenue share?
- Who are the actual 100 stores — can you get 3 names to interview?
- What's the timeline they're thinking?

---

## MVP DEFINITION (fill after scoping conversation)
The absolute minimum feature set to get first paying customers:

| Feature | Must Have | Nice to Have | Out of Scope |
|---|---|---|---|
| Basic POS (cash/card) | | | |
| Inventory tracking | | | |
| Customer accounts | | | |
| Trade-in management | | | |
| Reporting | | | |

---

## GO / NO-GO DECISION FRAMEWORK

**GO if:**
- Contact can name 5 specific stores that would pay
- Price point is confirmed ($X/month per store)
- MVP is defined and scoped to under 90 days of build time
- Contact commits to being a beta customer or referral partner in writing

**NO-GO / PAUSE if:**
- Contact goes quiet after the scoping conversation
- "100 stores" turns out to be vague enthusiasm
- Feature list is too large for solo development
- Price point doesn't make business sense

**Decision deadline:** End of Month 1 (June 23, 2026)
If no commitment by then, TCG POS is formally paused until further notice.

---

## TECHNICAL STACK (if GO decision is made)

**Language:** Python
**Backend:** FastAPI (better for multi-client SaaS than Flask)
**Database:** PostgreSQL (multi-tenant from the start)
**Frontend:** Simple HTML/CSS to start → upgrade later
**Payment processing:** Stripe
**Hosting:** AWS / DigitalOcean

**Estimated MVP build time (after Python foundation is solid):** 60-90 days
**Estimated MVP build time (right now, with current skills):** Not realistic solo

---

## MARKET CONTEXT

TCG POS is a real gap — most stores use generic POS systems (Square, Shopify) that don't understand:
- Card conditions and grading
- Buylist pricing
- Set-based inventory organization
- Trade-in workflows

Existing players: Crystal Commerce, GrowthZone, BinderPOS (research these before building)
Key question: why would a store choose your product over BinderPOS?

---

*Part of Chris Powers Second Brain | Notion: Projects database | Drive: 01_ACTIVE_PROJECTS/TCG_POS*
*Do not move to active build until GO decision is documented here.*
