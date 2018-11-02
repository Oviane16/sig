
from django.contrib.gis.db import models
class Region(models.Model):
    idreg = models.FloatField(null=True)
    id = models.BigIntegerField(primary_key=True)
    province = models.CharField(max_length=254,null=True)
    region = models.CharField(max_length=254,null=True)
    geom = models.MultiPolygonField(srid=4326,null=True)


# Auto-generated `LayerMapping` dictionary for WorldBorder model
regionborder_mapping = {
    'idreg': 'IDREG',
    'id': 'ID',
    'province': 'PROVINCE',
    'region': 'REGION',
    'geom': 'MULTIPOLYGON',
}
