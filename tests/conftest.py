import random
import string
import sys
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def wipe_jeeves_module_from_cache():
    try:
        return sys.modules.__delitem__('jeeves')   # noqa: WPS609
    except KeyError:
        return False


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
