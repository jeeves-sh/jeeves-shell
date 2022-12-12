from pathlib import Path

import pytest

from jeeves_shell import Jeeves
from jeeves_shell.cli import execute_app
from jeeves_shell.discover import construct_app
from jeeves_shell.errors import NoCommandsFound
from tests.base import environment_from_jeeves_file


def test_execute_empty_app():
    app = Jeeves()

    with pytest.raises(NoCommandsFound):
        execute_app(app)


def test_execute_non_empty_app(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'empty.py') as directory:
        app = construct_app(directory)

    with pytest.raises(SystemExit):
        execute_app(app)
