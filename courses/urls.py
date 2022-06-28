from django.urls import path


from .views import CourseApiView, AverageApiView

urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses'),
    path('averages/', AverageApiView.as_view(), name='averages')
]
