---
title: Pretty output with rich
hello_rich: examples/hello-rich.py
hide:
  - toc
---

{# todo: Document alternatives to rich such as colorama, maybe reuse my old table from yeti.sh #}

# :rainbow: Pretty output with `rich`

[:material-github: textualize/rich](https://github.com/textualize/rich) is a modern library for formatting shell output that we recommend using with `jeeves`.

!!! success "Installation"
    It will be installed as a dependency of `jeeves-shell`.

![Rich Logo](https://github.com/textualize/rich/raw/master/imgs/logo.svg)

{# todo: Vendor Rich logo instead of hot linking it #}

## Rich example

{{ code(page.meta.hello_rich, language='python', title='jeeves.py') }}

⇒

{{ j(page.meta.hello_rich, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', 'John']) }}

(Well, this output does not actually convey the effect because `rich` outputs shell markup that's ignored when converting to HTML… Just trust me — it <span style="color: red">will be red</span> in the terminal, I assure you!)
