from course_gather.models import (
    College,
    Course,
    MTUCourse,
    State,
)

from course_gather.serializers import (
    CollegeSerializer,
    CourseSerializer,
    MTUCourseSerializer,
    StateSerializer
)

from course_gather.filters import (
    CollegeFilter,
    CourseFilter,
    MTUCourseFilter,
    StateFilter
)

from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters


class StateViewSet(ReadOnlyModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    filterset_class = StateFilter
    filter_backends = (filters.DjangoFilterBackend,)


class CollegeViewSet(ReadOnlyModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
    filterset_class = CollegeFilter
    filter_backends = (filters.DjangoFilterBackend,)


class CourseViewSet(ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().select_related(
                                           'mtu_equiv',
                                           'transfer_course_college_code',
                                           'transfer_course_college_code',
                                           'transfer_course_state_code',
                                           'transfer_course_state_code')
    filterset_class = CourseFilter
    filter_backends = (filters.DjangoFilterBackend,)


class MTUCourseViewSet(ReadOnlyModelViewSet):
    serializer_class = MTUCourseSerializer
    queryset = MTUCourse.objects.all()
    filterset_class = MTUCourseFilter
    filter_backends = (filters.DjangoFilterBackend,)
