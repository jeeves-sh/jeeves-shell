import random
import string
from pathlib import Path

import more_itertools
import pytest

from jeeves_shell.discover import retrieve_commands_from_jeeves_file
from tests.base import environment_from_jeeves_file


@pytest.fixture()
def random_string() -> str:
    return ''.join(
        random.sample(
            string.ascii_lowercase,
            10,
        ),
    )


def test_missing_directory(jeeves_files: Path, random_string: str):
    assert not list(retrieve_commands_from_jeeves_file(
        Path(f'/tmp/random_{random_string}')
    ))


def test_missing_file(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'empty.py') as directory:
        names_and_commands = list(
            retrieve_commands_from_jeeves_file(
                directory=directory,
                jeeves_file_name=f'jeeves_{random_string}.py',
            ),
        )
        assert not list(names_and_commands)


def test_empty(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'empty.py') as directory:
        names_and_commands = list(retrieve_commands_from_jeeves_file(directory))
        assert len(names_and_commands) == 0, names_and_commands


def test_single(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'single.py') as directory:
        name, _command = more_itertools.first(
            retrieve_commands_from_jeeves_file(directory),
        )

        assert name == 'foo'


def test_multiple(jeeves_files: Path):
    with environment_from_jeeves_file(
        jeeves_files / 'multiple.py',
    ) as directory:
        command_names = list(
            map(
                more_itertools.first,
                retrieve_commands_from_jeeves_file(directory),
            )
        )

    assert command_names == ['foo', 'boo']


def test_syntax_error(jeeves_files: Path):
    with environment_from_jeeves_file(
        jeeves_files / 'syntax_error.txt',
    ) as directory:
        with pytest.raises(SyntaxError):
            list(retrieve_commands_from_jeeves_file(directory))
