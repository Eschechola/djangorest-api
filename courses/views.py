from rest_framework import generics

from .models import Course, Average
from .serializers import CourseSerializer, AverageSerializer

class CoursesApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AveragesApiView(generics.ListCreateAPIView):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer


class AverageApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer