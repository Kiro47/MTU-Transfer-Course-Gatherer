#!/usr/bin/env python3

import argparse
from logging import INFO, DEBUG, _nameToLevel
from os import path
from sys import exit


from scraper.args import Output_Types, convert_args
from scraper.transfers.file_utils import File_Utils
from scraper.transfers.data_gathering import Data_Gathering
from scraper.Logger import LoggerManager, Logger

"""
CSV Order:
    Header:
        single line at top of csv.
    Data:
        In one line, csv delimited.
            transfering_state_code,transfering_state_name,
            transfering_college_code,transferring_college_name,
            transfering_subject,transfering_number,
            transfering_credits,MTU_class_name,
            MTU_subject,MTU_number,MTU_credits
"""


def form_cli_args():
    """
    Constructs and validates CLI arguments

    :returns: ArgParse object of all arguments
    """
    # Args
    parser = argparse.ArgumentParser()
    # logging
    log_level = parser.add_mutually_exclusive_group()
    log_level.add_argument("--debug", action="store_true",
                           help=("Toggles debug mode on. "
                               "(Cannot be used with --log-level)"
                               ))
    log_level.add_argument("--log-level", default="INFO",
                           choices=_nameToLevel.keys(),
                           help=("Toggles logger level. "
                               "(Cannot be used with --debug)"
                               ))
    parser.add_argument("--log-file", default=None, help="File to log to")
    # Contents output
    parser.add_argument("--output", default="transfer-info",
                        help="Output file for the transfer data")
    parser.add_argument("--output-type", default="csv",
                        choices=Output_Types.get_names(),
                        help="Filetype to save data in")
    parser.add_argument("--minify", action="store_true",
                        help="Minify's the file contents " +
                        "(only works with JSON output)")
    # Read in options
    parser.add_argument("--in-file", default=None,
                        help=("File to read from instead of scraping fresh."
                            "  Used for converting into different formats"
                            ))
    parser.add_argument("--in-file-type", default=None,
                        choices=Output_Types.get_names(),
                        help="Filetype of '--in-file', defaults to extension")
    parser_args = parser.parse_args()
    return convert_args(parser_args)


def initialize_logging_manager(log_file: str = None, log_level: str = INFO):
    """
    Initializes the logger with everything needed
    """
    LoggerManager(log_file=log_file, log_level=log_level)


def main():
    # Get CLI args
    args = form_cli_args()
    # Initialize logger
    if args.debug:
        args.log_level = DEBUG
    initialize_logging_manager(args.log_file, args.log_level)
    log = Logger("main")
    log.debug("Starting banwebScrape.py")
    files = File_Utils()

    out_file = "{filename}.{extension}".format(filename=args.output,
                                               extension=args.output_type)
    log.info("Preparing to write data to {}".format(out_file))
    if args.in_file:
        # no scrape, load from file
        if path.exists(args.in_file):
            if args.in_file_type == Output_Types.CSV:
                class_list = files.read_from_csv_to_Class_Obj_List(
                        args.in_file)
            elif args.in_file_type == Output_Types.JSON:
                class_list = files.read_from_json_to_Class_Obj_List(
                        args.in_file)
        else:
            log.error("File {} not found.".format(args.in_file))
            exit(2)
    else:
        class_list = Data_Gathering().get_course_object_list()
        log.info("Data finished writing")

    if args.output_type == Output_Types.CSV:
        files.write_to_csv(class_list, out_file)
    elif args.output_type == Output_Types.JSON:
        files.write_to_json(class_list, out_file, args.minify)


if __name__ == "__main__":
    main()
