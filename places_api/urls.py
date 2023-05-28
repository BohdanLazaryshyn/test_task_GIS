from django.urls import path, include
from rest_framework import routers

from places_api.views import PlaceViewSet

router = routers.DefaultRouter()
router.register("places", PlaceViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "places_api"
