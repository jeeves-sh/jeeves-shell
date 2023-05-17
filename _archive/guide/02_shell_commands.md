---
title: Shell Commands
sample: guide/examples/shell.py
---

In a `Makefile`, the body of work is done by calling other commands: `python`, `docker`, `aws`, … We can certainly do the same with [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run) from Python code, but that is rather suboptimal.

We recommend using a Pythonic shell combinators library known as `sh`.

[![](https://raw.githubusercontent.com/amoffat/sh/master/logo-230.png)](https://github.com/amoffat/sh).

It is not bundled with `jeeves-shell` but can be separately installed:

```shell
poetry add --group dev sh
```

Here is a simple example.

{{ code(page.meta.sample, language='python', title='jeeves.py', annotations=["Equivalent to: `pip freeze | grep flake8-`"]) }}

Shall we execute it?

{{ j(page.meta.sample, args=['list-flake8-plugins']) }}

`sh` allows to call shell commands with conciseness and readability of Pythonic syntax. Read more [in the package docs](http://amoffat.github.io/sh). Seriously, you will never want to write a Bash script again.
