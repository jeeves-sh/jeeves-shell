import itertools
import sys
from pathlib import Path
from typing import List, Iterable

import more_itertools
from plumbum.cmd import poetry, isort

run = poetry['run']
kwargs = {'stdout': sys.stdout, 'stderr': sys.stderr}

LINE_LENGTH = 80


def _directories_with_a_file_in_them(pattern: str) -> List[Path]:
    return [
        sub_directory
        for sub_directory in Path.cwd().iterdir()
        if sub_directory.is_dir()
           and more_itertools.first_true(
            sub_directory.glob(pattern),
        )
    ]

def _python_directories() -> List[Path]:
    return _directories_with_a_file_in_them('*.py')


def _python_packages() -> List[Path]:
    return _directories_with_a_file_in_them('__init__.py')


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
    yield '--max-line-length', LINE_LENGTH

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


def _construct_pytest_args() -> Iterable[str]:
    yield '--strict-markers'
    yield '--strict-config'
    yield '--tb=short'
    yield '--doctest-modules'
    yield '--cov={}'.format(
        ','.join(
            map(str, _python_packages()),
        )
    )
    yield '--cov-report=term:skip-covered'
    yield '--cov-report=html'
    yield '--cov-report=xml'
    yield '--cov-branch'
    yield '--cov-fail-under=100'


def test():
    """Unit test code."""
    run('pytest', *_construct_pytest_args(), **kwargs)


def _construct_isort_args() -> Iterable[str]:
    """
    Isort configuration.

    https://github.com/timothycrosley/isort/wiki/isort-Settings
    See https://github.com/timothycrosley/isort#multi-line-output-modes

    Source: wemake-python-styleguide.
    """
    yield '--trailing-comma'
    yield '--use-parentheses'
    yield '--multi-line', 'VERTICAL_HANGING_INDENT'
    yield '--line-length', LINE_LENGTH


def fmt():
    """Auto format code."""
    isort(
        *_python_directories(),
        *_construct_isort_args(),
        **kwargs,
    )
