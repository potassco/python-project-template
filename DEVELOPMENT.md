## Development

To improve code quality, we use [nox] to run linters, type checkers, unit
tests, documentation and more. We recommend installing nox using [pipx] to have
it available globally.

```bash
# install
python -m pip install pipx
python -m pipx install nox

# run all sessions
nox

# list all sessions
nox -l

# run individual session
nox -s session_name

# run individual session (reuse install)
nox -Rs session_name
```

Note that the nox sessions create [editable] installs. In case there are issues,
try recreating environments by dropping the `-R` option. If your project is
incompatible with editable installs, adjust the `noxfile.py` to disable them.

We also provide a [pre-commit][pre] config to autoformat code upon commits. It
can be set up using the following commands:

```bash
python -m pipx install pre-commit
pre-commit install
```

## Deployment

To release this project on (test.)pypi.org please follow these instructions:

Long version:
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
TL;DR
 - create a github environmnent (Github->Your Project->Settings->Environments) with the safety regulations you prefer, e.g. restriction
   to a fixed set of branches like "test_release" or manual confirmation
   This step is important to prevent other people from releasing new versions on accident
 - create a [test.]pypi.org account (enable 2fa)
 - create a project with the same name
 - add the formerly created github environment
 - run the respective CI scripts either manually (test.pypi.org) or by tagging a release version (pypi.org)

[nox]: https://nox.thea.codes/en/stable/index.html
[pipx]: https://pypa.github.io/pipx/
[pre]: https://pre-commit.com/
[editable]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html

