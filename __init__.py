"""Mote for Hermes: write documents in Mote, see the rendered pages, export Word, PowerPoint and PDF."""

import functools
from pathlib import Path

from . import schemas, tools


def register(ctx):
    mote_path = ctx.get_config("mote_path", default="") or ""
    ctx.register_tool(name="mote_render", toolset="mote", schema=schemas.MOTE_RENDER,
                      handler=functools.partial(tools.render, mote_path=mote_path))
    ctx.register_tool(name="mote_export", toolset="mote", schema=schemas.MOTE_EXPORT,
                      handler=functools.partial(tools.export, mote_path=mote_path))
    skill = Path(__file__).parent / "skills" / "mote" / "SKILL.md"
    ctx.register_skill("mote", skill,
                       description="The Mote markup language: one source compiles to editable Word and PowerPoint files and to PDF or PNG pages.")
