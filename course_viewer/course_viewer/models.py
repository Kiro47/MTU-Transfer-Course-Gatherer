from django.db import models


class State(models.Model):
    '''
    The Transfer State
    '''
    state_code = models.CharField(max_length=2,
                                  help_text='',
                                  unique=True)
    state_name = models.CharField(max_length=200,
                                  unique=True)


class College(models.Model):
    '''
    The Transfer College
    '''
    college_code = models.CharField(max_length=15,
                                    help_text='',
                                    unique=True)
    college_name = models.CharField(max_length=200,
                                    unique=True)


class Course(models.Model):
    '''
    The Transfer Course
    '''
    course_name = models.CharField(max_length=200)
    course_credit = models.IntegerField()
    course_number = models.IntegerField()
    MTU_course_crn = models.ForeignKey('MTUCourse',
                                       on_delete=models.CASCADE)


class MTUCourse(models.Model):
    '''
    The MTU Course
    '''
    mtu_course_name = models.IntegerField()
    mtu_subject = models.CharField(max_length=200)
    mtu_crn = models.IntegerField()
    mtu_credits = models.IntegerField()
