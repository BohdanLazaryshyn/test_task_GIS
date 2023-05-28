from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from places_api.models import Place
from places_api.serializers import (
    PlaceSerializer,
    PlaceListSerializer,
    PlaceDetailSerializer
)


class PlacePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 1000


@extend_schema(
    description="In this endpoint, you can see all available places in your database. "
                "There is pagination here, so to go to another page, enter the page number.",
)
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

    @extend_schema(
        description="Here you create a new place with coordinates. "
                    "To do this, write the following elements in the dictionary: name, description and coordinates",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="In this endpoint, you can find detailed information about a specific place by ID. "
                    "To do this, enter the ID in the search field.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="In this endpoint, you have the option to Update information about an "
                    "existing location. Enter the ID of the place and the new information for it.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="In this endpoint, you have the option to Update information about "
                    "an existing location. Enter the ID of the place and the new information for it.",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Іn this endpoint you have the option to delete a "
                    "place from the database by the specified ID",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


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
        description="On this endpoint,ou can search for the nearest location from your database using coordinates. "
                    "Please enter the latitude in the 'lat' field and the longitude in the 'lng' field."
                    ,
        responses={200: PlaceSerializer},
    )
class NearestPlaceView(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer

    def get_queryset(self):
        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")
        try:
            lat = float(lat)
            lng = float(lng)
            if not (-180.0 <= lat <= 180.0) or not (-180.0 <= lng <= 180.0):
                raise ValidationError(
                    "Invalid coordinates. Latitude and longitude values should be within the range of -180.0 to 180.0"
                )
        except (TypeError, ValueError):
            raise ValidationError("Invalid coordinates")

        point = Point(lng, lat, srid=4326)
        queryset = Place.objects.annotate(distance=Distance("geom", point)).order_by("distance")[0:1]
        return queryset
