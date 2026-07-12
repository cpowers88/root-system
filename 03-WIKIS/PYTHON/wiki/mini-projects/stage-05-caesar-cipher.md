---
type: mini-project
stage: 05
status: draft
concepts: ["string", "list", "index", "dictionary", "for-loop", "function"]
solution_included: false
---

# Mini-Project: Caesar Cipher

## User Story

As a learner, I want to build a program that encodes and decodes a message using a Caesar cipher (shifting each letter by a fixed amount), so that I can prove I understand strings as sequences, list/string indexing, and using a dictionary to map data.

## Required Concepts

- [[glossary/string]]
- [[glossary/index]]
- [[glossary/list]]
- [[glossary/dictionary]]
- [[glossary/for-loop]]
- [[glossary/function]]

## Build Phases

### Phase 1 — Build the Alphabet Shift

Create a list of the alphabet letters (you can hardcode `"abcdefghijklmnopqrstuvwxyz"` as a string and index into it). Write a function `shift_letter(letter, shift_amount)` that returns the letter shifted forward by `shift_amount` positions, wrapping around from 'z' back to 'a' (use the modulo operator `%` to handle the wraparound).

### Phase 2 — Encode a Full Message

Write a function `encode_message(message, shift_amount)` that loops over every character in `message`, shifts the letters using `shift_letter()`, and leaves non-letter characters (spaces, punctuation) unchanged. Return the encoded string.

### Phase 3 — Decode and Verify

Write a function `decode_message(message, shift_amount)` that reverses the process (shift backward instead of forward). Test that `decode_message(encode_message("hello world", 3), 3)` returns the original message exactly.

## Acceptance Checklist

- [ ] `shift_letter()` correctly wraps around the alphabet (shifting 'z' forward by 1 gives 'a').
- [ ] `encode_message()` leaves spaces and punctuation unchanged, only shifting letters.
- [ ] `decode_message()` correctly reverses `encode_message()` for at least 3 different test messages and shift amounts.
- [ ] Uses at least one function that calls another function (matching Stage 4's pattern).
- [ ] Chris can explain, out loud, how the modulo operator (`%`) makes the wraparound work.

## Stretch Goals — Parked

- Handle both uppercase and lowercase letters correctly (needs slightly more conditional logic — fine to attempt, not required).
- Use a dictionary to precompute the full shifted alphabet mapping once, instead of recalculating per letter (a nice bridge toward Stage 8 efficiency thinking — optional).

## Reflection Questions

1. Why does the wraparound need the modulo operator instead of just subtracting 26 manually?
2. What would happen to your program if you fed it a message with numbers in it, and you hadn't handled non-letter characters specially?
3. Which part of this project relied most on Stage 5 (data shapes) versus Stage 4 (functions)?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
