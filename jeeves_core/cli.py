import logging
import sys
from pathlib import Path

from jeeves_core.discover import construct_app
from jeeves_core.errors import NoCommandsFound
from jeeves_core.jeeves import Jeeves

logger = logging.getLogger('jeeves')


def execute_app(typer_app: Jeeves):
    try:
        return typer_app()

    except AssertionError as err:
        raise NoCommandsFound(directory=Path.cwd()) from err


def app() -> None:    # pragma: no cover
    """Construct and return Typer app."""
    typer_app = construct_app()
    try:
        return execute_app(typer_app)

    except Exception as err:
        if typer_app.debug:
            raise

        else:
            logger.error(err)
            sys.exit(1)


if __name__ == '__main__':    # pragma: no cover
    app()
