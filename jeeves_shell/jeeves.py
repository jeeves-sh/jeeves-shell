from enum import Enum

from typer import Typer


class LogLevel(str, Enum):
    """Logging level for the application."""

    DEBUG = 'debug'
    INFO = 'info'     # noqa: WPS110
    ERROR = 'error'


class Jeeves(Typer):
    """Support Jeeves-specific options."""

    log_level: LogLevel = LogLevel.ERROR
