import sys
from pathlib import Path
from typing import List

import more_itertools
from plumbum.cmd import poetry, isort

run = poetry['run']
kwargs = {'stdout': sys.stdout, 'stderr': sys.stderr}


def _python_directories() -> List[Path]:
    return [
        sub_directory
        for sub_directory in Path.cwd().iterdir()
        if sub_directory.is_dir()
        and more_itertools.first_true(
            sub_directory.glob('*.py'),
        )
    ]


def lint():
    """Lint code."""
    directories = _python_directories()

    run('mypy', *directories, **kwargs)
    run('flakeheaven', 'lint', *directories, **kwargs)

    poetry('check', **kwargs)

    # We do not write anything to stdout here
    run('pip', 'check', stderr=sys.stderr)


def safety():
    """Check installed Python packages for vulnerabilities."""
    run('safety', 'check', '--full-report', **kwargs)


def test():
    """Unit test code."""
    run('pytest', **kwargs)


def fmt():
    """Auto format code."""
    isort(*_python_directories(), **kwargs)
