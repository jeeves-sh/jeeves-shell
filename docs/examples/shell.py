import typer
from sh import grep, pip


def list_flake8_plugins():
    """List installed plugins for Flake8."""
    typer.echo(
        grep( # (1)!
            'flake8-',
            _in=pip.freeze(),
        ),
    )
