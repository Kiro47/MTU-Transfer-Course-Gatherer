#!/usr/bin/env python3

from argparse import Namespace
from logging import _nameToLevel
from enum import Enum


class Output_Types(Enum):

    """
    Enums to make handling easier
    """

    CSV = "csv"
    JSON = "json"
    TXT = "txt"

    def __str__(self):
        return self.value

    @staticmethod
    def fromString(string: str) -> Enum:
        """
        To enum from string

        :string: String to parse to Output_Types

        :return: Output_Types enum of string, or None if invalid
        """
        if string:
            if string.upper() == "CSV":
                return Output_Types.CSV
            elif string.upper() == "JSON":
                return Output_Types.JSON
            elif string.upper() == "TXT":
                return Output_Types.TXT
            else:
                return None
        return None

    @staticmethod
    def get_names() -> list:
        """
        Returns possible values for enums
        """
        # I spent two hours trying to get all the member names and could not
        # find a way to make it happen.
        return ["csv", "json", "txt"]


def is_log_level(new_log_level: str) -> bool:
    """
    Verifies that input string is a valid log level

    :return: True is a valid log level, false otherwise
    """
    if new_log_level:
        return new_log_level.upper() in _nameToLevel
    return False


def convert_args(args: Namespace) -> Namespace:
    """
    Converts strings in argparser's namespace to their respective Enums

    :args: result of parser.parse_args() from argparse

    :return: A namespace with required enum strings converted to enums
    """
    if args.output_type:
        args.output_type = Output_Types.fromString(args.output_type)
    if args.in_file_type:
        args.in_file_type = Output_Types.fromString(args.in_file_type)
    return args
