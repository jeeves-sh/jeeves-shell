from dataclasses import dataclass
from pathlib import Path

from documented import DocumentedError


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
