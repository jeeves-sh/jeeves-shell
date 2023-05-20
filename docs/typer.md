---
title: Typer
hello_with_typer: examples/hello-typer.py
hide:
  - toc
---

Behind the scenes, Jeeves relies upon [Typer](https://typer.tiangolo.com).

{# fixme: Typer logo is hotlinked, vendor it instead #}

[![Typer](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com)

Every function in `jeeves.py` is converted into a Typer [command](https://typer.tiangolo.com/tutorial/commands/). Just as if you did:

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

## Example: Use Typer features directly

{# todo: Implement side by side macro, and use it for all code and jeeves examples #}

{{ code(page.meta.hello_with_typer, language='python', title='jeeves.py') }}

⇒

{{ j(page.meta.hello_with_typer, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', '--help']) }}

## Example: Typer Validation

{{ j(page.meta.hello_with_typer, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', '--style', 'de']) }}
