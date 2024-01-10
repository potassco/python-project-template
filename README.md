# fillname



>    Remove this block after following the instructions below to use the template
>
>    This project template is configured to ease collaboration. Linters, formatters,
>    and actions are already configured and ready to use.
>
>    To use the project template, run the `init.py` script to give the project a
>    name and some metadata. The script can then be removed. Then adjust the
>    `setup.cfg` file as needed.



## Installation

```shell
pip install -e .[all]
```

## Usage

```shell
fillname -h
```

## Development

To improve code quality, we run linters, type checkers, and unit tests. The
tools can be run using [nox]. We recommend installing nox using [pipx] to have
it available globally:

### Install [nox]

```bash
python -m pip install pipx
python -m pipx install nox
```

### Use [nox]

- Run all sessions 

```bash
nox
```

- Run individual sessions. 

```bash
nox -s session_name
```

- See the list of sessions

```bash
nox -l
```


To install your package into a virtual environment and run your test suite, invoke:

```bash
nox -s test
```

We also provide a nox session that creates an environment for development. The
project is installed in [editable] mode into this environment along with
linting, type checking and formatting tools. Activating it allows your editor
of choice to access these tools for, e.g., linting and autocompletion. To
create and then activate virtual environment run:

```bash
nox -s dev
source .nox/dev/bin/activate
```

Furthermore, we provide individual sessions to easily run linting, type
checking and formatting via nox. These also create editable installs. So you
can safely skip the recreation of the virtual environment and reinstallation of
your package in subsequent runs by passing the `-R` command line argument.
Note that editable installs have some caveats. In case there are issues, try
recreating environments by dropping the `-R` option. If your project is
incompatible with editable installs, adjust the `noxfile.py` to disable them.

```bash
nox -Rs format -- check
nox -Rs format
```

The former command allows you to inspect changes before applying them.

### Pre-commit

We also provide a [pre-commit][pre] config to automate this process. It can be
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
