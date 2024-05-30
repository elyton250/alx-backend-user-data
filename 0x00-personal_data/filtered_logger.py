#!/usr/bin/env python3
"""this function obscurate the stuff"""
import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s\
        %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        """this is the init
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """this is the formatter"""
        original = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            original, self.SEPARATOR
            )


def filter_datum(
    fields: List[str],
    redaction: str, message: str,
    separator: str
        ) -> str:
    """this function filters the message"""
    pattern = re.compile("|".join(
        f"{field}=[^{separator}]*"for field in fields))
    return pattern.sub(redaction, message)
