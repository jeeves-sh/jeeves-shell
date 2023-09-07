from jeeves_shell.discover import list_installed_plugins


def test_plugins():
    assert isinstance(list_installed_plugins(), dict)
