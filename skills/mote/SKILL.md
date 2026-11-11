---
name: mote
description: The Mote markup language (.mote files), which compiles one source to editable Word (DOCX) and PowerPoint (PPTX) files and to PDF or PNG pages. The skill applies when a .mote file is to be written, edited or corrected, or when a report, letter or slide deck is to be produced with the mote command; it does not apply to editing an existing .docx or .pptx file directly.
---

# Mote

The Mote language is Markdown extended by directives. A single source compiles to
an editable DOCX or PPTX file, or to PDF and PNG pages laid out as Word and
PowerPoint lay them out.

## Syntax

A **directive** has the form `#name(arguments)[body]`. The arguments are named,
written `name = value` and separated by commas; the body, in square brackets,
holds content.

- A string is quoted, as in `"center"`, and a color is a hex string, as in
  `"#2563eb"`.
- A length is written with a unit helper: `pt(12)`, `inch(1)`, `cm(2)` or `mm(5)`.
- Braces enclose both a property object, `{ before = pt(6), after = pt(6) }`, and
  an array, `{ "Q1", "Q2" }`.
- Markdown is valid wherever content is: `#` headings, paragraphs separated by
  blank lines, `**strong**`, `_emphasis_`, `` `code` ``, `- ` and `1. ` lists,
  `> ` quotations and pipe tables. Directives and Markdown may be mixed freely.
- The escapes `\#`, `\*`, `\]` and `\\` produce the literal characters in text.

## A document

```mote
#document(page = { size = "letter" }, margin = { top = inch(1), bottom = inch(1), left = inch(1), right = inch(1) })
#footer[Page #page_number() of #page_number(kind = "total")]

# Quarterly report

Revenue rose by **12%** in the second quarter.

#paragraph(alignment = "center", spacing = { before = pt(12) })[Prepared for the board.]

- Two new markets.
- Retention improved.
```

## Styles and defaults

A **style** is a named set of formatting, declared with `#style "Name"`. The style
`Normal` is the base paragraph style, and `Heading1` to `Heading6` format the
heading levels; `extends` inherits from another style. A quoted name after a
directive applies a style to that element. The `#set` directive gives defaults
to every following element of one kind, including elements written in Markdown.
A document that declares its typography once in this way is shorter, and easier
to change, than one that repeats attributes on each element.

```mote
#style "Normal" (run = { size = pt(11), color = "#1f2633" })
#style "Heading1" extends "Normal" (run = { size = pt(24), bold = true }, paragraph = { spacing = { after = pt(12) } })
#style "Lead" extends "Normal" (run = { size = pt(14), italic = true })
#set paragraph(spacing = { after = pt(8) })

# Observing run

#paragraph "Lead"[One clear signal.]

Ordinary paragraphs take the defaults.
```

## A slide deck

The `#presentation` declaration selects slide output. A `#slide` whose body holds
loose content is laid out automatically, and a leading heading becomes its title.

```mote
#presentation(size = "wide")
#slide[
  # Quarterly review

  - Revenue rose by 12%.
  - Two new markets.
]
```

## Compiling

```sh
mote report.mote --format docx -o report.docx
mote report.mote --format pdf -o report.pdf
mote report.mote --format png -o report      # report-1.png, report-2.png, ...
mote deck.mote --format pptx -o deck.pptx
mote report.mote                             # the evaluated model as JSON
```

An error stops compilation and names the file, line and column. A warning is
printed to standard error while the output is still written; each warning names
an element or attribute that did not render as written, and should be resolved.
The `--lua` option enables Lua expressions, which are disabled by default.

## Common mistakes

- A directive takes named arguments, and a positional value is usually an error.
- A length without a unit is ambiguous: a bare page or margin number means
  twips, and a bare drawing size means EMUs.
- A shape is placed at page or slide coordinates, and body text does not wrap
  around it.
- A slide holds either positioned boxes and shapes or loose content, never both.
- An unknown attribute is retained without effect. The only sign is a warning, so
  the warnings deserve attention after any change of attributes.

## Reference

Each page is short and self-contained. A task that touches several features
requires each of the corresponding pages.

- [Text and paragraphs](references/text.md): headings, paragraph spacing,
  indents, borders, inline formatting, line breaks, tabs and page breaks.
- [Styles and fonts](references/styles-and-fonts.md): paragraph and character
  styles, inheritance, font declarations and font files.
- [Page setup and sections](references/page-setup.md): page size, orientation,
  margins, columns, sections and breaks.
- [Headers and footers](references/headers-and-footers.md): running text, page
  numbers, and sections that change them.
- [Lists](references/lists.md): bulleted, numbered, nested and task lists.
- [Tables](references/tables.md): Markdown and directive tables, merged cells,
  borders, fills, repeated headers and table defaults.
- [Images and figures](references/images.md): images, their size and
  transforms, figures with numbered captions.
- [Notes, links and references](references/notes-and-references.md): footnotes,
  endnotes, hyperlinks, labels and cross-references to titles, numbers and pages.
- [Charts](references/charts.md): column, bar, line, area, pie and doughnut charts,
  with their data, colors, legends, labels and axes.
- [Shapes](references/shapes.md): positioned rectangles, ellipses and other
  geometry with fills, borders and text, and lines and arrows on slides.
- [Slides](references/slides.md): deck settings, themes, speaker notes,
  positioned boxes, built-in and custom slide layouts.
- [Data, conditions and loops](references/data.md): bindings, JSON and CSV files,
  imports, conditions, loops, and number, money and date formatting.
- [Lua](references/lua.md): arithmetic, comparisons, string formatting and
  functions, with the `--lua` option.
