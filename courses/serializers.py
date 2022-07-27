from rest_framework import serializers
from django.db.models import Avg

from .models import Course, Average


class AverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Average
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = '__all__'

    def validate_rate(self, value):
        if value in range (1, 6):
            return value
        raise serializers.ValidationError('Average can be between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):
    #nested relationship
    #returns all relations of averages
    averages = AverageSerializer(many=True, read_only=True)
    
    averages_media = serializers.SerializerMethodField() 

    #hyperlinked related field
    #returns links of averages
    # averages = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='average-detail')

    #primary key related field
    #returns primary keys of averages
    #averages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_averages_media(self, obj):
        media = obj.averages.aggregate(Avg('average')).get('average__avg')

        if media is None:
            return 0
        return round(media * 2) / 2