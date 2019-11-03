#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

URL_Base = "https://www.banweb.mtu.edu/owassb/mtu_transfer_detail."
URL_State = URL_Base + "P_TRNS_STATE"
URL_School = URL_Base + "P_TRNS_SCHOOL"
URL_Transcript = URL_Base + "P_TRNS_FULL"


class Class_Mapping(object):

    """
    Object containing relational information between transferable classes
    and MTU's counts for them.
    """

    transfering_state_code = ""
    transfering_college_code = ""
    transfering_subject = ""
    transfering_number = ""
    transfering_credits = ""
    MTU_class_name = ""
    MTU_subject = ""
    MTU_number = ""
    MTU_credits = ""

    def __init__(self, transfering_state_code, transfering_college_code,
                 transfering_subject, transfering_number,
                 transfering_credits, MTU_class_name, MTU_subject,
                 MTU_number, MTU_credits):
        """
        """
        self.transfering_state_code = transfering_state_code
        self.transfering_college_code = transfering_college_code
        self.transfering_subject = transfering_subject
        self.transfering_number = transfering_number
        self.transfering_credits = transfering_credits
        self.MTU_class_name = MTU_class_name
        self.MTU_subject = MTU_subject
        self.MTU_number = MTU_number
        self.MTU_credits = MTU_credits

    def __str__(self):
        return ("Transfering State Code: {}\nTransfering College Code: {}\n"
                "Transfering Subject: {}\nTransfering Course Number: {}\n"
                "Transfering Credits: {}\nMTU Class Name: {}"
                "\nMTU Subject: {}\nMTU Course Number: {}\nMTU Credits: {}"
                ).format(
            self.transfering_state_code, self.transfering_college_code,
            self.transfering_subject, self.transfering_number,
            self.transfering_credits, self.MTU_class_name,
            self.MTU_subject, self.MTU_number, self.MTU_credits)


def get_state_mapping():
    req = requests.get(URL_State)
    soup = BeautifulSoup(req.text, 'html5lib')
    content = soup.find("select", {"name": "state_code"})
    options = content.select('option[value]')
    state_dict = dict()
    for item in options:
        state_dict.update({
            item.get("value"): item.text.replace("\n", "")
        })
    return state_dict.items()
# print out mapping
# for tup in get_state_mapping():
#    print(tup)

# dump all state pages


def get_colleges_from_state(state_code):
    data = {"state_code": state_code}
    req = requests.post(URL_School, data)
    soup = BeautifulSoup(req.text, 'html5lib')
    content = soup.find("select", {"name": "SBGI_CODE"})
    options = content.select('option[value]')
    college_dict = dict()
    for item in options:
        college_dict.update({
            item.get("value"): item.text.replace("\n", "")
        })
    return college_dict.items()


def get_courses_from_college(state_code, college_code):
    data = {"SBGI_CODE": college_code, "state": state_code}
    req = requests.post(URL_Transcript, data)
    soup = BeautifulSoup(req.text, 'html5lib')
    # There's no IDs or classes for the tables only CSS padding
    # pray they never change the layout
    table = soup.table.table
    # DEBUG: strip out the CSS so I can actually read this
    for tag in table.findAll(True):
        for attribute in ["bgcolor", "style", "nowrap"]:
            del tag[attribute]
    table_rows = table.find_all('tr')
    class_mapping = None
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
        class_mapping = Class_Mapping(Oth_Subj, Oth_Numb, Oth_Cred,
                                      MTU_Name, MTU_Subj, MTU_Numb, MTU_Cred)
    # This is only returning one mapping atm, should return a list of mapping
    # objects, but not enough time today
    return class_mapping


#    print(table_rows.prettify)


data = {"state_code": "MI"}
req = requests.post(URL_School, data)
print(get_courses_from_college("MI", "001001"))
