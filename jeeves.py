from pathlib import Path

from plumbum.cmd import mypy, flakehell
from typer import Argument


def lint(path: Path = Argument('.')):
    """Run Python linters."""

    mypy(path)
    flakehell('lint', path)
