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

    levels = {
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }

    parser.add_argument(
        "--log",
        default="warning",
        choices=levels.values(),
        metavar=f"{{{','.join(levels.keys())}}}",
        help=dedent(
            """\
                set log level [%(default)s]"""
        ),
        type=cast(Any, levels.get),
    )

    parser.add_argument(
        "--version", "-v", action="version", version=f"%(prog)s {VERSION}"
    )
    return parser
