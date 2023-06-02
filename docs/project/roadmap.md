---
hide:
  - toc
roadmap:roadmap:
  - title: jeeves → social media
    $id: publish
    branches:
      - title: HN
      - title: dev.to
      - title: …
    is-blocked-by:
      - title: Tests are failing at CI
        bug: true
      - title: Generate Github workflows at jeeves-yeti-pyproject
        is-blocked-by:
          - title: "Implement `jeeves boilerplate`"

      - title: The word Build is twice repeated on the first card
        bug: true
      - title: Sync jeeves.py example with home page example
        is-blocked-by:
          - title: Add args to home page example
      - title: Copyright is 2022
        bug: true
      - title: Make social cards
      - title: In alternatives tables, highlight the chosen alternative with green background
      - title: sh command streams decorator — where?
        branches:
          - title: Part of Jeeves
          - title: Part of sh
          - title: Separate package
        is-blocked-by:
          - title: progress bars when executing sh commands
      - title: Support dependencies
        is-blocked-by:
          - title: Review awesome-python-dependency-injection
          - title: Document alternatives
          - title: pre-conditions perhaps

      - title: Build a Plugins page with catalog
        is-blocked-by:
          - title: Support cards in mkdocs-iolanta
          - title: Document jeeves-yeti-pyproject
            branches:
              - title: At jeeves.sh
              - title: At GitHub pages
            is-blocked-by:
              - title: jeeves-yeti-pyproject only scans and formats python packages, not individual files like jeeves.py
                bug: true
              - title: Move jeeves-yeti-pyproject → jeeves-sh org?
                branches:
                  - title: yes
                  - title: no
              - title: See if there is a tool to document Click with mkdocs
              - title: Terminal output from jeeves-yeti-pyproject is broken
                bug: true
                description: Look at TERM environment variable at CI



  - title: "`j fork 123` @ `jeeves-yeti-pyproject`"
    is-blocked-by:
      - title: Create the PR with proper base and title
        is-blocked-by:
          - title: Commit
            is-blocked-by:
              - title: switch -c to the proper branch
                is-blocked-by:
                  - title: Format branch name
                    is-blocked-by:
                      - title: Retrieve issue info or create an issue
                        is-blocked-by:
                          - title: "Issue `j fork` with issue arg or without"
                            is-blocked-by:
                              - title: Do some uncommitted changes

  - title: Convert j → self-contained binary

  - title: Choose software license and link to its human readable description

  - title: Some kind of Python conference at 2023
    $id: presentation
    is-blocked-by:
      title: Prepare a talk about Jeeves
      $id: jeeves-talk
      is-blocked-by:
        - title: Reload the site when a template is edited
        - title: File is deleted ⇒ dev server crashes
          bug: true
        - title: Review chainlit
          schema:url: https://github.com/Chainlit/chainlit
        - title: Does jeeves work well with Bash completion?
        - title: Document jeeves vs cookiecutter and stuff
          is-blocked-by:
            - title: project templates
        - title: Make a presentation or a video
        - title: parallel decorator
        
        - title: Mount points
          description: for instance, jeeves-mkdocs should be always a subcommand
          is-blocked-by:
            - title: How to define mount points
              branches:
                - title: in the plugin
                - title: in the project
                - title: both
        - title: mkdocs-typer
          description: Describe Typer docs → MkDocs site
          is-blocked-by:
            - title: "Use Iolanta for mkdocs-typer?"
              branches:
                - title: Yes
                - title: No

        - title: Jeeves + UI
          is-blocked-by:
            - title: Review editors which Jeeves might integrate with
            - title: How can Jeeves be integrated with i3

  - title: Name Jupyter notebooks after branch
  - title: PyCharm does not recognize sh imports
    bug: true
  - title: coverage is failing
    bug: true
  - title: _archive directory is just chilling there
    bug: true

  - title: Source environment variables from Typer
  - title: Document custom environment variables
    branches:
      - title: Annotate functions with JSON-LD or direct RDF
      - title: Just write custom YAML-LD
---

<body>{{ render("publish") }}</body>
