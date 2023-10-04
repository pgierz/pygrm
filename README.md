# pygrm

[![Release](https://img.shields.io/github/v/release/pgierz/pygrm)](https://img.shields.io/github/v/release/pgierz/pygrm)
[![Build status](https://img.shields.io/github/actions/workflow/status/pgierz/pygrm/main.yml?branch=main)](https://github.com/pgierz/pygrm/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/pgierz/pygrm/branch/main/graph/badge.svg)](https://codecov.io/gh/pgierz/pygrm)
[![Commit activity](https://img.shields.io/github/commit-activity/m/pgierz/pygrm)](https://img.shields.io/github/commit-activity/m/pgierz/pygrm)
[![License](https://img.shields.io/github/license/pgierz/pygrm)](https://img.shields.io/github/license/pgierz/pygrm)

This is a git repository manager, written in Python, which allows you to maintain a list of git projects you have on a particular computer in a configuration YAML file.

- **Github repository**: <https://github.com/pgierz/pygrm/>
- **Documentation** <https://pgierz.github.io/pygrm/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:pgierz/pygrm.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting
[this page](https://github.com/pgierz/pygrm/settings/secrets/actions/new).
- Create a [new release](https://github.com/pgierz/pygrm/releases/new) on Github.
Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
