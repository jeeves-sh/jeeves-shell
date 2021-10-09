---
title: Choosing dependency injection framework
number: 2
status: accepted
---

## Context

### Why does `jeeves` need a DI framework?

`jeeves` aims to be a Pythonic alternative to GNU Make. GNU Make enjoys an ad-hoc dependency framework, which permits to only execute a task if certain file is up to date, or to execute a dependent task only after running the task it depends on.

That's what `jeeves` has to do either. For example, `jeeves move` command, which will operate on currently selected task, must first ensure that Jira (or another task management) system connection has been established. Only then we can do any task manipulation.

### What do we currently use?

At the moment of writing, we're using {{ link('dependencies') }} library but I have certain reservations about it.

### Comparison

<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Requires Classes?</th>
      <th>Passing config params</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{{ link('dependencies') }}</td>
      <td>➕</td>
      <td>✔️</td>
      <td>Requires classes</td>
    </tr>

    <tr>
      <td>{{ link('typer') }}</td>
      <td></td>
      <td></td>
      <td>{{ link('typer-di') }}</td>
    </tr>

    <tr>
      <td>{{ link('python-inject') }}</td>
      <td>➖</td>
      <td></td>
      <td>🤔</td>
    </tr>
  </tbody>
</table>


!!! info
    At the moment of writing, `inject` seems to be an interesting choice to play with. I will try it. Document is to be continued...

## Decision

...

Consequences

...
