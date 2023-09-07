---
title: Your new jeeves-super-plugin
hello: examples/hello.py
---

# :fontawesome-solid-plug-circle-plus: Your new `jeeves-super-plugin`

* Create a Python 3.10+ virtual env for your new plugin project
* `pip install -U pip poetry`
* `poetry init`
* `poetry add jeeves-shell --extras=all`
* Write into `pyproject.toml`:

```toml
[tool.poetry.plugins.jeeves]
super-plugin = "jeeves_super_plugin:app"
```

* Create your Typer instance:

```python title="jeeves_super_plugin/__init__.py"
import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def hi(name: str):
    """Greet the user."""

@app.command()
def bye():
    """Bid farewell."""
```

* `poetry install`
* `j super-plugin`

You should see `hi` and `bye` as available commands.

## Special plugin name: `__root__`

```toml
[tool.poetry.plugins.jeeves]
__root__ = "jeeves_super_plugin:app"
```

This will mean that your plugin _replaces_ the default root Jeeves app, and your commands will be available as

* `j hi` instead of `j super-plugin hi`
* `j bye` instead of `j super-plugin bye`.

This is useful for plugins like `jeeves-yeti-pyproject`, to make the commands you very often use, like `lint`, faster to type.
