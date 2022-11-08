import string
import sys
import types
from pathlib import Path
from typing import List, Tuple

import more_itertools
from typer import Typer

from jeeves_core.entry_points import entry_points


def list_installed_plugins() -> List[Tuple[str, Typer]]:
    """Find installed plugins."""
    return [
        (entry_point.name, entry_point.load())
        for entry_point in entry_points(group='jeeves')
    ]


def _construct_app_from_plugins() -> Typer:
    plugins = list_installed_plugins()

    if len(plugins) == 1:
        return more_itertools.last(  # type: ignore
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


def _augment_app_with_jeeves_file(app: Typer) -> Typer:
    sys.path.insert(0, str(Path.cwd()))

    try:
        jeeves_module = __import__('jeeves')  # noqa: WPS421
    except ImportError:
        return app

    for name, command in vars(jeeves_module).items():  # noqa: WPS421
        if _is_name_suitable(name) and _is_function(command):
            app.command()(command)

    return app


def construct_app() -> Typer:
    """Discover plugins and construct a Typer app."""
    app = _construct_app_from_plugins()
    return _augment_app_with_jeeves_file(app)
