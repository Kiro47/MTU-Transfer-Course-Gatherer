#!/usr/bin/env python3

import logging
from os import path
import sys
from pathlib import Path
from singleton_decorator import singleton


@singleton
class LoggerManager(object):
    """
    Logging Manager, overall logging settings for the entire project
    """

    def __init__(self, log_file: str, log_level=logging.INFO):
        """
        Logging Manager initializer
        """
        self.logger = logging.getLogger()
        log_format = logging.Formatter(
            fmt=("[%(asctime)s][%(levelname)s][%(name)s:%(funcName)s] "
                 "%(message)s"),
            # Nearly ISO 8601 compliant, strftime doesn't support nanoseconds?
            # https://docs.python.org/3/library/time.html#time.strftime
            datefmt="%Y-%m-%dT%H:%M:%S"
        )
        stdio_handler = logging.StreamHandler(sys.stdout)

        if stdio_handler:
            stdio_handler.setFormatter(log_format)
            self.logger.addHandler(stdio_handler)

        self.logger.setLevel(log_level)

        # Setting up stdio first as file is much less error prone
        if log_file:
            file_path = path.split(log_file)  # 0  head, 1 tail
            if not file_path[1]:
                # is directory
                self.logger.critical("Provided logfile [{}] is a directory".
                                     format(log_file))
                sys.exit(2)
            if file_path[0]:
                # Is dir + file
                try:
                    Path(file_path[0]).mkdir(parents=True, exist_ok=True)
                except OSError as error:
                    self.logger.critical("Unable to create logfile [{}]".
                                         format(log_file), exc_info=error)
                    sys.exit(1)
            # logging will handle the actual file creation
            file_handler = logging.FileHandler(log_file)
            if file_handler:
                file_handler.setFormatter(log_format)
                self.logger.addHandler(file_handler)
        return

    def debug(self, logger_name, msg):
        """
        Wrapper for logger.debug()
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.debug(msg)

    def error(self, logger_name, msg):
        """
        Wrapper for logger.error()
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.error(msg)

    def info(self, logger_name, msg):
        """
        Wrapper for logger.info()
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.info(msg)

    def warning(self, logger_name, msg):
        """
        Wrapper for logger.warning()
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.warning(msg)

    def critical(self, logger_name, msg):
        """
        Wrapper for logger.critical()
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.critical(msg)


class Logger(object):

    """
    Logger object for normal use
    """

    def __init__(self, logger_name: str = "root"):
        """
        Initializes logger object
        """
        self.log = LoggerManager()
        self.logger_name = logger_name

    def debug(self, msg):
        """
        Wrapper for logger.debug()
        """
        self.log.debug(self.logger_name, msg)

    def error(self, msg):
        """
        Wrapper for logger.error()
        """
        self.log.error(self.logger_name, msg)

    def info(self, msg):
        """
        Wrapper for logger.info()
        """
        self.log.info(self.logger_name, msg)

    def warning(self, msg):
        """
        Wrapper for logger.warning()
        """
        self.log.warning(self.logger_name, msg)

    def critical(self, msg):
        """
        Wrapper for logger.critical()
        """
        self.log.critical(self.logger_name, msg)
