from rest_framework import serializers

from .models import TravelProjects, ProjectPlace

class TravelProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TravelProjects
        fields = '__all__'

class ProjectPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectPlace
        fields = '__all__'