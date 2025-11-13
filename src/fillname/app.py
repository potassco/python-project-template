import sys
from textwrap import dedent
from typing import Sequence

from clingo import Application, ApplicationOptions, Control

from fillname.utils.logging import colored, configure_logging


class FillnameApp(Application):
    """Application for reification with extensions."""

    def __init__(self, name):
        self.program_name = name
        self._log_level = "WARNING"

    def parse_log_level(self, log_level: str) -> bool:
        """
        Parse log
        """
        if log_level is not None:
            self._log_level = log_level.upper()
            return self._log_level in ["INFO", "WARNING", "DEBUG", "ERROR"]

        return True

    def register_options(self, options: ApplicationOptions) -> None:
        group = colored("blue", "Fillname Options")

        options.add(
            group,
            "log",
            dedent(
                """\
                Provide logging level.
                            <level> ={DEBUG|INFO|ERROR|WARNING}
                            (default: WARNING)"""
            ),
            self.parse_log_level,
            argument="<level>",
        )

    def main(self, ctl: Control, files: Sequence[str]) -> None:
        """
        Main function ran on call
        """
        # pylint: disable=W0201
        configure_logging(sys.stderr, self._log_level, sys.stderr.isatty())  # type: ignore
