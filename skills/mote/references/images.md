# Images and figures

An **image** is a block holding a PNG, JPEG or GIF file. A **figure** groups a
block, such as an image, table or chart, with a **caption**, the text that
describes it.

## Images

The Markdown form is `![Alternative text](photo.png "Title")`, and the directive
form `#image("photo.png", ...)`. A path is resolved relative to the source file;
a network address is not fetched.

```mote
#image("photo.png", width = inch(3), alignment = "center", alt = "Survey site at dawn", spacing = { before = pt(6), after = pt(6) })
```

- Without `width` or `height`, an image takes its pixel size at 96 pixels per
  inch. With one of them, the other follows the image's proportions; with both,
  the image is stretched to that frame. An image wider than the text column is
  reduced to fit.
- The `alignment` argument is `left`, `center` or `right`.
- The `alt` argument is the alternative text read by assistive software.
- The `crop` table gives `left`, `top`, `right` and `bottom` percentages, and
  `rotation`, `flip_horizontal` and `flip_vertical` transform the image.
- The `border` table gives `width` and `color`, and `link` makes the image a
  hyperlink in DOCX and PDF.

## Figures and captions

```mote
#figure(numbering = { enabled = true })[
  #image("photo.png", width = inch(3), alignment = "center")
  #caption(position = "below")[The survey site at dawn.]
]
```

- The `#caption` directive holds inline text, and its `position` is `above` or
  `below`. The editable DOCX keeps the order in which the caption is written, so
  the caption belongs on the side where it should appear.
- With `numbering = { enabled = true }`, the caption begins with a bold label and
  number such as "Figure 1. ". The label is "Table" when `kind = "table"` and
  "Figure" otherwise; the `numbering` table also accepts `label`, `start`,
  `format` and `separator`.
- A `#label("name")` inside the figure lets the text refer to its number, as
  described in [notes and references](notes-and-references.md).

## Limits

- Images are placed in the flow of the text. The `placement` argument, which
  describes floating and wrapped images, is retained without effect, and a
  warning reports that ordinary flow is used.
- An image inside a list item or quotation appears as its alternative text in
  square brackets in PDF and PNG output; the DOCX keeps the image.
- A missing or unreadable file produces a warning and placeholder text.
