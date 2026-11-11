# Lua

The Lua 5.1 language supplies arithmetic, comparison, string formatting and
functions. Lua is disabled unless the `--lua` option, or `enable_lua` in the
library, enables it; a source that uses Lua fails to compile without it.

## Expressions

With Lua enabled, an argument or binding value may be a Lua expression.

```mote lua
#let(sales = json("sales.json"), north = sales.regions[1].revenue, south = sales.regions[2].revenue)
#let(total = north + south, share = string.format("%.1f", north / total * 100))

Total revenue was #total million, of which North earned #share%.
#if(north > south)[North earned the larger part.]
```

- The operators are `+`, `-`, `*`, `/`, `..` (concatenation), `==`, `~=`, `<`,
  `>`, `and`, `or` and `not`.
- An index in square brackets counts from one, as in `sales.regions[1]`; a
  dotted Mote path such as `sales.regions.0` counts from zero.
- Every binding in scope is visible to Lua, and the value helpers, such as
  `format_number` and `upper`, are Lua functions.
- An expression is not written inline in text: its value is bound with `#let` and
  the binding inserted.

## Functions

A `#function` definition holds Lua statements and ends with `end`. Its result is
inserted where the function is called; a final parameter named `body` receives
the bracketed content of the call.

```mote lua
#function percent(part, whole)
  return string.format("%.1f%%", part / whole * 100)
end
#function callout(title, body)
  return {document.strong(title), ": ", body}
end

North earned #percent(62, 109) of revenue.

#paragraph[#callout("Note")[Figures are unaudited.]]
```

- A call accepts positional or named arguments: `#percent(whole = 109, part = 62)`.
- A function may return text, a number, a value, or content built with the
  `document` constructors, such as `document.paragraph`, `document.strong` or
  `document.table`; an array of content is inserted in order.

## Libraries

- The `string` functions are `format`, `len`, `sub`, `upper`, `lower`, `rep`,
  `reverse`, `byte` and `char`, also available as methods: `("x"):upper()`. The
  function `string.format` supports `%d`, `%i`, `%x`, `%X`, `%e`, `%E`, `%f`,
  `%g`, `%G`, `%s` and `%%`, with the flags `-`, `0`, `+` and space and widths of
  up to two digits.
- The `math` library is complete except for `random` and `randomseed`.
- The base functions `type`, `tostring`, `tonumber`, `pairs`, `ipairs`, `pcall`,
  `select`, `unpack` and `error` are available.

## Limits

- The pattern functions `string.find`, `string.match`, `string.gmatch` and
  `string.gsub` are not available, nor are the `table`, `os`, `io` and `debug`
  libraries, `require`, `load` or `print`.
- A compilation may spend ten seconds in Lua, adjustable with `--lua-timeout`,
  and allocate 256 MiB.
- A Lua table that is not a contiguous array becomes an object, and an empty
  table an empty object.
