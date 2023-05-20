---
title: Why plugins?
---

# :fontawesome-solid-plug: Why plugins?

{# todo: Share these use cases with the home page of the program #}

=== ":material-account-tie: For a company"

    You have multiple projects/repositories, and you have very similar or identical deployment, testing, and linting rules.

=== ":person_curly_hair: For an individual"

    You have multiple open source repositories, and you would like to maintain the same standards for each and avoid tedious and repeated setup tasks for them.

## What is a plugin?

`jeeves` plugin is an installable Python package which declares `jeeves` commands. You do not need to copy `jeeves.py` from one project to another; you can define a plugin with reusable commands, and install that plugin as dev dependency. 

## Plugin example: `jeeves-yeti-pyproject`

This is a custom plugin created to manage my own open source projects.

* It brings `pytest` and a few plugins for it as dependencies; `j test` command tests Python code exactly as I like it to be tested
* It also has a number of linters and `flake8` plugins, `j lint` uses a shared configuration for those
* I no longer have to install all those dev dependencies for every new project and to copy-paste their configuration files
* If one plugin conflicts with another, I resolve the issue only once and then just `poetry update` all my projects

```shell
poetry add --group dev jeeves-yeti-pyproject
```

## Top level documentation

{{ j(None) }}
