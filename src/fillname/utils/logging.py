"""
Setup project wide loggers.

This is a thin wrapper around Python's logging module. It supports colored
logging.
"""

import logging
from typing import TextIO

NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

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


def configure_logging(stream: TextIO, level: int) -> None:
    """
    Configure application logging.
    """
    log_message_str = "{}%(levelname)s:{}  - %(message)s{}"

    def make_handler(level: int, color: str) -> "logging.StreamHandler[TextIO]":
        handler = logging.StreamHandler(stream)
        handler.addFilter(SingleLevelFilter(level, False))
        handler.setLevel(level)
        formatter = logging.Formatter(log_message_str.format(COLORS[color], COLORS["GREY"], COLORS["NORMAL"]))
        handler.setFormatter(formatter)
        return handler

    handlers = [
        make_handler(logging.INFO, "GREEN"),
        make_handler(logging.WARNING, "YELLOW"),
        make_handler(logging.DEBUG, "BLUE"),
        make_handler(logging.ERROR, "RED"),
    ]
    logging.basicConfig(handlers=handlers, level=level)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger with the given name.
    """
    return logging.getLogger(name)
