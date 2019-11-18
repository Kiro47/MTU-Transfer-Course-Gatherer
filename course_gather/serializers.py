from course_gather.models import (
    College,
    Course,
    MTUCourse,
    State
)
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    mtu_equiv_id = serializers.CharField(
                                source='mtu_equiv_id.mtu_course_id',
                                read_only=True)
    mtu_course_subject = serializers.CharField(
                                source='mtu_equiv_id.mtu_subject',
                                read_only=True)
    transfer_college_code = serializers.CharField(
                                source='transfer_college_code.college_code',
                                read_only=True)
    transfer_college_name = serializers.CharField(
                                source='transfer_college_code.college_name',
                                read_only=True)
    transfer_state_name = serializers.CharField(
                                source='transfer_course_state_code.state_name',
                                read_only=True)
    transfer_state_code = serializers.CharField(
                                source='transfer_course_state_code.state_code',
                                read_only=True)

    class Meta:
        model = Course
        fields = ('mtu_equiv_id', 'mtu_course_subject',
                  'transfer_college_code', 'transfer_college_name',
                  'transfer_state_name', 'transfer_state_code',
                  'transfer_course_id', 'transfer_course_credit',
                  'transfer_course_number')


class MTUCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MTUCourse
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'
