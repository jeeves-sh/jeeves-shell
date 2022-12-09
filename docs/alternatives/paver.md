---
title: Evaluate Paver
number: 4
status: rejected
---

## Context

[Paver](https://pythonhosted.org/Paver/) is a project with goals very similar to mine: it proposes to replace GNU Make with Python functions. I have written a little example in it. 

```python
from paver.tasks import task, cmdopts


@task
@cmdopts([
    ('key=', 'k', 'Key of the task')
])
def select(options):
    """Select a Jira task to manipulate."""
    print(options)
```

## Decision

Unfortunately, I do not see a way to use Paver.

1. It apparently does not support command line arguments.

```shell
$ paver select RM3-588
---> pavement.select
Namespace(dry_run=None, pavement_file='pavement.py', select=Bunch())
Build failed: Unknown task: RM3-588
```

2. When you manage to propagate the command line option into the function, you cannot access it as a function argument.

```shell
$ paver select -k RM3-588
---> pavement.select
Namespace(dry_run=None, pavement_file='pavement.py', select=Bunch(key='RM3-588'))
```

So I have to dive into the `Namespace` object and then to `select` member inside it... Seriously?

3. Type annotations are not used to describe options or dependencies. I would think that a principle similar to FastAPI would be very helpful here. In particular:
    - By default, every argument is considered a command line argument;
    - Using a special `Depends()` object you can declare it as a dependency.

  And that's it. No additional decorators needed.

## Consequences

`paver` is great but it must be reworked too heavily, I am afraid, to be useful.
