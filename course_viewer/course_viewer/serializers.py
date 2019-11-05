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
