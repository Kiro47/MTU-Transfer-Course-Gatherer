from course_gather.models import (
    College,
    TransferCourse,
    MTUCourse,
    Location
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


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class TransferCourseSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(source='mtu_equiv.mtu_course_id')
    course_name = serializers.CharField(source='mtu_equiv.mtu_course_name')
    course_subject = serializers.CharField(source='mtu_equiv.mtu_subject')
    course_credits = serializers.CharField(source='mtu_equiv.mtu_credits')
    transfer_college = serializers.CharField(
                            source='transfer_course_college_code.college_name')
    transfer_location = serializers.CharField(
                        source='transfer_course_location_code.location_name')

    class Meta:
        model = TransferCourse
        fields = ['id', 'course_id', 'course_name', 'course_subject',
                  'course_credits', 'transfer_course_credit',
                  'transfer_course_number', 'transfer_college',
                  'transfer_location']
