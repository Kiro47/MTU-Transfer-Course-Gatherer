from course_gather.models import (
    College,
    TransferCourse,
    MTUCourse,
    Location,
)

from course_gather.serializers import (
    CollegeSerializer,
    TransferCourseSerializer,
    MTUCourseSerializer,
    LocationSerializer
)

from course_gather.filters import (
    CollegeFilter,
    TransferCourseFilter,
    MTUCourseFilter,
    LocationFilter
)

from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters


class LocationViewSet(ReadOnlyModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filterset_class = LocationFilter
    filter_backends = (filters.DjangoFilterBackend,)


class CollegeViewSet(ReadOnlyModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
    filterset_class = CollegeFilter
    filter_backends = (filters.DjangoFilterBackend,)


class TransferCourseViewSet(ReadOnlyModelViewSet):
    serializer_class = TransferCourseSerializer
    queryset = TransferCourse.objects.all()
    filterset_class = TransferCourseFilter
    filter_backends = (filters.DjangoFilterBackend,)


class MTUCourseViewSet(ReadOnlyModelViewSet):
    serializer_class = MTUCourseSerializer
    queryset = MTUCourse.objects.all()
    filterset_class = MTUCourseFilter
    filter_backends = (filters.DjangoFilterBackend,)
