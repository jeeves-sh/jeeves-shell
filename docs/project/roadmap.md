---
hide:
  - toc
roadmap:roadmap:
  - title: Publish and document jeeves-generate-mkdocs-material-insiders
    is-blocked-by: jeeves-generate

  - title: jeeves → social media
    $id: publish
    branches:
      - title: HN
      - title: dev.to
      - title: …
    is-blocked-by:
      - title: jeeves-generate → jeeves-yeti-pyproject
        is-blocked-by:
          - title: Publish jeeves-generate micro-framework
            $id: jeeves-generate
            is-blocked-by:
              - title: Do not generate anything if there are uncommitted changes
              - title: Integration with cookiecutter
                is-blocked-by:
                  - title: What about the uncontrolled generators?
              - title: LockingPath class
              - title: How to pass the locking instance of project directory?
                branches:
                  - title: Via dependencies
                  - title: Via Typer context
        
      - https://github.com/jeeves-sh/jeeves-shell/issues/15
      
      - title: On Typer card, say why Typer is cool
      - title: Document why we chose Typer
        is-blocked-by:
          - title: In alternatives tables, highlight the chosen alternative with green background

      - title: Document which license Jeeves is using
        is-blocked-by:
          - https://github.com/jeeves-sh/jeeves-shell/issues/18

      - title: Badges in README.md are in bad shape
        is-blocked-by:
          - title: Tests are failing @ CI
            bug: true

      - title: Implement & use Side By Side display with cards
      
      - title: Document use cases

      - title: Generate Github workflows at jeeves-yeti-pyproject
        is-blocked-by:
          - title: "Implement `jeeves boilerplate`"
            branches:
              - title: "Run tasks registered as plugins to jeeves-boilerplate"
              - title: "Somehow with Cookiecutter?"

      - title: Sync jeeves.py example with home page example
        is-blocked-by:
          - https://github.com/jeeves-sh/jeeves-shell/issues/19

      - title: Make social cards
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
