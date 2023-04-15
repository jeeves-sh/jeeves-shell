from typer import Typer

build = Typer()


@build.command(name='all')
def _build_all():
    """Build all."""


@build.command(name='python')
def _python():
    """Build Python."""


@build.command(name='rust')
def _rust():
    """Build Rust."""


def lint():
    """Lint."""
