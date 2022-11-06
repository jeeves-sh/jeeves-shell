import sys
from pathlib import Path

from plumbum import ProcessExecutionError
from plumbum.cmd import mypy, flakehell
from typer import Argument, Exit


def lint(path: Path = Argument('.')):
    """Run Python linters."""

    try:
        mypy(path, stderr=sys.stderr, stdout=sys.stdout)
        flakehell('lint', path, stderr=sys.stderr, stdout=sys.stdout)
    except ProcessExecutionError as err:
        raise Exit(err.retcode)
