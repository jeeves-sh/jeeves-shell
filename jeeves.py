import sys

from plumbum.cmd import poetry, isort

run = poetry['run']


kwargs = {'stdout': sys.stdout, 'stderr': sys.stderr}


def lint():
    """Lint the project."""
    directories = ['jeeves_core', 'tests']

    run('mypy', *directories, **kwargs)
    run('flakeheaven', 'lint', *directories, **kwargs)

    poetry('check', **kwargs)

    # We do not write anything to stdout here
    run('pip', 'check', stderr=sys.stderr)


def safety():
    """Check installed Python packages for vulnerabilities."""
    run('safety', 'check', '--full-report', **kwargs)


def test():
    """Unit test."""
    run('pytest', **kwargs)


def fmt():
    """Auto format code."""
    isort('jeeves_core', 'tests', **kwargs)
