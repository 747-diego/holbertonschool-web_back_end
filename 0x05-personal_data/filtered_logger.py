#!/usr/bin/env python3
"""0x05. Personal data."""

import typing
import logging
import os
import re


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated."""
    for obfuscated in fields:
        message = re.sub(obfuscated + "=.*?" + separator,
                         obfuscated + "=" + redaction + separator, message)
    return message
