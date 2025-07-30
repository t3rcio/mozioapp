

from django.contrib.gis.geos import Point

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import status

from django.conf import settings
from django.contrib.gis.gdal import GDALException

from core.models import Provider, ServiceArea
from core.serializers import ProviderSerializer, ServiceAreaCreateSerializer, ServiceAreaListSerializer, ServiceAreaSerializer

import logging

logging.basicConfig(
    filename=settings.LOG_FILENAME
)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(GenericAPIView, ListModelMixin):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaCreateSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ServiceAreaListSerializer
        elif self.request.method in ['PATCH', 'DELETE']:
            return ServiceAreaSerializer
        return ServiceAreaCreateSerializer

    def get(self, request, *args, **kwargs):
        id = request.GET.get("id", 0)
        if id:
            sa = ServiceArea.objects.get(pk=int(id))
            return Response(
                data=ServiceAreaSerializer(instance=sa).data,
                status=status.HTTP_200_OK
            )
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid():
                servicearea = serializer.save()
                return Response(
                    self.get_serializer(servicearea).data,
                    status=status.HTTP_201_CREATED
                )
        except GDALException:
            return Response('geojson_information invalid', status=status.HTTP_400_BAD_REQUEST)
        except Exception as _error:
            logging.error(str(_error))
            return Response(str(_error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            _vd = serializer.validated_data
            service_area = ServiceArea.objects.get(
                pk=int(request.data.get('pk')))
            service_area.__dict__.update(_vd)
            service_area.save()
            _status = status.HTTP_200_OK
        else:
            _status = status.HTTP_400_BAD_REQUEST

        return Response(
            status=_status
        )

    def delete(self, request, *args, **kwargs):
        service_area = ServiceArea.objects.get(pk=int(request.data.get('pk')))
        if service_area:
            service_area.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_polygons(request):
    latitude = 0.0
    longitude = 0.0

    try:
        latitude = float(request.query_params.get('lat'))
        longitude = float(request.query_params.get('lng'))
    except Exception as _error:
        logging.error(str(_error))
        return Response({'error': 'Invalid or missing lat/lng'}, status=400)

    point = Point(longitude, latitude)
    service_areas = ServiceArea.objects.filter(
        geojson_information__intersects=point)
    serializer = ServiceAreaSerializer(service_areas, many=True)
    return Response(serializer.data)
