import os

import nox

nox.options.sessions = "lint_flake8", "lint_pylint", "typecheck", "test"

PYTHON_VERSIONS = None
if "GITHUB_ACTIONS" in os.environ:
    PYTHON_VERSIONS = ["3.7", "3.11"]


@nox.session
def format(session):
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
    target = "html"
    options = []
    if session.posargs:
        target = session.posargs[0]
        options = session.posargs[1:]

    session.install("-e", ".[doc]")
    session.cd("doc")
    session.run("sphinx-build", "-M", target, ".", "_build", *options)


@nox.session
def lint_flake8(session):
    session.install("-e", ".[lint_flake8]")
    session.run("flake8", "src", "tests")


@nox.session
def lint_pylint(session):
    session.install("-e", ".[lint_pylint]")
    session.run("pylint", "fillname", "tests")


@nox.session
def typecheck(session):
    session.install("-e", ".[typecheck]")
    session.run("mypy", "-p", "fillname", "-p", "tests")


@nox.session(python=PYTHON_VERSIONS, reuse_venv=False)
def test(session):
    session.install(".[test]")
    session.run("coverage", "run", "-m", "unittest", "discover", "-v")
    session.run("coverage", "report", "-m", "--fail-under=100")


@nox.session
def dev(session):
    session.install("-e", ".[dev]")
