# Headers and footers

A **header** and a **footer** are running text repeated on every page of a
document. A slide deck instead uses the `footer`, `date` and `slide_number`
arguments of `#presentation`.

## Declaration

The `#header` and `#footer` directives precede the body. Each takes one body of
block content, which may hold several paragraphs and their formatting.

```mote
#header[#paragraph(alignment = "right")[Quarterly report · Confidential]]
#footer[#paragraph(alignment = "center")[Page #page_number() of #page_number(kind = "total")]]

# Results

The body starts here.
```

The field `#page_number()` displays the current page, and
`#page_number(kind = "total")` the number of pages. A field is evaluated at
layout, so the numbers remain correct when the text reflows.

## Spacing

- The `distance` argument is the distance from the page edge to the header or
  footer, and `height` is the space reserved for it.
- The document margins `margin.header` and `margin.footer` set these distances
  for the whole document and take precedence over `distance`.

The interval between `margin.header` and `margin.top` holds the header, and the
interval between `margin.footer` and `margin.bottom` holds the footer.

```mote
#document(margin = { top = inch(1.25), header = inch(0.5) })
#header(height = pt(24))[#paragraph(spacing = { after = pt(0) })[Board pack]]

Body text.
```

## Changes within a document

A **section** is a part of the document with its own page setup, written
`#section(...)[content]`. A header or footer declared inside a section replaces
the inherited one, and an empty body clears it. The `page_numbering` argument
restarts the page count.

```mote
#footer[Page #page_number()]

# Report

Main text.

#section(page = { orientation = "landscape" }, page_numbering = { restart = true, start = 1 })[
  #header[Appendix A]
  #footer[]

  Wide tables go here.
]
```

A different header or footer declared at the top level after body content also
begins a new section. An explicit `#section` is preferable, since it shows where
the break falls.

## Limits

- A document has no separate first-page, odd-page or even-page headers.
- The PDF and PNG output displays page numbers in decimal; a `format` string takes
  effect only in DOCX.
- A table or image in a header becomes plain text in PDF and PNG output, and a
  chart is omitted. Headers and footers are therefore best kept to text.
- Text that exceeds the reserved space is cut, with a warning.
