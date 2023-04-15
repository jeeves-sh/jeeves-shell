import copy
import sys
from pathlib import Path

import pytest

from jeeves_shell.import_by_path import import_by_path


@pytest.fixture(autouse=True)
def sys_path():
    # Remove the project directory
    sys.path.remove(str(Path(__file__).parent.parent))

    original_path = copy.copy(sys.path)

    yield
    sys.path = original_path


def test_nonsense():
    with pytest.raises(ImportError):
        import_by_path(Path('non_existent'))
