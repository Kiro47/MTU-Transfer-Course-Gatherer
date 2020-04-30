#!/usr/bin/env python3

from logging import INFO


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

# Fun stats information
# total_bytes_transfered = 0


def initialize_logging_manager(log_file: str = None, log_level: str = INFO):
    """
    Initializes the logger with everything needed
    """
    LoggerManager(log_file=log_file, log_level=log_level)


def main():
    # Initialize logger
    initialize_logging_manager()
    log = Logger("main")
    log.debug("Starting banwebScrape.py")
    files = File_Utils()
    files.write_to_csv(Data_Gathering().get_course_object_list(),
                       "./writer.csv")
    # global total_bytes_transfered
    # print("Bytes wasted: {}".format(
    #     total_bytes_transfered))


if __name__ == "__main__":
    main()
