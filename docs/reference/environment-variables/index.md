---
title: Environment variables

$id: environment-variables
table:columns:
  - table:self
  - default
  - purpose

table:rows:
  - rdfs:label: JEEVES_ROOT
    schema:url: JEEVES_ROOT/
    default: (current directory)
    purpose: Location of jeeves.py file or jeeves package.
  - rdfs:label: JEEVES_DISABLE_PLUGINS
    default: (unset)
    purpose: Set this to ignore any installed plugins (and thus only use jeeves.py or jeeves package commands). Might be useful for debugging.
---

# :material-application-variable: Environment variables

{{ render("environment-variables") }}
