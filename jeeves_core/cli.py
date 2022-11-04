import importlib.util
import sys
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Callable, Iterable

from typer import Typer

from jeeves_core.errors import InvalidCommand


def import_module_by_path(path: Path):
    """
    Import module knowing its filesystem path.

    Source: https://stackoverflow.com/a/67692/1245471
    """
    module_name = str(path).strip('/').replace('.', '_').replace('/', '.')
    spec = importlib.util.spec_from_file_location(module_name, path)
    foo = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = foo
    spec.loader.exec_module(foo)
    return foo


def remap_enter(_path: Tuple[str, ...], key: str, key_value: object):
    """Enter the node of the tree."""
    if isinstance(key_value, dict):
        return Typer(), key_value.items()

    if callable(key_value):
        return key_value, False

    raise InvalidCommand(
        name=key,
        command=key_value,
    )


def remap_exit(
    _path: Tuple[str, ...],
    _key: str,
    _old_parent,
    new_parent: Typer,
    new_items,
):
    """Exit the node of the tree."""
    for command_name, function_or_app in new_items:
        if isinstance(function_or_app, Typer):
            new_parent.add_typer(
                typer_instance=function_or_app,
                name=command_name,
            )
        else:
            new_parent.command(
                name=command_name,
            )(function_or_app)

    return new_parent


def collect_commands(path: Path) -> Iterable[Tuple[str, Callable]]:
    for directory in [path, *path.parents]:
        jeeves_file = directory / 'jeeves.py'

        if jeeves_file.is_file():
            jeeves_module = import_module_by_path(jeeves_file)

            for name, python_object in vars(jeeves_module).items():
                if callable(python_object):
                    yield name, python_object


def recursive_dict():
    return defaultdict(recursive_dict)


def app_from_tree(tree):
    root_app = Typer()

    for key, value in tree.items():
        if isinstance(value, dict):
            root_app.add_typer(
                app_from_tree(value),
                name=key,
            )

        else:
            root_app.command(name=key)(value)

    return root_app


def app() -> None:
    current_path = Path.cwd()
    names_and_commands = collect_commands(current_path)
    sequences_and_commands = [
        (name.split('__'), command)
        for name, command in names_and_commands
    ]

    tree = recursive_dict()

    for sequence, command in sequences_and_commands:
        root = tree
        for segment in sequence[:-1]:
            root = root[segment]

        root[sequence[-1]] = command

    return app_from_tree(tree)()


if __name__ == '__main__':
    app()
