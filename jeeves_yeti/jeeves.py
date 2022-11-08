import sys
from pathlib import Path

from plumbum import ProcessExecutionError
from plumbum.cmd import flakehell, isort, mypy
from typer import Exit, Typer

app = Typer(
    no_args_is_help=True,
    name='Yeti\'s Jeeves',
    help='Jeeves configuration for the Yeti. Mostly ad-hoc scripts for Python '
         'projects and stuff.',
)


def _find_python_packages(path: Path):
    for directory in path.iterdir():
        if (directory / '__init__.py').is_file():
            yield directory


@app.command()
def lint():
    """Run Python linters."""
    packages = list(_find_python_packages(Path.cwd()))

    try:  # noqa: WPS229
        mypy(*packages, stderr=sys.stderr, stdout=sys.stdout)
        flakehell('lint', *packages, stderr=sys.stderr, stdout=sys.stdout)
    except ProcessExecutionError as err:
        raise Exit(err.retcode)


@app.command()
def fmt():
    """Auto format Python code."""
    packages = list(_find_python_packages(Path.cwd()))

    try:
        isort(*packages, stderr=sys.stderr, stdout=sys.stdout)
    except ProcessExecutionError as err:
        raise Exit(err.retcode)
