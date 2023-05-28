from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from places_api.models import Place


class TestPlace(TestCase):
    def setUp(self):
        self.place_1 = Place.objects.create(
            name="Test place",
            description="Test description",
            geom="POINT(0 0)",
        )
        self.place_2 = Place.objects.create(
            name="Test place 2",
            description="Test description 2",
            geom="POINT(10 10)",
        )
        self.place_3 = Place.objects.create(
            name="Test place 3",
            description="Test description 3",
            geom="POINT(20 20)",
        )

    def test_get_list(self):
        response = self.client.get("/api/places/?page_size=0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_get_detail(self):
        response = self.client.get(f"/api/places/{self.place_1.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.place_1.name)
        self.assertEqual(response.data["description"], self.place_1.description)
        lat = response.data["coordinates"]["lat"]
        lng = response.data["coordinates"]["lng"]
        self.assertEqual((lat, lng), self.place_1.geom.coords)

    def test_create_place(self):
        url = "/api/places/"
        data = {
            "name": "New Place",
            "description": "Test description",
            "geom": "POINT(154 23)",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Place")
        self.assertEqual(response.data["description"], "Test description")
        self.assertEqual(response.data["geom"]["coordinates"], [154, 23])

    def test_update_place(self):
        url = f"/api/places/{self.place_1.id}/"
        data = {
            "name": "Updated Place",
            "description": "Updated description",
            "geom": "POINT(154 23)",
        }
        response = self.client.put(url, data, format="json", content_type="application/json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Place")
        self.assertEqual(response.data["description"], "Updated description")
        self.assertEqual(response.data["geom"]["coordinates"], [154, 23])

    def test_delete_place(self):
        url = f"/api/places/{self.place_1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Place.objects.count(), 2)

    def test_nearest_place(self):
        url = reverse('places_api:nearest-place')
        lat = 11.1
        lng = 12.5
        response = self.client.get(url, {"lat": lat, "lng": lng})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], self.place_2.name)
        self.assertEqual(response.data[0]["description"], self.place_2.description)
