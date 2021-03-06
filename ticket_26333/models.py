from django.contrib.gis.db import models as gis
from django.contrib.gis.geos import Point
from django.db import models

POINT = Point(-104.9903, 39.7392, srid=4326)

class PagedModel(models.Model):
    location = gis.PointField(srid=4326, default=POINT)

