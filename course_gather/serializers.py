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


class MTUCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MTUCourse
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    mtu_equiv = MTUCourseSerializer(read_only=True)
    transfer_course_state_code = StateSerializer(read_only=True)
    transfer_course_college_code = CollegeSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'mtu_equiv', 'transfer_course_credit',
                  'transfer_course_number', 'transfer_course_number',
                  'transfer_course_state_code', 'transfer_course_college_code']
