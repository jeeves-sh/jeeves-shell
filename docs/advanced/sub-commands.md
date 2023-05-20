---
title: Sub-commands
subcommands: advanced/examples/sub-commands.py
---

# :material-submarine: Sub-commands

If `j` exports too many commands, it might make sense to group them into subcommands. This is done by defining [Typer](../typer/) applications in [jeeves.py](../jeeves-py).

{{ code(page.meta.subcommands, language='python', title='jeeves.py') }}

## Top level documentation

{{ j(page.meta.subcommands, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

!!! info "Hidden commands"
    Note that we have to use underscore here, otherwise `def mypy` and other functions will be bound to the top-level `j` command. See {{ render("hidden-functions") }} for details. See {{ render("jeeves-package") }} to see how to avoid that.

{# todo: Reference to an mkdocs page with render() does not generate a link. #}

## Sub-command level documentation

{{ j(page.meta.subcommands, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['lint']) }}

## Nested command

{{ j(page.meta.subcommands, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['lint', 'flake8']) }}
