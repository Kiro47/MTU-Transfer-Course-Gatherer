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

    def __str__(self):
        return self.state_name


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

    def __str__(self):
        return self.college_name


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
    course_credit = models.IntegerField(
                    help_text='The number of credits the transfer course is')
    course_number = models.CharField(
                        max_length=15,
                        help_text='The course number of the transfer course')
    course_mtu_course_id = models.ForeignKey(
                'MTUCourse',
                related_name='course_mtu_course_id',
                on_delete=models.CASCADE,
                help_text='The MTU course associated with the transfer course')
    course_college_code = models.ForeignKey(
                            'College',
                            related_name='course_college_code',
                            on_delete=models.CASCADE,
                            help_text='The college that the course is at')
    course_state_code = models.ForeignKey(
                            'State',
                            related_name='course_state_code',
                            on_delete=models.CASCADE,
                            help_text='The state the course is located in')

    def __str__(self):
        return self.course_name


class MTUCourse(models.Model):
    '''
    The MTU Course
    '''
    mtu_course_id = models.CharField(
                            max_length=50,
                            help_text='The id of the MTU course')
    mtu_subject = models.CharField(
                        max_length=50,
                        help_text='The subject of the MTU course')
    mtu_credits = models.IntegerField(
                        help_text='The amount of credits the MTU course is')

    def __str__(self):
        return self.mtu_course_id
