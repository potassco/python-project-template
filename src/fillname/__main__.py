"""
The main entry point for the application.
"""

import sys

from clingo import clingo_main

from fillname.app import FillnameApp

from .utils.logging import configure_logging, get_logger
from .utils.parser import get_parser


def main() -> None:
    """
    Run the main function.
    """
    clingo_main(FillnameApp(sys.argv[0]), sys.argv[1:])
    sys.exit()


if __name__ == "__main__":
    main()
