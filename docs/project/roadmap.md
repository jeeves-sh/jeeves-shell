---
hide:
  - toc

roadmap:roadmap:
  - title: Use rich logger
  - title: Implement __rich__ at documented errors and warnings
  - title: console.print() an exception instead of logging it in jeeves
  - title: Custom Console for printing errors with red headings
  - title: Use rich for printing errors when available and plain print when not

  - title: "Fork pull request: `j fork`"
    is-blocked-by:
      - title: There are uncommitted changes
      - title: Ask for branch name
      - title: "Do `git switch -c`"
      - title: "Call `j commit` to save the changes"
      - title: "Call `gh pr create`"

  - title: "Invent a commit message with LLM at `j commit`"
    is-blocked-by:
      - title: Customize branch and commit message patterns via command line options & pyproject.toml
      - title: "Measure PR complexity at `j commit` & alert about the PR being too complex"

  - title: LockingPath class
  - title: How to pass the locking instance of project directory?
    branches:
      - title: Via dependencies
      - title: Via Typer context  

  - title: Publish and document jeeves-generate-mkdocs-material-insiders
    is-blocked-by: jeeves-generate

  - title: jeeves → social media
    "$id": publish
    branches:
      - title: HN
      - title: dev.to
      - title: …

    is-blocked-by:
      - title: "`j generate` @ `jeeves-yeti-pyproject`"
        is-blocked-by:
          - title: Generate GitHub workflows
          - title: docs/index.md | iolanta-jinja2 → README.md
          - title: poetry lock --no-update
          - title: … Any other generation commands?

          - title: What do we call when we want to process the DAG?
            branches:
              - title: DAG itself
                description: Would be preferable for the jeeves-generate case, and is most similar to Step Functions
              - title: One of functions of the DAG

          - title: Implement CI mode for jeeves-generate DAG
            description: Stop As soon as a task fails
          - title: Use the collected statistics of tasks performance to determine which tasks to run first
            is-blocked-by:
              - title: Record the statistics of tasks performance
          - title: Publish dry.jeeves.sh
            description: Transparent dry run functionality is important, that's what Make does not have
            is-blocked-by:
              - title: jeeves-dry → PyPI
                is-blocked-by:
                  - title: Update main Jeeves app
                  - title: Add dry-run argument to the Jeeves app
                  - title: Post-process iterators as commands
          - title: Publish generate.jeeves.sh
            "$id": jeeves-generate
            is-blocked-by:
              - title: jeeves-generate → PyPI
                is-blocked-by:
                  - title: Do not generate anything if there are uncommitted changes
                  - title: How to build a DAG?
                    branches:
                      - title: Use an existing library
                      - title: Build a new dependencies DAG library
                        is-blocked-by:
                          - title: Get dependencies from Annotated
                          - title: Get dependencies from decorator arguments
                    is-blocked-by:
                      - title: Compare Python dependencies libraries
                        is-blocked-by:
                          - title: I want iolanta-prov to finally write good comparisons
                        blocks:
                          - title: Add Edit button to jeeves.sh
                            blocks:
                              - title: Show my dependencies comparison to Artem
        
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
