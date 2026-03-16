from rest_framework import viewsets

from .models import TravelProjects, ProjectPlace
from .serializers import TravelProjectsSerializer, ProjectPlaceSerializer

class TravelProjectsViewSet(viewsets.ModelViewSet):
    queryset = TravelProjects.objects.all()
    serializer_class = TravelProjectsSerializer

class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer