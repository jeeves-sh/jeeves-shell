def _format_greeting(name: str) -> str:
    return f'Hello {name}!'


def hi(name: str):
    """Greet the user."""
    print(_format_greeting(name))
