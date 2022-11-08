from jeeves_core.discover import construct_app


def app() -> None:
    """Construct and return Typer app."""
    typer_app = construct_app()
    return typer_app()


if __name__ == '__main__':
    app()
