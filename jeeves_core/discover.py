import logging
import string
import types
from pathlib import Path
from typing import List, Tuple, Iterable, Any, Optional

import more_itertools
from typer import Typer

from jeeves_core.entry_points import entry_points
from jeeves_core.import_by_path import import_by_path

logger = logging.getLogger('jeeves')


def list_installed_plugins() -> List[Tuple[str, Typer]]:
    """Find installed plugins."""
    return [
        (entry_point.name, entry_point.load())
        for entry_point in entry_points(group='jeeves')
    ]


def _construct_app_from_plugins() -> Typer:   # pragma: nocover
    plugins = list_installed_plugins()

    if len(plugins) == 1:
        return more_itertools.last(
            more_itertools.first(plugins),
        )

    root_app = Typer()
    for name, sub_typer in plugins:
        root_app.add_typer(
            typer_instance=sub_typer,
            name=name,
        )

    return root_app


def _is_function(python_object) -> bool:
    return isinstance(python_object, types.FunctionType)


def _is_name_suitable(name: str):
    first_character = more_itertools.first(name)
    return first_character not in f'{string.ascii_uppercase}_'


def retrieve_commands_from_jeeves_file(   # type: ignore
    directory: Path,
    jeeves_file_name: Optional[str] = 'jeeves.py',
) -> Iterable[Tuple[str, Any]]:
    try:
        jeeves_module = import_by_path(path=directory / jeeves_file_name)
    except FileNotFoundError as err:
        logger.debug('File not found: %s', err.filename)
        return

    for name, command in vars(jeeves_module).items():  # noqa: WPS421
        if _is_name_suitable(name) and _is_function(command):
            yield name, command


def _augment_app_with_jeeves_file(
    app: Typer,
    path: Path,
) -> Typer:      # pragma: nocover
    for name, command in retrieve_commands_from_jeeves_file(path):
        app.command()(command)

    return app


def construct_app() -> Typer:  # pragma: nocover
    """Discover plugins and construct a Typer app."""
    app = _construct_app_from_plugins()
    return _augment_app_with_jeeves_file(app=app, path=Path.cwd())
