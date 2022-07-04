from django.urls import path


from .views import CourseApiView, CoursesApiView, AverageApiView, AveragesApiView

urlpatterns = [
    path('courses/', CoursesApiView.as_view(), name='courses'),
    path('averages/', AveragesApiView.as_view(), name='averages'),
    path('courses/<uuid:pk>/', CourseApiView.as_view(), name='course'),
    path('averages/<uuid:pk>/', AverageApiView.as_view(), name='average')
]
