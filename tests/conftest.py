import random
import string
from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def jeeves_files() -> Path:
    return Path(__file__).parent.parent / 'test_samples'


@pytest.fixture()
def random_string() -> str:
    return ''.join(
        random.sample(
            string.ascii_lowercase,
            10,
        ),
    )
