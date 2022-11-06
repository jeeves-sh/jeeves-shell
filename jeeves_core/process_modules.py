import importlib.util
import string
import sys
import types
from pathlib import Path
from typing import Iterable, Tuple, Callable

import more_itertools

from jeeves_core.errors import NoJeevesFile


def import_module_by_path(path: Path):
    """
    Import module knowing its filesystem path.

    Source: https://stackoverflow.com/a/67692/1245471
    """
    module_name = str(path).strip('/').replace('.', '_').replace('/', '.')
    spec = importlib.util.spec_from_file_location(module_name, path)

    if spec is None:
        raise ValueError('Spec is none. This is an unknown error. Panicking!')

    imported_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = imported_module

    try:
        spec.loader.exec_module(imported_module)   # type: ignore
    except FileNotFoundError as err:
        raise NoJeevesFile(path=path) from err

    return imported_module


def is_function(python_object) -> bool:
    return type(python_object) == types.FunctionType


def is_name_suitable(name: str):
    first_character = more_itertools.first(name)

    return first_character not in f'{string.ascii_uppercase}_'


def parse_module(path: Path) -> Iterable[Tuple[str, types.FunctionType]]:
    """Load and parse a module."""
    jeeves_module = import_module_by_path(path)

    for name, python_object in vars(jeeves_module).items():
        if is_name_suitable(name) and is_function(python_object):
            yield name, python_object
