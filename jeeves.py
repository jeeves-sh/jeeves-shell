from sh import mkdocs


def serve():
    """Serve documentation site."""
    mkdocs(
        'serve',
        '-a',
        'localhost:8211',
        _fg=True,
    )
