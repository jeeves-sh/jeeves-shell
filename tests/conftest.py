from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def jeeves_files() -> Path:
    return Path(__file__).parent / 'jeeves_files'
