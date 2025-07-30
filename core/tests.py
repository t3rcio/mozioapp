
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from random import choice
from core.models import Provider, ServiceArea
from core.serializers import ServiceAreaSerializer

import json


SERVICE_AREA_POLYGONS = [
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.880, -5.090],
            [-42.875, -5.090],
            [-42.875, -5.085],
            [-42.880, -5.085],
            [-42.880, -5.090]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.870, -5.088],
            [-42.865, -5.088],
            [-42.865, -5.083],
            [-42.870, -5.083],
            [-42.870, -5.088]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.860, -5.087],
            [-42.855, -5.087],
            [-42.855, -5.082],
            [-42.860, -5.082],
            [-42.860, -5.087]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.850, -5.086],
            [-42.845, -5.086],
            [-42.845, -5.081],
            [-42.850, -5.081],
            [-42.850, -5.086]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.890, -5.095],
            [-42.885, -5.095],
            [-42.885, -5.090],
            [-42.890, -5.090],
            [-42.890, -5.095]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.840, -5.084],
            [-42.835, -5.084],
            [-42.835, -5.079],
            [-42.840, -5.079],
            [-42.840, -5.084]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.880, -5.080],
            [-42.875, -5.080],
            [-42.875, -5.075],
            [-42.880, -5.075],
            [-42.880, -5.080]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.870, -5.078],
            [-42.865, -5.078],
            [-42.865, -5.073],
            [-42.870, -5.073],
            [-42.870, -5.078]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.860, -5.076],
            [-42.855, -5.076],
            [-42.855, -5.071],
            [-42.860, -5.071],
            [-42.860, -5.076]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.850, -5.074],
            [-42.845, -5.074],
            [-42.845, -5.069],
            [-42.850, -5.069],
            [-42.850, -5.074]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.840, -5.072],
            [-42.835, -5.072],
            [-42.835, -5.067],
            [-42.840, -5.067],
            [-42.840, -5.072]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.890, -5.070],
            [-42.885, -5.070],
            [-42.885, -5.065],
            [-42.890, -5.065],
            [-42.890, -5.070]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.830, -5.068],
            [-42.825, -5.068],
            [-42.825, -5.063],
            [-42.830, -5.063],
            [-42.830, -5.068]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.820, -5.066],
            [-42.815, -5.066],
            [-42.815, -5.061],
            [-42.820, -5.061],
            [-42.820, -5.066]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.810, -5.064],
            [-42.805, -5.064],
            [-42.805, -5.059],
            [-42.810, -5.059],
            [-42.810, -5.064]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.800, -5.062],
            [-42.795, -5.062],
            [-42.795, -5.057],
            [-42.800, -5.057],
            [-42.800, -5.062]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.880, -5.060],
            [-42.875, -5.060],
            [-42.875, -5.055],
            [-42.880, -5.055],
            [-42.880, -5.060]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.870, -5.058],
            [-42.865, -5.058],
            [-42.865, -5.053],
            [-42.870, -5.053],
            [-42.870, -5.058]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.860, -5.056],
            [-42.855, -5.056],
            [-42.855, -5.051],
            [-42.860, -5.051],
            [-42.860, -5.056]
        ]]
    },
    {
        "type": "Polygon",
        "coordinates": [[
            [-42.850, -5.054],
            [-42.845, -5.054],
            [-42.845, -5.049],
            [-42.850, -5.049],
            [-42.850, -5.054]
        ]]
    }
]


class ProviderTests(APITestCase):

    def test_create_provider(self):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "phone_number": "+55 86 99999-9999",
            "currency": "USD",
            "language": "EN-US"
        }
        response = self.client.post("/api/providers/", data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Provider.objects.count() > 0

    def test_create_provider_invalid_email(self):
        data = {
            "name": "Maria",
            "email": "email-invalido",
            "phone_number": "123"
        }
        response = self.client.post("/api/providers/", data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class ServiceAreaTests(APITestCase):

    def setUp(self):
        self.provider = Provider.objects.create(
            name="Empresa FOOBAR",
            email="contato@foobar.com",
            phone_number="+55 86 99999-9999"
        )
        self.geojson = json.dumps(choice(SERVICE_AREA_POLYGONS))

    def test_create_service_area_success(self):
        data = {
            "supplier": self.provider.id,
            "geojson_information": self.geojson,
            "price": "150.00"
        }
        response = self.client.post("/api/serviceareas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)

    def test_create_service_area_invalid_geojson(self):
        data = {
            "supplier": self.provider.id,
            "geojson_information": json.dumps({"type": "INVALID"}),
            "price": "200.00"
        }
        response = self.client.post("/api/serviceareas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_service_area_negative_price(self):
        data = {
            "supplier": self.provider.id,
            "geojson_information": self.geojson,
            "price": "-50.00"
        }
        response = self.client.post("/api/serviceareas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_service_area_geojson_information_none(self):
        data = {
            "supplier": self.provider.id,
            "price": "100.00"
            # geojson_information is None
        }
        response = self.client.post("/api/serviceareas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_service_areas(self):
        ServiceArea.objects.create(
            supplier=self.provider,
            geojson_information=self.geojson,
            price=120.00
        )
        response = self.client.get("/api/serviceareas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data.get("results", [])), 1)

    def test_retrieve_service_area(self):
        area = ServiceArea.objects.create(
            supplier=self.provider,
            geojson_information=self.geojson,
            price=99.90
        )
        pk = area.pk
        response = self.client.get(f"/api/serviceareas/?id={pk}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], "99.90")

    def test_update_service_area(self):
        area = ServiceArea.objects.create(
            supplier=self.provider,
            name='Some area name',
            geojson_information=self.geojson,
            price=120.00
        )
        payload = ServiceAreaSerializer(instance=area).data
        payload['price'] = '140.00'
        payload['pk'] = area.pk
        response = self.client.patch(
            f"/api/serviceareas/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        area.refresh_from_db()
        self.assertEqual(str(area.price), "140.00")

    def test_delete_service_area(self):
        area = ServiceArea.objects.create(
            supplier=self.provider,
            geojson_information=self.geojson,
            price=88.00
        )
        payload = ServiceAreaSerializer(instance=area).data
        payload['pk'] = area.pk
        response = self.client.delete(
            f"/api/serviceareas/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ServiceArea.objects.filter(id=area.id).exists())

    def test_create_service_area_with_nonexistent_provider(self):
        data = {
            "supplier": 999,
            "geojson_information": self.geojson,
            "price": "99.99"
        }
        response = self.client.post("/api/serviceareas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_service_area(self):
        geoarea = choice(SERVICE_AREA_POLYGONS)
        lng, lat = choice(geoarea.get('coordinates')[0])
        area = ServiceArea.objects.create(
            supplier=self.provider,
            geojson_information=json.dumps(geoarea),
            price=10.0
        )
        response = self.client.get(
            f'/api/serviceareas/search?lat={lat}&lng={lng}')
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)
        _assert = len(response.data) > 0
        self.assertTrue(_assert)
