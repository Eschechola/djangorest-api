from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    # CourseApiView,
    # CoursesApiView,
    # AverageApiView,
    # AveragesApiView,
    CourseViewSet,
    AverageViewSet)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('averages', AverageViewSet)

# urlpatterns = [
#     path('courses/', CoursesApiView.as_view(), name='courses'),
#     path('courses/<uuid:course_pk>/', CourseApiView.as_view(), name='course'),
#     path('courses/<uuid:course_pk>/averages', AveragesApiView.as_view(), name='courses_averages'),
#     path('courses/<uuid:course_pk>/average/<uuid:average_pk>/', AverageApiView.as_view(), name='course_average'),

#     path('averages/', AveragesApiView.as_view(), name='averages'),
#     path('averages/<uuid:pk>/', AverageApiView.as_view(), name='average')
# ]
