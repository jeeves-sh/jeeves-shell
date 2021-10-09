---
title: Choose commands structure
number: 3
---

## Context

At {{ link('decisions/dependency-injection.md') }} we have been discussing DI frameworks, but that was probably a bit premature. The more appropriate question would perhaps sound like:

> How should the application be structured overall?

Let us discuss a few options.

### Simplest case

If I were writing just a hard-coded tool for my most often used commands, with no concern about reusability, I would certainly use {{ link('typer') }}. How to structure various Typer commands? Something like this might have been appropriate.

=== "app.py"
    ```python
    import typer

    app = typer.Typer()
    ```

=== "move.py"
    ```python
    from jeeves.app import app
    from jeeves.jira import create_jira

    @app.command
    def move(key: str, project: str):
        issue = create_jira().issue(key)
        ...
    ```

In the simplest case, I would use Typer command functions as they are, and not use any dependency injection framework at all.

### Do we even need a DI here?

It is, I must confess, a bit annoying to have to constantly call `create_jira()` in every Jira-related task. I would prefer to just add a `jira` argument - and expect this argument filled in for me.

Something like this in `inject`:

```python
@app.command
def move(key: str, to: str, project: str, jira: None = Depends(jira))
    ...
```

Just like in FastAPI. Unfortunately, Typer, in contrast to FastAPI, does not support such a model. Can we fix that?

---

I tried to fix that using `inject` but failed. The argument to the function is considered by Typer to be an argument, or an option, which it is trying to interpret for the CLI.

Perhaps something akin to `functools.partial` can help but I presently do not see a way to apply it.

