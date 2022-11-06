from collections import defaultdict
from pathlib import Path
from typing import Dict, Any

from typer import Typer

from jeeves_core.errors import InvalidCommand, AppCreationFailed
from jeeves_core.process_modules import parse_module


def recursive_dict() -> Dict[str, Any]:  # type: ignore
    return defaultdict(recursive_dict)


def app_from_tree(tree: Dict[str, Any]):   # type: ignore
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
    names_and_commands = parse_module(Path.cwd() / 'jeeves.py')
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

    app = app_from_tree(tree)

    try:
        return app()
    except RuntimeError as err:
        raise AppCreationFailed(
            tree=tree,
        ) from err


if __name__ == '__main__':
    app()
