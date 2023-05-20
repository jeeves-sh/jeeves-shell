import typer

lint = typer.Typer(no_args_is_help=True)
test = typer.Typer(no_args_is_help=True)


@lint.command(name='mypy')
def _mypy():
    """Run mypy."""


@lint.command(name='flake8')
def _flake8():
    """Run flake8."""
    print(_flake8.__doc__)


@test.command(name='unit')
def _unit():
    """Run unit tests."""


@test.command(name='integration')
def _integration():
    """Run integration tests."""
