import rich


def hi(name: str):
    """Greet the user."""
    rich.print(f'Hello [red]{name}[/red]!')
