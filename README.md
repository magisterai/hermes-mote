# Mote for Hermes

[Mote](https://github.com/magisterai/mote-rs) is a document language built on
Markdown. One source compiles to an editable Word document, an editable
PowerPoint deck, and PDF or PNG pages, from one small executable that renders a
page in milliseconds.

This plugin gives Hermes Agent the whole loop: it writes a document in Mote,
renders the pages, looks at them, fixes the source, and exports the file.

## Tools

| Tool | Effect |
| --- | --- |
| `mote_render` | Renders a `.mote` or `.md` source to PNG pages and returns the page images to the model, with every warning and error and its line and column. |
| `mote_export` | Compiles the source to `.docx`, `.pptx` or `.pdf`. |

The plugin also bundles the Mote skill, which the agent loads with
`skill_view("mote:mote")`: a short language guide and a reference page for each
topic (text, tables, charts, slides, data, and so on).

## Install

The plugin calls the `mote` executable, which is built from source:

```sh
cargo install --git https://github.com/magisterai/mote-rs mote
hermes plugins install mote
hermes plugins enable mote
```

The plugin looks for `mote` at the `mote_path` setting, then on `PATH`, then in
`~/.cargo/bin`.

## Try it

> Write a one-page annual report for a community garden in Mote, with a table
> of harvests and a chart. Render it, check every page, fix anything that looks
> wrong, then export it to Word.

## What it does on your machine

- Runs the local `mote` executable as a subprocess on the source file you name.
- Writes rendered pages to a new temporary directory, and exported files next to
  the source or at the path you give.
- Makes no network calls, reads no credentials, and keeps no background process.

## License

MIT.
