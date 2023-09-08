from collections import defaultdict

import pytest
from jeeves_shell import Jeeves
from jeeves_shell.discover import construct_root_app
from jeeves_shell.errors import PluginConflict


def test_fallback():
    assert isinstance(construct_root_app(defaultdict(list)), Jeeves)


def test_conflict():
    with pytest.raises(PluginConflict) as error_info:
        construct_root_app(plugins_by_mount_point=defaultdict(
            list,
            __root__=[Jeeves(), Jeeves()],
        ))

    assert 'Plugins' in str(error_info.value)  # noqa: WPS441
