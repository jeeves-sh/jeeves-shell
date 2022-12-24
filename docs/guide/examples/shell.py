import typer
from sh import grep, pip


def list_flake8_plugins():
    """List installed plugins for Flake8."""
    typer.echo(
        grep(         # (1)!
            pip.freeze(),
            'flake8-',
        ).stdout,
    )
