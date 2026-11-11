# Styles and fonts

A **paragraph style** formats whole paragraphs and headings, and a **character
style** formats a run of text within a paragraph. A **font declaration** gives a
name to a typeface, and may supply the font files used to lay out PDF and PNG
output. Styles become named Word styles in DOCX, so the recipient can restyle the
document in Word.

## Paragraph styles

```mote
#style "Normal" (run = { font = "Helvetica", size = pt(11), color = "#1f2633" }, paragraph = { spacing = { after = pt(6), line = { rule = "multiple", value = 1.15 } } })
#style "Heading2" extends "Normal" (run = { size = pt(15), bold = true, color = "#14213d" }, paragraph = { spacing = { before = pt(18), after = pt(6) }, keep_with_next = true })
#style "Note" extends "Normal" (run = { size = pt(9), italic = true }, paragraph = { indent = { left = pt(18) } })

## Method

#paragraph "Note"[Measurements were taken at dawn.]
```

- The `run` table accepts the character formatting of `#span`: `font`, `size`,
  `color`, `highlight`, `bold`, `italic`, `underline`, `small_caps`, `strike` and
  `double_strike`.
- The `paragraph` table accepts the paragraph formatting of `#paragraph`:
  `alignment`, `spacing` (including `line`), `indent`, `border`, `fill`, `tabs`,
  `keep_with_next`, `keep_together`, `page_break_before` and `widow_control`.
- The style `Normal` underlies every paragraph, `Heading1` to `Heading6` format
  the heading levels, and `Caption` formats captions. A declaration of one of
  these names sets its formatting.
- A style that `extends` another inherits its formatting and overrides the fields
  it gives. The name, the word `extends` and the parent stand on one line.

## Character styles

```mote
#style "Brand" (type = "character", run = { bold = true, color = "#14213d" })

The survey is run by #span "Brand"[Meridian].
```

A quoted style name follows `#paragraph`, `#heading`, `#span`, `#strong`,
`#emphasis`, `#code`, `#list`, `#ordered_list`, `#blockquote` and the other
inline directives, directly and on the same line.

## Fonts

The document font and size are set by `#document(default_font = "Helvetica",
default_size = pt(11))`, or by the style `Normal`. A font declaration names a
typeface and, optionally, the files that PDF and PNG output use to measure and
draw it.

```mote
#font(name = "Body", latin = "Source Serif 4", files = { regular = "fonts/SourceSerif4-Regular.ttf" })
#style "Normal" (run = { font = "Body", size = pt(11) })

Text set in Source Serif 4.
```

- The `latin`, `east_asian` and `complex_script` arguments give the typeface for
  each script; `name` is the alias by which styles and spans refer to it.
- The `files` table gives `regular`, `bold`, `italic` and `bold_italic` paths,
  relative to the source. A face without a file is substituted, with a warning.
- The DOCX names the typeface and does not embed it, so the recipient's Word
  displays it only if the font is installed.

## Limits

- Without declared files, PDF and PNG output use the installed fonts that Mote
  can resolve, which at present excludes some installed system fonts such as
  Georgia; a substituted font is reported with a warning. Declared files avoid
  the substitution.
