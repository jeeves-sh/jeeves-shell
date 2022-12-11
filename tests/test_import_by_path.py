from pathlib import Path

import pytest

from jeeves_shell.import_by_path import import_by_path


def test_empty_module_name():
    module_path = Path(__file__).parent / 'jeeves_files/single.py'
    imported_module = import_by_path(module_path)
    assert imported_module.__name__ == str(module_path)


def test_nonsense():
    with pytest.raises(RuntimeError):
        import_by_path(Path('non_existent'), 'non_existing_module')
