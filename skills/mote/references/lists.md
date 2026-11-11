# Lists

A **list** is a block holding a sequence of **items**. An unordered list marks
its items with bullets, and an ordered list numbers them. An item holds text and
may hold further blocks, including another list.

## Markdown lists

A line beginning with `-` and a space starts an unordered item, and digits
followed by `.` and a space start an ordered item. A line indented beyond the
marker continues the item, and an indented marker begins a nested item.

```mote
- Prepare the report
  in draft.
  1. Check the totals.
  2. Write the summary.
- Share the report.
- [x] Book the room.
- [ ] Send the agenda.
```

The markers `[ ]` and `[x]` after a list marker make an item a task with an
unchecked or checked box.

## List directives

The `#list` and `#ordered_list` directives hold `#item` directives, and an item's
body is block content. The explicit form is required for list formatting.

```mote
#ordered_list(start = 3, format = "upper_roman", indent = { left = pt(36), hanging = pt(18) })[
  #item[Review the findings.]
  #item[Approve the budget.
    #list[
      #item[Operations]
      #item[Research]
    ]
  ]
]
```

- The `start` argument is the first number of an ordered list, and `format` is
  `decimal`, `lower_alpha`, `upper_alpha`, `lower_roman` or `upper_roman`.
- The `indent` table gives `left`, `hanging`, and `level`, the additional indent
  for each level of nesting.
- The `tight` argument removes the space after each item, and
  `spacing = { after = ... }` sets it.
- An item accepts `checked = true` or `checked = false`, which makes it a task.

## Limits

- The body of `#list` or `#ordered_list` holds only items; text directly inside
  it is an error.
