# Notes, links and references

A **footnote** is numbered text at the foot of the page that cites it, and an
**endnote** is numbered text at the end of the document. A **link** leads to an
external address, and a **reference** displays the title, number or page of a
labelled place in the document.

## Footnotes and endnotes

```mote
The result is provisional#footnote[The sample is small.], and the archive holds the
original records#endnote[Archive catalogue, volume 2.].

A measured result[^method].

[^method]: Three independent samples.
```

The directives `#footnote` and `#endnote` take block content at the point of
citation. The Markdown form `[^name]` cites a footnote defined on its own line as
`[^name]: text`, anywhere in the document. Footnotes and endnotes are numbered
separately.

## Links

```mote
See [the survey site](https://example.com/survey "Survey results"), write to
<reader@example.com>, or visit #link("https://example.com")[#span(bold = true)[the archive]].
```

Markdown links, addresses in angle brackets and bare `https://` addresses all
become links; `#link(url)[text]` takes formatted text. Links are blue and
underlined unless their text is formatted otherwise. A title, as in
`[text](url "Title")`, or the `tooltip` argument of `#link`, becomes the screen
tip shown when a pointer rests on the link in Word, PowerPoint and PDF viewers.

## Labels and references

A **label**, written `#label("name")`, is an invisible name attached to the
block that follows it, or to the figure that contains it. A reference to it is
written `#ref("name")`, and may precede the label.

```mote
The results appear in #ref("results", kind = "number"), on page #ref("results", kind = "page").

#figure(kind = "table", numbering = { enabled = true })[
  #label("results")
  #table[
    #row[#cell[Region] #cell[Revenue]]
    #row[#cell[North] #cell[120]]
  ]
  #caption[Revenue by region]
]

See [the summary](#summary).

#label("summary")
# Summary
```

- The `kind` argument of `#ref` is `title`, the default when a title exists,
  `number`, as in "Table 1", `page`, or `text`.
- The Markdown form `[text](#name)` displays its own text and refers to the label
  `name`.
- A label name is unique within the document.
