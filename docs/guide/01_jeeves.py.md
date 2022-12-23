---
title: jeeves.py file
position: 1
simple: guide/examples/simple.py
---

Create a `jeeves.py` file with the following contents in an arbitrary directory.

{{ code(page.meta.simple, language='python', title='jeeves.py') }}

Residing in that directory, run `j`. Here's what you should see:

{{ j(page.meta.simple, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

Every function in `jeeves.py` is now exposed as a subcommand of `j` and gets auto documentation. Indeed:

{{ j(page.meta.simple, args=['hello', '--help']) }}

Let's try it out!

{{ j(page.meta.simple, args=['hello', '--style', 'british', 'Berty']) }}

## Behind the scenes

[![Typer](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com)

…every function in `jeeves.py` is converted into a [Typer](https://typer.tiangolo.com) [command](https://typer.tiangolo.com/tutorial/commands/), just as if you did:

```python
from typer import Typer

app = Typer()

@app.command()
def hello(
    # ...
):
    """Greet the user."""
    ...

if __name__ == '__main__':
    app()
```

The boilerplate is thus significantly reduced.

Meanwhile, you still **can** use most Typer features. In our particular example, we relied upon Typer

* to provide an option and an argument for our command,
* to validate & convert raw user's input into an `Enum`,
* and to automatically generate a `--help` message.
