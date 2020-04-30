#!/usr/bin/env python3

from scraper.transfers.file_utils import File_Utils
from scraper.transfers.data_gathering import get_course_object_list

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


def main():
    files = File_Utils()
    files.write_to_csv(get_course_object_list(), "./writer.csv")
    # global total_bytes_transfered
    # print("Bytes wasted: {}".format(
    #     total_bytes_transfered))


if __name__ == "__main__":
    main()
