---
title: New DI library for Jeeves
status: draft
---

## Decision

Implementation of such a library does not currently seem possible because of technical difficulties with the syntax we originally wanted.

## Context

In order to make the syntax as concise and as similar to `GNU Make` as possible, the idea is to use `Depends()` syntax from FastAPI.

```python
from pathlib import Path
from dino import Depends
import sh


def python_packages() -> list[Path]:
    return [child for child in Path.cwd().itderdir() if (child / '__init__.py').is_file()]


def lint(packages: list[Path] = Depends(python_packages)):
    sh.flakeheaven.lint(*packages)
```

### How to implement this?

`Depends` must transparently output the `list[Path]` value which the consuming code expects to see.

* `Depends.__init__()` won't work: it must output an instance of `Depends`;
* `Depends.__new__()` isn't going to be helpful either: it will be evaluated on module level which essentially means
  * we're modifying a global variable,
  * which is in addition a function's default parameter;
* 🤔 `Depends.__get__` might be a way, but…

### Where to store the resolved value?

* Inside the `Depends` instance: we again get a global mutable state; that's wrong: we should get another invocation of `python_packages` every time `lint` is called;
* In silently global scope like `contextvars`: the problem is the same;
* In `Typer` app context: would be curious, but the hell how to gain access there if not to write `ctx: Context` in **every** function?
  * This means the implementation is tied to `Typer`… but who cares. 
