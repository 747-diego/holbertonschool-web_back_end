#!/usr/bin/env python3
"""0x05. Personal data."""

import typing
import logging
import os
import re


import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """Redacting-Fields."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Logging-the-Occurences."""
        loggedOccurences = logging.Formatter(self.FORMAT).format(record)
        fields = self.fields
        red = self.REDACTION
        sep = self.SEPARATOR
        return(filter_datum(fields, red, loggedOccurences, sep))


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated."""
    for obfuscated in fields:
        message = re.sub(obfuscated + "=.*?" + separator,
                         obfuscated + "=" + redaction + separator, message)
    return(message)
