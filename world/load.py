import os
from django.contrib.gis.utils import LayerMapping
from .models import Region

regionborder_mapping = {
    'idreg': 'IDREG',
    'id': 'ID',
    'province': 'PROVINCE',
    'region': 'REGION',
    'geom': 'MULTIPOLYGON',
}

region_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'c_regions1.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Region, region_shp, regionborder_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)