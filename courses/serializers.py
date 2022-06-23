from rest_framework import serializers

from .models import Course, Average


class AverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Average
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = {
            'id',
            'courseid'
            'name',
            'email',
            'comment',
            'average',
            'publishedAt',
            'isActive'
        }


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = {
            'id',
            'title',
            'url',
            'publishedAt',
            'isActive'
        }
