
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from core.models import Provider, ServiceArea

import json


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'name',
            'currency',
            'email',
            'language',
            'phone_number'
        ]


class NestedProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name']


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = [
            'pk',
            'supplier',
            'name',
            'price',
            'geojson_information'
        ]


class ServiceAreaListSerializer(serializers.ModelSerializer):
    supplier = NestedProviderSerializer(read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = 'geojson_information'
        fields = [
            'supplier',
            'name',
            'price',
            'geojson_information'
        ]


class ServiceAreaCreateSerializer(GeoFeatureModelSerializer):

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Price can not be negative')
        return price

    def validate_geojson_information(self, geojson_information):
        if geojson_information is None:
            raise serializers.ValidationError(
                'geojson_information can not be None')
        return geojson_information

    class Meta:
        model = ServiceArea
        geo_field = 'geojson_information'
        fields = [
            'supplier',
            'name',
            'price',
        ]
