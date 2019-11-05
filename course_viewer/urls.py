"""course_viewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from course_viewer.viewsets import (
    CollegeViewSet,
    CourseViewSet,
    MTUCourseViewSet,
    StateViewSet
)
router = DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'mtu-courses', MTUCourseViewSet)
router.register(r'states', StateViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/')),
    path('api/', include((router.urls, 'course_viewer'), namespace='views'))
]
