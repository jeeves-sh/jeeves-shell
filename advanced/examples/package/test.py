import typer

test = typer.Typer()


@test.command()
def unit():
    """Run unit tests."""


@test.command()
def integration():
    """Run integration tests."""
