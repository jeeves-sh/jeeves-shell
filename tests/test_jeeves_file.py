import sys
import tempfile
from pathlib import Path

import funcy
import pytest
from base import environment_from_jeeves_file, environment_from_jeeves_package
from typer import Typer

from jeeves_shell.discover import retrieve_commands_from_jeeves_file


@pytest.fixture(autouse=True)
def reload_jeeves():
    yield
    sys.modules.pop('jeeves', None)


def test_missing_directory(jeeves_files: Path, random_string: str):
    assert not list(
        retrieve_commands_from_jeeves_file(
            Path(f'/tmp/random_{random_string}'),   # noqa: S108
        ),
    )


def test_missing_file(jeeves_files: Path, random_string: str):
    with environment_from_jeeves_file(jeeves_files / 'empty.py') as directory:
        names_and_commands = list(
            retrieve_commands_from_jeeves_file(directory=directory),
        )
        assert not list(names_and_commands)


def test_empty(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'empty.py') as directory:
        names_and_commands = list(retrieve_commands_from_jeeves_file(directory))
        assert len(names_and_commands) == 0, names_and_commands


def test_single(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'single.py') as directory:
        name, _command = funcy.first(
            retrieve_commands_from_jeeves_file(directory),
        )

        assert name == 'foo'


def test_sub_app(jeeves_files: Path):
    with environment_from_jeeves_file(jeeves_files / 'sub_app.py') as directory:
        command_by_name = dict(retrieve_commands_from_jeeves_file(directory))

        assert set(command_by_name.keys()) == {'build', 'lint'}

        sub_command: Typer = command_by_name['build']
        assert {
            command.name for command in sub_command.registered_commands
        } == {'all', 'python', 'rust'}


def test_multiple(jeeves_files: Path):
    with environment_from_jeeves_file(
        jeeves_files / 'multiple.py',
    ) as directory:
        command_names = list(
            map(
                funcy.first,
                retrieve_commands_from_jeeves_file(directory),
            ),
        )

    assert command_names == ['foo', 'boo']


def test_missing(jeeves_files: Path):
    with tempfile.TemporaryDirectory() as raw_directory:
        assert not list(
            retrieve_commands_from_jeeves_file(
                # This directory does not exist ⬎
                Path(raw_directory) / 'foo',
            ),
        )


def test_syntax_error(jeeves_files: Path):
    with environment_from_jeeves_file(
        jeeves_files / 'syntax_error.txt',
    ) as directory:
        with pytest.raises(SyntaxError):
            list(retrieve_commands_from_jeeves_file(directory))


def test_import_error(jeeves_files: Path):
    with environment_from_jeeves_file(
        jeeves_files / 'import_error.py',
    ) as directory:
        with pytest.raises(ImportError):
            list(retrieve_commands_from_jeeves_file(directory))


def test_package(jeeves_files: Path):
    with environment_from_jeeves_package(
        jeeves_files / 'package',
    ) as directory:
        command_names = set(
            map(
                funcy.first,
                retrieve_commands_from_jeeves_file(directory),
            ),
        )

        assert command_names == {'lint', 'test'}
