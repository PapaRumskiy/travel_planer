import requests
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TravelProjects, ProjectPlace
from .serializers import TravelProjectsSerializer, ProjectPlaceSerializer

class TravelProjectsViewSet(viewsets.ModelViewSet):
    queryset = TravelProjects.objects.all()
    serializer_class = TravelProjectsSerializer

    def destroy(self, request, *args, **kwargs):
        """Prevent deletion of a travel project if any of its places are marked as visited"""
        project = self.get_object()
        if project.place.filter(visited=True).exists():
            return Response(
                {"error": "Cannot delete project"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new project place.
        Validate that the place exists in the Art Institute API.
        Enforce a maximum of 10 places per project.
        Prevent adding duplicate external places to the same project.
        """
        project_id = request.data.get("project")
        external_id = request.data.get("external_id")

        try:
            project = TravelProjects.objects.get(id=project_id)
        except TravelProjects.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        if project.place.count() >= 10:
            return Response({"error": "Maximum 10 places allowed per project"}, status=status.HTTP_400_BAD_REQUEST)

        if project.place.filter(external_id=external_id).exists():
            return Response({"error": "Place already exists in this project"}, status=status.HTTP_400_BAD_REQUEST)

        api_url = f"https://api.artic.edu/api/v1/artworks/{external_id}"
        response = requests.get(api_url)
        if response.status_code != 200:
            return Response({"error": "Place not found in Art Institute API"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)