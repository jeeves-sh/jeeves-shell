import sys
from pathlib import Path


def import_by_path(path: Path):
    """Import Jeeves by path."""
    string_path = str(path)
    sys.path.insert(0, string_path)

    import jeeves   # noqa: WPS433

    sys.path.remove(string_path)

    return jeeves
