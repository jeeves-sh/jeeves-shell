from pathlib import Path

from jeeves_core.process_modules import parse_module

modules = Path(__file__).parent / 'modules'


def test_typing_optional():
    assert not list(parse_module(modules / 'typing_optional.py'))


def test_uppercase():
    assert not list(parse_module(modules / 'uppercase.py'))
