import sys
from dataclasses import dataclass
from pathlib import Path

import funcy
from documented import DocumentedError, Documented
from typer import Typer


@dataclass
class NoCommandsFound(DocumentedError):   # type: ignore
    """
    No Jeeves commands found, and there is nothing to show.

    To get some commands,
        - either create a `jeeves.py` file in current directory,
        - or install a Jeeves plugin.

    Current directory: {self.directory}
    """

    directory: Path


@dataclass
class PluginConflict(DocumentedError):   # type: ignore
    """
    Conflicting plugins detected.

    Multiple plugins are registered at the same mount point.

    Mount point: {self.mount_point}
    Plugins:
    {self.plugin_list}
    """

    mount_point: str
    plugins: list[Typer]

    @property
    def plugin_list(self) -> str:
        """Format plugin list."""
        return '\n'.join(
            f'• {plugin}' for plugin in self.plugins
        )


@dataclass
class UnsuitableRootApp(DocumentedError):   # type: ignore
    """
    Typer app wants to be used as root Jeeves app but it has a callback.

    Typer app: {self.app}
    Registered callback: {self.app.registered_callback}

    Unable to assign standard Jeeves callback to the app because it has one.
    """

    app: Typer


@dataclass
class FormattedError(Documented):    # type: ignore  # pragma: no cover
    """**{self.exception_class}:** {self.message}"""  # noqa: D400

    exception: Exception

    @property
    def exception_class(self):
        """Class of the exception."""
        return self.exception.__class__.__name__

    @property
    def message(self):
        """Exception message."""
        return str(self.exception)


class TracebackAdvice(Documented):  # pragma: no cover
    """
    💡 To see Python traceback, use:

    `j --log-level info {self.args}`
    """  # noqa: D400

    @property
    def args(self):
        """Format current CLI args."""
        return ' '.join(funcy.rest(sys.argv))
