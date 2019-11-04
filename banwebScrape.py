#!/usr/bin/python3

from bs4 import BeautifulSoup
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
        return ("Transfering State Code: {}\nTransfering State Name: {}\n"
                "Transfering College Code: {}\nTransfering College Name: {}\n"
                "Transfering Subject: {}\nTransfering Course Number: {}\n"
                "Transfering Credits: {}\nTransfering State Name\n"
                "MTU Class Name: {}\nMTU Subject: {}\n"
                "MTU Course Number: {}\nMTU Credits: {}"
                ).format(
            self.transfering_state_code, self.transfering_state_name,
            self.transfering_college_code, self.transferring_college_name,
            self.transfering_subject, self.transfering_number,
            self.transfering_credits, self.transfering_state_name,
            self.MTU_class_name, self.MTU_subject,
            self.MTU_number, self.MTU_credits)

    def toCSV(self):
        return "{},{},{},{},{},{},{},{},{},{}\n".format(
                self.transfering_state_code, self.transfering_state_name,
                self.transfering_college_code, self.transferring_college_name,
                self.transfering_subject, self.transfering_number,
                self.transfering_credits, self.MTU_class_name,
                self.MTU_subject, self.MTU_number, self.MTU_credits
            )


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
        """
        self.college_code = college_code
        self.college_name = college_name
        self.college_state_code = college_state_code
        self.college_state_name = college_state_name
        self.class_list = list()

    def __str__(self):
        """
        """
        return (
                "College Code: {}\nCollege Name: {}\n"
                "State Code: {}\nClass List: [{}]\n"
                ).format(
                        self.college_code, self.college_name,
                        self.state_code, self.college_state_name,
                        ", ".join(self.class_list)
                        )


def get_state_mapping():
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


def dump_to_csv(college_obj_list, csv_name):
    """
    """
    try:
        csv_file = open(csv_name, "w+")
        print("Dumping to CSV: {}".format(csv_name))
        # Write header in
        csv_file.write(
            "Transfering State Code,Transfering State Name,"
            "Transfering College Code,Transfering College Name,"
            "Transfering Subject,Transfering Course Number,"
            "Transfering Credits,MTU Class Name,"
            "MTU Subject,MTU Course Number,MTU Credits\n")

        for college in college_obj_list:
            for course in college.class_list:
                csv_file.write(course.toCSV())
    except ():
        if csv_file is not None:
            csv_file.close()
    finally:
        csv_file.close()


def main():
    print("Acquiring state map")
    state_mapping = get_state_mapping()
    print("Mapping colleges to states")
    college_obj_list = get_college_object_list(state_mapping)
    print("Getting course data from colleges")
    get_courses_from_college(college_obj_list)
    dump_to_csv(college_obj_list, "/tmp/output.csv")
    global total_bytes_transfered
    print("Bytes wasted: {}".format(
        total_bytes_transfered))


if __name__ == "__main__":
    main()
