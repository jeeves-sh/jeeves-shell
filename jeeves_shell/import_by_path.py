import sys
from pathlib import Path


def import_by_path(path: Path):
    """Import Jeeves by path."""
    sys.path.insert(0, str(path))

    import jeeves   # noqa: WPS433

    return jeeves
