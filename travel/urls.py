from rest_framework import routers
from django.urls import path, include
from .views import TravelProjectsViewSet, ProjectPlaceViewSet

router = routers.DefaultRouter()
router.register(r'travel-projects', TravelProjectsViewSet)
router.register(r'project-places', ProjectPlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]