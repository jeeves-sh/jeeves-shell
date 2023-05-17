---
title: Shell Commands
sample: examples/shell.py
hide:
  - toc
---

# :material-bash: Shell Commands

`make` is an orchestrator — it doesn't do much work itself, it calls other commands which do the work. That's what we recommend doing with `jeeves` as well. Among numerous ways to call other programs from Python we recommend a library named, quite concisely, `sh`: [:material-github: amoffat/sh](https://github.com/amoffat/sh).

!!! info "Alternatives"
    See [shell cobminators](../decisions/shell-combinators/) to check out other available tools.

{# fixme: rendering `shell-combinators` will render the table inline — not the link to the page. #}

[![](https://github.com/amoffat/sh/blob/db126f2eec64b8c0b26e557908c296cd159f900a/images/logo-230.png?raw=true)](https://github.com/amoffat/sh)

{# fixme: "jeeeves-shell[all] does not install `sh` at this point" #}

By default, it is bundled as a dependency for `jeeves`, and here is a simple example.

{{ code(page.meta.sample, language='python', title='jeeves.py', annotations=["Equivalent to: `pip freeze | grep flake8-`"]) }}

Shall we execute it?

{{ j(page.meta.sample, args=['list-flake8-plugins']) }}

`sh` allows to call shell commands with conciseness and readability of Pythonic syntax. See [:book: the package docs](http://amoffat.github.io/sh) for more detail.

{# todo: Document `rich` as terminal UI library with examples #}
