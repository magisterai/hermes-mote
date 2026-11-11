# Charts

The `#chart` directive produces an editable Office chart in DOCX and PPTX, with
its data in an embedded workbook, and draws the same chart in PDF and PNG. The
directive takes named arguments and no body.

## Data

A **category** labels a position along the chart, and a **series** is a named
sequence of values, one for each category.

```mote
#chart(
  kind = "column",
  title = "Revenue by quarter",
  width = inch(6),
  height = inch(3),
  data = {
    categories = { "Q1", "Q2", "Q3", "Q4" },
    series = {
      { name = "2025", values = { 12, 15, 16, 19 } },
      { name = "2026", values = { 14, 17, 21, 24 } }
    }
  }
)
```

- A single series may be written `data = { name = "Sales", values = { 4, 7 } }`.
- A value is a number or a numeric string; any other value counts as zero.
- The data may be a binding, such as a JSON resource loaded with `json(...)`.

## Kinds

The `kind` argument is one of `column`, `bar`, `line`, `area`, `pie` and
`doughnut`, or one of the stacked forms `stacked_column`, `stacked_bar`,
`stacked_area`, `percent_stacked_column`, `percent_stacked_bar` and
`percent_stacked_area`. The default is `column`. A pie or doughnut chart plots
only the first series.

## Size

The default size is 6 by 3.5 inches. A chart wider than the text column of a
document is reduced to fit, with its proportions kept. The `width` and `height`
arguments require units.

## Appearance

```mote
#chart(
  kind = "bar",
  title = { text = "Coverage", size = pt(13), bold = true, color = "#0b3b4f" },
  data = { categories = { "North", "South" }, series = { { name = "Cover", values = { 26, 31 } } } },
  colors = { "#2563eb", "#059669" },
  background = "#ffffff",
  border = { color = "#cbd5e1", width = pt(1) },
  plot_area = { fill = "#f8fafc" },
  gridlines = { major = true, minor = false },
  axis = { category = { title = "Region" }, value = { title = "Percent" } },
  legend = "bottom",
  data_labels = { value = true, position = "outside_end" },
  gap_width = 80
)
```

- The `colors` array gives one color for each series in order, or for each slice
  of a pie or doughnut chart. The default palette begins with blue, green and
  amber.
- The `legend` argument is `true`, `false`, or one of `"right"`, `"left"`, `"top"`
  and `"bottom"`. Unless it is given, a pie or doughnut chart, and a chart with
  more than one series, shows a legend.
- The `data_labels` argument is `true` for values, or a table selecting `value`,
  `category`, `series` and `percent`, with a `position` of `center`, `inside_end`,
  `inside_base`, `outside_end`, `best_fit`, `left`, `right`, `top` or `bottom`.
- The `gap_width` argument is the space between groups of bars, and `overlap` the
  overlap of bars within a group, each as a percentage of a bar's width.
- A chart without a `title` has no title area.
- The lines follow Office's default chart style: light grey (`#D9D9D9`) gridlines and
  category axis at 0.75 pt, no value axis line and no tick marks. The `gridlines`
  table's `color` and `width` replace the gridline defaults.

## The value axis

The range and step of the value axis follow Office's automatic rules. The data's
range is padded by a twentieth at each nonzero end, the step is 1, 2 or 5 times a
power of ten chosen for the height of the chart, and every step is labelled. No
argument sets the minimum, maximum or step.

## Limits

- Scatter, bubble, radar, stock, combination and 3D charts are not available, nor
  are secondary axes, trendlines, error bars or colors for individual points.
- An area chart shows no data labels in PDF and PNG output.
- In PDF and PNG output, a chart inside a table cell becomes text, and a chart in
  a header or footer is omitted, each with a warning.
- A horizontal bar chart may omit value-axis labels that would collide.
