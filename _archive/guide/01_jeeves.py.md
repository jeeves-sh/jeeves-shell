---
title: jeeves.py file
position: 1
simple: guide/examples/simple.py
---

Create a `jeeves.py` file with the following contents in an arbitrary directory.

{{ code(page.meta.simple, language='python', title='jeeves.py') }}

Residing in that directory, run `j`. Here's what you should see:

{{ j(page.meta.simple, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

Every function in `jeeves.py` is now exposed as a subcommand of `j` and gets auto documentation. Indeed:

{{ j(page.meta.simple, args=['hello', '--help']) }}

Let's try it out!

{{ j(page.meta.simple, args=['hello', '--style', 'british', 'Berty']) }}
