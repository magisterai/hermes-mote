"""Tool handlers. Each runs the local `mote` executable and never raises."""

import base64
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

INSTALL_HINT = (
    "The mote executable was not found. Install it from source with "
    "`cargo install --git https://github.com/magisterai/mote-rs mote`, or set the plugin "
    "setting mote_path to its location."
)
DEFAULT_PAGES = 4
MAXIMUM_PAGES = 8
TIMEOUT_SECONDS = 120


def find_mote(configured=""):
    """The mote executable: the configured path, then PATH, then Cargo's install directory."""
    candidates = [configured] if configured else []
    candidates.append(shutil.which("mote") or "")
    candidates.append(str(Path.home() / ".cargo" / "bin" / "mote"))
    for candidate in candidates:
        if candidate and os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return None


def run_mote(executable, arguments):
    """Runs mote and returns (succeeded, diagnostics) with one diagnostic per stderr line."""
    completed = subprocess.run([executable, *arguments], capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
    diagnostics = [line for line in completed.stderr.splitlines() if line.strip()]
    return completed.returncode == 0, diagnostics


def common_arguments(args):
    arguments = []
    if args.get("layout") in ("document", "presentation"):
        arguments += ["--layout", args["layout"]]
    if args.get("lua"):
        arguments.append("--lua")
    return arguments


def source_path(args):
    raw = str(args.get("path") or "").strip()
    if not raw:
        return None, "No path was given."
    path = Path(raw).expanduser().resolve()
    if not path.is_file():
        return None, f"No source file at {path}."
    return path, None


def render(args, mote_path="", **kwargs):
    try:
        executable = find_mote(mote_path)
        if executable is None:
            return json.dumps({"error": INSTALL_HINT})
        path, problem = source_path(args)
        if problem:
            return json.dumps({"error": problem})
        dpi = min(max(int(args.get("dpi") or 96), 36), 300)
        directory = Path(tempfile.mkdtemp(prefix=f"mote-{path.stem}-"))
        succeeded, diagnostics = run_mote(
            executable, ["--format", "png", "--dpi", str(dpi), *common_arguments(args), "-o", str(directory / "page"), "--", str(path)])
        if not succeeded:
            return json.dumps({"error": "Mote reported an error and wrote no pages.", "diagnostics": diagnostics})
        rendered = sorted(directory.glob("page-*.png"), key=lambda page: int(page.stem.rsplit("-", 1)[1]))
        requested = [number for number in (args.get("pages") or []) if isinstance(number, int)]
        numbers = [number for number in requested if 1 <= number <= len(rendered)] or list(range(1, len(rendered) + 1))
        numbers = numbers[:MAXIMUM_PAGES] if requested else numbers[:DEFAULT_PAGES]
        summary = (f"Rendered {path.name}: {len(rendered)} page(s) at {dpi} dpi in {directory}. "
                   f"Showing page(s) {', '.join(map(str, numbers))}. "
                   + (f"{len(diagnostics)} warning(s):\n" + "\n".join(diagnostics) if diagnostics else "No warnings."))
        content = [{"type": "text", "text": summary}]
        for number in numbers:
            encoded = base64.b64encode(rendered[number - 1].read_bytes()).decode("ascii")
            content.append({"type": "text", "text": f"Page {number} of {len(rendered)}:"})
            content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded}"}})
        # The text summary serves models that cannot receive images in a tool result; the paths let them
        # inspect the pages with the vision tool instead.
        fallback = summary + "\nPage files:\n" + "\n".join(str(rendered[number - 1]) for number in numbers)
        return {"_multimodal": True, "content": content, "text_summary": fallback,
                "meta": {"pages": len(rendered), "directory": str(directory), "native_vision": True}}
    except subprocess.TimeoutExpired:
        return json.dumps({"error": f"Mote did not finish within {TIMEOUT_SECONDS} seconds."})
    except Exception as error:
        return json.dumps({"error": f"Rendering failed: {error}"})


def export(args, mote_path="", **kwargs):
    try:
        executable = find_mote(mote_path)
        if executable is None:
            return json.dumps({"error": INSTALL_HINT})
        path, problem = source_path(args)
        if problem:
            return json.dumps({"error": problem})
        output_format = args.get("format")
        if output_format not in ("docx", "pptx", "pdf"):
            return json.dumps({"error": "The format must be docx, pptx or pdf."})
        output = Path(args.get("output") or path.with_suffix("." + output_format)).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        succeeded, diagnostics = run_mote(
            executable, ["--format", output_format, *common_arguments(args), "-o", str(output), "--", str(path)])
        if not succeeded:
            return json.dumps({"error": "Mote reported an error and wrote no output.", "diagnostics": diagnostics})
        return json.dumps({"output": str(output), "bytes": output.stat().st_size, "warnings": diagnostics})
    except subprocess.TimeoutExpired:
        return json.dumps({"error": f"Mote did not finish within {TIMEOUT_SECONDS} seconds."})
    except Exception as error:
        return json.dumps({"error": f"Export failed: {error}"})
