---
title: Choose a DI library
status: rejected

criteria:
  requires-classes:
    title: Requires classes
    comment: The DI library cannot work on plain functions, it needs classes.
    weight: -1
    blocker: yes
  injectable-functions:
    title: Functions are injectable
    comment: Functions can be injected, not just classes.
    blocker: yes
  depends-annotation:
    title: "`Depends` annotation"
    comment: Annotation to automatically inject one function into another.
  requires-container:
    title: Requires a container object to be explicitly created.
    weight: -1
    blocker: yes

alternatives:
  - id: https://github.com/proofit404/dependencies
    requires-classes: yes
  - id: https://github.com/ivankorobkov/python-inject
    requires-classes: no
    injectable-functions: no
  - id: https://github.com/Neoteroi/rodi
    requires-classes: yes
  - id: https://github.com/ets-labs/python-dependency-injector
    requires-classes: yes
  - id: https://github.com/bobthemighty/punq
    requires-classes: no
    depends-annotation: no
  - id: https://github.com/BradLewis/simple-injection
    requires-classes: yes
  - id: https://github.com/adriangb/di
    requires-container: yes
  - id: https://github.com/avito-tech/trainspotting
    requires-container: yes
  - id: https://github.com/akshay2000/Pychkari
    requires-container: yes
---

I haven't found a suitable library.

!!! warning "todo"
    This document is going to be expanded with a visualization of available libraries.
