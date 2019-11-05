from course_viewer.models import (
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
    course_mtu_course_id = serializers.CharField(
                                source='course_mtu_course_id.mtu_course_id',
                                read_only=True)
    course_mtu_course_subject = serializers.CharField(
                                source='course_mtu_course_id.mtu_subject',
                                read_only=True)
    course_college_code = serializers.CharField(
                                source='course_college_code.college_code',
                                read_only=True)
    course_college_name = serializers.CharField(
                                source='course_college_code.college_name',
                                read_only=True)
    course_state_name = serializers.CharField(
                                source='course_state_code.state_name',
                                read_only=True)
    course_state_code = serializers.CharField(
                                source='course_state_code.state_code',
                                read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class MTUCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MTUCourse
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'
