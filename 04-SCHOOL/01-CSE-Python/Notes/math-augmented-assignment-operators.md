---
type: note
timeline: reference
tags: [python, school]
created: 2026-07-19
---

# Math — Augmented Assignment Operators

- -= → x -= 2 is x = x - 2
- *= → x *= 3 is x = x * 3
- /= → x /= 2 is x = x / 2 (always gives a float)
- //= → x //= 2 is x = x // 2 (floor division)
- %= → x %= 3 is x = x % 3 (remainder)
- **= → x **= 2 is x = x ** 2 (exponent)

Common uses you'll hit constantly in loops: += for running totals/counters, -= for countdowns, *= for compounding (interest, doubling), %= less common but shows up in cyclic logic (like wrapping an index around an array).

## '%=' uses

%= reassigns a variable to its remainder after division. Fewer everyday use cases than +=, but it comes up in a handful of specific patterns.
Wrapping an index around a fixed range — useful for cycling through a list or array without going out of bounds:
pythonindex = 7
index %= 5   # index = 2, wraps back into range 0-4
Cyclic counters, like a clock or a rotating turn order:
pythonhour = 14
hour %= 12   # hour = 2
Stripping a number down to just its "leftover" part, e.g. checking or reducing something to a remainder repeatedly (rare, but shows up in some math/algorithm problems, like digit extraction loops):
pythonn = 1234
digit = n % 10   # 4
You'll use %= far less than += or -= in everyday loops — it's mostly reserved for cyclic/wraparound logic rather than accumulation.