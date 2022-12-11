import importlib.util
import sys
from pathlib import Path
from typing import Optional


def import_by_path(path: Path, module_name: Optional[str] = None):
    if module_name is None:
        module_name = str(path)

    spec = importlib.util.spec_from_file_location(
        name=module_name,
        location=path,
    )

    if spec is None:
        raise RuntimeError(f'Unexpected error: cannot build spec from {path}')

    imported_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = imported_module
    spec.loader.exec_module(imported_module)   # type: ignore
    return imported_module
