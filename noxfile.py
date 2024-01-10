import os

import nox

nox.options.sessions = "lint_flake8", "lint_pylint", "typecheck", "test"

EDITABLE_TESTS = True
PYTHON_VERSIONS = None
if "GITHUB_ACTIONS" in os.environ:
    PYTHON_VERSIONS = ["3.7", "3.11"]
    EDITABLE_TESTS = False


@nox.session
def format(session):
    """
    Autoformat source files. -- check: Inspect changes.
    """
    session.install("-e", ".[format]")
    check = "check" in session.posargs

    autoflake_args = [
        "--in-place",
        "--imports=fillname",
        "--ignore-init-module-imports",
        "--remove-unused-variables",
        "-r",
        "src",
        "tests",
    ]
    if check:
        autoflake_args.remove("--in-place")
    session.run("autoflake", *autoflake_args)

    isort_args = ["--profile", "black", "src", "tests"]
    if check:
        isort_args.insert(0, "--check")
        isort_args.insert(1, "--diff")
    session.run("isort", *isort_args)

    black_args = ["src", "tests"]
    if check:
        black_args.insert(0, "--check")
        black_args.insert(1, "--diff")
    session.run("black", *black_args)


@nox.session
def doc(session):
    """
    Build and open the documentation. -- open: Open after build, clean: Clean built files.
    """
    target = "html"
    options = []
    open = "open" in session.posargs
    clean = "clean" in session.posargs
    
    session.posargs.remove("open") if open else None
    session.posargs.remove("clean") if clean else None

    if session.posargs:
        target = session.posargs[0]
        options = session.posargs[1:]
    
    session.install("-e", ".[doc]")
    session.cd("doc")
    if clean:
        session.run("rm", "-rf", "_build")
    session.run("sphinx-build", "-M", target, ".", "_build", *options)
    if open:
        session.run("open", "_build/html/index.html")

@nox.session
def dev(session):
    """
    Create a development environment in editable mode. Activate it by running `source .nox/dev/bin/activate`.
    """
    session.install("-e", ".[dev]")

@nox.session
def lint_flake8(session):
    """
    Run flake8 linter.
    """
    session.install("-e", ".[lint_flake8]")
    session.run("flake8", "src", "tests")


@nox.session
def lint_pylint(session):
    """
    Run pylint.
    """
    session.install("-e", ".[lint_pylint]")
    session.run("pylint", "fillname", "tests")


@nox.session
def typecheck(session):
    """
    Typecheck the code using mypy.
    """
    session.install("-e", ".[typecheck]")
    session.run("mypy", "-p", "fillname", "-p", "tests")


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    """
    Run the tests. -- test_path: Test to be ran e.g. tests.test_main.TestMain.test_logger
    """

    args = ['.[test]']
    if EDITABLE_TESTS:
        args.insert(0, '-e')
    session.install(*args)
    if session.posargs:
        session.run("coverage", "run", "-m", "unittest", session.posargs[0], "-v")
    else:
        session.run("coverage", "run", "-m", "unittest", "discover", "-v")
        session.run("coverage", "report", "-m", "--fail-under=100")

