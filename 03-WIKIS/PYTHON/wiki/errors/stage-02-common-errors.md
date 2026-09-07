---
type: error-log
stage: 02
status: draft
tags: [errors, debugging-preview]
timeline: reference
---

# Stage 2 Common Errors

## 1. Missing colon after `if`/`elif`/`else`

```python
if age >= 18
    print("Adult")
```

```text
SyntaxError: expected ':'
```

**Why it happens:** Python requires a colon at the end of the `if`/`elif`/`else` line, right before the indented block begins.

**Fix:** add `:` at the end of the condition line.

## 2. `IndentationError`

```python
if age >= 18:
print("Adult")
```

```text
IndentationError: expected an indented block after 'if' statement
```

**Why it happens:** the body of an `if` must be indented (4 spaces is the Python convention) — Python uses indentation, not braces, to know what's inside a branch.

**Fix:** indent every line that belongs inside the `if`/`elif`/`else` block consistently.

## 3. Using `=` instead of `==` in a condition

```python
if age = 18:
    print("Exactly 18")
```

```text
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

**Why it happens:** `=` is assignment, not comparison — Python actually catches this one for you with a helpful hint, but it's worth recognizing on sight.

**Fix:** use `==` to compare.

## 4. Logic mistake: separate `if` statements instead of `elif`

```python
score = 95
if score >= 90:
    print("A")
if score >= 80:
    print("B")
```

This doesn't raise an error, but it prints **both** "A" and "B" — not what was probably intended.

**Why it happens:** each `if` is checked independently. Without `elif`, Python has no idea the second check should only happen if the first one failed.

**Fix:** use `elif` when only one branch should ever run: `if score >= 90: ... elif score >= 80: ...`.

## How to Read Any of These

1. Read the **last line first** — it names the error type and the specific problem.
2. For logic mistakes (no error message, just wrong output) — print intermediate values, or trace through the conditions by hand with the actual input you used.
3. Ask: "Is this an error Python caught, or a mistake in what I told it to do?" Both matter, but they're debugged differently.

## Related

- [[concepts/if-elif-else]]
- [[concepts/comparisons-and-boolean-logic]]
