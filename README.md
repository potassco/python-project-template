# fillname

>    Remove this block after following the instructions below to use the template.
>
>    This project template is configured to ease collaboration. Linters, formatters,
>    and actions are already configured and ready to use.
>
>    To use the project template, run the `init.py` script to give the project a
>    name and some metadata. The script can then be removed. Then adjust the
>    `setup.cfg` file as needed.

## Installation

```shell
pip install .
```

## Usage

```shell
fillname -h
```

## Development

To improve code quality, we use [nox] to run linters, type checkers, unit tests, documentation and more. We recommend installing nox using [pipx] to have
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

We provide a [pre-commit][pre] config to automate this process. It can be
set up using the following commands:

```bash
python -m pipx install pre-commit
pre-commit install
```

This blackens the source code whenever `git commit` is used.

[doc]: https://potassco.org/clingo/python-api/current/
[nox]: https://nox.thea.codes/en/stable/index.html
[pipx]: https://pypa.github.io/pipx/
[pre]: https://pre-commit.com/
[black]: https://black.readthedocs.io/en/stable/
[editable]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html
