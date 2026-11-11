"""Tool schemas: what the model reads to decide when to call each Mote tool."""

MOTE_RENDER = {
    "name": "mote_render",
    "description": (
        "Render a Mote source file (.mote or .md) to PNG pages and look at them. "
        "Returns the page images directly into your context, together with every "
        "warning and error that Mote reported, each with its file, line and column. "
        "Use it after writing or editing a Mote document to check the layout, then fix "
        "the source and render again. Load the skill with skill_view('mote:mote') before "
        "writing Mote for the first time."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path of the Mote source file. Imports, data files and images resolve relative to it.",
            },
            "pages": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1},
                "description": "Page numbers to return as images, starting at 1. Defaults to the first four pages.",
            },
            "dpi": {
                "type": "integer",
                "minimum": 36,
                "maximum": 300,
                "description": "Resolution of the page images. Defaults to 96, which is enough to judge layout.",
            },
            "layout": {
                "type": "string",
                "enum": ["document", "presentation"],
                "description": "Forces document pages or presentation slides. By default a source with #presentation(...) is laid out as slides.",
            },
            "lua": {
                "type": "boolean",
                "description": "Enables Lua expressions and #function definitions in the source.",
            },
        },
        "required": ["path"],
    },
}

MOTE_EXPORT = {
    "name": "mote_export",
    "description": (
        "Compile a Mote source file to an editable Word document (docx), an editable "
        "PowerPoint deck (pptx) or a PDF. Returns the output path and any warnings. "
        "Use it once the rendered pages look right."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Path of the Mote source file."},
            "format": {"type": "string", "enum": ["docx", "pptx", "pdf"], "description": "The output format."},
            "output": {
                "type": "string",
                "description": "Output file path. Defaults to the source path with the format's extension.",
            },
            "layout": {
                "type": "string",
                "enum": ["document", "presentation"],
                "description": "Forces document pages or presentation slides for PDF output.",
            },
            "lua": {"type": "boolean", "description": "Enables Lua expressions and #function definitions."},
        },
        "required": ["path", "format"],
    },
}
