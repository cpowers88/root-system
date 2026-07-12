---
type: error-log
stage: 03
status: draft
tags: [stage-03, errors, debugging-preview]
---

# Stage 3 Common Errors

## 1. Program "freezes" — infinite loop

```python
count = 0
while count < 5:
    print("stuck")
```

**No error message at all** — the program just keeps running forever (in a terminal, `Ctrl+C` stops it).

**Why it happens:** `count` never changes inside the loop, so `count < 5` is always `True`.

**Fix:** make sure something inside the loop body updates whatever the condition checks (`count += 1`).

## 2. Off-by-one with `range()`

```python
for i in range(5):
    print(i)
# prints 0,1,2,3,4 — if you expected 1-5, this is the bug
```

**No error message** — just unexpected output.

**Why it happens:** `range(5)` produces 5 numbers starting at 0, stopping *before* 5.

**Fix:** use `range(1, 6)` if you want 1 through 5.

## 3. `TypeError` from looping over a non-iterable

```python
for x in 5:
    print(x)
```

```text
TypeError: 'int' object is not iterable
```

**Why it happens:** a plain number isn't a sequence of items to step through — only things like strings, `range()`, and (later) lists can be looped over directly.

**Fix:** loop over `range(5)` if you meant "5 times," not the number `5` itself.

## 4. Counter/accumulator reset every pass

```python
for n in [1, 2, 3]:
    total = 0           # BUG: this resets total every single pass
    total += n
print(total)   # only ever shows the last number, not the sum
```

**No error message** — wrong output.

**Why it happens:** `total = 0` is inside the loop, so it wipes out the running total on every pass instead of building on it.

**Fix:** move the initialization (`total = 0`) above the loop, so it only happens once.

## How to Read Any of These

1. If there's no error message but the output looks wrong, suspect a logic bug like off-by-one or a misplaced initialization — print the variable's value each pass to see what's actually happening.
2. If the program hangs and never finishes, suspect an infinite loop — check what the `while` condition depends on and whether it's actually being updated.

## Related

- [[concepts/for-loops]]
- [[concepts/while-loops]]
- [[concepts/counters-and-accumulators]]
