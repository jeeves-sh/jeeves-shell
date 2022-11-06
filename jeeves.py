import sys
from pathlib import Path

from plumbum import ProcessExecutionError
from plumbum.cmd import mypy, flakehell
from typer import Argument, Exit


def _find_python_packages(path: Path):
    for directory in path.iterdir():
        if (directory / '__init__.py').is_file():
            yield directory


def lint():
    """Run Python linters."""

    packages = list(_find_python_packages(Path.cwd()))

    try:
        mypy(*packages, stderr=sys.stderr, stdout=sys.stdout)
        flakehell('lint', *packages, stderr=sys.stderr, stdout=sys.stdout)
    except ProcessExecutionError as err:
        raise Exit(err.retcode)
