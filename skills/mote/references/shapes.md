# Shapes

A **shape** is positioned geometry with optional text, available in documents and
on slides, and written `#shape(...)[text]`. A **line**, written `#line(...)`, is a
straight connector with optional arrowheads, available on slides only.

## A shape

```mote
#shape(
  position = { x = inch(5.5), y = inch(1), width = inch(2.5), height = inch(1.25) },
  kind = "round_rect",
  fill = "#dcfce7",
  border = { color = "#15803d", width = pt(1) },
  text = { size = pt(10), color = "#14532d", alignment = "center", vertical_alignment = "center" }
)[Key finding: retention rose for the third quarter running.]
```

- The `position` argument is required. It gives `width` and `height`, and `x` and
  `y`, which default to zero.
- The `kind` argument is `rectangle`, the default, or one of `round_rect`,
  `ellipse`, `triangle`, `diamond`, `hexagon`, `chevron`, `cloud`,
  `parallelogram` and `trapezoid`.
- The `fill` argument is a color. The `border` argument gives `width`, `color`,
  `style` (`solid`, `dashed`, `dotted` or `none`) and `opacity`.
- The remaining appearance arguments are `opacity`, a percentage such as `35`;
  `rotation`, in degrees; `flip_horizontal` and `flip_vertical`; and
  `shadow = { color, blur, distance, angle, opacity }`.
- The optional body holds the shape's text: paragraphs, inline formatting and
  lists.

## Placement

In a document, `x` and `y` are measured from the top-left corner of the page on
which the `#shape` directive falls, not from the margin or from the text. The
shape occupies almost no space in the text, and the text does not wrap around it.
A shape therefore belongs in a margin, beside short lines, or behind text with a
low `opacity`.

```mote
#paragraph[This line sits inside a highlighted band.]

#shape(
  position = { x = inch(1), y = inch(1), width = inch(6.5), height = pt(18) },
  fill = "#fde68a",
  opacity = 35
)
```

On a slide, `x` and `y` are measured from the top-left corner of the slide, and
the slide holds only positioned objects.

## Shape text

The `text` table sets defaults for the body: `font`, `size`, `color`, `bold`,
`italic`, `underline`, `alignment` (`left`, `center`, `right` or `justify`),
`vertical_alignment` (`top`, `center` or `bottom`), `margin` (lengths for `left`,
`right`, `top` and `bottom`) and `fit`. The `fit` value determines the treatment
of text that exceeds the shape:

- `clip`, the default, cuts the text at the shape's edge;
- `shrink` reduces the text until it fits;
- `resize_shape` extends the text area downwards.

A table, image or page break inside a shape is omitted, with a warning.

## Lines and arrows

```mote
#presentation(size = "wide")
#slide[
  #line(
    from = { x = inch(1), y = inch(1) },
    to = { x = inch(4), y = inch(2) },
    border = { width = pt(2), color = "#28734f" },
    arrow = "triangle",
    cap = "round"
  )
]
```

The `arrow` argument is the marker at the end, one of `triangle`, `stealth`,
`diamond`, `oval` and `none`, or a table `{ start = "oval", end = "triangle" }`
giving both ends. The `cap` argument is `flat`, `round` or `square`. In a document
a line appears as the text `[line]`, with a warning; a thin rectangle serves
instead.
