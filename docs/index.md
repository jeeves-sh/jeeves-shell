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

<div id="hero">
  <div id="termynal" data-ty-startDelay="600">
    <span data-ty="input"> ls</span>
    <span data-ty><code>jeeves.py</code></span>
    <span data-ty="input"> j hi</span>
    <span data-ty>Hello <strong>john-connor</strong>!</span>
    <span data-ty>This code is running on: <strong>Cyberdyne Systems v101 T800 sky512</strong>!</span>
  </div>
</div>

</div>

{# todo: Implement Roadmap page #}

# What is this?

`jeeves` is kind of Pythonic replacement for **GNU Make**.

{# todo: Implement this pro-et-contra comparison for GNU make. #}

## Why?

<table>
  <thead>
    <tr>
      <th><code>make</code> helps us orchestrate repeated tasks</th>
      <th>but, <code>make</code> can be difficult</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Run tests & linters</li>
          <li>Compile code</li>
          <li>Build images & other artifacts</li>
          <li>Deploy</li>
          <li>And much more</li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>make</code> syntax can be challenging</li>
          <li>
            Especially for
            <ul>
              <li>conditions</li>
              <li>value checks</li>
              <li>cycles</li>
            </ul>
          </li>
          <li><code>bash</code> is no easier</li>
          <li>
            <code>bash</code> + <code>make</code> integration makes stuff even more complicated<br/>
            <em>(for instance, when you have to distinguish between <code>make</code> and <code>bash</code> variables)</em>
          </li>
          <li><code>make</code> goals cannot define parameters (except environment variables)</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## What does `jeeves` do?

* :simple-python: Implement repeated & tedious administration tasks in Python
* :slight_smile: Reduce boilerplate
* :material-share: Share automated workflows across projects
* :people_holding_hands: …and teams

## Get started

Create a new file in the root directory of your project:

{{ code(page.meta.hello, language='python', title='jeeves.py') }}

Install Jeeves:

=== "pip"

    ```bash
    pip install 'jeeves-shell[all]'
    ```

=== "poetry"

    ```bash
    poetry add --group dev --extras=all jeeves-shell'
    ```

Check it out!

{{ j(page.meta.hello, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['hi', "world"]) }}

Find out more [in the tutorial…](jeeves-py)

<script src="/assets/termynal/termynal.js" data-termynal-container="#termynal"></script>
