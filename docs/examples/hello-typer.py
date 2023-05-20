from enum import Enum, auto

import typer


class GreetingStyle(Enum):
    """Style of the greeting."""

    ENGLISH = 'en'
    ITALIAN = 'it'


def hi(
    name: str = typer.Argument(
        ...,
        help='Name of the one we would like to greet.',
        envvar='NAME_TO_GREET',
    ),
    style: GreetingStyle = typer.Option(
        GreetingStyle.ENGLISH,
        help='Style of the greeting.',
    ),
):
    """Greet the user."""
    greeting = {
        GreetingStyle.ENGLISH: 'Hello',
        GreetingStyle.ITALIAN: 'Buongiorno',
    }[style]

    typer.echo(f'{greeting} {name}!')
