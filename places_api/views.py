from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from places_api.models import Place
from places_api.serializers import (
    PlaceSerializer,
    PlaceListSerializer,
    PlaceDetailSerializer
)


class PlacePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 1000


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = PlacePagination

    def get_serializer_class(self):
        if self.action == "list":
            return PlaceListSerializer
        elif self.action == "retrieve":
            return PlaceDetailSerializer
        return PlaceSerializer
