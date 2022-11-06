import string
import sys
import types
from importlib import util as importlib_util
from pathlib import Path
from typing import Iterable, List, Tuple

import more_itertools

from jeeves_core.errors import NoJeevesFile

ParsedModule = Iterable[Tuple[List[str], types.FunctionType]]


def import_module_by_path(path: Path):
    """
    Import module knowing its filesystem path.

    Source: https://stackoverflow.com/a/67692/1245471
    """
    module_name = _construct_module_name(path)
    spec = importlib_util.spec_from_file_location(module_name, path)

    if spec is None:
        raise ValueError('Spec is none. This is an unknown error. Panicking!')

    imported_module = importlib_util.module_from_spec(spec)
    sys.modules[module_name] = imported_module

    try:
        spec.loader.exec_module(imported_module)   # type: ignore
    except FileNotFoundError as err:
        raise NoJeevesFile(path=path) from err

    return imported_module


def _construct_module_name(path: Path):
    formatted_path = str(path).strip('/').replace('.', '_')
    return formatted_path.replace('/', '.')


def _is_function(python_object) -> bool:
    return isinstance(python_object, types.FunctionType)


def _is_name_suitable(name: str):
    first_character = more_itertools.first(name)
    return first_character not in f'{string.ascii_uppercase}_'


def parse_module(path: Path) -> ParsedModule:
    """Load and parse a module."""
    jeeves_module = import_module_by_path(path)

    for name, python_object in vars(jeeves_module).items():  # noqa: WPS421
        if _is_name_suitable(name) and _is_function(python_object):
            yield name.split('__'), python_object
