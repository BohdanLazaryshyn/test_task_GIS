from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
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


class NearestPlaceView(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer

    def get_queryset(self):
        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")
        if lat and lng:
            point = Point(float(lng), float(lat), srid=4326)
            queryset = Place.objects.annotate(distance=Distance("geom", point)).order_by("distance")[0:1]
            return queryset
        return Place.objects.none()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="lat",
                required=True,
                location=OpenApiParameter.QUERY,
                description="Latitude of the target location.",
                type=OpenApiTypes.NUMBER,
            ),
            OpenApiParameter(
                name="lng",
                required=True,
                location=OpenApiParameter.QUERY,
                description="Longitude of the target location.",
                type=OpenApiTypes.NUMBER,
            ),
        ],
        responses={200: PlaceSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
