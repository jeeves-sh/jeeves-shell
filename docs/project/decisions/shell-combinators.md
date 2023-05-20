---
$id: shell-combinators
title: Use sh for shell combinators
hide:
  - toc

schema:wasDerivedFrom: https://lab.abilian.com/Tech/Python/Shell%20in%20Python/

table:columns:
  - table:self
  - $id: import-hook
    rdfs:comment: "`from some_library import ls, ssh, aws` is extremely convenient."
  - $id: native-kwargs
    rdfs:comment: Convert Python keyword arguments to shell --arguments.
  - $id: minimalism
    title: Minimalism Score
  - $id: return-code-exceptions
    rdfs:title: Return code exceptions
    rdfs:comment: Separate exception class for each return code.
  - $id: partial-commands
    rdfs:comment: Concise functools.partial() support for shell commands.
  - $id: subcommands
    rdfs:comment: Support to easily compose subcommands like `git fetch`.
  - $id: execution-contexts
    title: Execution Context
    rdfs:comment: Execution context allows to concisely pipe output for all commands in a group to the same stream, for example, without providing the same set of options to each command.
  - notes

table:rows:
  - schema:url: https://github.com/tomerfiliba/plumbum
    rdfs:label: tomerfiliba/plumbum
    import-hook: yes
    native-kwargs: no
    partial-commands: yes
    separate-exception-per-return-code: no
    subcommands: yes
    minimalism: 1
    execution-contexts: no
    notes: Does shell coloring and building of CLI applications

  - schema:url: https://github.com/amoffat/sh
    rdfs:label: amoffat/sh
    import-hook: yes
    minimalism: 3
    native-kwargs: yes
    separate-exception-per-return-code: yes
    partial-commands: yes
    subcommands: yes
    execution-contexts: yes

  - schema:url: https://github.com/aeroxis/sultan
    rdfs:label: aeroxis/sultan
    import-hook: no

  - schema:url: https://github.com/elcaminoreal/seashore
    rdfs:label: elcaminoreal/seashore
    import-hook: no

  - schema:url: https://github.com/dgilland/shelmet
    rdfs:label: dgilland/shelmet
    import-hook: no
---

# Use `sh` for shell combinators

{# todo: mkdocs-iolanta must render table in the page body itself #}
{# todo: mark sh in green #}
{# todo: import last release date and stars count from GitHub #}

{{ render("shell-combinators") }}
