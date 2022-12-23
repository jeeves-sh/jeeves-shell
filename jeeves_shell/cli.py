import logging
import sys
from pathlib import Path

from jeeves_shell.discover import construct_app
from jeeves_shell.errors import NoCommandsFound
from jeeves_shell.jeeves import Jeeves, LogLevel

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
        if typer_app.log_level == LogLevel.ERROR:
            logger.error(err)
            sys.exit(1)

        else:
            raise


if __name__ == '__main__':    # pragma: no cover
    app()
