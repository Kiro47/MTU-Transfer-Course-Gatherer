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

    class Meta:
        ordering = ['state_code']
        verbose_name = 'state'
        verbose_name_plural = 'states'
        db_table = 'states'


class College(models.Model):
    '''
    The Transfer College
    '''
    college_code = models.CharField(
                    max_length=15,
                    primary_key=True,
                    help_text='The code of the transfer college')
    college_name = models.CharField(
                        max_length=50,
                        help_text='The name of the transfer college')

    def __str__(self):
        return self.college_name

    class Meta:
        ordering = ['college_code']
        verbose_name = 'college'
        verbose_name_plural = 'colleges'
        db_table = 'colleges'


class Course(models.Model):
    '''
    The Transfer Course
    '''
    transfer_course_credit = models.FloatField(
                    blank=True,
                    help_text='The number of credits the transfer course is')
    transfer_course_number = models.CharField(
                        max_length=15,
                        help_text='The course number of the transfer course')
    mtu_equiv_id = models.ForeignKey(
                'MTUCourse',
                related_name='mtu_equiv_id',
                on_delete=models.CASCADE,
                help_text='The MTU course associated with the transfer course')
    transfer_course_college_code = models.ForeignKey(
                            'College',
                            related_name='transfer_course_college_code',
                            on_delete=models.CASCADE,
                            help_text='The college that the course is at')
    transfer_course_state_code = models.ForeignKey(
                            'State',
                            related_name='transfer_course_state_code',
                            on_delete=models.CASCADE,
                            help_text='The state the course is located in')

    def __str__(self):
        return self.transfer_course_number

    class Meta:
        ordering = ['transfer_course_number']
        verbose_name = 'transfer_course'
        verbose_name_plural = 'transfer_courses'
        db_table = 'transfer_courses'


class MTUCourse(models.Model):
    '''
    The MTU Course
    '''
    mtu_course_id = models.CharField(
                            max_length=50,
                            help_text='The id of the MTU course')
    mtu_course_name = models.CharField(
                            max_length=50,
                            help_text='The Name of the MTU course')
    mtu_subject = models.CharField(
                        max_length=50,
                        help_text='The subject of the MTU course')
    mtu_credits = models.FloatField(
                        blank=True,
                        help_text='The amount of credits the MTU course is')

    def __str__(self):
        return self.mtu_course_id

    class Meta:
        ordering = ['mtu_course_id']
        verbose_name = 'MTUCourse'
        verbose_name_plural = 'MTUCourses'
        db_table = 'mtu_courses'
