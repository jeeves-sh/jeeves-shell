from pathlib import Path

import sh


def install_mkdocs_insiders():
    """Install Insiders version of `mkdocs-material` theme."""
    name = 'mkdocs-material-insiders'

    if not (Path.cwd() / name).is_dir():
        sh.gh.repo.clone(f'jeeves-sh/{name}')

    sh.pip.install('-e', name)


def deploy_to_github_pages():
    """Build the docs & deploy → gh-pages branch."""
    sh.mkdocs('gh-deploy', '--force', '--clean', '--verbose')


def install_graphviz():
    """Install graphviz, which is a prerequisite for some helper packages."""
    sh.sudo('apt-get', 'install', '-y', 'graphviz')


def serve():
    """Serve documentation locally."""
    sh.mkdocs.serve('-a', 'localhost:8971', _fg=True)


def cover_image():
    """Generate cover image for the front page."""
    assets = Path(__file__).parent / 'docs/assets'
    sh.convert(
        assets / 'cover-original.png',
        '-crop',
        'x400+0+100',
        assets / 'cover.png',
    )
