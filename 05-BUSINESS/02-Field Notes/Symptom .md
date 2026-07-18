Symptom — the visible surface effect, not the cause. Like a stain on the ceiling: it's real, but it's not the leak.
→ Your answer, with a line pointing to which part of the note/map shows it.
Waste — effort, time, or motion spent that produces no value and would vanish in a well-run version of this business. Like re-measuring a wall because the first note got lost.
→ Your answer + evidence pointer.
Root-cause hypothesis — the one underlying mechanism you believe is driving multiple symptoms at once. Like a slow roof leak explaining the stain, the mold smell, and the tripped breaker all at the same time. This should be a claim you could be wrong about, not a fact.
→ Your answer + evidence pointer.
Constraint — a hard boundary any solution has to work inside, not a problem to solve away. Like a load-bearing wall — you design around it, you don't remove it.
→ Your answer + evidence pointer.

## Small Business problem — Daily Gate (Day 1, Systems Audit)

**Symptom** — Payment is frequently late or less than the amount invoiced or agreed to.
Evidence: `observation_one.md`, Amendment Q7 — "This happens on almost every job... probably in the 80-90th% of jobs you need to wait for pay," with reduced payment separately common. This is the cleanest visible, measurable surface effect across the whole workflow — the thing you can actually count.

**Waste** — Small extras performed and absorbed without billing or documentation.
Evidence: swimlane Step 6a ("often never even recorded... just a phone call explanation") plus the added insight that owners do small fixes "without even a mention." This is pure motion-and-material spend that produces zero return and isn't even visible to the client as delivered value — the worst kind of waste, since it doesn't even buy goodwill.

**Root-cause hypothesis** — No durable, written record gets created at the moment either the original price or any change is agreed to — so nothing exists afterward except memory to bill against, defend, or enforce.
Evidence, converging three separate ways: the swimlane's 6a annotation, the systems inventory's "no record" answer at every company tier (small, medium, and large), and the data-flow trace's explicit finding that "durable approval dies when the phone call ends." One mechanism, and it's falsifiable: if it's right, jobs with a written change order should get paid faster/fuller than jobs without one.

**Constraint** — The owner is the sole holder of almost all job information (pricing, scope, approvals), there's no admin capacity to offload it to, and margins are thin enough that any added tool has to prove itself immediately or it gets abandoned.
Evidence: `observation_one.md`'s "what breaks if I remove this" answer — remove the owner and the business doesn't exist — plus the systems inventory showing "Owner" as the small-tier system across nearly every step. Trust/adoption resistance is a real design requirement layered on top of this wall, not the wall itself.
