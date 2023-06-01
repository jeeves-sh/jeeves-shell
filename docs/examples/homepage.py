import rich
import sh


def hi():
    """Hello world."""
    user_name = sh.whoami()
    machine = sh.uname('-a')

    rich.print(f'Hello [b]{user_name}[/b]!')
    rich.print(f'This code is running on: [b]{machine}[/b].')
