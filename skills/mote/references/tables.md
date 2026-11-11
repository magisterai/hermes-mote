# Tables

A **table** holds rows, and a **row** holds cells. A **cell** holds block
content: paragraphs, lists, images, and further tables.

## Markdown tables

A Markdown table has a header line, a delimiter line of at least three hyphens
per column, and body lines. A colon on the left, the right or both sides of a
delimiter aligns the column left, right or centre. The header row is bold and
repeats on each page.

```mote
| Region | Revenue | Change |
| :--- | ---: | :---: |
| North | 4.2 | +12% |
| South | 3.1 | +4% |
```

## Table directives

The `#table`, `#row` and `#cell` directives give full control.

```mote
#table(
  width = inch(6.5),
  alignment = "center",
  cell = { margin = { vertical = pt(4), horizontal = pt(8) } },
  borders = { all = { style = "single", width = pt(0.5), color = "#cbd5e1" } }
)[
  #row(repeat_header = true)[
    #cell(fill = "#1e3a8a")[#span(bold = true, color = "#ffffff")[Region]]
    #cell(fill = "#1e3a8a", alignment = "right")[#span(bold = true, color = "#ffffff")[Revenue]]
  ]
  #row[#cell[North] #cell(alignment = "right")[4.2]]
  #row[#cell(colspan = 2, fill = "#f1f5f9")[Totals are in millions of dollars.]]
]
```

- The table accepts `width`, `alignment` (`left`, `center` or `right`), `style`, a
  `cell` table of defaults for every cell, and `borders`.
- The `borders` table gives `top`, `right`, `bottom`, `left`, `inside_h` and
  `inside_v`, or `all`, `outside` and `inside` for groups of edges; each edge has
  `style`, `width` and `color`, and `style = "none"` removes it.
- A row accepts `repeat_header`, which repeats a leading row on each page, and
  `cant_split`, which keeps the row on one page.
- A cell accepts `width`, `colspan`, `rowspan`, `fill`, `alignment`,
  `vertical_alignment` (`top`, `center` or `bottom`), `margin` and `borders`. The
  `margin` table gives `all`, `vertical`, `horizontal`, or individual edges.

## Defaults for every table

The `#set table(...)` directive gives every following table the same width,
cell defaults and borders.

```mote
#set table(
  width = inch(6.5),
  cell = { margin = { vertical = pt(6), horizontal = pt(10) } },
  borders = { all = { style = "none" }, inside_h = { width = pt(0.5), color = "#d5dbe8" } }
)

| Item | Cost |
| --- | ---: |
| Survey | 1,200 |
```

## Limits

- The row arguments `height` and `height_rule`, the table arguments `indent`,
  `cell_spacing` and `layout`, and the cell arguments `text_direction` and
  `no_wrap` affect DOCX only; PDF and PNG output ignores them with a warning.
- In PDF and PNG output, a chart inside a cell is replaced by text, with a
  warning.
