from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils import timezone

WGS84 = 4326  # world geodesic system


class Base(models.Model):
    '''
    A Base model
    '''
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Provider(Base):
    '''
    Providers Model
    '''
    currency = models.CharField(max_length=32, default='USD')
    email = models.EmailField(max_length=256, default='')
    language = models.CharField(max_length=32, default='EN-US')
    name = models.CharField(max_length=256, default='')
    phone_number = models.CharField(max_length=256, default='')

    def __str__(self):
        return 'Provider: {}'.format(self.name)

    def __repr__(self):
        return 'Prodiver <{}>'.format(self.pk)


class ServiceArea(Base):
    '''
    ServiceArea Model
    '''
    supplier = models.ForeignKey(
        Provider, related_name='service_areas', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256, default='')
    price = models.DecimalField(decimal_places=2, max_digits=9)
    geojson_information = gis_models.PolygonField(srid=WGS84)

    @property
    def provider(self):
        return self.supplier

    def __str__(self):
        return 'ServiceArea: {}'.format(self.name)

    def __repr__(self):
        return 'ServiceArea <{}>'.format(self.pk)
