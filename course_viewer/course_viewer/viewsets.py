from course_viewer.models import (
    College,
    Course,
    MTUCourse,
    State
)

from course_viewer.serializers import (
    CollegeSerializer,
    CourseSerializer,
    MTUCourseSerializer,
    StateSerializer
)

from rest_framework import viewsets


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CollegeViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class MTUCourseViewSet(viewsets.ModelViewSet):
    serializer_class = MTUCourseSerializer
    queryset = MTUCourse.objects.all()
