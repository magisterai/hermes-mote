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

```sh
hermes plugins install mote
hermes plugins enable mote
hermes mote install
```

The plugin calls the `mote` executable. The command `hermes mote install` builds
it from source with Rust's `cargo`, at a pinned commit of
[mote-rs](https://github.com/magisterai/mote-rs); [rustup](https://rustup.rs)
installs Rust. The command `hermes mote status` shows which executable the plugin
uses: the `mote_path` setting, then `mote` on `PATH`, then `~/.cargo/bin/mote`.

## Try it

> Write a one-page annual report for a community garden in Mote, with a table
> of harvests and a chart. Render it, check every page, fix anything that looks
> wrong, then export it to Word.

## What it does on your machine

- Runs the local `mote` executable as a subprocess on the source file you name.
- `hermes mote install`, when you run it, downloads the mote-rs source at a pinned
  commit and its Rust dependencies from crates.io, and builds them with `cargo`.
- Writes rendered pages to a new temporary directory, and exported files next to
  the source or at the path you give.
- The tools make no network calls, read no credentials, and keep no background
  process.

## License

MIT.
