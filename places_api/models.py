from django.contrib.gis.db import models


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    geom = models.PointField()
