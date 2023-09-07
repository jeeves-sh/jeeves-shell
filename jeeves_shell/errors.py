from dataclasses import dataclass
from pathlib import Path

from documented import DocumentedError
from typer import Typer


@dataclass
class NoCommandsFound(DocumentedError):
    """
    No Jeeves commands found, and there is nothing to show.

    To get some commands,
        - either create a `jeeves.py` file in current directory,
        - or install a Jeeves plugin.

    Current directory: {self.directory}
    """

    directory: Path


@dataclass
class PluginConflict(DocumentedError):
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
class UnsuitableRootApp(DocumentedError):
    """
    Typer app wants to be used as root Jeeves app but it has a callback.

    Typer app: {self.app}
    Registered callback: {self.app.registered_callback}

    Unable to assign standard Jeeves callback to the app because it has one.
    """

    app: Typer
