#!/usr/bin/env python3


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
                "MTU Subject: {}\nMTU Course Number: {}\nMTU Credits: {}\n\n"
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
