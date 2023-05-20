---
title: "Start Jeeves project"
hide:
  - toc

$id: jeeves-alternatives
table:columns:
  - table:self
  - language
  - last-release
  - command-name
  - $id: cli-commands
    rdfs:label: Engine for CLI commands
  - $id: plugins
    rdfs:label: Plugin support
  - $id: dependencies
    rdfs:label: Dependencies system
  - notes

table:rows:
  - rdfs:label: GNU Make
    language: make + bash
    dependencies: yes
    plugins: no
    command-name: make

  - schema:url: https://pythonhosted.org/Paver
    rdfs:label: Paver
    language: python
    dependencies: yes
    plugins: no
    last-release: 2017-12-31
    cli-commands: Own syntax with decorators
    command-name: paver
    notes: Envelops setuptools and distutils, conflicting with Poetry.

  - schema:url: https://www.pyinvoke.org
    rdfs:label: invoke
    language: python
    last-release: 2023-05-16
    dependencies: yes
    cli-commands: "Own syntax with @task decorators"
    command-name: invoke
    notes: Has tools to define CLI commands (without type hints support though) and calling commands. Subjectively — too much is stuffed into one single package.

  - schema:url: https://scons.org
    rdfs:label: scons
    language: python
    last-release: 2023-03-21
    dependencies: yes
    cli-commands: No way to define custom commands
    command-name: scons

  - schema:url: https://github.com/basherpm/basher
    rdfs:label: basher
    language: bash

  - schema:url: https://github.com/python-manage/manage
    language: python
    last-release: 2021-02-07
    rdfs:label: manage
    dependencies: no
    cli-commands:
      $id: click
      schema:url: https://click.palletsprojects.com
    plugins: no
    command-name: manage

  - schema:url: https://github.com/jeeves-sh/jeeves-shell
    rdfs:label: jeeves
    language: python
    last-release: 2023-05-19
    dependencies: no
    cli-commands:
      schema:url: https://tiangolo.com/typer
      rdfs:label: typer
    plugins: yes
    command-name: j
---

# :rocket: Start Jeeves project

## Context

There are a few alternatives available, none of which I 100% like. 

{# todo: describe google Fire as alternative #}

{{ render("jeeves-alternatives") }}

## Decision

Create a new project — the documentation for which you are reading ☺
