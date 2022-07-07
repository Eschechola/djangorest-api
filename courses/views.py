from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins;
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Average
from .serializers import CourseSerializer, AverageSerializer

"""
API V1

"""
# class CourseApiView(APIView):
#     """
#     API Courses
#     """

#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CourseSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AverageApiView(APIView):
#     """
#     API Average
#     """
    
#     def get(self, request):
#         averages = Average.objects.all()
#         serializer = AverageSerializer(averages, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AverageSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
API V2

"""

class CoursesApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AveragesApiView(generics.ListCreateAPIView):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer

    # get queryset busca uma lista 
    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(courseId=self.kwargs.get('course_pk'))
        return self.queryset.all()

class AverageApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer

    #get object busca somente um objeto
    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(),
                courseId = self.kwargs.get('course_pk'),
                pk = self.kwargs.get('average_pk'))
        return get_object_or_404(self.queryset(), pk=self.kwargs.get('average_pk'))


"""
API V3

"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, url_path="get-averages", methods=["get"])
    def get_averages(self, request, pk=None):
        course = self.get_object()
        serializer = AverageSerializer(course.averages.all(), many=True)
        return Response(serializer.data)


#remove o destroy impedindo delete
class AverageViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer