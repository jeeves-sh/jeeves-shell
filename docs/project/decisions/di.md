---
title: Jeeves needs DI
status: accepted
---

# Decision

`jeeves` needs a Dependency Injection framework to keep its capabilities on par with GNU Make.

## Context

At the moment of writing this, it is user's responsibility to ensure that:

* a command calls the functions it depends upon,
* functions are only called if they really need to,
* and they are only called once if that is what the logic demands.

