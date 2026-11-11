# Text and paragraphs

A **block** is a unit of content laid out on its own lines, such as a paragraph
or a heading. **Inline content** is the text within a block, with any formatting
applied to part of it.

## Paragraphs and headings

Ordinary text forms paragraphs, and a blank line separates them; a single line
ending within a paragraph supplies a space. A heading is written in Markdown as
`#` to `######` followed by a space, or as `#heading(level = 2)[Title]`. The
`#paragraph` and `#heading` directives accept the same formatting arguments.

```mote
#heading(level = 1, alignment = "center")[Annual report]

#paragraph(
  alignment = "justify",
  spacing = { before = pt(6), after = pt(12), line = { rule = "multiple", value = 1.15 } },
  indent = { left = pt(18), first_line = pt(12) }
)[The year closed with revenue above forecast in every region.]
```

- The `alignment` argument is `left`, `center`, `right` or `justify`.
- The `spacing` table gives `before` and `after`, the space outside the block,
  and `line`, which is a length for an exact line height or a table whose
  `rule` is `multiple`, `exact` or `at_least` and whose `value` is a number or a
  length accordingly.
- The `indent` table gives `left`, `right`, `first_line` and `hanging` lengths.
- The `fill` argument shades the paragraph, and `border` draws rules: a table of
  `top`, `right`, `bottom`, `left` or `all`, each with `style`, `width` and `color`.
- The booleans `keep_with_next`, `keep_together`, `page_break_before` and
  `widow_control` govern pagination.

## Inline formatting

The Markdown forms are `**strong**` (or `*strong*`), `_emphasis_`, `~~struck~~`
and `` `code` ``. A `#span` applies any combination of character formatting.

```mote
Revenue reached #span(bold = true, color = "#15803d")[$4.2 million], or
#span(size = pt(14), font = "Courier")[12% above] the plan. Water is
H#subscript[2]O, the area is 3 m#superscript[2], and #underline(style = "double")[this]
is underlined, #highlight(fill = "#fef08a")[this] highlighted, and
#small_caps[this] in small capitals.
```

- The `#span` arguments are `font`, `size`, `color`, `highlight`, `bold`,
  `italic`, `underline`, `small_caps`, `strike` and `double_strike`. An explicit
  `false` disables formatting inherited from an enclosing span or style.
- The directives `#strong`, `#emphasis`, `#underline`, `#strike`, `#highlight`,
  `#superscript`, `#subscript`, `#small_caps` and `#code` each take one inline
  body.
- A quoted name applies a character style: `#span "Brand"[Meridian]`.

## Breaks and tabs

The field `#line_break()` begins a new line within the same paragraph, and
`#tab()` advances to the next tab stop. The `tabs` argument of a paragraph sets
the stops, each with a `position`, an `alignment` of `left`, `center`, `right` or
`decimal`, and an optional `leader` such as `dot`.

```mote
#paragraph(tabs = { { position = inch(6.5), alignment = "right", leader = "dot" } })[Introduction#tab()1]
#paragraph[First line#line_break()Second line]
```

The directive `#break()` begins a new page, and `#break(type = "column")` a new
column.

## Limits

- A single asterisk pair produces strong text, not emphasis; emphasis requires
  underscores.
- A font that is not installed is substituted in PDF and PNG output; DOCX
  retains the name, and Word substitutes it in turn.
