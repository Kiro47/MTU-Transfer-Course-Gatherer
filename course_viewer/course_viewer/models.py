from django.db import models


class State(models.Model):
    '''
    The Transfer State
    '''
    state_code = models.CharField(
                    max_length=2,
                    unique=True,
                    help_text='The abbreviation of the transfer college state')

    state_name = models.CharField(
                    max_length=200,
                    unique=True,
                    help_text='The long name of the transfer college state')


class College(models.Model):
    '''
    The Transfer College
    '''
    college_code = models.CharField(
                    max_length=15,
                    unique=True,
                    help_text='The code of the transfer college')
    college_name = models.CharField(
                        max_length=50,
                        help_text='The name of the transfer college')


class Course(models.Model):
    '''
    The Transfer Course
    '''
    course_name = models.CharField(
                        max_length=50,
                        help_text='The name of the transfer course')
    course_id = models.CharField(
                        max_length=15,
                        help_text='The id of the transfer course')
    course_credit = models.IntegerField()
    course_number = models.IntegerField()
    MTU_course_crn = models.ForeignKey('MTUCourse',
                                       related_name='mtu_course_crn',
                                       on_delete=models.CASCADE)


class MTUCourse(models.Model):
    '''
    The MTU Course
    '''
    mtu_course_name = models.CharField(
                            max_length=50,
                            help_text='The name of the MTU course')
    mtu_subject = models.CharField(
                        max_length=50,
                        help_text='The subject of the MTU course')
    mtu_credits = models.IntegerField()
