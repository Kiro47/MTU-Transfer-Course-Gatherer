from course_gather.models import (
    College,
    Course,
    MTUCourse,
    State
)
from django_filters import rest_framework as filters


class CollegeFilter(filters.FilterSet):
    college_code = filters.CharFilter(field_name='college_code',
                                      lookup_expr='icontains')
    college_name = filters.CharFilter(field_name='college_name',
                                      lookup_expr='icontains')

    class Meta:
        model = College
        fields = ['college_code',
                  'college_name']


class CourseFilter(filters.FilterSet):
    transfer_course_credit = filters.NumberFilter(
                                        field_name='transfer_course_credit',
                                        lookup_expr='icontains')
    transfer_course_number = filters.CharFilter(
                                        field_name='transfer_course_number',
                                        lookup_expr='icontains')
    mtu_equiv = filters.CharFilter(field_name='mtu_equiv',
                                   lookup_expr='icontains')
    transfer_course_college_code = filters.CharFilter(
                                    field_name='transfer_course_college_code',
                                    lookup_expr='icontains')
    transfer_course_state_code = filters.CharFilter(
                                    field_name='transfer_course_state_code',
                                    lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['transfer_course_credit', 'transfer_course_number',
                  'mtu_equiv', 'transfer_course_college_code',
                  'transfer_course_state_code']


class MTUCourseFilter(filters.FilterSet):

    mtu_course_id = filters.CharFilter(field_name='mtu_course_id',
                                       lookup_expr='icontains')
    mtu_course_name = filters.CharFilter(field_name='mtu_course_name',
                                         lookup_expr='icontains')
    mtu_subject = filters.CharFilter(field_name='mtu_subject',
                                     lookup_expr='icontains')
    mtu_credits = filters.NumberFilter(field_name='mtu_credits',
                                       lookup_expr='icontains')

    class Meta:
        model = MTUCourse
        fields = ['mtu_course_id', 'mtu_course_name',
                  'mtu_subject', 'mtu_credits']


class StateFilter(filters.FilterSet):
    state_code = filters.CharFilter(field_name='state_code',
                                    lookup_expr='icontains')
    state_name = filters.CharFilter(field_name='state_name',
                                    lookup_expr='icontains')

    class Meta:
        model = State
        fields = ['state_code',
                  'state_name']
