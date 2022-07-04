from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Course, Average
from .serializers import CourseSerializer, AverageSerializer


class CourseApiView(APIView):
    """
    API Courses
    """

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AverageApiView(APIView):
    """
    API Average
    """
    
    def get(self, request):
        averages = Average.objects.all()
        serializer = AverageSerializer(averages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AverageSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
