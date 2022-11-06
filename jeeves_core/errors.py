from dataclasses import dataclass
from pathlib import Path

from documented import DocumentedError


@dataclass
class InvalidCommand(DocumentedError):
    """
    Something that is not a callable cannot be registered as a Jeeves command.

        Object: {self.command}
        Name: {self.name}
    """

    name: str
    command: object


@dataclass
class NoPluginsInstalled(DocumentedError):
    """
    No plugins installed 🤷

    This might mean that you have installed `jeeves-core` but no plugins.

    Look out for interesting plugins at https://jeeves.sh 🙂
    """


@dataclass
class NoJeevesFile(DocumentedError):
    """
    `jeeves.py` file not found.

    Expected to be found at: {self.path}
    """

    path: Path


@dataclass
class AppCreationFailed(DocumentedError):
    """
    Typer app creation has failed.

    Tree: {self.tree}
    """

    tree: object
