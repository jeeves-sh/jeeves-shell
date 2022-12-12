import itertools
import sys
from pathlib import Path
from typing import List, Iterable

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


def _construct_mypy_flags() -> Iterable[str]:
    """
    Mypy configuration.

    - http://bit.ly/2zEl9WI
    - Source: wemake-python-package.
    """
    yield '--disallow-redefinition'
    yield '--check-untyped-defs'
    yield '--disallow-any-explicit'
    yield '--disallow-any-generics'
    yield '--disallow-untyped-calls'
    yield '--ignore-missing-imports'
    yield '--implicit-reexport'
    yield '--local-partial-types'
    yield '--strict-optional'
    yield '--strict-equality'
    yield '--no-implicit-optional'
    yield '--warn-no-return'
    yield '--warn-unused-ignores'
    yield '--warn-redundant-casts'
    yield '--warn-unused-configs'
    yield '--warn-unreachable'


def _construct_flake8_args() -> Iterable[str]:
    """
    Base flake8 configuration.

    https://flake8.pycqa.org/en/latest/user/configuration.html
    Source: wemake-python-styleguide.
    """
    yield '--format', 'wemake'

    yield '--show-source'
    yield '--doctests'

    # Darglint: https://github.com/terrencepreilly/darglint
    yield '--strictness', 'long'
    yield '--docstring-style', 'numpy'

    # Plugins
    yield '--max-complexity', 6
    yield '--max-line-length', 80

    yield '--i-control-code'


def lint():
    """Lint code."""
    directories = _python_directories()

    run(
        'mypy',
        *directories,
        *_construct_mypy_flags(),
        **kwargs,
    )

    run(
        'flakeheaven', 'lint',
        *directories,
        *itertools.chain(
            _construct_flake8_args(),
        ),
        **kwargs,
    )

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
