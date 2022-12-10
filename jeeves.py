import sys

from plumbum.cmd import poetry


run = poetry['run']


def lint():
    """Lint the project."""
    directories = ['jeeves_core', 'tests']
    kwargs = {'stdout': sys.stdout, 'stderr': sys.stderr}

    run('mypy', *directories, **kwargs)
    run('flakeheaven', 'lint', *directories, **kwargs)

    poetry('check', **kwargs)
    run('pip', 'check', **kwargs)
    run('safety', 'check', '--full-report', **kwargs)


def unit():
    """Unit test."""
    run('pytest')
