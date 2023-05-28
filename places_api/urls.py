from django.urls import path, include
from rest_framework import routers

from places_api.views import PlaceViewSet, NearestPlaceView

router = routers.DefaultRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("nearest-place/", NearestPlaceView.as_view({"get": "list"}), name="nearest-place"),
]

app_name = "places_api"
