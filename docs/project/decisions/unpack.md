---
title: Unpack a dataclass or TypedDict → Typer command arguments
---

# `Unpack[]` a dataclass or TypedDict → Typer command arguments

## Context

When designing command-line interfaces with Typer, we often encounter scenarios where multiple commands share similar or identical sets of arguments. To avoid redundancy and improve code maintainability, we are considering using the Unpack[] type hint, which would allow us to unpack fields from a `dataclass` or `TypedDict` directly into command arguments.

!!! info "Votum Separatum: Callbacks"
  Functions that accept multiple common parameters are often united under one Typer sub-application. This allows for the use of callback functions and Typer context to handle shared parameters.

`typing.Unpack` was introduced in [PEP 646 Variadic Generics](https://peps.python.org/pep-0646/) and then further extended in [PEP 692 Using TypedDict for more precise **kwargs typing](https://peps.python.org/pep-0692/#using-unpack-with-types-other-than-typeddict). We can make use of that.

## Decision

We will use the `Unpack[]` type hint to unpack fields from dataclasses or TypedDicts and map them directly to Typer command arguments.

Example:

```python
from typing import Unpack
from dataclasses import dataclass
from typer import Typer

@dataclass
class Person:
    first_name: str
    last_name: str

app = Typer()
    
@app.command()
def process_person(person: Unpack[Person]):
    ...
```

This approach allows users to provide each attribute of `Person` as a separate argument: `command --first-name John --last-name Doe`.


## Consequences

We will need to implement this for Typer mainstream code base.

* Source code: [`def get_params_from_function`](https://github.com/tiangolo/typer/blob/master/typer/utils.py#L108) function,
* which needs to be refactored a bit and generalized,
* and expanded to support `Unpack`.
* There is a [GitHub issue](https://github.com/tiangolo/typer/issues/154) which might contain relevant research.
