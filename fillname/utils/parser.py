"""
The command line parser for the project.
"""

import logging
from argparse import ArgumentParser
from textwrap import dedent
from typing import Any, cast

from pkg_resources import require

__all__ = ["get_parser"]

VERSION = require("fillname")[0].version


def get_parser() -> ArgumentParser:
    """
    Return the parser for command line options.
    """
    parser = ArgumentParser(
        description=dedent(
            """\
            fillname
            filldescription
            """
        )
    )

    levels = [
        ("error", logging.ERROR),
        ("warning", logging.WARNING),
        ("info", logging.INFO),
        ("debug", logging.DEBUG),
    ]

    def get(levels, name):
        for key, val in levels:
            if key == name:
                return val
        return None  # nocoverage

    parser.add_argument(
        "--log",
        default="warning",
        choices=[val for _, val in levels],
        metavar=f"{{{','.join(key for key, _ in levels)}}}",
        help=dedent(
            """\
            set log level [%(default)s]"""
        ),
        type=cast(Any, lambda name: get(levels, name)),
    )

    parser.add_argument(
        "--version", "-v", action="version", version=f"%(prog)s {VERSION}"
    )
    return parser
