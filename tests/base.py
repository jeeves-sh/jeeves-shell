import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def environment_from_jeeves_file(path: Path):
    with tempfile.TemporaryDirectory() as raw_directory:
        directory = Path(raw_directory)
        (directory / 'jeeves.py').write_text(
            path.read_text(),
        )
        yield directory
