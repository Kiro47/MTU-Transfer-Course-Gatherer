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
    mtu_course_crn = models.CharField(
                            max_length=50,
                            help_text='The CRN of the MTU course')
    mtu_course_subject = models.CharField(
                        max_length=50,
                        help_text='The subject of the MTU course')
    mtu_course_id = models.CharField(
                        max_length=10,
                        help_text='The course ID of the MTU course')
    mtu_course_section = models.CharField(
                            max_length=3,
                            help_text='The section of the MTU course')
    mtu_course_campus = models.CharField(
                            max_length=2,
                            default="1",
                            help_text='The campus code of the MTU course')
    mtu_course_credits = models.FloatField(
                        blank=True,
                        help_text='The amount of credits the MTU course is')
    mtu_course_name = models.CharField(
                            max_length=50,
                            help_text='The Name of the MTU course')
    mtu_course_days = models.CharField(
                            max_length=7,
                            help_text='The days the class is scheduled for')
    mtu_course_time = models.CharField(
                            max_length=40,
                            help_text='The hours the MTU course runs')
    mtu_course_capacity = models.IntegerField(
                            help_text='The capacity of the class')
    mtu_course_capacity_enrolled = models.IntegerField(
                            help_text='The amount of students currently \
                            enrolled in the course')
    mtu_course_capacity_remaining = models.IntegerField(
                            help_text='The seats remaining in the course')
    mtu_course_instructor = models.CharField(
                            max_length=60,
                            help_text='The last name of the professor(s) \
                            teaching the course')
    mtu_course_duration = models.CharField(
                            max_length=30,
                            help_text='The date range the class runs')
    mtu_course_location = models.CharField(
                            max_length=10,
                            help_text='The MTU building location code the \
                            class is located in')
    mtu_course_fee = models.CharField(
                            max_length=80,
                            help_text='The fee associated with the course')

    def __str__(self):
        return self.mtu_course_id

    class Meta:
        ordering = ['mtu_course_id']
        verbose_name = 'MTUCourse'
        verbose_name_plural = 'MTUCourses'
        db_table = 'mtu_courses'
