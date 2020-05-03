#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from singleton_decorator import singleton

from .data_types import Class_Object
from ..Logger import Logger

URL_Base = "https://www.banweb.mtu.edu/owassb/mtu_transfer_detail."
URL_State = URL_Base + "P_TRNS_STATE"
URL_School = URL_Base + "P_TRNS_SCHOOL"
URL_Transcript = URL_Base + "P_TRNS_FULL"


@singleton
class Data_Scraping(object):

    """
    Class containing methods for scraping data from Banweb
    """

    def __init__(self):
        """
        Initializer for Data_Scraping object

        primarily exists for logging initialization
        """
        self.log = Logger(self.__class__.__name__)

    def get_state_mapping(self):
        """
        Get a list of states from MTU's banweb course transfer database

        :returns: A Dictioary of State Codes with their State Value
        """
        req = requests.get(URL_State)
        soup = BeautifulSoup(req.text, 'html5lib')
        content = soup.find("select", {"name": "state_code"})
        options = content.select('option[value]')
        state_dict = dict()
        for item in options:
            state_dict.update({
                item.get("value"): item.text.replace("\n", "")
            })
        return state_dict

    def get_colleges_from_state(self, state_code):
        """
        Gathers course data from the MTU Banweb database for the specified
        state and generates a dictionary of Colleges associated with a state

        :state_code: The code of the state to gather colleges from

        :returns: A Dictionary of college IDs  with an associated College Name
        """
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
        return college_dict

    def get_courses_from_college(self, college_object_list):
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
                    self.log.warning("Following row was not of length 7 \
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
