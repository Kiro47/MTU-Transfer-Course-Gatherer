#!/usr/bin/env

from singleton_decorator import singleton

from .data_scraping import Data_Scraping
from .data_types import College_Object
from ..Logger import Logger


@singleton
class Data_Gathering(object):
    """
    Class containing methods for gathering data from Data_Scraping
    """

    def __init__(self):
        """
        Initializer for Data_Gathering object

        primarily exists for logging initialization
        """
        self.log = Logger(self.__class__.__name__)

    def get_college_object_list(self, state_mapping):
        """
        Gathers a list of College Objects from MTU's Banweb database

        :state_mapping: A Dictionary of State Codes to State Names

        :returns: A list of College Objects
        """
        # Singleton checks are very cheap, but when we're recalling it this
        # many times over, variable assignment is cheaper.
        scrape = Data_Scraping()
        college_obj_list = list()
        for state_code, state_name in state_mapping.items():
            colleges_from_state = scrape.get_colleges_from_state(state_code)
            for college_code, college_name in colleges_from_state.items():
                college_obj_list.append(
                    College_Object(
                        college_code, college_name,
                        state_code, state_name
                    )
                )
        return college_obj_list

    def college_obj_list_to_class_obj_list(self, college_obj_list):
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

    def get_course_object_list(self):
        """
        Gathers live data from the MTU Banweb DB for classes
        and stores it into a list of Course Objects

        :returns: List of Course Objects
        """
        self.log.info("Acquiring state map")
        state_mapping = Data_Scraping().get_state_mapping()
        self.log.info("Mapping colleges to states")
        college_obj_list = self.get_college_object_list(state_mapping)
        self.log.info("Getting course data from colleges")
        Data_Scraping().get_courses_from_college(college_obj_list)
        return self.college_obj_list_to_class_obj_list(college_obj_list)
