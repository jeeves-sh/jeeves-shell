---
title: Register a new command
number: 7
status: accepted
---

## Context

`jeeves` is planned to be a tool that is easy to integrate into any existing project. Somehow, creating a new `jeeves` command must be no harder than writing a new `Makefile` goal.

Suppose we're writing a new project and for it we want to introduce a new command:

```python
def acme(foo: str):
    ...
```

and we want to make it available as `j acme buzinga`. How do we do that?

### Look for all Python functions in a file with a special name

This is very similar to what `GNU Make` does - just look for `jeeves.py` in the current directory.

We can scan such a file for every callable and register all such callables as Typer commands.

# Decision

After some thought, I came up with a very simple approach. I am defining commands using `setuptools` entry points:

```toml
[tool.poetry.plugins.jeeves]
create = "jeeves_jira:create"
clone = "jeeves_jira:clone"
fork = "jeeves_jira:fork"
list = "jeeves_jira:list_issues"
select = "jeeves_jira:select"
link = "jeeves_jira:link"
auth = "jeeves_jira:auth"
update = "jeeves_jira:update"
roadmap = "jeeves_jira:roadmap"
heatmap = "jeeves_jira:heatmap"
status = "jeeves_jira:status"
comment = "jeeves_jira:comment"
lint = "jeeves_jira:lint"
evaluate = "jeeves_jira:evaluate"
```

Easily enough, this registers commands:


