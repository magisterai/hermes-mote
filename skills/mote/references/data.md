# Data, conditions and loops

A **binding** gives a name to a value. A value is a string, number, boolean,
length, color, array or object, and may be read from a JSON or CSV file. A
**condition** includes content when a value is true, and a **loop** repeats
content for each member of an array or object. None of these requires Lua.

## Bindings

```mote
#let(client = "Acme", total = 1234.5, accent = color("#2563eb"), report = { quarter = "Q3", totals = { 10, 20 } })
#let(second = report.totals.1)

#heading(level = 1)[Report for #client]

The #report.quarter total is #span(color = accent)[#format_money(total)], and the second figure is #second.
```

- The form `#name` inserts a value, and `#name.field` a field of an object.
- An array index in a path counts from zero, and is written in an expression,
  as in `report.totals.1`; the inserted form `#name.0` is not an index.
- A binding made inside a directive body is local to that body.

## Files

```mote
#let(sales = json("sales.json"), rows = csv("sales.csv"))

#chart(kind = "line", title = sales.title, data = sales.chart)

#table[
  #row(repeat_header = true)[#cell[**Region**] #cell[**Revenue**]]
  #for region in sales.regions {#row[#cell[#region.name] #cell[#region.revenue]]}
]

#for row in rows {#paragraph[#row.region: #row.revenue million, up #row.change%.]}
```

- The function `json(path)` reads a JSON file, and `csv(path)` reads a CSV file
  as an array of objects, one for each record, keyed by the header row; every
  CSV value is a string. A path is relative to the source file.
- The function `#import("shared.mote")` evaluates another source and makes its
  bindings, defaults, styles and fonts available, without inserting its text.

## Conditions and loops

```mote
#let(sales = json("sales.json"))

#for region in sales.regions {
  #paragraph[#region.name: #if(region.paid)[paid] else [awaiting payment].]
}
```

- The form `#if(value)[content] else [other content]` includes one branch. The
  values `nil`, `false`, zero, an empty string, an empty array or object and a
  zero length are false; every other value, including the string `"false"`, is
  true.
- The form `#for name in value {content}` repeats its content, which is Mote
  markup, for each member. A loop may generate rows, cells, list items and
  paragraphs where the enclosing directive accepts them.

## Value helpers

- `upper(text)` and `lower(text)` change case.
- `format_number(value, decimals)` rounds a number, as in
  `format_number(1234.5, 1, grouping = true)`, which gives `1,234.5`; grouping is
  off by default.
- `format_money(amount, currency)` gives `$1,234.50`, or `EUR 1,234.50` for
  another currency.
- `date("2026-11-04")` is a date, and `length(12, "pt")` a length.

## Limits

- Arithmetic and comparison, such as `total * 1.2` or `count > 3`, require Lua,
  described in [Lua](lua.md).
- A `#section` generated inside a condition or loop also repeats its body as
  ordinary content; sections belong at the top level.
