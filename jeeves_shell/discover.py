import logging
import os
import string
import types
from pathlib import Path
from typing import Any, Iterable, List, Optional, Tuple

import more_itertools
import typer

from jeeves_shell.entry_points import entry_points
from jeeves_shell.import_by_path import import_by_path
from jeeves_shell.jeeves import Jeeves, LogLevel

logger = logging.getLogger('jeeves')


def list_installed_plugins() -> List[Tuple[str, Jeeves]]:
    """Find installed plugins."""
    return [
        (entry_point.name, entry_point.load())
        for entry_point in entry_points(group='jeeves')
    ]


def _construct_app_from_plugins() -> Jeeves:   # pragma: nocover
    if os.getenv('JEEVES_DISABLE_PLUGINS'):
        plugins = []
    else:
        plugins = list_installed_plugins()

    if len(plugins) == 1:
        _name, plugin = more_itertools.first(plugins)
        return plugin

    root_app = Jeeves(no_args_is_help=True)
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
    jeeves_file_name: str = 'jeeves.py',
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
    app: Jeeves,
    path: Path,
) -> Jeeves:      # pragma: nocover
    for name, command in retrieve_commands_from_jeeves_file(path):
        app.command()(command)

    return app


def _configure_callback(app: Jeeves) -> Jeeves:
    def _root_app_callback(   # noqa: WPS430
        log_level: LogLevel = typer.Option(
            LogLevel.ERROR,
            help='Logging level.',
        ),
    ):   # pragma: nocover
        app.log_level = log_level
        logging.basicConfig(
            level={
                LogLevel.ERROR: logging.ERROR,
                LogLevel.INFO: logging.INFO,
                LogLevel.DEBUG: logging.DEBUG,
            }[log_level],
        )

    app.callback()(_root_app_callback)
    return app


def construct_app(current_directory: Optional[Path] = None) -> Jeeves:
    """Discover plugins and construct a Typer app."""
    if current_directory is None:       # pragma: no cover
        current_directory = Path.cwd()

    app = _construct_app_from_plugins()
    app = _configure_callback(app)
    return _augment_app_with_jeeves_file(app=app, path=current_directory)
