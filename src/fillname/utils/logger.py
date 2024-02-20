"""
Setup project wide loggers.
"""

import logging
import sys

COLORS = {
    "GREY": "\033[90m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "NORMAL": "\033[0m",
}


class SingleLevelFilter(logging.Filter):
    """
    Filter levels.
    """

    passlevel: int
    reject: bool

    def __init__(self, passlevel: int, reject: bool):
        # pylint: disable=super-init-not-called
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record: logging.LogRecord) -> bool:
        if self.reject:
            return record.levelno != self.passlevel  # nocoverage

        return record.levelno == self.passlevel


def setup_logger(name: str, level: int) -> logging.Logger:
    """
    Setup logger.
    """

    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)
    log_message_str = "{}%(levelname)s:{}  - %(message)s{}"

    def set_handler(level: int, color: str) -> None:
        handler = logging.StreamHandler(sys.stderr)
        handler.addFilter(SingleLevelFilter(level, False))
        handler.setLevel(level)
        formatter = logging.Formatter(log_message_str.format(COLORS[color], COLORS["GREY"], COLORS["NORMAL"]))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    set_handler(logging.INFO, "GREEN")
    set_handler(logging.WARNING, "YELLOW")
    set_handler(logging.DEBUG, "BLUE")
    set_handler(logging.ERROR, "RED")

    return logger
