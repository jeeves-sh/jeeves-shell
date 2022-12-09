from pathlib import Path

from jeeves_core.discover import construct_app
from jeeves_core.errors import NoCommandsFound


def app() -> None:    # pragma: no cover
    """Construct and return Typer app."""
    typer_app = construct_app()
    try:
        return typer_app()
    except AssertionError as err:
        raise NoCommandsFound(directory=Path.cwd()) from err


if __name__ == '__main__':    # pragma: no cover
    app()
