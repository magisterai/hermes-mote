# Page setup and sections

The `#document` declaration sets the page size, margins and columns of a
document. A **section** is a part of the document with its own page setup.

## Page size and margins

```mote
#document(
  page = { size = "a4", orientation = "portrait" },
  margin = { top = cm(2.5), bottom = cm(2.5), left = cm(2), right = cm(2), header = cm(1.2), footer = cm(1.2) }
)

The page is A4 with two-centimetre side margins.
```

- The `page.size` value is `letter`, `legal`, `tabloid`, `a3`, `a4` or `a5`, and
  `page.orientation` is `portrait` or `landscape`. The fields `page.width` and
  `page.height` give any other size.
- The `margin` table gives `top`, `bottom`, `left` and `right`, the distances
  `header` and `footer` from the page edges to the running text, and `gutter`, a
  binding margin.
- The default page is Letter, portrait.

## Columns

```mote
#document(columns = { count = 2, gap = pt(18), separator = true })

Text flows down the first column and continues in the second.

#break(type = "column")

The column break moves this paragraph to the second column.
```

The `columns` table gives `count`, the `gap` between columns, and `separator`,
which draws a rule between them. The columns are of equal width.

## Sections

```mote
# Report

Portrait text.

#section(page = { orientation = "landscape" }, columns = { count = 1 })[
  ## Appendix

  A landscape page for a wide table.
]

Portrait text resumes on a new page.
```

- A section takes `page`, `margin` and `columns` tables, which override the
  document's setup, and its own headers and footers, as described in
  [headers and footers](headers-and-footers.md).
- The `properties = { start = "continuous" }` argument begins a section on the
  same page rather than a new one; `next_page`, the default, `odd_page` and
  `even_page` are the other values.
- The `page_numbering = { restart = true, start = 1 }` argument restarts the page
  numbers.

## Breaks

The directive `#break()` begins a new page, and `#break(type = "column")` a new
column. A paragraph or heading with `page_break_before = true` begins a page, and
`keep_with_next = true` keeps a heading on the page of the paragraph after it.

## Limits

- Columns of unequal width are not available.
- In PDF and PNG output, an odd-page or even-page section start and a section's
  `vertical_alignment` produce a warning; the DOCX applies them.
