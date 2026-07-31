---
type: reference
timeline: reference
title: "Markdown Cheat Sheet 2026 — All 30+ Syntax & Examples"
source: "https://toolsbase.dev/en/reference/markdown-cheatsheet"
author:
  - "[[Toolsbase]]"
published: 2026-03-16
created: 2026-07-22
description: "All 30+ Markdown syntax patterns: headings, bold, lists, links, tables, code blocks, task lists. With live examples. One-click copy. Free."
tags: [programming]
---
## Markdown Cheat Sheet

Searchable Markdown syntax reference organized by category. Covers headings, emphasis, lists, links, code blocks, tables, and advanced syntax with one-click copy.

## How to Use

1. 1
	### Search for syntax
	Enter a keyword in the search field, or filter by category (Heading, Emphasis, etc.) to find the syntax you need.
2. 2
	### Review description and example
	Check the syntax description, example code, and how it renders to understand the correct usage.
3. 3
	### Copy the syntax
	Click the copy button to copy the syntax to your clipboard and paste it directly into your Markdown document.

## \# Heading 1Largest heading (H1). Use for page or document titles.

#### Example

```
# My Document Title
```

#### Rendered

My Document Title (large bold text)

## \## Heading 2Second-level heading (H2). Use for major sections.

#### Example

```
## Section Title
```

#### Rendered

Section Title (medium bold text)

## \### Heading 3Third-level heading (H3). Use for subsections.

#### Example

```
### Subsection Title
```

#### Rendered

Subsection Title (smaller bold text)

## \#### Heading 4Fourth-level heading (H4). Use for minor headings.

#### Example

```
#### Minor Heading
```

#### Rendered

Minor Heading (small bold text)

## \*\*bold\*\*Bold text. Wrap text with double asterisks or double underscores.

#### Example

```
This is **bold** text
```

#### Rendered

This is bold text (bold)

## \*italic\*Italic text. Wrap text with a single asterisk or underscore.

#### Example

```
This is *italic* text
```

#### Rendered

This is italic text (italic)

## \*\*\*bold italic\*\*\*Bold and italic combined. Wrap text with triple asterisks.

#### Example

```
This is ***bold italic*** text
```

#### Rendered

This is bold italic text (bold + italic)

## ~~strikethrough~~Strikethrough text. Wrap text with double tildes.

#### Example

```
This is ~~strikethrough~~ text
```

#### Rendered

This is ~~strikethrough~~ text (with line through)

## \`inline code\`Inline code. Wrap text with backticks for monospace code display.

#### Example

```
Use \`console.log()\` to debug
```

#### Rendered

Use console.log() to debug (monospace)

## \- itemBullet list. Start lines with -, \*, or + followed by a space.

#### Example

```
- Apple
- Banana
- Cherry
```

#### Rendered

• Apple • Banana • Cherry

## 1\. itemNumbered list. Start lines with numbers followed by a period and space.

#### Example

```
1. First
2. Second
3. Third
```

#### Rendered

1\. First 2. Second 3. Third

## \- item - nested itemNested list. Indent items with 2 or 4 spaces to create sub-items.

#### Example

```
- Item
  - Sub-item
  - Sub-item
```

#### Rendered

• Item ∘ Sub-item ∘ Sub-item

## \- \[ \] unchecked - \[x\] checkedTask list (GitHub Flavored Markdown). Use \[ \] for unchecked and \[x\] for checked items.

#### Example

```
- [ ] Todo
- [x] Done
```

#### Rendered

☐ Todo ☑ Done

## \[link text\](https://example.com)Hyperlink. Use \[link text\](URL) format.

#### Example

```
[Visit GitHub](https://github.com)
```

#### Rendered

Visit GitHub (clickable link)

## \[link text\](https://example.com "title")Link with a tooltip title. Add a quoted title after the URL.

#### Example

```
[GitHub](https://github.com "GitHub Home")
```

#### Rendered

GitHub (link with tooltip on hover)

## !\[alt text\](image.png)Inline image. Similar to a link but prefixed with!

#### Example

```
![Logo](logo.png)
```

#### Rendered

\[Image: Logo\]

## \[link text\]\[ref\] \[ref\]: https://example.comReference-style link. Define the URL separately to keep text clean.

#### Example

```
[GitHub][gh]

[gh]: https://github.com
```

#### Rendered

GitHub (clickable link using reference)

## <https://example.com>Automatic link. Wrap a URL or email in angle brackets.

#### Example

```
<https://example.com>
```

#### Rendered

https://example.com (clickable)

## \`\`\` code here \`\`\`Fenced code block. Wrap code with triple backticks.

#### Example

```
\`\`\`
function hello() {
  return 'hi';
}
\`\`\`
```

#### Rendered

Code block with monospace font

## \`\`\`javascript const x = 1; \`\`\`Syntax-highlighted code block. Add the language name after opening backticks.

#### Example

```
\`\`\`javascript
const x = 42;
\`\`\`
```

#### Rendered

Code block with JavaScript syntax highlighting

## \> blockquote textBlockquote. Start a line with > to indent it as a quote.

#### Example

```
> To be, or not to be.
```

#### Rendered

| To be, or not to be. (indented)

## \> quote >> nested quoteNested blockquote. Use >> for a second level of indentation.

#### Example

```
> Outer quote
>> Inner quote
```

#### Rendered

| Outer quote || Inner quote (double indented)

## \---Horizontal rule. Use three or more dashes, asterisks, or underscores on a line.

#### Example

```
---
```

#### Rendered

─────────────── (full-width horizontal line)

#### Example

```
| Name | Age |
| ---- | --- |
| Alice | 30 |
```

#### Rendered

Table with Name and Age columns

## | Left | Center | Right | |:--- |:----: | ----: | | L | C | R |Table column alignment. Use:--- for left,:---: for center, and ---: for right alignment.

#### Example

```
| Left | Center | Right |
| :--- | :----: | ----: |
| L    |   C    |     R |
```

#### Rendered

Table with left, center, and right aligned columns

## text\[^1\] \[^1\]: footnote contentFootnote (extended Markdown). Add \[^ref\] in text and define the note at the bottom.

#### Example

```
See note[^1]

[^1]: This is the footnote.
```

#### Rendered

See note¹... ¹ This is the footnote.

## Term: DefinitionDefinition list (extended Markdown). Write the term on one line and its definition preceded by a colon on the next.

#### Example

```
HTML
: HyperText Markup Language
```

#### Rendered

HTML (term) HyperText Markup Language (definition)

## \\\*escaped asterisk\\\*Escape special characters. Use a backslash \\ to display Markdown characters literally.

#### Example

```
\*not italic\*
```

#### Rendered

\*not italic\* (asterisks displayed as-is)

## <!-- HTML comment -->HTML comment. Will not appear in the rendered output.

#### Example

```
<!-- This comment is hidden -->
```

#### Rendered

(nothing visible)

## H~2~OSubscript text (extended Markdown). Wrap text with single tildes.

#### Example

```
H~2~O
```

#### Rendered

H₂O

## x^2^Superscript text (extended Markdown). Wrap text with carets.

#### Example

```
x^2^
```

#### Rendered

x²

## \==highlighted==Highlighted text (extended Markdown). Wrap text with double equal signs.

#### Example

```
==important text==
```

#### Rendered

important text (with yellow highlight)

## About Markdown Cheat Sheet

Markdown Cheat Sheet is a quick reference for Markdown syntax. It covers everything from basic formatting like headings and emphasis to advanced features like tables, footnotes, and extended syntax. Each pattern includes a description, example code, and rendered output so you can understand the result at a glance.

### Key Features

- 30+ Markdown syntax patterns organized by category
- Description, example, and rendered output for each pattern
- Category filtering (Headings, Emphasis, Lists, etc.)
- Real-time search functionality
- One-click copy of syntax examples

### Use Cases

- Quick reference while writing a GitHub README or Pull Request description
- Looking up table and code block syntax when writing technical documentation
- Learning Markdown as a beginner contributing to an open-source project
- Checking the correct syntax for callouts, footnotes, or task lists in GitHub Flavored Markdown
- Reference while writing content in Notion, Confluence, Obsidian, or a static site generator
- Formatting a Slack message or Discord post that supports Markdown

## FAQ

What is Markdown?

Markdown is a lightweight markup language that uses plain text formatting to convert to HTML. It was created by John Gruber in 2004 and is now widely used in README files, documentation, blogging platforms, and note-taking apps.

What is the difference between standard Markdown and extended Markdown?

Standard Markdown (CommonMark) includes basic syntax like headings, bold, italic, links, and code blocks. Extended Markdown (GitHub Flavored Markdown, MultiMarkdown, etc.) adds tables, task lists, footnotes, strikethrough, and more. Support varies by platform.

What is the difference between \* and \_ for emphasis?

Both work the same for bold and italic, but there is a difference with underscores: underscores inside words (like some\_variable\_name) are not treated as emphasis markers. Asterisks are recommended for consistency.

How do I add a line break?

End a line with two or more spaces, or add a blank line between paragraphs to create a new paragraph. Some processors also support a backslash \\ at the end of a line.

Do all Markdown parsers support the same syntax?

No. Core syntax like headings, bold, and links is widely supported, but extended syntax like tables, footnotes, and definition lists depends on the parser. Always check what your target platform supports.