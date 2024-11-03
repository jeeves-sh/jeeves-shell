import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.errors import NotRenderableError
from rich.panel import Panel

from jeeves_shell.discover import construct_app
from jeeves_shell.errors import NoCommandsFound, TracebackAdvice, FormattedError
from jeeves_shell.jeeves import Jeeves, LogLevel

logger = logging.getLogger('jeeves')


def execute_app(typer_app: Jeeves):
    try:
        return typer_app()

    except RuntimeError as err:
        raise NoCommandsFound(directory=Path.cwd()) from err


def print_unhandled_exception(err: Exception):  # pragma: no cover
    """Print unhandled exception as an error message."""
    console = Console()

    try:
        console.print(Panel(err, style='red'))  # type: ignore
    except NotRenderableError:
        console.print(Panel(FormattedError(exception=err), style='red'))

    console.print(TracebackAdvice())


def app() -> None:    # pragma: no cover
    """Construct and return Typer app."""
    typer_app = construct_app()
    try:
        return execute_app(typer_app)

    except Exception as err:
        if typer_app.log_level == LogLevel.ERROR:
            print_unhandled_exception(err)
            sys.exit(1)

        else:
            raise


if __name__ == '__main__':    # pragma: no cover
    app()
