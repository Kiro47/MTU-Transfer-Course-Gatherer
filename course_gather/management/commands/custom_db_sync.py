from django.core.management.base import BaseCommand
from course_gather.models import (
    College,
    Course,
    MTUCourse,
    State
)
from pathlib import Path
import csv


class Command(BaseCommand):
    """
    Command class for custom db sync
    """
    def add_arguments(self, parser):
        """
        Adds custom arguments to read from CLI. Required by Django.

        :parser: ArgParse parser
        """
        parser.add_argument('file_path', type=Path)

    def handle(self, *args, **options):
        """
        Handle function required by Django.
        This gets the ball rolling per se in that it calls the add_sub_tables
        function, passing in the data dictionary parsed from the CSV file from
        banwebScrape.

        :*args: Arguments variable to satisfy Django. Unused
        :**options: Dictionary of passed in values to arguments
        """
        file_path = options['file_path']
        desired_lines = list()
        try:
            with open(file_path, 'r') as csv_file:
                for line in csv_file.readlines()[1:]:
                    desired_lines.append(line.strip('\n'))
        except FileNotFoundError as e:
            print(f'Error: {e}')

        data = self.create_dicts(desired_lines)
        self.add_sub_tables(data)

    def create_dicts(self, desired_lines):
        """
        Creates the data dictionary of key value pairs obtained from the
        CSV file

        :desired_lines: List of lines from the CSV file excluding the header

        :returns: List of dictionary entries that represent each row from the
                  CSV file
        """
        keys = [
            'transfering_state_code',
            'transfering_state_name',
            'transfering_college_code',
            'transfering_college_name',
            'transfering_subject',
            'transfering_number',
            'transfering_credits',
            'MTU_class_name',
            'MTU_subject',
            'MTU_number',
            'MTU_credits']
        dict_list = list()
        for x in csv.reader(desired_lines, quotechar='"', delimiter=',',
                            quoting=csv.QUOTE_ALL, skipinitialspace=True):
            dict_list.append(dict(zip(keys, x)))
        return dict_list

    def add_sub_tables(self, data):
        """
        Calls the respective function for every table in the database.
        Every table uses sets to ensure uniqueness, but still allows very
        slight differences.
        :data: The list of dictionaries to then pass into the sub functions.
        """
        self.add_transfer_states(data)
        self.add_transfer_colleges(data)
        self.add_mtu_courses(data)
        self.add_courses(data)

    def add_courses(self, data):
        """
        Adds the entries for the Courses table via Django models.
        THIS MUST BE CALLED LAST.

        :data: List of dictionaries that contain the CSV data
        """
        for entry in data:
            transfer_state_code = entry['transfering_state_code']
            transfer_college_code = entry['transfering_college_code']
            transfer_course_number = entry['transfering_number']
            transfering_credits = entry['transfering_credits']
            try:
                transfering_credits = float(entry['transfering_credits'])
            except ValueError:
                transfering_credits = 0.0

            mtu_equiv = entry['MTU_number']
            mtu_subject = entry['MTU_subject']
            mtu_course_name = entry['MTU_class_name']
            try:
                mtu_credits = float(entry['MTU_credits'])
            except ValueError:
                mtu_credits = 0.0
            Course.objects.update_or_create(
                    transfer_course_state_code=State.objects.get(
                                               state_code=transfer_state_code),
                    transfer_course_college_code=College.objects.get(
                                           college_code=transfer_college_code),
                    mtu_equiv=MTUCourse.objects.get(
                                            mtu_course_id=mtu_equiv,
                                            mtu_subject=mtu_subject,
                                            mtu_course_name=mtu_course_name,
                                            mtu_credits=mtu_credits),
                    transfer_course_number=transfer_course_number,
                    transfer_course_credit=transfering_credits)

    def add_mtu_courses(self, data):
        """
        Adds the MTUCourse table entries via Django models.

        :data: List of dictionaries that contain the CSV data
        """
        mtu_course_set = set()
        for entry in data:
            class_number = entry['MTU_number']
            class_name = entry['MTU_class_name']
            class_subject = entry['MTU_subject']
            try:
                class_credits = float(entry['MTU_credits'].replace('"', ''))
            except (KeyError, ValueError):
                class_credits = 0

            class_tuple = tuple([class_number, class_name,
                                 class_subject, class_credits])
            mtu_course_set.add(class_tuple)

        for x in mtu_course_set:
            MTUCourse.objects.update_or_create(
                                            mtu_course_id=x[0],
                                            mtu_course_name=x[1],
                                            mtu_subject=x[2],
                                            mtu_credits=x[3])

    def add_transfer_colleges(self, data):
        """
        Adds the College table entries via Django models.

        :data: List of dictionaries that contain the CSV data
        """
        college_set = set()
        for entry in data:
            college_code = entry['transfering_college_code']
            college_name = entry['transfering_college_name']
            college_set.add(tuple([college_code, college_name]))
        for x in college_set:
            College.objects.update_or_create(college_code=x[0],
                                             college_name=x[1])

    def add_transfer_states(self, data):
        """
        Adds the State table entries via Django models.

        :data: List of dictionaries that contain the CSV data
        """
        state_set = set()
        for entry in data:
            state_code = entry['transfering_state_code']
            state_name = entry['transfering_state_name']
            state_set.add(tuple([state_code, state_name]))

        for x in state_set:
            State.objects.update_or_create(state_code=x[0], state_name=x[1])
