import itertools
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
        (entry_point.name, entry_point.load())  # type: ignore
        for entry_point in entry_points(group='jeeves')  # type: ignore
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


def _is_typer(python_object) -> bool:
    return isinstance(python_object, typer.Typer)


def _is_name_suitable(name: str):
    first_character = more_itertools.first(name)
    return first_character not in f'{string.ascii_uppercase}_'


def retrieve_commands_from_jeeves_file(   # type: ignore   # noqa: C901
    directory: Path,
) -> Iterable[Tuple[str, Any]]:
    """Convert directory path → sequence of commands & subcommands."""
    if not directory.exists():
        return

    try:
        jeeves_module = import_by_path(
            path=directory,
        )

    except ImportError as err:    # pragma: nocover
        # We could not import something.
        if err.name == 'jeeves':
            # We couldn't import jeeves module. We can skip that.
            logger.debug('Module not found: %s', err)
            return

        # Something that `jeeves` module is importing can't be imported, that is
        # a problem.
        raise

    for name, command in vars(jeeves_module).items():  # noqa: WPS421
        if not _is_name_suitable(name):
            continue

        if _is_function(command) or _is_typer(command):
            yield name, command


def _augment_app_with_jeeves_file(
    app: Jeeves,
    path: Path,
) -> Jeeves:      # pragma: nocover
    commands = retrieve_commands_from_jeeves_file(path)
    for name, command in commands:
        if _is_typer(command):
            app.add_typer(typer_instance=command, name=name)
        else:
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
        if directory_from_environment := os.environ.get('JEEVES_ROOT'):
            current_directory = Path(directory_from_environment)
        else:
            current_directory = Path.cwd()

    app = _construct_app_from_plugins()
    app = _configure_callback(app)
    return _augment_app_with_jeeves_file(app=app, path=current_directory)
