---
title: Debugging
---

## Enable debug mode

```shell
j --log-level info whatever commands --with args etc
```

* This will set log level to `info`. The even more verbose option is `debug`;
* Any of these levels will also mean that any unhandled exception will be printed in full, traceback included.

## Disable plugins

```shell
JEEVES_DISABLE_PLUGINS=1 j
```

