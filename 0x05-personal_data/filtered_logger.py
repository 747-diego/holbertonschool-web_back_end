#!/usr/bin/env python3
"""0x05. Personal data."""

import typing
import logging
import mysql.connector
import re
from os import environ

# A TUPLE CONTAINED WITH THE 5 MOST IMPORTANT FIELDS FROM USER DATA
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """No arguments and returns a logging.Logger object."""
    pieFields = list(PII_FIELDS)
    loggedData = logging.getLogger('user_data')

    loggedData.propagate = False
    loggedData.setLevel(logging.INFO)

    fieldsFormatted = RedactingFormatter(pieFields)
    fieldsHandled = logging.StreamHandler()

    loggedData.setFormatter(fieldsFormatted)
    loggedData.addHandler(fieldsHandled)

    Data = loggedData
    return(Data)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """A-function that returns a connector to the database."""
    # STORING CREDENTIALS INTO ENVIROMENTAL VARIABLES
    userName = environ['PERSONAL_DATA_DB_USERNAME']
    userPassword = environ['PERSONAL_DATA_DB_PASSWORD']
    personalHost = environ['PERSONAL_DATA_DB_HOST']
    personalName = environ['PERSONAL_DATA_DB_NAME']

    MYSQLconnector = mysql.connector.connect(user=userName,
                                             password=userPassword,
                                             host=personalHost,
                                             database=personalName)
    return(MYSQLconnector)


def main() -> None:
    """Take no arguments and returns nothing."""
    test = get_db().cursor()
    test.execute("SELECT * FROM users;")

    for row in enumerate(test):
        get_logger().info(row)
    test.close()


if __name__ == "__main__":
    main()
