---
title: Welcome to jeeves!
hello: examples/hello.py
hide:
  - toc
  - navigation
---

# :material-bow-tie: Welcome to Jeeves!

<div class="grid" markdown>

{{ code("examples/homepage.py", language='python', title='jeeves.py') }}

<div id="termynal" data-ty-startDelay="600">
  <span data-ty="input"> ls</span>
  <span data-ty><code>jeeves.py</code></span>
  <span data-ty="input"> j hi</span>
  <span data-ty>Hello <strong>john-connor</strong>!</span>
  <span data-ty>This code is running on: <strong>Cyberdyne T800</strong>!</span>
</div>

</div>

# Features

<div class="grid cards" markdown>

-   :fontawesome-solid-terminal:{ .lg .middle } __Build custom shell commands__

    ---

    …to build, compile, lint, format, test, deploy, and :rocket: otherwise propel your project.

-   :material-tools:{ .lg .middle } __`make` → `j`__

    ---

    Single entry point to all your custom commands.

-   :simple-python:{ .lg .middle } __`Makefile` → `jeeves.py`__

    ---

    Write your workflows @ Python programming language.

    [:octicons-arrow-right-24: `jeeves.py`](jeeves-py)

-   :material-typewriter:{ .lg .middle } __Based on Typer__

    ---

    Brings documentation, arguments, options, validation & more.

    [:octicons-arrow-right-24: Typer](typer)

-   :material-battery:{ .lg .middle } __Batteries__

    ---

    Execute shell commands & format output.

    [:octicons-arrow-right-24: `sh`](sh) & [`rich`](rich) 

-   :fontawesome-solid-plug:{ .lg .middle } __Plugins__

    ---

    Share your setup among projects.

    [:octicons-arrow-right-24: Plugins](plugins/why)

</div>

{# todo: Implement Roadmap page #}

# Installation

=== "pip"

    ```bash
    pip install 'jeeves-shell[all]'
    ```

=== "poetry"

    ```bash
    poetry add --group dev --extras=all jeeves-shell
    ```

Find out more [in the tutorial…](jeeves-py)

<script src="/assets/termynal/termynal.js" data-termynal-container="#termynal"></script>
