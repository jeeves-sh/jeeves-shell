---
$id: hidden-functions
title: def _hidden()
hidden: examples/hidden.py
---

# `def _hidden()` functions

If function name starts from an underscore, it will _not_ be converted to a command.

That is useful for helper reusable functions.

{{ code(page.meta.hidden, language='python', title='jeeves.py') }}

⇒

{{ j(page.meta.hidden, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}
