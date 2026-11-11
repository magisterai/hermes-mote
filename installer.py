"""The `hermes mote` command: builds the mote executable from source at a pinned commit."""

import shutil
import subprocess
import sys

from . import tools

REPOSITORY = "https://github.com/magisterai/mote-rs"
# The commit is pinned so that an install builds exactly the source a reviewer can read; a newer Mote
# reaches users through a reviewed bump of this value, never by following a branch.
REVISION = "9976715e0253ff9bc5a057471ed1f98063b9febe"


def install_command():
    return ["cargo", "install", "--locked", "--git", REPOSITORY, "--rev", REVISION, "mote"]


def setup_arguments(parser):
    commands = parser.add_subparsers(dest="mote_command")
    commands.add_parser("install", help="Build and install the mote executable from source with cargo")
    commands.add_parser("status", help="Show which mote executable the plugin uses")


def handle(arguments, mote_path=""):
    command = getattr(arguments, "mote_command", None)
    if command == "install":
        return install()
    if command == "status":
        return status(mote_path)
    print("Usage: hermes mote <install|status>")
    return 1


def status(mote_path=""):
    executable = tools.find_mote(mote_path)
    if executable is None:
        print("The mote executable was not found. Run `hermes mote install`.")
        return 1
    print(f"mote: {executable}")
    return 0


def install():
    if shutil.which("cargo") is None:
        print("Building Mote needs Rust's cargo, which was not found. Install Rust from https://rustup.rs, "
              "then run `hermes mote install` again.")
        return 1
    command = install_command()
    print("Building Mote from source; the first build takes a few minutes.")
    print("$ " + " ".join(command))
    completed = subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)
    if completed.returncode != 0:
        print("The build failed; cargo's output above names the cause.")
        return completed.returncode
    return status()
