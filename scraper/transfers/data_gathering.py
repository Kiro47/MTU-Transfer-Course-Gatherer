#!/usr/bin/env python3

from .data_scraping import get_colleges_from_state, get_courses_from_college, \
    get_state_mapping
from .data_types import College_Object


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
