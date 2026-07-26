---
type: report
timeline: now
status: complete
tags: [technology, mcp, bootcamp, system-evolution]
created: 2026-07-26
---

# Claude Independent Verdict — MCP Bootcamp Lane (Days 1–8)

**Gate:** 2026-07-26 Joint Review 1
**Bar:** the July 25 acceptance test in `ADVISOR_BUILDER_INTEGRATION_BOOT_CAMP_REVIEW_2026-07-17.md` (lines 525–550), including its honest floor
**Protocol:** written from artifacts and live execution, not from the daily reports. I ran the server myself before scoring it.

## Verdict

**The lane failed its own acceptance test — and the single condition it passed is
the one that was hardest to build and is in better shape than any report claims.
Modify the format; do not revert the work.**

Scored strictly: **1 of 7 pass conditions met.** The honest floor permits waiving
two of the remaining six. Even at the floor, this is a fail.

That is the correct headline, and it is not the useful one. The useful one is
below, in the process finding.

## What I verified myself

I did not take Day 4 or Day 5 status from any report. I executed
`mcp_contracts.py` against the fixture directly, then drove `server.py` over real
stdio with an SDK client — initialize, `list_resources`, `read_resource`,
`list_tools`, `call_tool`, plus five failure paths.

**The server works end to end.** This is new information; nothing on disk records
it having been run.

```
INITIALIZE ok -> bootcamp-friction-server 0.1.0
RESOURCES    -> [('All Friction Records', 'friction://all-records')]
READ_RESOURCE-> rows: 6
TOOLS        -> ['search_by_problem_keyword', 'count_by_friction_category']
CALL search('estimates')  -> 1 structured JSON record
CALL count()              -> 6 rows
EDGE empty keyword -> isError=True   (rejected before the handler ran)
EDGE literal %     -> isError=False, 6 rows   <-- open defect
EDGE literal _     -> isError=False, 6 rows   <-- open defect
EDGE missing arg   -> isError=True, "Input validation error: 'keyword' is a required property"
EDGE unknown tool  -> isError=True, "Unknown tool: no_such_tool"
```

Environment note: the MCP SDK (1.28.1) is installed in the project `.venv`, not
system Python. My first check used the wrong interpreter and briefly suggested the
server had never been runnable. It is, and it does.

### Two findings that change the Day 5 picture

**1. One of the two deferred edge cases was already closed — by Chris's own schema.**
The July 22 session deferred "empty keyword" and "literal `%`/`_`" as open threads.
Empty keyword is *not* open. The `"minLength": 1` Chris wrote into the
`inputSchema` causes the SDK to reject the call before the handler executes. The
contract did the job a contract exists to do, and nobody knew because nobody ran it.

**2. The wildcard case is genuinely open, and it is the more interesting one.**
`%` and `_` both return all six rows. Parameterized `?` binding stopped SQL
injection — the thing the Day 4 explain-back gate was about — but it does **not**
escape `LIKE` metacharacters. Those are different defenses against different
problems, and passing the injection gate did not close this. That distinction is
the single best remaining teaching item in the lane.

**3. The evening reading's technical prediction was wrong.** It named
`arguments["keyword"]` on `server.py:74` as "the first thing Inspector will break."
It is not: `required: ["keyword"]` in the declared schema rejects the call first,
with a clean structured error. The reading pointed at a real-looking risk that the
code had already defended. Worth recording — the reading is generated nightly and
its technical claims are not currently verified before Chris reads them.

## Scored against the real bar

| July 25 acceptance condition | Result |
|---|---|
| stdio server, exactly 1 resource + 2 read-only tools, typed/validated inputs, structured outputs **and error responses** | **PASS** — verified live today, including structured errors |
| pytest suite green: normal, edge, invalid, prohibited-operation | **FAIL** — no test file exists |
| Verified through MCP Inspector | **FAIL** — never run |
| One successful connection from a real MCP host | **FAIL** — *waivable at the floor* |
| Tool-call logging to stderr/file only, stdout never touched | **FAIL** — zero logging code anywhere in `Code\` |
| One-page operator/security handoff | **FAIL** — *waivable at the floor*; Day 6 never ran |
| Chris cold-explains host → client → server → tool → result, no notes | **NOT ATTEMPTED** — partial evidence below |

Days 6, 7 and 8 never ran. `MASTER_BLUEPRINT.md` carries layers for Days 1–4 only;
Day 5 has working code and no blueprint layer. No file in `Code\` or `Docs\` has
changed since **July 23, 16:16**.

## The process finding — the one worth the review's time

**The honest floor had a trigger, a date, and a defined cut. It never fired.**

The bar reads: *"if by end of Thu Jul 23 the server/tests/Inspector triad isn't
solid, cut the host-connection step and/or the written handoff."* On July 23 the
triad was not solid — that was precisely the trigger condition. Nobody ran the
check. So scope never flexed down, and instead of the reduced-scope pass the floor
was designed to deliver, the lane took an unreduced fail.

The stop rule was well-designed and correctly dated. It had no owner and no
scheduled moment of evaluation, so it was inert.

This is the same failure class as this month's other finding, one turn earlier in
the chain. July's was *machine output became truth without a check*. This is
*a check that was never run at all*. Both are the same root defect: the system
writes good rules and does not schedule their verification.

That generalizes past this bootcamp, and it is the item I would carry to the
August decision gate.

## Chris's explain-back, scored honestly

Offered unprompted this morning, not under gate conditions:

> *"we can ask for cheese, it will come back with 12 types of cheese, or go deeper
> and say swiss cheese and it will ask if we want sharp or whatever."*

**What this gets right, and it is not trivial:** discovery precedes invocation. You
ask the counter what it has before you order. That is exactly `list_tools` /
`list_resources` → `call_tool`, and it is the right shape. It also carries the
access boundary implicitly — you talk to the counter, you do not walk behind it.
The server owns the data; you get what it chooses to expose. That is the
least-privilege idea in plain language.

**What it misses, and the miss is precise:** in the analogy *the counter asks the
clarifying question*. MCP servers never do that. The server publishes a typed menu
up front — the `inputSchema` — and the **model** decides what to order and fills in
the arguments. There is no back-and-forth negotiation at the counter.

Chris's own code proves this better than the analogy does. The `minLength: 1` case
above is a blank order slip being rejected by the order form itself. The deli guy
did not ask "did you mean something?" — the menu refused to accept it. That is the
difference between a conversation and a contract, and it is the whole point of MCP.

The analogy also does not yet separate **resource** ("here is the entire case, look
at everything") from **tool** ("count how many cheeses per category"). The
docstrings in `mcp_contracts.py` state that distinction cleanly — better than the
spoken version does.

**Score:** partial. Discovery-then-invocation and the access boundary are real and
held four days after last contact. Host / client / server separation and the
typed-contract mechanism are not demonstrated. The formal cold explain-back
condition remains untried, and I would not mark it passed from this.

## What the lane actually earned

Per the bar's own instruction, harvest as **MCP fundamentals capability plus a
reusable fixture-audit-table pattern** — *not* Advisor-Builder market evidence.
Nothing here is proof of demand, willingness to pay, or deployment readiness, and
the sprint plan said so before it started.

Durable and verified:
- A working stdio MCP server with validated inputs and structured error responses.
- Three read-only contracts, executing correctly, with docstrings that state *why*
  each is a resource or a tool rather than only what it does.
- A two-table FK-linked fixture built from a real field observation, not a synthetic one.
- One reusable wiki page (`sql-python-sqlite3-integration.md`).
- Four master-blueprint lens layers (Days 1–4).

That is a real four-day outcome. It is not an eight-day outcome, and the file should
stop implying one.

## Recommendation to the Joint Review

**Modify.** Specifically:

1. **Finish-to-acceptance beats advance-a-lens.** The one-lens-per-day structure
   kept moving forward while leaving the acceptance conditions behind it unmet. Day
   5 code was written the same afternoon Day 5 verification was skipped. Close a
   narrow thing completely before opening the next lens.
2. **Give every stop rule an owner and a scheduled check.** A dated trigger nobody
   is assigned to evaluate does not exist. This is the finding I would generalize.
3. **The cheapest real win available:** ~90 minutes closes pytest, the `LIKE`
   wildcard defect, and stderr logging — three of the five open conditions — against
   code that already works. That is a far better Monday than starting Day 6.
4. **Do not schedule it against the simulation week.** Monday is 20 academic blocks
   with an explicit "optional system work displacing academic blocks: 0" target. The
   MCP remainder is a weekend item or it waits.
5. **Verify the evening reading's technical claims** before they reach Chris, or
   mark them explicitly as unverified prompts. Finding 3 above is the first known
   instance of a wrong one.

## Confidence

**High** on everything mechanical — I ran the server, the failure paths, and the
contracts, and the timestamps are independent of anyone's memory. **High** on the
acceptance scoring; the bar is unusually explicit and I scored it as written.
**Moderate** on the explain-back score, from one unprompted comment rather than a
gate. **None** on any claim about market value, which this lane was never built to
produce.

---

# Cross-Read Addendum — 2026-07-26, after reading Codex's lane

Everything above was written blind and is left unedited. Codex's
`Docs\weekly-code-learning-review-2026-07-20-to-2026-07-25.md` was published the
same morning. **The blindness ran one direction:** Codex read my `_smoke_tmp.py`
output and folded its results in (its lines 89–94), so its code-correctness
judgment is partly downstream of mine. Score the convergence accordingly — it is
strong on the findings we reached separately, weaker on the ones it inherited.

## Where we converge independently

Displacement as the primary failure; MCP as useful partial proof rather than a
pass; adopt the teaching loop for PYTHON; Stage 3 not yet closed; the `%`/`_`
wildcard defect; no pytest; no logging. Neither lane needed the other to reach
these, and Codex states the displacement finding more plainly than I did.

## Where Codex is right and I was wrong

**1. The empty-keyword claim above is overstated. Correct it.**
I wrote that the thread "is *not* open" because `minLength: 1` rejects it. Codex's
item 3 is sharper and correct: the schema rejects it **at the protocol boundary
only**. `handle_call_tool()` and `search_by_problem_keyword()` do not independently
enforce it — calling the contract function directly with `""` still returns all six
rows. That is defense at one layer, not defense in depth, and the hole is live for
exactly the caller a pytest suite would use. My framing would have led someone to
skip a test that is still needed.

**2. I cannot support "Chris's own schema," and the record says otherwise.**
Codex's ownership section records that parts of `server.py` — resource registration
and second-tool wiring — were completed by Claude while Chris was occupied, with
the required diff review and explain-back never performed. `minLength: 1` sits in
`list_tools`, inside that region. I had no authorship record and inferred from the
artifact. Withdraw the attribution; the schema line's author is unestablished and
probably not Chris.

This also makes Day 5 a **live-pairing rule violation**, not just an unfinished day.
The sprint's binding rule was that no AI produces a finished artifact Chris did not
type, decide, or explain back. That is a heavier finding than "Day 5 didn't close,"
and it belongs in the review.

**3. A real defect I missed entirely.**
`DB_PATH = "bootcamp_fixture.db"` is working-directory-relative. The server cannot
find its database when launched from anywhere but `Code\`. I ran my client from
inside `Code\`, so I never hit it. This is precisely what breaks acceptance
condition #4 — a real MCP host launches the server with its own working directory.
Codex's catch is better than anything in my gap list, and it converts "host
connection was never attempted" into "host connection would have failed."

I verified this rather than accepting it, and the defect is **worse than either of
us stated**. `sqlite3.connect()` on a relative path does not fail when the file is
absent — it silently *creates* an empty database there, then dies on the first
query with `no such table: businesses`. So a host launching this server from its
own working directory gets a confusing schema error instead of a clean
file-not-found, plus a stray 0-byte decoy `.db` littered wherever it started. My
own check produced exactly such a file in the project root, which is the cleanest
possible demonstration of the bug.

Also Codex-only and worth keeping: SQLite foreign-key enforcement is never enabled
via `PRAGMA`, and connections are not context-managed, so a raising query leaks one.

## What survives unchanged

The process finding — that the honest floor's July 23 trigger had a date and a
defined cut but no owner, and so never fired — is mine alone and Codex does not
reach it. I still regard it as the most transferable item from the week. Codex's
"no optional `.ROOT` update begins until the day's primary proof is recorded"
constraint is the same defect approached from the other side, and the two
recommendations compose rather than compete: its rule sets the priority, mine
assigns someone to check it.

## Revised recommendation

Unchanged in direction — **Modify** — with the cheap-win list corrected. The ~90
minute item is now **four** fixes, not three: pytest, the `LIKE` wildcard escape,
stderr logging, and the absolute DB path. Add contract-level validation of the
empty keyword so the guarantee holds below the protocol boundary.

And the Day 5 explain-back is no longer optional cleanup. Chris needs to read the
`server.py` diff he did not write and explain it back before that day can close
honestly.
