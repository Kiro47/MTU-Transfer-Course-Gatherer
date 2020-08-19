from django.db import models


class Location(models.Model):
    '''
    The Transfer State
    '''
    location_code = models.CharField(
                    max_length=2,
                    unique=True,
                    help_text='The abbreviation of the \
                    transfer college location')

    location_name = models.CharField(
                    max_length=200,
                    unique=True,
                    help_text='The long name of the transfer college location')

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['location_code']
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        db_table = 'locations'


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
    mtu_equiv = models.ForeignKey(
                'MTUCourse',
                related_name='mtu_equiv',
                on_delete=models.CASCADE,
                help_text='The MTU course associated with the transfer course')
    transfer_course_college_code = models.ForeignKey(
                            'College',
                            related_name='transfer_course_college_code',
                            on_delete=models.CASCADE,
                            help_text='The college that the course is at')
    transfer_course_location_code = models.ForeignKey(
                            'Location',
                            related_name='transfer_course_location_code',
                            on_delete=models.CASCADE,
                            help_text='The location the course is located in')

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
