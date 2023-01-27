# fillname

filldescription


To use the project template do the following:
1. Rename the folder <fillname> using your project name
2. A global substitution of <fillname> by your project name
3. A global substitution of <filldescription> by your project description
4. The clingo API will be part of the requirements. Check the version you want to use on [`setup.cfg`](setup.cfg).
5. Check the version you want to use for python and update the README Installation section bellow. Also update the [CI](.github/workflows/ci-test.yml) to run tests only in this version.
6. The main function that will be called with `fillname` is in [`fillname/__init__.py`](.fillname/__init__.py). It includes a `logger` and `argparse` which are imported from the [utils folder](fillname\utils), if not needed can be removed.
7. A test folder is included to promote unit-testing. Tests will be called using `pytest` by the github CI.
8. All set! Now you have CI ***Remove these instructions***

## Installation

Requires Python 3.9

**Local dev mode using pip**

```shell 
pip install -e .[dev]
```

## Usage

```shell 
fillname -h
```

## Tests

Run tests using `pytest`

```shell
$ pytest -v tests/test.py
```

Add flag `-s` to show print statements in the code