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


def construct_app() -> Typer:
    """Discover plugins and construct a Typer app."""
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
