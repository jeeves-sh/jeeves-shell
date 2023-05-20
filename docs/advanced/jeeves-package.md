---
$id: jeeves-package
title: Jeeves package

package: advanced/examples/package

init: advanced/examples/package/__init__.py
test: advanced/examples/package/test.py
lint: advanced/examples/package/lint.py
---

# :package: `jeeves` package instead of :simple-python: `jeeves.py` file

Instead of {{ render('jeeves.py') }} file, a Python package named `jeeves` can also be used.

* That helps to structure code better if you have multiple commands,
* You no longer need to make sub-commands hidden.

=== "jeeves/__init__.py"

    {{ code(page.meta.init, language='python', indent=4, title='jeeves/__init__.py') }}

=== "jeeves/test.py"

    {{ code(page.meta.test, language='python', indent=4, title="jeeves/test.py") }}

=== "jeeves/lint.py"

    {{ code(page.meta.lint, language='python', indent=4, title="jeeves/lint.py") }}

## Top level documentation

{{ j(page.meta.package, environment={'JEEVES_DISABLE_PLUGINS': 'true'}) }}

## Command documentation

{{ j(page.meta.package, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['lint']) }}

## Sub command documentation

{{ j(page.meta.package, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['lint', 'flake8', '--help']) }}

## …and execution

{{ j(page.meta.package, environment={'JEEVES_DISABLE_PLUGINS': 'true'}, args=['lint', 'flake8']) }}
