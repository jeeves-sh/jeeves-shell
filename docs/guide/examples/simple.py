from enum import Enum

from typer import Option


class GreetingStyle(Enum):
    """Style of a greeting."""

    BRITISH = 'british'
    COCKNEY = 'cockney'
    PUNK = 'punk'


def hello(
    name: str,
    style: GreetingStyle = Option(GreetingStyle.BRITISH),
):
    """Greet the user."""
    print({
        GreetingStyle.BRITISH: f'How do you do {name}!',
        GreetingStyle.COCKNEY: f'Oi {name}!',
        GreetingStyle.PUNK: f'Hoi {name}!',
    }[style])
