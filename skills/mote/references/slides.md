# Slides

A **deck** is a sequence of slides, declared by `#presentation`. A **slide** holds
either loose content, which is laid out automatically, or positioned objects. A
**box** is a positioned rectangle holding text, or exactly one image, table or
chart. A **layout** is a named arrangement of **slots**, boxes whose position is
given once and filled on each slide.

## The deck

```mote
#presentation(
  size = "wide",
  background = "#ffffff",
  theme = { colors = { accent1 = "#2563eb", text = "#1f2633" }, fonts = { heading = "Helvetica", body = "Helvetica" } },
  footer = "Meridian Transit Survey",
  slide_number = true
)

#slide(notes = "Open with the headline number.")[
  #heading(level = 1)[Quarterly review]

  - Revenue rose by 12%.
  - Two new markets.
]
```

- The `size` argument is `wide` (16:9), `standard` (4:3), or a table of `width`
  and `height`.
- The `background` argument is a color or a table with an image `src` and a `fit`
  of `stretch`, `cover` or `contain`.
- The `theme` table gives `colors` (`accent1` to `accent6`, `text`, `background`,
  `hyperlink`) and `fonts` (`heading`, `body`), which charts and text inherit.
- The `footer`, `date` and `slide_number` arguments add those fields to every
  slide; a slide may override or disable each one.
- The `notes` argument of a slide gives the speaker notes, as plain text.

A deck may also be written as Markdown: in a source with `#presentation`, each
level-one heading begins a slide, and a line of `---` between blank lines
separates slides.

## Positioned slides

```mote
#presentation(size = "wide")
#slide[
  #box(position = { x = inch(0.6), y = inch(0.4), width = inch(12), height = inch(1) })[
    #heading(level = 1)[Results]
  ]
  #box(position = { x = inch(0.6), y = inch(1.6), width = inch(5.8), height = inch(4.5) },
       fill = "#f8fafc", margin = { left = pt(12), right = pt(12) }, text = { size = pt(20), fit = "shrink" })[
    - Revenue rose by 12%.
    - Retention improved.
  ]
  #box(position = { x = inch(6.8), y = inch(1.6), width = inch(5.8), height = inch(4.5) })[
    #chart(kind = "column", data = { categories = { "Q1", "Q2" }, series = { { name = "Revenue", values = { 10, 12 } } } })
  ]
]
```

- Coordinates are measured from the top-left corner of the slide; a wide slide
  is 13.333 by 7.5 inches, and a standard slide 10 by 7.5 inches.
- A box accepts the appearance and `text` arguments of a shape, described in
  [shapes](shapes.md), including `fit = "shrink"` for text that must fit.
- Shapes and lines may stand beside boxes on a positioned slide.

## Layouts

The built-in layouts are `title_slide` (`title`, `subtitle`), `title_and_content`
(`title`, `content`), `section_header` (`title`, `subtitle`), `two_column`
(`title`, `left`, `right`), `comparison` (`title`, `left_title`, `left`,
`right_title`, `right`), `image_and_caption` (`title`, `image`, `caption`),
`chart_and_caption` (`title`, `chart`, `caption`) and `blank`. A slide names its
layout and fills slots with `#box(slot = "name")`.

```mote
#presentation(size = "wide")
#layout(name = "report", based_on = "title_and_content")[
  #box(slot = "title", fill = "#eff6ff", text = { color = "#2563eb" })
]

#slide(layout = "two_column")[
  #box(slot = "title")[#heading(level = 1)[Two markets]]
  #box(slot = "left")[North grew by 12%.]
  #box(slot = "right")[South grew by 4%.]
]

#slide(layout = "report")[
  #box(slot = "title")[#heading(level = 1)[Summary]]
  #box(slot = "content")[Both markets grew.]
]
```

A `#layout` declaration defines a custom layout: its body holds empty slot boxes
with a `position`, a `kind` (`text`, `image`, `table`, `chart` or `content`) and
default appearance, and `based_on` inherits the slots of another layout. A slot
box on a slide may override any of the slot's properties.

## Limits

- A slide holds loose content or positioned objects, never both.
- Layouts become ordinary positioned objects in the PPTX, not PowerPoint
  placeholders or slide masters.
