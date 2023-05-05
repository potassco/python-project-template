# fillname

This project template is configured to ease collaboration. Linters, formatters,
and actions are already configured and ready to use.

To use the project template, run the `init.py` script to give the project a
name and some metadata. The script can then be removed afterward and the
`setup.cfg` file adjusted.

## Installation

```shell
pip install fillname
```

## Usage

```shell
fillname -h
```

## Development

To improve code quality, we run linters, type checkers, and unit tests. The
tools can be run using [nox]. We recommend installing nox using [pipx] to have
it available globally:

```bash
python -m pip install pipx
python -m pipx install nox
nox
```

You can invoke `nox -s` to run individual sessions. For example, to
install your package into a virtual environment and run your test
suite, invoke:

```bash
nox -s test
```

We provide a nox session that creates a development virtual
environment containing [editable install][editable] of your package,
along with linting, type checking and formatting packages. Activating
this environment allows your editor of choice to access these packages
for e.g. automatic linting and autocompletion. Due to the editable
install, changes made to your python source code are immediately
reflected in the activated virtual environment without requiring a
re-installation. To create and then activate virtual environment run:

```bash
nox -s dev
source .nox/dev/bin/activate
```

We also provide individual sessions to easily run linting, type
checking and formatting via nox. These also create editable installs,
so you can safely skip the re-creation of the virtual environment and
re-installation of your package in subsequent runs by passing the `-R`
command line argument. For example, to auto-format your code using
[black], run:

```bash
nox -Rs format -- check
nox -Rs format
```

The former command allows you to inspect changes before applying them.

We also provide a [pre-commit][pre] config to automate this
process. It can be set up using the following commands:

```bash
python -m pipx install pre-commit
pre-commit install
```

This blackens the source code whenever `git commit` is used.

**Note**: The test session does *not* use an editable install, and
therefore should not be run using the `-R` option. We do not use an
editable install when testing as end users will be using a regular
install, and there are some [subtle differences][editlimit] between
the two.

[doc]: https://potassco.org/clingo/python-api/current/
[nox]: https://nox.thea.codes/en/stable/index.html
[pipx]: https://pypa.github.io/pipx/
[pre]: https://pre-commit.com/
[black]: https://black.readthedocs.io/en/stable/
[editable]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html
[editlimit]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html#limitations
