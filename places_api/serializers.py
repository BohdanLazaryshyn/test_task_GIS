from rest_framework import serializers

from places_api.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("id", "name")


class PlaceDetailSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()

    def get_coordinates(self, obj):
        return {"lat": obj.geom.y, "lng": obj.geom.x}

    class Meta:
        model = Place
        fields = ("id", "name", "description", "coordinates")

