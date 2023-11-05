import typer

lint = typer.Typer(no_args_is_help=True)


@lint.command()
def mypy():
    """Run mypy."""


@lint.command()
def flake8():
    """Run flake8."""
    print(flake8.__doc__)
