---
title: Install
position: 0
empty: guide/examples/empty.py
---

The core package of `jeeves` is named [`jeeves-shell`](https://pypi.org/project/jeeves-shell).

```shell
pip install jeeves-shell
```

If you are working on a [Poetry](https://pypoetry.org)-based Python project then probably this will be appropriate:

```shell
poetry add --group dev jeeves-shell
```

A new shell command named `j` is now available. Run it:

{{ j(page.meta.empty, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

it doesn't do much yet, as you can see. Let's create some actions for it.