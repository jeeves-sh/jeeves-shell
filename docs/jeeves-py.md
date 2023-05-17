---
title: jeeves.py
hello: examples/hello.py
hide:
  - toc
---

# :simple-python: jeeves.py

{# todo: draw a picture where Makefile is crossed away and jeeves.py is shown instead #}

While GNU make goals are specified in a file named `Makefile`, Jeeves looks for commands in a file named `jeeves.py` in current directory.

## Commands

{# todo: describe google Fire as alternative #}

Every Python function in `jeeves.py` is converted into a command.

* Docstrings are used as command documentation,
* Command arguments are configured by arguments of respective functions (and their type hints!)

Let's recall the Hello World script we [:arrow_backward: had referenced before](../#get-started):

{{ code(page.meta.hello, language='python', title='jeeves.py') }}

Check out how automated documentation works:

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

Or, for the given command:

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', '--help']) }}


## Behind the scenes: Typer

{# fixme: Typer logo is hotlinked, vendor it instead #}

[![Typer](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com)

What Jeeves does here is converting every function in `jeeves.py` into a [Typer](https://typer.tiangolo.com) [command](https://typer.tiangolo.com/tutorial/commands/). Just as if you did:

```python
from typer import Typer

app = Typer()

@app.command()
def hi(name: str):
    """…"""

if __name__ == '__main__':
    app()
```

* That's one way how Jeeves reduces the boilerplate;
* The other way is to expose all those commands via the `j` shortcut.

Nonetheless, you still **can** use most Typer features, such as:

* define `typer.Argument`'s and `typer.Option`'s for your commands,
* validate user input using type hints,
* and much more.
