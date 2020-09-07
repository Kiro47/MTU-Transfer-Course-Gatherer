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


class ShellCourse(models.Model):
    '''
    Shell object of courses that is the intermediary between
    Courses and MTUCourses
    TransferCourse <=> Shell <=> MTUCourse
    '''
    shell_name = models.CharField(max_length=50,
                                  unique=True,
                                  null=False,
                                  blank=False)
    transfer_courses = models.ManyToManyField('TransferCourse',
                                              related_name='transfer_course',
                                              help_text='Transfer courses')

    mtu_courses = models.ManyToManyField('MTUCourse',
                                         related_name='mtu_course',
                                         help_text='MTU Courses')

    def __str__(self):
        return self.shell_name

    class Meta:
        ordering = ['shell_name']
        verbose_name = 'course_shell'
        verbose_name_plural = 'course_shells'
        db_table = 'course_shells'


class TagCourse(models.Model):
    '''
    Generic Tag model for holding class tags
    '''
    text = models.CharField(max_length=30,
                            null=True,
                            blank=True,
                            help_text='The Tag text')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']
        verbose_name = 'course_tag'
        verbose_name_plural = 'course_tags'
        db_table = 'course_tags'


class TransferCourse(models.Model):
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
                            max_length=3,
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
    mtu_course_fee = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         help_text='The fee cost(USD) \
                                         of a course')
    mtu_course_tags = models.ManyToManyField('TagCourse',
                                             related_name='course_tags',
                                             help_text='Tags that apply to \
                                             the course')

    def __str__(self):
        return self.mtu_course_id

    class Meta:
        ordering = ['mtu_course_id']
        verbose_name = 'MTUCourse'
        verbose_name_plural = 'MTUCourses'
        db_table = 'mtu_courses'
