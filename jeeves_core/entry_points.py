import sys

if sys.version_info < (3, 10):    # pragma: no cover
    from importlib_metadata import entry_points
else:    # pragma: no cover
    from importlib.metadata import entry_points
