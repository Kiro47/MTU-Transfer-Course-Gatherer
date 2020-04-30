#!/usr/bin/env python3

import csv

from .data_types import Class_Object
from ..Logger import Logger


class File_Utils(object):

    """
    File utilities for writing and reading data from files
    """

    def __init__(self):
        """
        Blank init
        """
        self.log = Logger(self.__class__.__name__)

    def write_to_csv(self, class_obj_list, output_file_name):
        """
        Writes the class_obj_list to a a value quoted CSV file

        :class_obj_list: Class Object list to get data from
        :output_file_name: Name of the file to write to

        :returns: None
        """
        with open(output_file_name, 'w') as csv_file:
            field_names = [
                'Transfering State Code', 'Transfering State Name',
                "Transfering College Code", "Transfering College Name",
                "Transfering Subject", "Transfering Course Number",
                "Transfering Credits", "MTU Class Name", "MTU Subject",
                "MTU Course Number", "MTU Credits"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names,
                                    quoting=csv.QUOTE_ALL)

            writer.writeheader()
            for course in class_obj_list:
                writer.writerow(course.toDict())

    def read_from_csv(self, input_file_name):
        """
        Reads a CSV file and outputs the contents

        :input_file_name: File to read from

        :returns: None
        """
        with open(input_file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            self.log.debug("Reading CSV from [{}]".format(input_file_name))
            for row in csv_reader:
                print('"{}"'.format('", "'.join(row)))

    def read_from_csv_to_Class_Obj_List(self, input_file_name):
        """
        Reads from a file and returns a list of Class_Object's to rebuild data

        :input_file_name: File to read from

        :returns: A list of ClassObjects
        """
        class_obj_list = list()
        with open(input_file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_class_obj = Class_Object(
                    row['Transfering State Code'],
                    row['Transfering State Name'],
                    row["Transfering College Code"],
                    row["Transfering College Name"],
                    row["Transfering Subject"],
                    row["Transfering Course Number"],
                    row["Transfering Credits"],
                    row["MTU Class Name"],
                    row["MTU Subject"],
                    row["MTU Course Number"],
                    row["MTU Credits"]
                )
                class_obj_list.append(new_class_obj)
        return class_obj_list
