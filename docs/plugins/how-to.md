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
super_plugin = "jeeves_super_plugin:app"
```

* Create your Typer instance:

```python title="jeeves_super_plugin/__init__.py"
import typer

app = typer.Typer()

@app.command()
def hi(name: str):
    """Greet the user."""

@app.command()
def bye():
    """Bid farewell."""
```

* `poetry install`
* `j`

You should see:

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', '--help']) }}
