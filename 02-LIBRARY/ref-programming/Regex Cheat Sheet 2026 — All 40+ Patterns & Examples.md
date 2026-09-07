---
type: reference
timeline: reference
title: "Regex Cheat Sheet 2026 — All 40+ Patterns & Examples"
source: "https://toolsbase.dev/en/reference/regex-cheatsheet"
author:
  - "[[Toolsbase]]"
published: 2026-03-16
created: 2026-07-22
description: "All 40+ regex patterns: anchors, quantifiers, character classes, groups, lookaheads, flags. With test examples. One-click copy. Free."
tags: [programming]
---
## Regex Cheat Sheet

Searchable regular expression cheat sheet organized by category. Covers anchors, quantifiers, character classes, groups, flags, and common patterns with one-click copy.

## How to Use

1. 1
	### Search or filter by category
	Enter a pattern or keyword in the search field, or click a category button (Anchors, Quantifiers, etc.) to narrow down the list.
2. 2
	### Review description and examples
	Check each pattern's description, usage example, and expected output to understand how it works.
3. 3
	### Copy the pattern
	Click the copy button on any card to copy the pattern to your clipboard for immediate use in your code or terminal.

## ^Match at the start of a string (or line with m flag)

#### Example

```
/^Hello/.test('Hello World')
```

#### Output

```
true
```

## $Match at the end of a string (or line with m flag)

#### Example

```
/World$/.test('Hello World')
```

#### Output

```
true
```

## \\bMatch a word boundary (between word and non-word character)

#### Example

```
'cat catalog'.match(/\bcat\b/g)
```

#### Output

```
['cat']
```

## \\BMatch a non-word boundary

#### Example

```
'catalog'.match(/\Bcat\B/g)
```

#### Output

```
null
```

## \*Match 0 or more occurrences of the preceding element

#### Example

```
'color colour'.match(/colou*r/g)
```

#### Output

```
['color', 'colour']
```

## +Match 1 or more occurrences of the preceding element

#### Example

```
'ac abc'.match(/ab+c/g)
```

#### Output

```
['abc']
```

## ?Match 0 or 1 occurrence of the preceding element (optional)

#### Example

```
'color colour'.match(/colou?r/g)
```

#### Output

```
['color', 'colour']
```

## {n}Match exactly n occurrences of the preceding element

#### Example

```
'aaa aa a'.match(/a{2}/g)
```

#### Output

```
['aa', 'aa']
```

## {n,}Match n or more occurrences of the preceding element

#### Example

```
'aaa aa a'.match(/a{2,}/g)
```

#### Output

```
['aaa', 'aa']
```

## {n,m}Match between n and m occurrences of the preceding element

#### Example

```
'aaaa aaa aa a'.match(/a{2,3}/g)
```

#### Output

```
['aaa', 'aaa', 'aa']
```

## \\dMatch any digit character (equivalent to \[0-9\])

#### Example

```
'abc 123'.match(/\d+/g)
```

#### Output

```
['123']
```

## \\DMatch any non-digit character (equivalent to \[^0-9\])

#### Example

```
'abc 123'.match(/\D+/g)
```

#### Output

```
['abc ']
```

## \\wMatch any word character (equivalent to \[A-Za-z0-9\_\])

#### Example

```
'hello world_2'.match(/\w+/g)
```

#### Output

```
['hello', 'world_2']
```

## \\WMatch any non-word character (equivalent to \[^A-Za-z0-9\_\])

#### Example

```
'hello world'.match(/\W+/g)
```

#### Output

```
[' ']
```

## \\sMatch any whitespace character (space, tab, newline, etc.)

#### Example

```
'hello world'.match(/\s+/g)
```

#### Output

```
[' ']
```

## \\SMatch any non-whitespace character

#### Example

```
'hello world'.match(/\S+/g)
```

#### Output

```
['hello', 'world']
```

## \[abc\]Match any one character listed in the brackets

#### Example

```
'cat bat hat'.match(/[cbh]at/g)
```

#### Output

```
['cat', 'bat', 'hat']
```

## \[a-z\]Match any character in the specified range

#### Example

```
'Hello World'.match(/[a-z]+/g)
```

#### Output

```
['ello', 'orld']
```

## \[^abc\]Match any character not listed in the brackets

#### Example

```
'cat 123'.match(/[^\d ]+/g)
```

#### Output

```
['cat']
```

## (...)Capture a group and allow backreference with $1, $2, etc.

#### Example

```
'2024-03-15'.replace(/(\d{4})-(\d{2})-(\d{2})/, '$2/$3/$1')
```

#### Output

```
'03/15/2024'
```

## (?:...)Group without capturing (more efficient than capturing group)

#### Example

```
'foobar foobaz'.match(/foo(?:bar|baz)/g)
```

#### Output

```
['foobar', 'foobaz']
```

## (?=...)Match only if followed by the specified pattern (not consumed)

#### Example

```
'100px 200em'.match(/\d+(?=px)/g)
```

#### Output

```
['100']
```

## (?!...)Match only if NOT followed by the specified pattern

#### Example

```
'100px 200em'.match(/\d+(?!px)/g)
```

#### Output

```
['10', '200']
```

## (?<=...)Match only if preceded by the specified pattern (not consumed)

#### Example

```
'$100 €200'.match(/(?<=\$)\d+/g)
```

#### Output

```
['100']
```

## (?<!...)Match only if NOT preceded by the specified pattern

#### Example

```
'$100 200'.match(/(?<!\$)\d+/g)
```

#### Output

```
['200']
```

## gGlobal: find all matches instead of stopping at the first

#### Example

```
'aaa'.match(/a/g)
```

#### Output

```
['a', 'a', 'a']
```

## iCase-insensitive: match regardless of upper/lower case

#### Example

```
'Hello HELLO'.match(/hello/gi)
```

#### Output

```
['Hello', 'HELLO']
```

## mMultiline: ^ and $ match start/end of each line

#### Example

```
'line1\nline2'.match(/^line/gm)
```

#### Output

```
['line', 'line']
```

## sDotall:. matches newline characters as well

#### Example

```
'foo\nbar'.match(/foo.bar/s)
```

#### Output

```
['foo\nbar']
```

## uUnicode: enables full Unicode support including surrogate pairs

#### Example

```
'\u{1F600}'.match(/./u)[0].length
```

#### Output

```
2
```

## .Match any single character except newline (use s flag for newline too)

#### Example

```
'cat bat'.match(/.at/g)
```

#### Output

```
['cat', 'bat']
```

## a|bMatch either the left or right expression

#### Example

```
'cat dog bird'.match(/cat|dog/g)
```

#### Output

```
['cat', 'dog']
```

## \\.Escape a special character to match it literally

#### Example

```
'3.14'.match(/3\.14/)
```

#### Output

```
['3.14']
```

## (?\<name>...)Capture a named group, accessible via match.groups.name

#### Example

```
'2024-03-15'.match(/(?<y>\d{4})-(?<m>\d{2})-(?<d>\d{2})/).groups
```

#### Output

```
{y: '2024', m: '03', d: '15'}
```

## \[\\w.+\\-\]+@\[\\w\\-\]+\\.\[a-z\]{2,}Match a basic email address (simplified pattern)

#### Example

```
/.+@.+/.test('user@example.com')
```

#### Output

```
true
```

## https?:\\/\\/\[\\w\\-.\_~:/?#\\\[\\\]@!$&'()\*+,;=%\]+Match an HTTP or HTTPS URL

#### Example

```
/https?:\/\/.+/.test('https://example.com')
```

#### Output

```
true
```

## 0\\d{1,4}-\\d{1,4}-\\d{4}Match a Japanese phone number format (e.g. 03-1234-5678)

#### Example

```
/0\d{1,4}-\d{1,4}-\d{4}/.test('03-1234-5678')
```

#### Output

```
true
```

## (?:25\[0-5\]|2\[0-4\]\\d|\[01\]?\\d\\d?)\\.(?:25\[0-5\]|2\[0-4\]\\d|\[01\]?\\d\\d?)\\.(?:25\[0-5\]|2\[0-4\]\\d|\[01\]?\\d\\d?)\\.(?:25\[0-5\]|2\[0-4\]\\d|\[01\]?\\d\\d?)Match a valid IPv4 address (0.0.0.0 – 255.255.255.255)

#### Example

```
/valid IPv4 pattern/.test('192.168.1.1')
```

#### Output

```
true
```

## \\d{4}\[-/\](?:0\[1-9\]|1\[0-2\])\[-/\](?:0\[1-9\]|\[12\]\\d|3\[01\])Match a date in YYYY-MM-DD or YYYY/MM/DD format

#### Example

```
/\d{4}[-\/]\d{2}[-\/]\d{2}/.test('2024-03-15')
```

#### Output

```
true
```

## #(?:\[0-9a-fA-F\]{3}|\[0-9a-fA-F\]{6})\\bMatch a CSS hex color code (#RGB or #RRGGBB)

#### Example

```
'color: #fff and #1a2b3c'.match(/#[0-9a-fA-F]{3,6}/g)
```

#### Output

```
['#fff', '#1a2b3c']
```

## \\d{3}-\\d{4}Match a Japanese postal code (e.g. 123-4567)

#### Example

```
/\d{3}-\d{4}/.test('123-4567')
```

#### Output

```
true
```

## About Regex Cheat Sheet

Regex Cheat Sheet is a quick reference for regular expression syntax. It covers all major constructs including anchors, quantifiers, character classes, capturing groups, lookahead/lookbehind assertions, and flags. Common real-world patterns for email, URL, IP address, and date formats are also included. Each entry provides a practical example with expected output.

### Key Features

- 40+ essential regex patterns across 7 categories
- Practical example and expected output for each pattern
- Category filtering (anchors, quantifiers, char classes, etc.)
- Real-time search by pattern or description
- One-click copy of any pattern

### Use Cases

- Quick syntax reference while writing a regex in JavaScript, Python, or Go
- Copying ready-made patterns for email, URL, phone number, or date validation
- Learning regex fundamentals — anchors, quantifiers, character classes, and groups
- Refreshing knowledge of lookahead, lookbehind, and non-capturing groups
- Referencing flags (global, multiline, case-insensitive) when debugging regex behavior
- Using as a cheat sheet during code review or pair programming sessions

## FAQ

What is the difference between \* and +?

\* matches 0 or more occurrences, while + requires at least 1. For example, /ab\*c/ matches 'ac', 'abc', 'abbc', but /ab+c/ only matches 'abc', 'abbc' — not 'ac'.

What is the difference between a capturing group (...) and a non-capturing group (?:...)?

A capturing group stores the matched text and makes it available as $1, $2, etc. in replacements or match.groups. A non-capturing group only groups for precedence and quantifiers without storing the match, which is more efficient.

What is the difference between lookahead (?=...) and lookbehind (?<=...)?

Lookahead (?=...) asserts that the pattern must follow the current position. Lookbehind (?<=...) asserts that the pattern must precede the current position. Neither consumes characters, so they are called zero-width assertions.

What does the g flag do?

The g (global) flag makes the regex engine find all matches in the string instead of stopping after the first. Without g, methods like String.match() return only the first match.

How do I match a literal dot or other special character?

Escape it with a backslash. For example, use \\. to match a literal dot, \\( to match a literal parenthesis, and \\\* to match a literal asterisk. Without the backslash,. matches any character.