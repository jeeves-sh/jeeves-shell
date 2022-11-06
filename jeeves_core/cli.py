from collections import defaultdict
from pathlib import Path
from typing import Any, Dict

from typer import Typer

from jeeves_core.errors import AppCreationFailed
from jeeves_core.process_modules import parse_module

Tree = Dict[str, Any]    # type: ignore


def recursive_dict() -> Tree:
    return defaultdict(recursive_dict)


def app_from_tree(tree: Dict[str, Any]):   # type: ignore
    root_app = Typer()

    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            root_app.add_typer(
                app_from_tree(sub_tree),
                name=key,
            )

        else:
            root_app.command(name=key)(sub_tree)

    return root_app


def construct_tree() -> Tree:
    """Construct tree of commands."""
    tree = recursive_dict()

    for sequence, command in parse_module(Path.cwd() / 'jeeves.py'):
        root = tree
        for segment in sequence[:-1]:
            root = root[segment]

        root[sequence[-1]] = command

    return tree


def app() -> None:
    """Construct and return Typer app."""
    tree = construct_tree()

    typer_app = app_from_tree(tree)

    try:
        return typer_app()
    except RuntimeError as err:
        raise AppCreationFailed(
            tree=tree,
        ) from err


if __name__ == '__main__':
    app()
