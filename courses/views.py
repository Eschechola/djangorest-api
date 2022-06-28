from rest_framework.views import APIView
from rest_framework.response import Response


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


class AverageApiView(APIView):
    """
    API Average
    """
    def get(self, request):
        averages = Average.objects.all()
        serializer = AverageSerializer(averages, many=True)
        return Response(serializer.data)
