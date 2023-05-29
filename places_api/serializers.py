from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from places_api.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    geom = GeometryField()

    class Meta:
        model = Place
        fields = "__all__"


class PlaceListSerializer(PlaceSerializer):
    class Meta:
        model = Place
        fields = ("id", "name")


class PlaceDetailSerializer(PlaceSerializer):
    coordinates = serializers.SerializerMethodField()

    @extend_schema_field(serializers.ListField(child=serializers.FloatField()))
    def get_coordinates(self, obj):
        return {"lat": obj.geom.y, "lng": obj.geom.x}

    class Meta:
        model = Place
        fields = ("id", "name", "description", "coordinates")
