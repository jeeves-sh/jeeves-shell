from typer import Typer


class Jeeves(Typer):
    """Support Jeeves-specific options."""

    debug: bool = False
