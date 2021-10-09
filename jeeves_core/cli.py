from importlib.metadata import entry_points
from typing import Tuple

from benedict import benedict
from boltons.iterutils import remap
from rich.traceback import install
from typer import Typer

from jeeves_core.errors import InvalidCommand, NoPluginsInstalled


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


def app() -> None:
    """Construct a Typer app from installed Jeeves plugins."""
    install(show_locals=False)

    try:
        points = entry_points()['jeeves']
    except KeyError as err:
        raise NoPluginsInstalled() from err

    if not points:
        raise NoPluginsInstalled()

    commands_tree = benedict()
    for point in points:
        commands_tree[point.name] = point.load()

    typer_app = remap(
        root=commands_tree,
        enter=remap_enter,
        exit=remap_exit,
    )

    return typer_app()


if __name__ == '__main__':
    app()
