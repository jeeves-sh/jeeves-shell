# Jeeves Shell

[![Build Status](https://github.com/jeeves-sh/jeeves-shell/workflows/test/badge.svg?branch=master&event=push)](https://github.com/jeeves-sh/jeeves-shell/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/jeeves-sh/jeeves-shell/branch/master/graph/badge.svg)](https://codecov.io/gh/jeeves-sh/jeeves-shell)
[![Python Version](https://img.shields.io/pypi/pyversions/jeeves-shell.svg)](https://pypi.org/project/jeeves-shell/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

![](docs/assets/cover.png)

A Pythonic replacement for GNU Make, with re-usability and modularity added as a bonus.

Jeeves transforms your shell experience by enabling you to create custom Python-based shell commands to manage and automate your development workflows.

## Features

- **Custom Shell Commands**: Construct commands to build, compile, lint, format, test, deploy, and propel your projects forward.
- **Python-Powered**: Use Python for readable and maintainable workflows.
- **Rich Integrations**: Stylish command output with `rich` and `sh`.
- **Plugin System**: Share your setup across projects.

## Quick Start

Install with pip:

    pip install 'jeeves-shell[all]'

Or with poetry:

    poetry add --group dev --extras=all jeeves-shell

## Example

Create a file named `jeeves.py` in the root of your project.

```python
import rich
import sh


def hi():
    """Hello world."""
    user_name = sh.whoami()
    machine = sh.uname('-a')

    rich.print(f'Hello [b]{user_name}[/b]!')
    rich.print(f'This code is running on: [b]{machine}[/b].')
```

And then execute in your shell:

```shell
j hi
```

this should print something along the lines of:

```
Hello john-connor!
This code is running on: Cyberdyne T800!
```

## Learn More

Read [the tutorial](https://jeeves.sh/jeeves-py/)!

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).
