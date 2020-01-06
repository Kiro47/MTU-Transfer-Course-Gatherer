#!/usr/bin/env python3

from bs4 import BeautifulSoup
import csv
import requests

URL_Base = "https://www.banweb.mtu.edu/owassb/mtu_transfer_detail."
URL_State = URL_Base + "P_TRNS_STATE"
URL_School = URL_Base + "P_TRNS_SCHOOL"
URL_Transcript = URL_Base + "P_TRNS_FULL"

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
total_bytes_transfered = 0


class Class_Object(object):

    """
    Object containing relational information between transferable classes
    and MTU's counts for them.
    """

    transfering_state_code = ""
    transfering_state_name = ""
    transfering_college_code = ""
    transferring_college_name = ""
    transfering_subject = ""
    transfering_number = ""
    transfering_credits = ""
    MTU_class_name = ""
    MTU_subject = ""
    MTU_number = ""
    MTU_credits = ""

    def __init__(
            self,
            transfering_state_code, transfering_state_name,
            transfering_college_code, transferring_college_name,
            transfering_subject, transfering_number,
            transfering_credits, MTU_class_name, MTU_subject,
            MTU_number, MTU_credits):
        """
        Initializer for the Class_Object containing all data
        """
        self.transfering_state_code = transfering_state_code
        self.transfering_state_name = transfering_state_name
        self.transfering_college_code = transfering_college_code
        self.transferring_college_name = transferring_college_name
        self.transfering_subject = transfering_subject
        self.transfering_number = transfering_number
        self.transfering_credits = transfering_credits
        self.MTU_class_name = MTU_class_name
        self.MTU_subject = MTU_subject
        self.MTU_number = MTU_number
        self.MTU_credits = MTU_credits

    def __str__(self):
        """
        Converts Class_Object into a human readable string
        """
        return ("Transfering State Code: {}\nTransfering State Name: {}\n"
                "Transfering College Code: {}\nTransfering College Name: {}\n"
                "Transfering Subject: {}\nTransfering Course Number: {}\n"
                "Transfering Credits: {}\nMTU Class Name: {}\n"
                "MTU Subject: {}\nMTU Course Number: {}\nMTU Credits: {}"
                ).format(
            self.transfering_state_code, self.transfering_state_name,
            self.transfering_college_code, self.transferring_college_name,
            self.transfering_subject, self.transfering_number,
            self.transfering_credits, self.MTU_class_name, self.MTU_subject,
            self.MTU_number, self.MTU_credits)

    def toCSV(self):
        """
        Converts Class_Object to a CSV row entry with values quoted
        """
        return '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"\n'.format(
                self.transfering_state_code, self.transfering_state_name,
                self.transfering_college_code, self.transferring_college_name,
                self.transfering_subject, self.transfering_number,
                self.transfering_credits, self.MTU_class_name,
                self.MTU_subject, self.MTU_number, self.MTU_credits
            )

    def toDict(self):
        """
        Converts Class_Object to a dictionary
        """
        return {
                'Transfering State Code': self.transfering_state_code,
                'Transfering State Name': self.transfering_state_name,
                "Transfering College Code": self.transfering_college_code,
                "Transfering College Name": self.transferring_college_name,
                "Transfering Subject": self.transfering_subject,
                "Transfering Course Number": self.transfering_number,
                "Transfering Credits": self.transfering_credits,
                "MTU Class Name": self.MTU_class_name,
                "MTU Subject": self.MTU_subject,
                "MTU Course Number": self.MTU_number,
                "MTU Credits": self.MTU_credits
                }


class College_Object(object):

    """
    Object containg relational information about a college, it's state
    and a list of it's classes.
    """

    college_code = ""
    college_name = ""
    college_state_code = ""
    college_state_name = ""
    class_list = None

    def __init__(
            self, college_code, college_name, college_state_code,
            college_state_name):
        """
        Initialization of a college Object
        """
        self.college_code = college_code
        self.college_name = college_name
        self.college_state_code = college_state_code
        self.college_state_name = college_state_name
        self.class_list = list()

    def __str__(self):
        """
        Prints a course to a human readable string
        """
        return (
                "College Code: {}\nCollege Name: {}\n"
                "State Code: {}\nState Name: {}\nClass List: [{}]\n"
                ).format(
                        self.college_code, self.college_name,
                        self.college_state_code, self.college_state_name,
                        self.class_list
                        )


class File_Utils(object):

    """
    File utilities for writing and reading data from files
    """

    def __init__(self):
        """
        Blank init
        """

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


def get_state_mapping():
    """
    Get a list of states from MTU's banweb course transfer database

    :returns: A Dictioary of State Codes with their State Value
    """
    req = requests.get(URL_State)
    global total_bytes_transfered
    total_bytes_transfered += len(req.content)
    soup = BeautifulSoup(req.text, 'html5lib')
    content = soup.find("select", {"name": "state_code"})
    options = content.select('option[value]')
    state_dict = dict()
    for item in options:
        state_dict.update({
            item.get("value"): item.text.replace("\n", "")
        })
    return state_dict


def get_colleges_from_state(state_code):
    """
    Gathers course data from the MTU Banweb database for the specified
    state and generates a dictionary of Colleges associated with a state

    :state_code: The code of the state to gather colleges from

    :returns: A Dictionary of college IDs  with an associated College Name
    """
    data = {"state_code": state_code}
    req = requests.post(URL_School, data)
    global total_bytes_transfered
    total_bytes_transfered += len(req.content)
    soup = BeautifulSoup(req.text, 'html5lib')
    content = soup.find("select", {"name": "SBGI_CODE"})
    options = content.select('option[value]')
    college_dict = dict()
    for item in options:
        college_dict.update({
            item.get("value"): item.text.replace("\n", "")
        })
    return college_dict


def get_courses_from_college(college_object_list):
    """
    Gathers course data from the MTU Banweb database for the specified
    Colleges and stored it inside the associated College Objct

    :college_object_list: A list of College Objects to store data into

    :returns: None
    """
    for college_obj in college_object_list:
        data = {
                "SBGI_CODE": college_obj.college_code,
                "state": college_obj.college_state_code
                }
        req = requests.post(URL_Transcript, data)
        global total_bytes_transfered
        total_bytes_transfered += len(req.content)
        soup = BeautifulSoup(req.text, "html5lib")
        # There's no IDs or classes for the tables only CSS padding
        # pray they never change the layout
        table = soup.table.table
        # DEBUG: strip out the CSS so I can actually read this
        for tag in table.findAll(True):
            for attribute in ["bgcolor", "style", "nowrap"]:
                del tag[attribute]
        table_rows = table.find_all('tr')
        # First two rows are just identifiers we don't care about
        for row in table_rows[2::]:
            table_columns = row.find_all('td')
            if len(table_columns) != 7:
                print("Following row was not of length 7 \
                issues may occur, skipping. [{}]".format(row))
                continue
            Oth_Subj = table_columns[0].find(text=True)
            Oth_Numb = table_columns[1].find(text=True)
            Oth_Cred = table_columns[2].find(text=True)
            MTU_Name = table_columns[3].find(text=True)
            MTU_Subj = table_columns[4].find(text=True)
            MTU_Numb = table_columns[5].find(text=True)
            MTU_Cred = table_columns[6].find(text=True)
            college_obj.class_list.append(
                    Class_Object(
                        college_obj.college_state_code,
                        college_obj.college_state_name,
                        college_obj.college_code,
                        college_obj.college_name,
                        Oth_Subj, Oth_Numb, Oth_Cred,
                        MTU_Name, MTU_Subj, MTU_Numb, MTU_Cred
                        )
                    )
    return None


def get_college_object_list(state_mapping):
    """
    Gathers a list of College Objects from MTU's Banweb database

    :state_mapping: A Dictionary of State Codes to State Names

    :returns: A list of College Objects
    """
    college_obj_list = list()
    for state_code, state_name in state_mapping.items():
        colleges_from_state = get_colleges_from_state(state_code)
        for college_code, college_name in colleges_from_state.items():
            college_obj_list.append(
                    College_Object(
                        college_code, college_name,
                        state_code, state_name
                    )
                    )
    return college_obj_list


def college_obj_list_to_class_obj_list(college_obj_list):
    """
    Converts a compiled College Object list into a more flat and
    usable overall College Course List

    :college_obj_list: List of College Objects to parse from

    :returns: A List of Course Objects
    """
    class_obj_list = list()
    for college_obj in college_obj_list:
        class_obj_list.extend(college_obj.class_list)
    return class_obj_list


def get_course_object_list():
    """
    Gathers live data from the MTU Banweb DB for classes
    and stores it into a list of Course Objects

    :returns: List of Course Objects
    """
    print("Acquiring state map")
    state_mapping = get_state_mapping()
    print("Mapping colleges to states")
    college_obj_list = get_college_object_list(state_mapping)
    print("Getting course data from colleges")
    get_courses_from_college(college_obj_list)
    return college_obj_list_to_class_obj_list(college_obj_list)


def main():
    files = File_Utils()
    files.write_to_csv(get_course_object_list(), "/tmp/writer.csv")
    global total_bytes_transfered
    print("Bytes wasted: {}".format(
        total_bytes_transfered))


if __name__ == "__main__":
    main()
